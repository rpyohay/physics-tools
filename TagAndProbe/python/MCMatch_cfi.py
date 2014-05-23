import FWCore.ParameterSet.Config as cms

#match between tag and gen electron
McMatchTag = cms.EDProducer("MCTruthDeltaRMatcherNew",
                            matchPDGId = cms.vint32(11),
                            src = cms.InputTag("Tag"),
                            distMin = cms.double(0.3),
                            matched = cms.InputTag("genParticles"),
                            checkCharge = cms.bool(True)
                            )

#match between loose photon and gen electron
McMatchPhoton = cms.EDProducer("MCTruthDeltaRMatcherNew",
                               matchPDGId = cms.vint32(11),
                               src = cms.InputTag("probePhotons"),
                               distMin = cms.double(0.3),
                               matched = cms.InputTag("genParticles")
                               )

#match between isolated photon and gen electron
McMatchIso = cms.EDProducer("MCTruthDeltaRMatcherNew",
                            matchPDGId = cms.vint32(11),
                            src = cms.InputTag("probePhotonsPassingIsolation"),
                            distMin = cms.double(0.3),
                            matched = cms.InputTag("genParticles"),
                            checkCharge = cms.bool(True)
                            )

#match between isolated and IDed photon and gen electron
McMatchIdEB = cms.EDProducer("MCTruthDeltaRMatcherNew",
                             matchPDGId = cms.vint32(11),
                             src = cms.InputTag("probePhotonsPassingIdEB"),
                             distMin = cms.double(0.3),
                             matched = cms.InputTag("genParticles"),
                             checkCharge = cms.bool(True)
                             )
McMatchIdEE = McMatchIdEB.clone()
McMatchIdEE.src = cms.InputTag("probePhotonsPassingIdEE")

#match between photon passing isolation, ID, and trigger and gen electron
McMatchHLTEB = cms.EDProducer("MCTruthDeltaRMatcherNew",
                              matchPDGId = cms.vint32(11),
                              src = cms.InputTag("probePhotonsPassingHLTEB"),
                              distMin = cms.double(0.3),
                              matched = cms.InputTag("genParticles"),
                              checkCharge = cms.bool(True)
                              )
McMatchHLTEE = McMatchHLTEB.clone()
McMatchHLTEE.src = cms.InputTag("probePhotonsPassingHLTEE")

#MC match sequences
mc_match_sequence = cms.Sequence(McMatchTag +  McMatchPhoton + McMatchIso + McMatchIdEB +
                                 McMatchIdEE + McMatchHLTEB + McMatchHLTEE)
no_intermediates_mc_match_sequence = cms.Sequence(McMatchTag + McMatchPhoton)
