import FWCore.ParameterSet.Config as cms

#to get the isolation cuts
from PhysicsTools.TagAndProbe.Isolation_cfi import isoCuts

#configurable ID cuts
#IDCutsEB = "(hadronicOverEm < 0.05) && (trkSumPtHollowConeDR04 < (0.001*pt + 2.0)) && (sigmaIetaIeta < 0.011) && (r9 < 0.98)"
IDCutsEB = "(hadronicOverEm < 0.05) && (trkSumPtHollowConeDR04 < (0.001*pt + 2.0)) && (sigmaIetaIeta < 0.013)"
IDCutsEE = "(hadronicOverEm < 0.05) && (trkSumPtHollowConeDR04 < (0.001*pt + 2.0)) && (sigmaIetaIeta < 0.030)"
HOverECut = "hadronicOverEm < 0.05"
trackIsoCut = "trkSumPtHollowConeDR04 < (0.001*pt + 2.0)"
sigmaIetaIetaCutEB = "sigmaIetaIeta < 0.011"
sigmaIetaIetaCutEE = "sigmaIetaIeta < 0.030"
R9Cut = "r9 < 1.0"

#ECAL and HCAL isolation + track isolation, H/E, and sigmaIetaIeta
probePhotonsPassingIdEB = cms.EDFilter(
    "PhotonRefSelector",
    src = cms.InputTag("probePhotons"),
    cut = cms.string(isoCuts + " && " + IDCutsEB)
    )
probePhotonsPassingIdEE = probePhotonsPassingIdEB.clone()
probePhotonsPassingIdEE.cut = cms.string(isoCuts + " && " + IDCutsEE)

#H/E
probePhotonsPassingHOverE = cms.EDFilter("PhotonRefSelector",
                                         src = cms.InputTag("probePhotons"),
                                         cut = cms.string(HOverECut)
                                         )

#sigmaIetaIeta
probePhotonsPassingSigmaIetaIetaEB = cms.EDFilter("PhotonRefSelector",
                                                  src = cms.InputTag("probePhotons"),
                                                  cut = cms.string(sigmaIetaIetaCutEB)
                                                  )
probePhotonsPassingSigmaIetaIetaEE = probePhotonsPassingSigmaIetaIetaEB.clone()
probePhotonsPassingSigmaIetaIetaEE.cut = cms.string(sigmaIetaIetaCutEE)

#R9
probePhotonsPassingR9 = cms.EDFilter("PhotonRefSelector",
                                     src = cms.InputTag("probePhotons"),
                                     cut = cms.string(R9Cut)
                                     )

#ID sequence
ID_sequence = cms.Sequence(probePhotonsPassingHOverE + probePhotonsPassingSigmaIetaIetaEB +
                           probePhotonsPassingR9)
