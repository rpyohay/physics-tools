import FWCore.ParameterSet.Config as cms

#trigger on top of rho-corrected PU subtraction
probePhotonsPassingPURhoCorrectedHLTEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedIdEB", "rhoCorrected", "TagProbe"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon32_CaloIdL_Photon26_CaloIdL_v2", "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag("hltEG32CaloIdLClusterShapeFilter")
    )
probePhotonsPassingPURhoCorrectedHLTEE = probePhotonsPassingPURhoCorrectedHLTEB.clone()
probePhotonsPassingPURhoCorrectedHLTEE.InputProducer = cms.InputTag(
    "probePhotonsPassingPUCorrectedIdEE", "rhoCorrected", "TagProbe"
    )

#trigger on top of nPV-corrected PU subtraction
probePhotonsPassingPUNPVCorrectedHLTEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedIdEB", "nPVCorrected", "TagProbe"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon32_CaloIdL_Photon26_CaloIdL_v2", "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag("hltEG32CaloIdLClusterShapeFilter")
    )
probePhotonsPassingPUNPVCorrectedHLTEE = probePhotonsPassingPUNPVCorrectedHLTEB.clone()
probePhotonsPassingPUNPVCorrectedHLTEE.InputProducer = cms.InputTag(
    "probePhotonsPassingPUCorrectedIdEE", "nPVCorrected", "TagProbe"
    )

#PU-corrected trigger sequence
PU_corrected_trigger_sequence = cms.Sequence(
    probePhotonsPassingPURhoCorrectedHLTEB + probePhotonsPassingPUNPVCorrectedHLTEB +
    probePhotonsPassingPURhoCorrectedHLTEE + probePhotonsPassingPUNPVCorrectedHLTEE
    )
