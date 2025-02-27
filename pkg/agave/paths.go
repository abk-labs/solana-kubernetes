package agave

import (
	_ "embed"

	"github.com/abklabs/svmkit/pkg/paths"

	"dario.cat/mergo"
	"github.com/BurntSushi/toml"
)

//go:embed defaults/agave_default_paths.toml
var defaultAgavePathsToml []byte

type AgavePaths struct {
	paths.Paths

	AgaveRunBinPath   *string `pulumi:"agaveRunBinPath,optional" toml:"agaveRunBinPath,omitempty"`
	AgaveStopBinPath  *string `pulumi:"agaveStopBinPath,optional" toml:"agaveStopBinPath,omitempty"`
	AgaveCheckBinPath *string `pulumi:"agaveCheckBinPath,optional" toml:"agaveCheckBinPath,omitempty"`
}

func NewDefaultAgavePaths(base *paths.Paths) (*AgavePaths, error) {
	var b *paths.Paths
	if base == nil {
		def, err := paths.NewDefaultPaths()
		if err != nil {
			return nil, err
		}
		b = def
	} else {
		b = base
	}

	agavePaths := &AgavePaths{
		Paths: *b,
	}

	if err := toml.Unmarshal(defaultAgavePathsToml, agavePaths); err != nil {
		return nil, err
	}
	return agavePaths, nil
}

func (f *AgavePaths) Merge(other *AgavePaths) error {
	if other == nil {
		return nil
	}
	if err := f.Paths.Merge(&other.Paths); err != nil {
		return err
	}
	return mergo.Merge(f, other, mergo.WithOverride)
}
