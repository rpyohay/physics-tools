import FWCore.ParameterSet.Config as cms

#to get the configurable ID cuts defined elsewhere
from PhysicsTools.TagAndProbe.PUSubtractedIsolation_cfi import *

#PU rho-corrected ECAL and HCAL isolation + track isolation, H/E, and sigmaIetaIeta
probePhotonsPassingPUCorrectedIdEB = cms.EDProducer(
    "PUSubtractedPhotonSelector",
    photonSrc = cms.InputTag("probePhotons"),
    rhoSrc = cms.InputTag("kt6PFJets", "rho", "TagProbe"),
    PVSrc = cms.InputTag("offlinePrimaryVertices", "", "RECO"),
    ETMultiplier = cms.vdouble(ECAL_ET_MULTIPLIER, HCAL_ET_MULTIPLIER, 0.001, 0.0, 0.0),
    constant = cms.vdouble(ECAL_CONSTANT, HCAL_CONSTANT, 2.0, 0.05, 0.013),
    rhoEffectiveArea = cms.vdouble(ECAL_RHO_EFFECTIVE_AREA, HCAL_RHO_EFFECTIVE_AREA, 0.0, 0.0,
                                   0.0),
    nPVEffectiveArea = cms.vdouble(ECAL_NPV_EFFECTIVE_AREA, HCAL_NPV_EFFECTIVE_AREA, 0.0, 0.0,
                                   0.0),
    combinedIsoMax = cms.double(-1.0), #GeV
    type = cms.vuint32(ECAL, HCAL, TRACK, HOVERE, SIGMAIETAIETA),
    coneSize = cms.vuint32(DR04, DR04, DR04, DR04, DR04)
    )
probePhotonsPassingPUCorrectedIdEE = probePhotonsPassingPUCorrectedIdEB.clone()
probePhotonsPassingPUCorrectedIdEE.constant = cms.vdouble(ECAL_CONSTANT, HCAL_CONSTANT, 2.0, 0.05,
                                                          0.030)

#PU rho-corrected combined isolation, H/E, R9, R9Id, IsoVL, and sigmaIetaIeta
preIsoVLR9Id = cms.EDProducer(
    "PUSubtractedPhotonSelector",
    photonSrc = cms.InputTag("probePhotonsPassingIsolation"),
    rhoSrc = cms.InputTag("kt6PFJets", "rho", "TagProbe"),
    PVSrc = cms.InputTag("offlinePrimaryVertices", "", "RECO"),
    ETMultiplier = cms.vdouble(ECAL_ET_MULTIPLIER, HCAL_ET_MULTIPLIER, 0.001, 0.0, 0.0, 0.0, 0.0),
    constant = cms.vdouble(ECAL_CONSTANT, HCAL_CONSTANT, 2.0, 0.05, 0.011, 0.8, 1.0),
    rhoEffectiveArea = cms.vdouble(ECAL_RHO_EFFECTIVE_AREA, HCAL_RHO_EFFECTIVE_AREA, 0.0, 0.0,
                                   0.0, 0.0, 0.0),
    nPVEffectiveArea = cms.vdouble(ECAL_NPV_EFFECTIVE_AREA, HCAL_NPV_EFFECTIVE_AREA, 0.0, 0.0,
                                   0.0, 0.0, 0.0),
    combinedIsoMax = cms.double(6.0), #GeV
    type = cms.vuint32(ECAL, HCAL, TRACK, HOVERE, SIGMAIETAIETA, R9MIN, R9MAX),
    coneSize = cms.vuint32(DR03, DR03, DR03, DR03, DR03, DR03, DR03)
    )
probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLR9IdEB = cms.EDFilter(
    "PhotonSelector",
    src = cms.InputTag("preIsoVLR9Id", "rhoCorrected", "TagProbe"),
    cut = cms.string("")
    )

#PU rho-corrected combined isolation, H/E, R9, R9Id, and sigmaIetaIeta
preR9Id = cms.EDProducer(
    "PUSubtractedPhotonSelector",
    photonSrc = cms.InputTag("probePhotons"),
    rhoSrc = cms.InputTag("kt6PFJets", "rho", "TagProbe"),
    PVSrc = cms.InputTag("offlinePrimaryVertices", "", "RECO"),
    ETMultiplier = cms.vdouble(ECAL_ET_MULTIPLIER, HCAL_ET_MULTIPLIER, 0.001, 0.0, 0.0, 0.0, 0.0),
    constant = cms.vdouble(ECAL_CONSTANT, HCAL_CONSTANT, 2.0, 0.05, 0.011, 0.8, 1.0),
    rhoEffectiveArea = cms.vdouble(ECAL_RHO_EFFECTIVE_AREA, HCAL_RHO_EFFECTIVE_AREA, 0.0, 0.0,
                                   0.0, 0.0, 0.0),
    nPVEffectiveArea = cms.vdouble(ECAL_NPV_EFFECTIVE_AREA, HCAL_NPV_EFFECTIVE_AREA, 0.0, 0.0,
                                   0.0, 0.0, 0.0),
    combinedIsoMax = cms.double(6.0), #GeV
    type = cms.vuint32(ECAL, HCAL, TRACK, HOVERE, SIGMAIETAIETA, R9MIN, R9MAX),
    coneSize = cms.vuint32(DR03, DR03, DR03, DR03, DR03, DR03, DR03)
    )
