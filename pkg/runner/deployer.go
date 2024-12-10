package runner

import (
	"fmt"
	"io"
	"path/filepath"
	"strings"
	"text/template"

	"github.com/pkg/sftp"
	"golang.org/x/crypto/ssh"
)

var runWrapperTemplate = template.Must(template.New("runWrapper").Parse(`ret=0 ; ( set -euo pipefail ; cd {{ .RootPath }} ; {{ .Cmd }} ; ) || ret=$? ; rm -rf {{ .RootPath }} ; exit $ret`))

type DeployerHandler interface {
	// IngestReaders is responsible for keeping the readers drained.
	// After the readers have been closed, it MUST signal completion by
	// closing the provided done channel.
	IngestReaders(done chan<- struct{}, stdout io.Reader, stderr io.Reader) error
	AugmentError(error) error
}

type Deployer struct {
	Payload *Payload
	Client  *ssh.Client
}

func (p *Deployer) Deploy() error {
	sftpClient, err := sftp.NewClient(p.Client)
	if err != nil {
		return fmt.Errorf("failed to create SFTP client: %w", err)
	}

	defer sftpClient.Close()

	for _, f := range p.Payload.Files {
		path := filepath.Join(p.Payload.RootPath, f.Path)

		dir := filepath.Dir(path)

		if err = sftpClient.MkdirAll(dir); err != nil {
			return fmt.Errorf("failed to create remote directory for %s: %w", dir, err)
		}

		remoteFile, err := sftpClient.Create(path)

		if err != nil {
			return fmt.Errorf("failed to create remote file %s: %w", path, err)
		}

		if err = copyFile(remoteFile, f, path); err != nil {
			return err
		}
	}

	return nil
}

func copyFile(remoteFile *sftp.File, f PayloadFile, path string) error {
	defer remoteFile.Close()

	if err := remoteFile.Chmod(f.Mode); err != nil {
		_ = remoteFile.Close()
		return fmt.Errorf("couldn't change ownership of file %s: %w", path, err)
	}

	if _, err := io.Copy(remoteFile, f.Reader); err != nil {
		_ = remoteFile.Close()
		return fmt.Errorf("failed to write to remote file %s: %w", path, err)
	}

	return nil
}

func (p *Deployer) Run(cmdSegs []string, dontCleanup bool, handler DeployerHandler) error {
	runWrapper := &strings.Builder{}

	err := runWrapperTemplate.Execute(runWrapper, struct {
		*Payload
		Cmd string
	}{
		p.Payload,
		strings.Join(cmdSegs, " "),
	})

	if err != nil {
		return fmt.Errorf("couldn't format the deployer's run wrapper: %w", err)
	}

	execSession, err := p.Client.NewSession()
	if err != nil {
		return fmt.Errorf("failed to create SSH session: %w", err)
	}
	defer execSession.Close()

	stdoutPipe, err := execSession.StdoutPipe()
	if err != nil {
		return fmt.Errorf("failed to get stdout pipe: %w", err)
	}

	stderrPipe, err := execSession.StderrPipe()
	if err != nil {
		return fmt.Errorf("failed to get stderr pipe: %w", err)
	}

	if err = execSession.Start(runWrapper.String()); err != nil {
		return fmt.Errorf("failed to start command: %w", err)
	}

	done := make(chan struct{})

	if err = handler.IngestReaders(done, stdoutPipe, stderrPipe); err != nil {
		return fmt.Errorf("couldn't bind command stream handlers: %w", err)
	}

	<-done

	if err = execSession.Wait(); err != nil {
		err = handler.AugmentError(err)
		return fmt.Errorf("command execution failed: %w", err)
	}

	return nil
}
