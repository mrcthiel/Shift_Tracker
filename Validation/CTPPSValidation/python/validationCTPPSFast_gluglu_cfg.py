import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

# file with rootfile names
sourcefile = 'files.txt'

# path to rootfiles
#path = '/afs/cern.ch/work/m/mthiel/private/ANALYZER/CMSSW_8_0_12/src/analyzer/analyzer/mount/'
path = 'mount/'
source = []
# read input files from source file
with open(sourcefile,'r') as f:
  lines = f.read().splitlines()
  for i in lines :
    source += ['file:' + i]

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(source),
    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
    secondaryFileNames = cms.untracked.vstring()
)

#process.source = cms.Source("PoolSource",
#        fileNames = cms.untracked.vstring(
            #'file:../GluGluTo2Jets.root'
#            'file:GluGluTo2Jets_M_100_7TeV_exhume_cff_py_GEN_SIM_RECOBEFMIX_DIGI_RECO.root'
#    ),
#      duplicateCheckMode = cms.untracked.string('noDuplicateCheck')
#)



process.validation = cms.EDAnalyzer('CTPPSFastValidation',
    MCEvent = cms.untracked.InputTag("LHCTransport"),
    ChgGenPartCollectionName = cms.untracked.InputTag("genParticles"),
    psimHitTag = cms.InputTag('CTPPSSimHits','CTPPSHits'),
    recHitTag = cms.InputTag("CTPPSFastRecHits","CTPPSFastRecHits"),
    tracksPPSTag = cms.InputTag("CTPPSFastTracks","CTPPSFastTrack"),
    jetsTag = cms.InputTag('ak4PFJets'),
    fPhysChannelTag = cms.string('ExHuMe (ggTo2Jets)')  
)

process.TFileService = cms.Service("TFileService",
                fileName = cms.string('outValidation_gluglu_LHCT_NoPU.root')
                #fileName = cms.string('outValidation_LHCT_ggTo2Jets.root')
)

process.options = cms.untracked.PSet(
            SkipEvent = cms.untracked.vstring('ProductNotFound')
            )

process.p = cms.Path(process.validation)
