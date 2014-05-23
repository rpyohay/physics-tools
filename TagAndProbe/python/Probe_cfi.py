import FWCore.ParameterSet.Config as cms

#configurable probe definition
probeDef = "(hadronicOverEm < 0.1) && (et > 35.0) && ((abs(superCluster.eta) < 1.4442) || ((abs(superCluster.eta) > 1.566) && (abs(superCluster.eta) < 2.5)))"

#basic probe photon selection
probePhotons = cms.EDFilter("PhotonSelector",
                            src = cms.InputTag("photons", "", "RECO"),
                            cut = cms.string(probeDef)
                            )

#probe sequences
probe_sequence = cms.Sequence(probePhotons)
