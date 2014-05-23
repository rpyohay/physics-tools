import FWCore.ParameterSet.Config as cms

#for the reused parameter sets
from PhysicsTools.TagAndProbe.Reusables_cff import *

#loose --> ID'ed photon, tag required to fire specific HLT, PU-corrected isolations
PhotonToIDPUCorrectedEB = cms.EDAnalyzer("TagProbeFitTreeProducer",
                                         dataCommonStuff,
                                         CommonStuffForPhotonProbe,
                                         tagProbePairs = cms.InputTag("tagPhoton"),
                                         arbitration = cms.string("BestMass"),
                                         massForArbitration = cms.double(91.2), #GeV
                                         flags = cms.PSet(
    probe_passing_rho = cms.InputTag(
    "probePhotonsPassingPUCorrectedIdEB", "rhoCorrected", "TagProbe"
    ),
    probe_passing_nPV = cms.InputTag(
    "probePhotonsPassingPUCorrectedIdEB", "nPVCorrected", "TagProbe"
    )
    ),
                                         probeMatches = cms.InputTag("McMatchPhoton"),
                                         allProbes = cms.InputTag("probePhotons"),
                                         )
PhotonToIDPUCorrectedEB.variables = cms.PSet(ProbePhotonVariablesToStore,
                                             PUSubtractedProbePhotonVariablesToStore)
PhotonToIDPUCorrectedEB.variables.probe_dR1jet00 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet00"
    )
PhotonToIDPUCorrectedEB.variables.probe_dR2jet00 = cms.InputTag(
    "photonDRTo2ndNearestIDedUncorrectedJet00"
    )
PhotonToIDPUCorrectedEB.variables.probe_dR3jet00 = cms.InputTag(
    "photonDRTo3rdNearestIDedUncorrectedJet00"
    )
PhotonToIDPUCorrectedEB.variables.probe_dRjet03 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet03"
    )
PhotonToIDPUCorrectedEB.variables.probe_dRjet05 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet05"
    )
PhotonToIDPUCorrectedEB.variables.probe_dRjet07 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet07"
    )
PhotonToIDPUCorrectedEB.variables.probe_dRjet09 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet09"
    )
PhotonToIDPUCorrectedEB.variables.probe_nJets03 = cms.InputTag("JetMultiplicity03")
PhotonToIDPUCorrectedEB.variables.probe_nJets05 = cms.InputTag("JetMultiplicity05")
PhotonToIDPUCorrectedEB.variables.probe_nJets07 = cms.InputTag("JetMultiplicity07")
PhotonToIDPUCorrectedEB.variables.probe_nJets09 = cms.InputTag("JetMultiplicity09")
PhotonToIDPUCorrectedEE = PhotonToIDPUCorrectedEB.clone()
PhotonToIDPUCorrectedEE.flags = cms.PSet(
    probe_passing_rho = cms.InputTag(
    "probePhotonsPassingPUCorrectedIdEE", "rhoCorrected", "TagProbe"
    ),
    probe_passing_nPV = cms.InputTag(
    "probePhotonsPassingPUCorrectedIdEE", "nPVCorrected", "TagProbe"
    )
    )

#loose --> ID'ed photon, no trigger requirement on tag, PU-corrected isolations
PhotonToIDNoHLTPUCorrectedEB = PhotonToIDPUCorrectedEB.clone()
PhotonToIDNoHLTPUCorrectedEB.tagProbePairs = cms.InputTag("tagPhotonNoHLT")
PhotonToIDNoHLTPUCorrectedEE = PhotonToIDNoHLTPUCorrectedEB.clone()
PhotonToIDNoHLTPUCorrectedEE.flags = cms.PSet(
    probe_passing_rho = cms.InputTag(
    "probePhotonsPassingPUCorrectedIdEE", "rhoCorrected", "TagProbe"
    ),
    probe_passing_nPV = cms.InputTag(
    "probePhotonsPassingPUCorrectedIdEE", "nPVCorrected", "TagProbe"
    )
    )

#loose --> photon passing ECAL isolation, tag required to fire specific HLT, PU-corrected
#isolation
PhotonToECALIsoPUCorrected = PhotonToIDPUCorrectedEB.clone()
PhotonToECALIsoPUCorrected.flags = cms.PSet(
    probe_passing_rho = cms.InputTag("probePhotonsPassingPUSubtractedECALIsolation",
                                     "rhoCorrected", "TagProbe"),
    probe_passing_nPV = cms.InputTag("probePhotonsPassingPUSubtractedECALIsolation",
                                     "nPVCorrected", "TagProbe")
    )

