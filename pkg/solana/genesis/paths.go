package genesis

import (
	_ "embed"

	"github.com/abklabs/svmkit/pkg/paths"

	"dario.cat/mergo"
	"github.com/BurntSushi/toml"
)

//go:embed defaults/genesis_default_paths.toml
var defaultGenesisPathsToml []byte

type GenesisPaths struct {
	paths.Paths

	GenesisPrimordialAccountsPath *string `pulumi:"genesisPrimordialAccountsPath,optional" toml:"genesisPrimordialAccountsPath,omitempty"`
	GenesisValidatorAccountsPath  *string `pulumi:"genesisValidatorAccountsPath,optional" toml:"genesisValidatorAccountsPath,omitempty"`
	GenesisSolanaSplCachePath     *string `pulumi:"genesisSolanaSplCachePath,optional" toml:"genesisSolanaSplCachePath,omitempty"`
}

func NewDefaultGenesisPaths(base *paths.Paths) (*GenesisPaths, error) {
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

	gp := &GenesisPaths{
		Paths: *b,
	}

	if err := toml.Unmarshal(defaultGenesisPathsToml, gp); err != nil {
		return nil, err
	}
	return gp, nil
}

func (p *GenesisPaths) Merge(other *GenesisPaths) error {
	if other == nil {
		return nil
	}
	if err := p.Paths.Merge(&other.Paths); err != nil {
		return err
	}
	return mergo.Merge(p, other, mergo.WithOverride)
}

func (p *GenesisPaths) MergeFlags(flags *GenesisFlags) error {
	if flags == nil {
		return nil
	}

	if flags.LedgerPath != nil && *flags.LedgerPath != "" {
		p.Paths.LedgerPath = flags.LedgerPath
	}

	return nil
}
