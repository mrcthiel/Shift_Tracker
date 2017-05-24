# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: GluGluTo2Jets_M_100_7TeV_exhume_cff.py --conditions auto:run2_mc --fast -n 100 --eventcontent AODSIM -s GEN,SIM,RECOBEFMIX,DIGI:pdigi_valid,RECO --datatier GEN-SIM-DIGI-RECO --beamspot Realistic25ns13TeV2016Collision --pileup NoPileUp --era Run2_25ns --customise SimTransport/HectorProducer/FastSimWithCTPPS_cff.customise --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RECO',eras.Run2_25ns,eras.fastSim)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('FastSimulation.Configuration.Geometries_MC_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeV2016Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('FastSimulation.Configuration.SimIdeal_cff')
process.load('FastSimulation.Configuration.Reconstruction_BefMix_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('FastSimulation.Configuration.Reconstruction_AftMix_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

import sys
for arg in sys.argv[2:]:
        opt = arg[0:arg.find("=")]
        if opt=="shift_n":
         Shift = int(arg[arg.find("=")+1:])
        if opt=="LabelShift":
         Label = arg[arg.find("=")+1:]
        if opt=="job":
         N = int(arg[arg.find("=")+1:])


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(750)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('GluGluTo2Jets_M_100_7TeV_exhume_cff.py nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $') 
)

# Output definition

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RECO'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fileName = cms.untracked.string('GluGluTo2Jets_M_100_7TeV_exhume_cff_py_GEN_SIM_RECOBEFMIX_DIGI_RECO.root'),
    outputCommands = process.AODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
process.RandomNumberGeneratorService.generator.initialSeed  = cms.untracked.uint32(923875 + N*10)
process.generator = cms.EDFilter("ExhumeGeneratorFilter",
    ExhumeParameters = cms.PSet(
        AlphaEw = cms.double(0.0072974),
        B = cms.double(4.0),
        BottomMass = cms.double(4.6),
        CharmMass = cms.double(1.42),
        HiggsMass = cms.double(120.0),
        HiggsVev = cms.double(246.0),
        LambdaQCD = cms.double(80.0),
        MinQt2 = cms.double(0.64),
        MuonMass = cms.double(0.1057),
        PDF = cms.double(11000),
        Rg = cms.double(1.2),
        StrangeMass = cms.double(0.19),
        Survive = cms.double(0.03),
        TauMass = cms.double(1.77),
        TopMass = cms.double(175.0),
        WMass = cms.double(80.33),
        ZMass = cms.double(91.187)
    ),
    ExhumeProcess = cms.PSet(
        MassRangeHigh = cms.double(2000.0),
        MassRangeLow = cms.double(300.0),
        ProcessType = cms.string('GG'),
        ThetaMin = cms.double(0.3)
    ),
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring()
    ),
    comEnergy = cms.double(13000.0),
    maxEventsToPrint = cms.untracked.int32(2),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.reconstruction_befmix_step = cms.Path(process.reconstruction_befmix)
process.digitisation_step = cms.Path(process.pdigi_valid)
process.reconstruction_step = cms.Path(process.reconstruction)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.reconstruction_befmix_step,process.digitisation_step,process.reconstruction_step,process.endjob_step,process.AODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from SimTransport.HectorProducer.FastSimWithCTPPS_cff
from SimTransport.HectorProducer.FastSimWithCTPPS_cff import customise 
process.load('FastSimulation.CTPPSRecHitProducer.CTPPSRecHitProducer_cfi') ########################################################################################################################################


shift = cms.untracked.vdouble(-0.25,-0.2,-0.15,-0.1,-0.05,-0.04,-0.03,-0.02,-0.01,0,0.01,0.02,0.03,0.04,0.05,0.1,0.15,0.2,0.25)

if Label == "ShiftArmBTrack1X":
        process.CTPPSFastRecHits.ShiftArmBTrack1X = shift[Shift]
if Label == "ShiftArmBTrack1Y":
        process.CTPPSFastRecHits.ShiftArmBTrack1Y = shift[Shift]
if Label == "ShiftArmBTrack2X":
        process.CTPPSFastRecHits.ShiftArmBTrack2X = shift[Shift]
if Label == "ShiftArmBTrack2Y":
        process.CTPPSFastRecHits.ShiftArmBTrack2Y = shift[Shift]
if Label == "ShiftArmFTrack1X":
        process.CTPPSFastRecHits.ShiftArmFTrack1X = shift[Shift]
if Label == "ShiftArmFTrack1Y":
        process.CTPPSFastRecHits.ShiftArmFTrack1Y = shift[Shift]
if Label == "ShiftArmFTrack2X":
        process.CTPPSFastRecHits.ShiftArmFTrack2X = shift[Shift]
if Label == "ShiftArmFTrack2Y":
        process.CTPPSFastRecHits.ShiftArmFTrack2Y = shift[Shift]

#call to customisation function customise imported from SimTransport.HectorProducer.FastSimWithCTPPS_cff
process = customise(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
