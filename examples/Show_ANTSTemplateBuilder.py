import os
import csv
import sys
import string
import argparse

########################################
########################################
#####  Download some test data
########################################
########################################
import urllib2
homeDir=os.getenv("HOME")
requestedPath=os.path.join(homeDir,'nipypeTestPath')
mydatadir=os.path.realpath(requestedPath)
if not os.path.exists(mydatadir):
    os.makedirs(mydatadir)
print mydatadir

#### Download some test data from the web.
MyFileURLs=[
           ('http://slicer.kitware.com/midas3/download?bitstream=13121','01_T1_half.nii.gz'),
           ('http://slicer.kitware.com/midas3/download?bitstream=13122','02_T1_half.nii.gz'),
           ('http://slicer.kitware.com/midas3/download?bitstream=13124','03_T1_half.nii.gz'),
           ('http://slicer.kitware.com/midas3/download?bitstream=13128','01_T1_inv_half.nii.gz'),
           ('http://slicer.kitware.com/midas3/download?bitstream=13123','02_T1_inv_half.nii.gz'),
           ('http://slicer.kitware.com/midas3/download?bitstream=13125','03_T1_inv_half.nii.gz'),
           ]
for tt in MyFileURLs:
    myURL=tt[0]
    localFilename=os.path.join(mydatadir,tt[1])
    if not os.path.exists(localFilename):
        remotefile = urllib2.urlopen(myURL)

        localFile = open(localFilename, 'wb')
        localFile.write(remotefile.read())
        localFile.close()
        print("Downloaded file: {0}".format(localFilename))
    else:
        print("File previously downloaded {0}".format(localFilename))



input_images=[
os.path.join(mydatadir,'01_T1_half.nii.gz'),
os.path.join(mydatadir,'02_T1_half.nii.gz'),
os.path.join(mydatadir,'03_T1_half.nii.gz')
]
input_passive_images=[
{'INV_T1':os.path.join(mydatadir,'01_T1_inv_half.nii.gz')},
{'INV_T1':os.path.join(mydatadir,'02_T1_inv_half.nii.gz')},
{'INV_T1':os.path.join(mydatadir,'03_T1_inv_half.nii.gz')}
]

###################################
###################################
####### Run a template build with ANTS
###################################
###################################
from nipype.interfaces.base import CommandLine, CommandLineInputSpec, TraitedSpec, File, Directory, traits, isdefined, BaseInterface
from nipype.interfaces.utility import Merge, Split, Function, Rename, IdentityInterface
import nipype.interfaces.io as nio   # Data i/o
import nipype.pipeline.engine as pe  # pypeline engine

from nipype.workflows.smri.ants.ANTSBuildTemplate import ANTSTemplateBuildSingleIterationWF
from nipype.workflows.smri.ants.antsSimpleAverageWF import antsSimpleAverageWF

inputID = pe.Node(interface=IdentityInterface(fields=
                    ['imageList']),
                    run_without_submitting=True,
                    name='InputImages' )
inputID.inputs.imageList=input_images

passiveDeformedImages = pe.Node(interface=IdentityInterface(fields=
                    ['ListOfPassiveImagesDictionaries']),
                    run_without_submitting=True,
                    name='passiveDeformedImages' )
passiveDeformedImages.inputs.ListOfPassiveImagesDictionaries=input_passive_images

########################
## The work for template builder
########################

tbuilder=pe.Workflow(name="TemplateBuilder")
tbuilder.base_dir=requestedPath

myInitAvgWF = antsSimpleAverageWF()
tbuilder.connect(inputID, 'imageList', myInitAvgWF, 'InputSpec.images')

buildTemplateIteration1=ANTSTemplateBuildSingleIterationWF(1,"",'MULTI')

tbuilder.connect(myInitAvgWF, 'OutputSpec.average_image', buildTemplateIteration1, 'InputSpec.fixed_image')
tbuilder.connect(inputID, 'imageList', buildTemplateIteration1, 'InputSpec.images')
tbuilder.connect(passiveDeformedImages, 'ListOfPassiveImagesDictionaries', buildTemplateIteration1, 'InputSpec.ListOfPassiveImagesDictionaries')

#tbuilder.connect(MergeByExtendListElementsNode, 'ListOfExtendedPassiveImages', buildTemplateIteration1, 'InputSpec.ListOfPassiveImagesDictionaries')

#buildTemplateIteration2 = buildTemplateIteration1.clone(name='buildTemplateIteration2')
#buildTemplateIteration2 = ANTSTemplateBuildSingleIterationWF('Iteration02',CLUSTER_QUEUE,TEMPLATE_BUILD_RUN_MODE)
#tbuilder.connect(buildTemplateIteration1, 'OutputSpec.template', buildTemplateIteration2, 'InputSpec.fixed_image')
#tbuilder.connect(MergeT1s[subjectid], 'out', buildTemplateIteration2, 'InputSpec.images')
#tbuilder.connect(MergeByExtendListElementsNode, 'ListOfExtendedPassiveImages', buildTemplateIteration2, 'InputSpec.ListOfPassiveImagesDictionaries')

tbuilder.run()