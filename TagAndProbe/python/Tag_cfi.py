import FWCore.ParameterSet.Config as cms

#configurable tag definition
## tagDef = "(sigmaIetaIeta < 0.009) && (hasPixelSeed = 1.0) && (hadronicOverEm < 0.05) && (pt > 35.0) && (abs(eta) < 1.479) && (abs(abs(superCluster.eta) - 1.479) >= 0.1)"
tagDef = "(sigmaIetaIeta < 0.009) && (hasPixelSeed = 1.0) && (hadronicOverEm < 0.05) && (pt > 25.0) && (abs(superCluster.eta) < 1.4442) && (ecalRecHitSumEtConeDR04 < (0.006*pt + 4.2)) && (hcalTowerSumEtConeDR04 < (0.0025*pt + 2.2)) && (trkSumPtHollowConeDR04 < (0.001*pt + 2.0))"

#step 1: tag should be tightly matched to a track
## trackMatchedPhotons = cms.EDProducer(
##     "TrackMatchedPhotonProducer",
##     src = cms.InputTag("probePhotonsEB"),
##     ReferenceTrackCollection = cms.untracked.InputTag("generalTracks", "", "RECO"),
##     deltaR = cms.untracked.double(0.04),
##     trackPTMin = cms.double(15.0),
##     trackEtaMax = cms.double(1.479),
##     )
trackMatchedPhotons = cms.EDProducer(
    "TrackMatchedPhotonProducer",
    srcObject = cms.InputTag("probePhotons"),
    srcObjectsToMatch = cms.VInputTag(cms.InputTag("generalTracks", "", "RECO")),
    deltaRMax = cms.double(0.04),
    srcObjectsToMatchSelection = cms.string("(pt > 15.0) && (abs(eta) < 1.479)")
    )

#step 2: tag should have good shower shape, a pixel seed, have good H/E, be reasonably high pT,
#and be in EB
goodPhotons = cms.EDFilter("PhotonRefSelector",
                           src = cms.InputTag("trackMatchedPhotons"),
                           cut = cms.string(tagDef)
                           )

#step 3: tag should have fired the HLT path under study
Tag = cms.EDProducer(
    "trgMatchedPhotonProducer",
    InputProducer = cms.InputTag("goodPhotons"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon32_CaloIdL_Photon26_CaloIdL_v2", "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag("hltEG32CaloIdLClusterShapeFilter"),
    matchUnprescaledTriggerOnly = cms.untracked.bool(False)
    )

#tag sequence
tag_sequence = cms.Sequence(trackMatchedPhotons + goodPhotons + Tag)
