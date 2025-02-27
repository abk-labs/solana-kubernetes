package tuner

import (
	_ "embed"

	"github.com/abklabs/svmkit/pkg/paths"

	"dario.cat/mergo"
	"github.com/BurntSushi/toml"
)

//go:embed defaults/tuner_default_paths.toml
var defaultTunerPathsToml []byte

type TunerPaths struct {
	paths.Paths

	TunerLogPath    *string `pulumi:"tunerLogPath,optional" toml:"tunerLogPath,omitempty"`
	TunerConfPath   *string `pulumi:"tunerConfPath,optional" toml:"tunerConfPath,omitempty"`
	TunerRunBinPath *string `pulumi:"tunerRunBinPath,optional" toml:"tunerRunBinPath,omitempty"`
}

func NewDefaultTunerPaths(base *paths.Paths) (*TunerPaths, error) {
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

	tp := &TunerPaths{
		Paths: *b,
	}

	if err := toml.Unmarshal(defaultTunerPathsToml, tp); err != nil {
		return nil, err
	}
	return tp, nil
}

func (f *TunerPaths) Merge(other *TunerPaths) error {
	if other == nil {
		return nil
	}
	if err := f.Paths.Merge(&other.Paths); err != nil {
		return err
	}
	return mergo.Merge(f, other, mergo.WithOverride)
}
