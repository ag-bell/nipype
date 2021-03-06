# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.dti import ProjThresh
def test_ProjThresh_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    args=dict(argstr='%s',
    ),
    in_files=dict(argstr='%s',
    mandatory=True,
    position=0,
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    threshold=dict(position=1,
    mandatory=True,
    argstr='%d',
    ),
    output_type=dict(),
    )
    inputs = ProjThresh.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_ProjThresh_outputs():
    output_map = dict(out_files=dict(),
    )
    outputs = ProjThresh.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
