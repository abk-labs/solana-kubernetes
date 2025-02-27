package paths

import (
	_ "embed"

	"dario.cat/mergo"
	"github.com/BurntSushi/toml"
)

//go:embed defaults/default_paths.toml
var defaultPathsToml []byte

type Paths struct {
	LogPath                         *string `pulumi:"logPath,optional" toml:"logPath,omitempty"`
	SystemdPath                     *string `pulumi:"systemdPath,optional" toml:"systemdPath,omitempty"`
	LedgerPath                      *string `pulumi:"ledgerPath,optional" toml:"ledgerPath,omitempty"`
	AccountsPath                    *string `pulumi:"accountsPath,optional" toml:"accountsPath,omitempty"`
	ValidatorIdentityKeypairPath    *string `pulumi:"validatorIdentityKeypairPath,optional" toml:"validatorIdentityKeypairPath,omitempty"`
	ValidatorVoteAccountKeypairPath *string `pulumi:"validatorVoteAccountKeypairPath,optional" toml:"validatorVoteAccountKeypairPath,omitempty"`
}

func NewDefaultPaths() (*Paths, error) {
	var fl Paths
	if err := toml.Unmarshal(defaultPathsToml, &fl); err != nil {
		return nil, err
	}
	return &fl, nil
}

func (fl *Paths) Merge(other *Paths) error {
	if other == nil {
		return nil
	}
	return mergo.Merge(fl, other, mergo.WithOverride)
}
