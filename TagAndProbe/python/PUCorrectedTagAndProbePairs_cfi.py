import FWCore.ParameterSet.Config as cms

#probe is a rho-corrected isolated photon
## tagPURhoCorrectedIsoPhotons = cms.EDProducer(
##     "CandViewShallowCloneCombiner",
##     decay = cms.string("Tag rhoCorrectedIsolatedPhotons"),
##     checkCharge = cms.bool(False),                                   
##     cut = cms.string("60 < mass < 120")
##     )

#probe is an nPV-corrected isolated photon
## tagPUNPVCorrectedIsoPhotons = cms.EDProducer(
##     "CandViewShallowCloneCombiner",
##     decay = cms.string("Tag nPVCorrectedIsolatedPhotons"),
##     checkCharge = cms.bool(False),                                   
##     cut = cms.string("60 < mass < 120")
##     )

#probe is a rho-corrected IDed photon
tagPURhoCorrectedIdEBPhotons = cms.EDProducer(
    "CandViewShallowCloneCombiner",
    decay = cms.string("Tag probePhotonsPassingPURhoCorrectedIdEB"),
    checkCharge = cms.bool(False),                                  
    cut = cms.string("60 < mass < 120")
)
tagPURhoCorrectedIdEEPhotons = tagPURhoCorrectedIdEBPhotons.clone()
tagPURhoCorrectedIdEEPhotons.decay = cms.string("Tag probePhotonsPassingPURhoCorrectedIdEE")

#probe is an nPV-corrected IDed photon
tagPUNPVCorrectedIdEBPhotons = cms.EDProducer(
    "CandViewShallowCloneCombiner",
    decay = cms.string("Tag probePhotonsPassingPUNPVCorrectedIdEB"),
    checkCharge = cms.bool(False),                                  
    cut = cms.string("60 < mass < 120")
)
tagPUNPVCorrectedIdEEPhotons = tagPUNPVCorrectedIdEBPhotons.clone()
tagPUNPVCorrectedIdEEPhotons.decay = cms.string("Tag probePhotonsPassingPUNPVCorrectedIdEE")

#probe is a rho-corrected photon passing isolation, ID, and trigger
tagPURhoCorrectedHLTEBPhotons = cms.EDProducer(
    "CandViewShallowCloneCombiner",
    decay = cms.string("Tag probePhotonsPassingPURhoCorrectedHLTEB"),
    checkCharge = cms.bool(False),                                  
    cut = cms.string("60 < mass < 120")
)
tagPURhoCorrectedHLTEEPhotons = tagPURhoCorrectedHLTEBPhotons.clone()
tagPURhoCorrectedHLTEEPhotons.decay = cms.string("Tag probePhotonsPassingPURhoCorrectedHLTEE")

#probe is an nPV-corrected photon passing isolation, ID, and trigger
tagPUNPVCorrectedHLTEBPhotons = cms.EDProducer(
    "CandViewShallowCloneCombiner",
    decay = cms.string("Tag probePhotonsPassingPUNPVCorrectedHLTEB"),
    checkCharge = cms.bool(False),                                  
    cut = cms.string("60 < mass < 120")
)
tagPUNPVCorrectedHLTEEPhotons = tagPUNPVCorrectedHLTEBPhotons.clone()
tagPUNPVCorrectedHLTEEPhotons.decay = cms.string("Tag probePhotonsPassingPUNPVCorrectedHLTEE")

#PU-corrected tag and probe sequence
PU_corrected_tag_and_probe_sequence = cms.Sequence(tagPURhoCorrectedIdEBPhotons +
                                                   tagPUNPVCorrectedIdEEPhotons)
