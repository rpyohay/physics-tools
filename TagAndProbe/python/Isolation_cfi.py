import FWCore.ParameterSet.Config as cms

#configurable isolation cuts
isoCuts = "(ecalRecHitSumEtConeDR03 < (0.012*pt + 6.0)) && (hcalTowerSumEtConeDR03 < (0.005*pt + 4.0) && (trkSumPtHollowConeDR03 < (0.002*pt + 4.0)))"
ECALIsoCut = "ecalRecHitSumEtConeDR03 < (0.012*pt + 6.0)"
HCALIsoCut = "hcalTowerSumEtConeDR03 < (0.005*pt + 4.0)"
trackIsoCut = "trkSumPtHollowConeDR03 < (0.002*pt + 4.0)"

#ECAL, HCAL, and track only
probePhotonsPassingIsolation = cms.EDFilter(## "PhotonSelector",
    "PhotonRefSelector",
                                            src = cms.InputTag("probePhotons"),
                                            cut = cms.string(isoCuts)
                                            )

#ECAL only
probePhotonsPassingECALIsolation = cms.EDFilter("PhotonRefSelector",
                                                src = cms.InputTag("probePhotons"),
                                                cut = cms.string(ECALIsoCut)
                                                )

#HCAL only
probePhotonsPassingHCALIsolation = cms.EDFilter("PhotonRefSelector",
                                                src = cms.InputTag("probePhotons"),
                                                cut = cms.string(HCALIsoCut)
                                                )

#track only
probePhotonsPassingTrackIsolation = cms.EDFilter("PhotonRefSelector",
                                                 src = cms.InputTag("probePhotons"),
                                                 cut = cms.string(trackIsoCut)
                                                 )

#isolation sequence
iso_sequence = cms.Sequence(probePhotonsPassingIsolation + probePhotonsPassingECALIsolation +
                            probePhotonsPassingHCALIsolation + probePhotonsPassingTrackIsolation)
