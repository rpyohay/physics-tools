import FWCore.ParameterSet.Config as cms

#isolation cone sizes
DR03 = 0
DR04 = 1

#configurable PU-subtracted isolation cuts
ECAL_ET_MULTIPLIER = 0.006
ECAL_CONSTANT = 4.2 #GeV
ECAL_RHO_EFFECTIVE_AREA = 0.093
ECAL_NPV_EFFECTIVE_AREA = 0.09524
ECAL = 0
HCAL_ET_MULTIPLIER = 0.0025
HCAL_CONSTANT = 2.2 #GeV
HCAL_RHO_EFFECTIVE_AREA = 0.02808
HCAL_NPV_EFFECTIVE_AREA = 0.06014
CONE_SIZE = DR03
HCAL = 1
TRACK = 2
HOVERE = 3
SIGMAIETAIETA = 4
R9MIN = 5
R9MAX = 6

##-------------------- Import the JEC services -----------------------
from JetMETCorrections.Configuration.DefaultJEC_cff import *
##-------------------- Import the Jet RECO modules -----------------------
from RecoJets.Configuration.RecoPFJets_cff import *
##-------------------- Turn-on the FastJet density calculation -----------------------
kt6PFJets.doRhoFastjet = True
## kt6PFJets.Rho_EtaMax = cms.double(2.5)

#ECAL only, PU subtracted
probePhotonsPassingPUSubtractedECALIsolation = cms.EDProducer(
    "PUSubtractedPhotonSelector",
    photonSrc = cms.InputTag("probePhotons"),
    rhoSrc = cms.InputTag("kt6PFJets", "rho", "TagProbe"),
    PVSrc = cms.InputTag("offlinePrimaryVertices", "", "RECO"),
    ETMultiplier = cms.vdouble(ECAL_ET_MULTIPLIER),
    constant = cms.vdouble(ECAL_CONSTANT),
    rhoEffectiveArea = cms.vdouble(ECAL_RHO_EFFECTIVE_AREA),
    nPVEffectiveArea = cms.vdouble(ECAL_NPV_EFFECTIVE_AREA),
    combinedIsoMax = cms.double(-1.0),
    type = cms.vuint32(ECAL),
    coneSize = cms.vuint32(DR04)
    )

#HCAL only, PU subtracted
probePhotonsPassingPUSubtractedHCALIsolation = cms.EDProducer(
    "PUSubtractedPhotonSelector",
    photonSrc = cms.InputTag("probePhotons"),
    rhoSrc = cms.InputTag("kt6PFJets", "rho", "TagProbe"),
    PVSrc = cms.InputTag("offlinePrimaryVertices", "", "RECO"),
    ETMultiplier = cms.vdouble(HCAL_ET_MULTIPLIER),
    constant = cms.vdouble(HCAL_CONSTANT),
    rhoEffectiveArea = cms.vdouble(HCAL_RHO_EFFECTIVE_AREA),
    nPVEffectiveArea = cms.vdouble(HCAL_NPV_EFFECTIVE_AREA),
    combinedIsoMax = cms.double(-1.0),
    type = cms.vuint32(HCAL),
    coneSize = cms.vuint32(DR04)
    )

#ECAL and HCAL only, PU corrected
probePhotonsPassingPUCorrectedIsolation = cms.EDProducer(
    "PUSubtractedPhotonSelector",
    photonSrc = cms.InputTag("probePhotons"),
    rhoSrc = cms.InputTag("kt6PFJets", "rho", "TagProbe"),
    PVSrc = cms.InputTag("offlinePrimaryVertices", "", "RECO"),
    ETMultiplier = cms.vdouble(ECAL_ET_MULTIPLIER, HCAL_ET_MULTIPLIER),
    constant = cms.vdouble(ECAL_CONSTANT, HCAL_CONSTANT),
    rhoEffectiveArea = cms.vdouble(ECAL_RHO_EFFECTIVE_AREA, HCAL_RHO_EFFECTIVE_AREA),
    nPVEffectiveArea = cms.vdouble(ECAL_NPV_EFFECTIVE_AREA, HCAL_NPV_EFFECTIVE_AREA),
    combinedIsoMax = cms.double(-1.0), #GeV
    type = cms.vuint32(ECAL, HCAL),
    coneSize = cms.vuint32(DR04)
    )

#ECAL, HCAL, and track combined isolation, PU corrected
preCombIso = cms.EDProducer(
    "PUSubtractedPhotonSelector",
    photonSrc = cms.InputTag("probePhotons"),
    rhoSrc = cms.InputTag("kt6PFJets", "rho", "TagProbe"),
    PVSrc = cms.InputTag("offlinePrimaryVertices", "", "RECO"),
    ETMultiplier = cms.vdouble(ECAL_ET_MULTIPLIER, HCAL_ET_MULTIPLIER, 0.0),
    constant = cms.vdouble(ECAL_CONSTANT, HCAL_CONSTANT, 0.0),
    rhoEffectiveArea = cms.vdouble(ECAL_RHO_EFFECTIVE_AREA, HCAL_RHO_EFFECTIVE_AREA, 0.0),
    nPVEffectiveArea = cms.vdouble(ECAL_NPV_EFFECTIVE_AREA, HCAL_NPV_EFFECTIVE_AREA, 0.0),
    combinedIsoMax = cms.double(6.0), #GeV
    type = cms.vuint32(ECAL, HCAL, TRACK),
    coneSize = cms.vuint32(DR03, DR03, DR03)
    )
probePhotonsPassingPUCorrectedCombinedIsolation = cms.EDFilter(
    "PhotonSelector",
    src = cms.InputTag("preCombIso", "rhoCorrected", "TagProbe"),
    cut = cms.string("")
    )

#PU-subtracted isolation sequence
PU_subtracted_iso_sequence = cms.Sequence(kt6PFJets + preCombIso + 
                                          probePhotonsPassingPUCorrectedCombinedIsolation)
