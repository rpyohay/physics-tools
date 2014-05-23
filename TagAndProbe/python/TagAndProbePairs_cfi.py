import FWCore.ParameterSet.Config as cms

#tag required to fire specific HLT
tagPhoton = cms.EDProducer("CandViewShallowCloneCombiner",
                           decay = cms.string("Tag probePhotons"),
                           checkCharge = cms.bool(False),
                           cut = cms.string("60 < mass < 120")
                           )

#no trigger requirement on tag
tagPhotonNoHLT = cms.EDProducer("CandViewShallowCloneCombiner",
                                decay = cms.string("goodPhotons probePhotons"),
                                checkCharge = cms.bool(False),
                                cut = cms.string("60 < mass < 120")
                                )

#probe is isolated photon
tagIsoPhotons = cms.EDProducer(
    "CandViewShallowCloneCombiner",
    decay = cms.string("Tag probePhotonsPassingIsolation"), # charge conjugate states are implied
    checkCharge = cms.bool(False),                                   
    cut = cms.string("60 < mass < 120")
    )

#probe is an IDed and isolated photon
tagIdEBPhotons = cms.EDProducer(
    "CandViewShallowCloneCombiner",
    decay = cms.string("Tag probePhotonsPassingIdEB"), # charge conjugate states are implied
    checkCharge = cms.bool(False),                                  
    cut = cms.string("60 < mass < 120")
    )
tagIdEEPhotons = tagIdEBPhotons.clone()
tagIdEEPhotons.decay = cms.string("Tag probePhotonsPassingIdEE")

#probe is a photon passing isolation, ID, and trigger
tagHLTEBPhotons = cms.EDProducer(
    "CandViewShallowCloneCombiner",
    decay = cms.string("Tag probePhotonsPassingHLTEB"), # charge conjugate states are implied
    checkCharge = cms.bool(False),                                   
    cut = cms.string("60 < mass < 120")
    )
tagHLTEEPhotons = tagHLTEBPhotons.clone()
tagHLTEEPhotons.decay = cms.string("Tag probePhotonsPassingHLTEE")

#probe is a SC
tagSC = cms.EDProducer(
    "CandViewShallowCloneCombiner",
    decay = cms.string("Tag probePhotons"), # charge conjugate states are implied
    checkCharge = cms.bool(False),                                   
    cut = cms.string("60 < mass < 120")
    )

#probe is a photon passing everything except HLT + IsoVL and R9Id
tagIsoVLR9Id = cms.EDProducer(
    "CandViewShallowCloneCombiner",
    decay = cms.string("Tag probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLR9IdEB"),
    checkCharge = cms.bool(False),                                   
    cut = cms.string("60 < mass < 120")
    )

#probe is a photon passing everything except HLT + IsoVL
tagIsoVL = cms.EDProducer(
    "CandViewShallowCloneCombiner",
    decay = cms.string("Tag probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLEB"),
    checkCharge = cms.bool(False),                                   
    cut = cms.string("60 < mass < 120")
    )

#probe is a photon passing everything except HLT + R9Id
tagR9Id = cms.EDProducer(
    "CandViewShallowCloneCombiner",
    decay = cms.string("Tag probePhotonsPassingPUCorrectedCombinedIsoIdR9IdEB"),
    checkCharge = cms.bool(False),                                   
    cut = cms.string("60 < mass < 120")
    )

#tag and probe sequences
tag_and_probe_sequence = cms.Sequence(tagSC + tagIsoVLR9Id + tagIsoVL + tagR9Id)
loose_probe_tag_and_probe_sequence = cms.Sequence(tagPhoton + tagPhotonNoHLT)