#loose --> photon passing ECAL isolation, no trigger requirement on tag, PU-corrected isolation
PhotonToECALIsoNoHLTPUCorrected = PhotonToECALIsoPUCorrected.clone()
PhotonToECALIsoNoHLTPUCorrected.tagProbePairs = cms.InputTag("tagPhotonNoHLT")

#loose --> photon passing HCAL isolation, tag required to fire specific HLT, PU-corrected isolation
PhotonToHCALIsoPUCorrected = PhotonToIDPUCorrectedEB.clone()
PhotonToHCALIsoPUCorrected.flags = cms.PSet(
    probe_passing_rho = cms.InputTag("probePhotonsPassingPUSubtractedHCALIsolation",
                                     "rhoCorrected", "TagProbe"),
    probe_passing_nPV = cms.InputTag("probePhotonsPassingPUSubtractedHCALIsolation",
                                     "nPVCorrected", "TagProbe")
    )

#loose --> photon passing HCAL isolation, no trigger requirement on tag, PU-corrected isolation
PhotonToHCALIsoNoHLTPUCorrected = PhotonToHCALIsoPUCorrected.clone()
PhotonToHCALIsoNoHLTPUCorrected.tagProbePairs = cms.InputTag("tagPhotonNoHLT")

#loose --> ID'ed photon, tag required to fire specific HLT, only dR < 0.9 jet cleaning,
#PU-corrected isolations
PhotonToIDPUCorrected09EB = cms.EDAnalyzer("TagProbeFitTreeProducer",
                                           dataCommonStuff,
                                           CommonStuffForPhotonProbe,
                                           tagProbePairs = cms.InputTag("tagPhoton"),
                                           arbitration = cms.string("BestMass"),
                                           massForArbitration = cms.double(91.2), #GeV
                                           flags = cms.PSet(
    probe_passing_rho = cms.InputTag(
    "probePhotonsPassingPUCorrectedIdEB", "rhoCorrected", "TagProbe"
    ),
    probe_passing_nPV = cms.InputTag(
    "probePhotonsPassingPUCorrectedIdEB", "nPVCorrected", "TagProbe"
    )
    ),
                                           probeMatches = cms.InputTag("McMatchPhoton"),
                                           allProbes = cms.InputTag("probePhotons"),
                                           )
PhotonToIDPUCorrected09EB.variables = cms.PSet(ProbePhotonVariablesToStore,
                                               PUSubtractedProbePhotonVariablesToStore)
PhotonToIDPUCorrected09EB.variables.probe_dR1jet00 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet00"
    )
PhotonToIDPUCorrected09EB.variables.probe_dR2jet00 = cms.InputTag(
    "photonDRTo2ndNearestIDedUncorrectedJet00"
    )
PhotonToIDPUCorrected09EB.variables.probe_dR3jet00 = cms.InputTag(
    "photonDRTo3rdNearestIDedUncorrectedJet00"
    )
PhotonToIDPUCorrected09EB.variables.probe_dRjet09 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet09"
    )
PhotonToIDPUCorrected09EB.variables.probe_nJets09 = cms.InputTag("JetMultiplicity09")
PhotonToIDPUCorrected09EE = PhotonToIDPUCorrected09EB.clone()
PhotonToIDPUCorrected09EE.flags = cms.PSet(
    probe_passing_rho = cms.InputTag(
    "probePhotonsPassingPUCorrectedIdEE", "rhoCorrected", "TagProbe"
    ),
    probe_passing_nPV = cms.InputTag(
    "probePhotonsPassingPUCorrectedIdEE", "nPVCorrected", "TagProbe"
    )
    )