probePhotonsPassingPUCorrectedCombinedIsoIdR9IdEB = cms.EDFilter(
    "PhotonSelector",
    src = cms.InputTag("preR9Id", "rhoCorrected", "TagProbe"),
    cut = cms.string("")
    )

#PU rho-corrected combined isolation, H/E, R9, IsoVL, and sigmaIetaIeta
preIsoVL = cms.EDProducer(
    "PUSubtractedPhotonSelector",
    photonSrc = cms.InputTag("probePhotonsPassingIsolation"),
    rhoSrc = cms.InputTag("kt6PFJets", "rho", "TagProbe"),
    PVSrc = cms.InputTag("offlinePrimaryVertices", "", "RECO"),
    ETMultiplier = cms.vdouble(ECAL_ET_MULTIPLIER, HCAL_ET_MULTIPLIER, 0.001, 0.0, 0.0, 0.0, 0.0),
    constant = cms.vdouble(ECAL_CONSTANT, HCAL_CONSTANT, 2.0, 0.05, 0.011, 0.0, 1.0),
    rhoEffectiveArea = cms.vdouble(ECAL_RHO_EFFECTIVE_AREA, HCAL_RHO_EFFECTIVE_AREA, 0.0, 0.0,
                                   0.0, 0.0, 0.0),
    nPVEffectiveArea = cms.vdouble(ECAL_NPV_EFFECTIVE_AREA, HCAL_NPV_EFFECTIVE_AREA, 0.0, 0.0,
                                   0.0, 0.0, 0.0),
    combinedIsoMax = cms.double(6.0), #GeV
    type = cms.vuint32(ECAL, HCAL, TRACK, HOVERE, SIGMAIETAIETA, R9MIN, R9MAX),
    coneSize = cms.vuint32(DR03, DR03, DR03, DR03, DR03, DR03, DR03)
    )
probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLEB = cms.EDFilter(
    "PhotonSelector",
    src = cms.InputTag("preIsoVL", "rhoCorrected", "TagProbe"),
    cut = cms.string("")
    )

#PU rho-corrected combined isolation, H/E, R9, and sigmaIetaIeta
preAll = cms.EDProducer(
    "PUSubtractedPhotonSelector",
    photonSrc = cms.InputTag("probePhotons"),
    rhoSrc = cms.InputTag("kt6PFJets", "rho", "TagProbe"),
    PVSrc = cms.InputTag("offlinePrimaryVertices", "", "RECO"),
    ETMultiplier = cms.vdouble(ECAL_ET_MULTIPLIER, HCAL_ET_MULTIPLIER, 0.001, 0.0, 0.0, 0.0, 0.0),
    constant = cms.vdouble(ECAL_CONSTANT, HCAL_CONSTANT, 2.0, 0.05, 0.011, 0.0, 1.0),
    rhoEffectiveArea = cms.vdouble(ECAL_RHO_EFFECTIVE_AREA, HCAL_RHO_EFFECTIVE_AREA, 0.0, 0.0,
                                   0.0, 0.0, 0.0),
    nPVEffectiveArea = cms.vdouble(ECAL_NPV_EFFECTIVE_AREA, HCAL_NPV_EFFECTIVE_AREA, 0.0, 0.0,
                                   0.0, 0.0, 0.0),
    combinedIsoMax = cms.double(6.0), #GeV
    type = cms.vuint32(ECAL, HCAL, TRACK, HOVERE, SIGMAIETAIETA, R9MIN, R9MAX),
    coneSize = cms.vuint32(DR03, DR03, DR03, DR03, DR03, DR03, DR03)
    )
probePhotonsPassingPUCorrectedCombinedIsoIdAllEB = cms.EDFilter(
    "PhotonSelector",
    src = cms.InputTag("preAll", "rhoCorrected", "TagProbe"),
    cut = cms.string("")
    )

#PU-corrected ID sequence
PU_corrected_ID_sequence = cms.Sequence(preIsoVLR9Id +
                                        probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLR9IdEB +
                                        preR9Id + 
                                        probePhotonsPassingPUCorrectedCombinedIsoIdR9IdEB +
                                        preIsoVL + 
                                        probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLEB +
                                        preAll +
                                        probePhotonsPassingPUCorrectedCombinedIsoIdAllEB)
