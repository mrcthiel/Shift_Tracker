import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            #'file:../test_pg3_LHCT.root'
            'file:/eos/user/d/dilson/pps/root/pg_LHCT_1.root',
            'file:/eos/user/d/dilson/pps/root/pg_LHCT_10.root',
            'file:/eos/user/d/dilson/pps/root/pg_LHCT_11.root',
            'file:/eos/user/d/dilson/pps/root/pg_LHCT_12.root',
            'file:/eos/user/d/dilson/pps/root/pg_LHCT_13.root',
            'file:/eos/user/d/dilson/pps/root/pg_LHCT_14.root',
            'file:/eos/user/d/dilson/pps/root/pg_LHCT_15.root',
            'file:/eos/user/d/dilson/pps/root/pg_LHCT_16.root',
            'file:/eos/user/d/dilson/pps/root/pg_LHCT_17.root',
            'file:/eos/user/d/dilson/pps/root/pg_LHCT_18.root',
            'file:/eos/user/d/dilson/pps/root/pg_LHCT_19.root',
            'file:/eos/user/d/dilson/pps/root/pg_LHCT_2.root',
            'file:/eos/user/d/dilson/pps/root/pg_LHCT_20.root',
            'file:/eos/user/d/dilson/pps/root/pg_LHCT_3.root',
            'file:/eos/user/d/dilson/pps/root/pg_LHCT_4.root',
            'file:/eos/user/d/dilson/pps/root/pg_LHCT_5.root',
            'file:/eos/user/d/dilson/pps/root/pg_LHCT_6.root',
            'file:/eos/user/d/dilson/pps/root/pg_LHCT_7.root',
            'file:/eos/user/d/dilson/pps/root/pg_LHCT_9.root'
    ),
      duplicateCheckMode = cms.untracked.string('noDuplicateCheck')
)

process.validation = cms.EDAnalyzer('CTPPSFastValidation',
    MCEvent = cms.untracked.InputTag("LHCTransport"),
    ChgGenPartCollectionName = cms.untracked.InputTag("genParticles"),
    psimHitTag = cms.InputTag('CTPPSSimHits','CTPPSHits'),
    recHitTag = cms.InputTag("CTPPSFastRecHits","CTPPSFastRecHits"),
    tracksPPSTag = cms.InputTag("CTPPSFastTracks","CTPPSFastTrack"),
    jetsTag = cms.InputTag('ak4PFJets'),
    fPhysChannelTag = cms.string('Particle Gun')  
)

process.TFileService = cms.Service("TFileService",
                fileName = cms.string('/eos/user/d/dilson/pps/outValidation_pg_LHCT.root')
                #fileName = cms.string('outValidation_LHCT_PG.root')
)

process.options = cms.untracked.PSet(
            SkipEvent = cms.untracked.vstring('ProductNotFound')
            )

process.p = cms.Path(process.validation)
