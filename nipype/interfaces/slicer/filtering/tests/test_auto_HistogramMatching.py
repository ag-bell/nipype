# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.slicer.filtering.histogrammatching import HistogramMatching
def test_HistogramMatching_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    outputVolume=dict(position=-1,
    hash_files=False,
    argstr='%s',
    ),
    numberOfHistogramLevels=dict(argstr='--numberOfHistogramLevels %d',
    ),
    args=dict(argstr='%s',
    ),
    referenceVolume=dict(position=-2,
    argstr='%s',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    inputVolume=dict(position=-3,
    argstr='%s',
    ),
    threshold=dict(argstr='--threshold ',
    ),
    numberOfMatchPoints=dict(argstr='--numberOfMatchPoints %d',
    ),
    )
    inputs = HistogramMatching.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_HistogramMatching_outputs():
    output_map = dict(outputVolume=dict(position=-1,
    ),
    )
    outputs = HistogramMatching.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