#loose --> ID'ed photon, no trigger requirement on tag, only dR < 0.9 jet cleaning, PU-corrected
#isolations
PhotonToIDNoHLTPUCorrected09EB = PhotonToIDPUCorrected09EB.clone()
PhotonToIDNoHLTPUCorrected09EB.tagProbePairs = cms.InputTag("tagPhotonNoHLT")
PhotonToIDNoHLTPUCorrected09EE = PhotonToIDNoHLTPUCorrected09EB.clone()
PhotonToIDNoHLTPUCorrected09EE.flags = cms.PSet(
    probe_passing_rho = cms.InputTag(
    "probePhotonsPassingPUCorrectedIdEE", "rhoCorrected", "TagProbe"
    ),
    probe_passing_nPV = cms.InputTag(
    "probePhotonsPassingPUCorrectedIdEE", "nPVCorrected", "TagProbe"
    )
    )

#loose --> photon passing ECAL isolation, tag required to fire specific HLT, only dR < 0.9 jet
#cleaning, PU-corrected isolation
PhotonToECALIsoPUCorrected09 = PhotonToIDPUCorrected09EB.clone()
PhotonToECALIsoPUCorrected09.flags = cms.PSet(
    probe_passing_rho = cms.InputTag("probePhotonsPassingPUSubtractedECALIsolation",
                                     "rhoCorrected", "TagProbe"),
    probe_passing_nPV = cms.InputTag("probePhotonsPassingPUSubtractedECALIsolation",
                                     "nPVCorrected", "TagProbe")
    )

#loose --> photon passing ECAL isolation, no trigger requirement on tag, only dR < 0.9 jet
#cleaning, PU-corrected isolation
PhotonToECALIsoNoHLTPUCorrected09 = PhotonToECALIsoPUCorrected09.clone()
PhotonToECALIsoNoHLTPUCorrected09.tagProbePairs = cms.InputTag("tagPhotonNoHLT")

#loose --> photon passing HCAL isolation, tag required to fire specific HLT, only dR < 0.9 jet
#cleaning, PU-corrected isolation
PhotonToHCALIsoPUCorrected09 = PhotonToIDPUCorrected09EB.clone()
PhotonToHCALIsoPUCorrected09.flags = cms.PSet(
    probe_passing_rho = cms.InputTag("probePhotonsPassingPUSubtractedHCALIsolation",
                                     "rhoCorrected", "TagProbe"),
    probe_passing_nPV = cms.InputTag("probePhotonsPassingPUSubtractedHCALIsolation",
                                     "nPVCorrected", "TagProbe")
    )

#loose --> photon passing HCAL isolation, no trigger requirement on tag, only dR < 0.9 jet
#cleaning, PU-corrected isolation
PhotonToHCALIsoNoHLTPUCorrected09 = PhotonToHCALIsoPUCorrected09.clone()
PhotonToHCALIsoNoHLTPUCorrected09.tagProbePairs = cms.InputTag("tagPhotonNoHLT")

#PU-corrected efficiency sequences
PU_corrected_efficiency_sequence = cms.Sequence(PhotonToIDPUCorrectedEB +
                                                PhotonToIDNoHLTPUCorrectedEB +
                                                PhotonToECALIsoPUCorrected +
                                                PhotonToECALIsoNoHLTPUCorrected +
                                                PhotonToHCALIsoPUCorrected +
                                                PhotonToHCALIsoNoHLTPUCorrected +
                                                PhotonToIDPUCorrectedEE +
                                                PhotonToIDNoHLTPUCorrectedEE)
PU_corrected_efficiency_09_sequence = cms.Sequence(
    PhotonToIDPUCorrected09EB + PhotonToIDNoHLTPUCorrected09EB + PhotonToECALIsoPUCorrected09 +
    PhotonToECALIsoNoHLTPUCorrected09 + PhotonToHCALIsoPUCorrected09 +
    PhotonToHCALIsoNoHLTPUCorrected09 + PhotonToIDPUCorrected09EE + PhotonToIDNoHLTPUCorrected09EE
    )
PU_corrected_tag_HLT_efficiency_sequence = cms.Sequence(
    PhotonToIDPUCorrectedEB + PhotonToECALIsoPUCorrected + PhotonToHCALIsoPUCorrected +
    PhotonToIDPUCorrectedEE
    )
PU_corrected_tag_HLT_efficiency_09_sequence = cms.Sequence(
    PhotonToIDPUCorrected09EB + PhotonToECALIsoPUCorrected09 + PhotonToHCALIsoPUCorrected09 +
    PhotonToIDPUCorrected09EE
    )
test_sequence = cms.Sequence(PhotonToECALIsoPUCorrected)
