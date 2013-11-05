# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.afni.preprocess import To3D
def test_To3D_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    out_file=dict(name_source=['in_folder'],
    name_template='%s',
    argstr='-prefix %s',
    ),
    datatype=dict(argstr='-datum %s',
    ),
    filetype=dict(argstr='-%s',
    ),
    args=dict(argstr='%s',
    ),
    outputtype=dict(),
    assumemosaic=dict(argstr='-assume_dicom_mosaic',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    in_folder=dict(position=-1,
    mandatory=True,
    argstr='%s/*.dcm',
    ),
    skipoutliers=dict(argstr='-skip_outliers',
    ),
    funcparams=dict(argstr='-time:zt %s alt+z2',
    ),
    )
    inputs = To3D.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_To3D_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = To3D.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value