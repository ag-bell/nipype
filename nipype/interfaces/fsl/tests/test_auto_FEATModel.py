# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.model import FEATModel
def test_FEATModel_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    fsf_file=dict(copyfile=False,
    mandatory=True,
    position=0,
    argstr='%s',
    ),
    args=dict(argstr='%s',
    ),
    ev_files=dict(copyfile=False,
    mandatory=True,
    position=1,
    argstr='%s',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    output_type=dict(),
    )
    inputs = FEATModel.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_FEATModel_outputs():
    output_map = dict(design_cov=dict(),
    design_file=dict(),
    design_image=dict(),
    con_file=dict(),
    fcon_file=dict(),
    )
    outputs = FEATModel.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
