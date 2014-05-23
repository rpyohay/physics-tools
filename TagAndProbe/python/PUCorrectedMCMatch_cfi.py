import FWCore.ParameterSet.Config as cms

#match between rho-corrected isolated photon and gen electron
McMatchPURhoCorrectedIso = cms.EDProducer(
    "MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("probePhotonsPassingPUCorrectedIsolation", "rhoCorrected", "TagProbe"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
    )

#match between nPV-corrected isolated photon and gen electron
McMatchPUNPVCorrectedIso = cms.EDProducer(
    "MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("probePhotonsPassingPUCorrectedIsolation", "nPVCorrected", "TagProbe"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
    )

#match between rho-corrected isolated and IDed photon and gen electron
McMatchPURhoCorrectedIdEB = cms.EDProducer(
    "MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("probePhotonsPassingPUCorrectedIdEB", "rhoCorrected", "TagProbe"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
    )
McMatchPURhoCorrectedIdEE = McMatchPURhoCorrectedIdEB.clone()
McMatchPURhoCorrectedIdEE.src = cms.InputTag("probePhotonsPassingPUCorrectedIdEE", "rhoCorrected",
                                             "TagProbe")

#match between nPV-corrected isolated and IDed photon and gen electron
McMatchPUNPVCorrectedIdEB = cms.EDProducer(
    "MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("probePhotonsPassingPUCorrectedIdEB", "nPVCorrected", "TagProbe"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
    )
McMatchPUNPVCorrectedIdEE = McMatchPUNPVCorrectedIdEB.clone()
McMatchPUNPVCorrectedIdEE.src = cms.InputTag("probePhotonsPassingPUCorrectedIdEE", "nPVCorrected",
                                             "TagProbe")

#match between photon passing rho-corrected isolation, ID, and trigger and gen electron
McMatchPURhoCorrectedHLTEB = cms.EDProducer(
    "MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("probePhotonsPassingPURhoCorrectedHLTEB"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
    )
McMatchPURhoCorrectedHLTEE = McMatchPURhoCorrectedHLTEB.clone()
McMatchPURhoCorrectedHLTEE.src = cms.InputTag("probePhotonsPassingPURhoCorrectedHLTEE")

#match between photon passing nPV-corrected isolation, ID, and trigger and gen electron
McMatchPUNPVCorrectedHLTEB = cms.EDProducer(
    "MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("probePhotonsPassingPUNPVCorrectedHLTEB"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
    )
McMatchPUNPVCorrectedHLTEE = McMatchPUNPVCorrectedHLTEB.clone()
McMatchPUNPVCorrectedHLTEE.src = cms.InputTag("probePhotonsPassingPUNPVCorrectedHLTEE")

#PU-corrected MC match sequence
PU_corrected_mc_match_sequence = cms.Sequence(McMatchPURhoCorrectedIso +
                                              McMatchPUNPVCorrectedIso +
                                              McMatchPURhoCorrectedIdEB +
                                              McMatchPUNPVCorrectedIdEB +
                                              McMatchPURhoCorrectedHLTEB +
                                              McMatchPUNPVCorrectedHLTEB +
                                              McMatchPURhoCorrectedIdEE +
                                              McMatchPUNPVCorrectedIdEE +
                                              McMatchPURhoCorrectedHLTEE +
                                              McMatchPUNPVCorrectedHLTEE)
