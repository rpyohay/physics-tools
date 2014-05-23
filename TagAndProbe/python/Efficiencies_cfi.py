import FWCore.ParameterSet.Config as cms

#for the reused parameter sets
from PhysicsTools.TagAndProbe.Reusables_cff import *

## loose photon --> isolation
PhotonToIsolation = cms.EDAnalyzer("TagProbeFitTreeProducer",
                                   ## pick the defaults
                                   mcTruthCommonStuff,
                                   CommonStuffForPhotonProbe,
                                   # choice of tag and probe pairs, and arbitration
                                   tagProbePairs = cms.InputTag("tagPhoton"),
                                   arbitration = cms.string("BestMass"),
                                   massForArbitration = cms.double(91.2), #GeV
                                   flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingIsolation"),
    probe_passingALL_EB = cms.InputTag("probePhotonsPassingHLTEB"),
    probe_passingALL_EE = cms.InputTag("probePhotonsPassingHLTEE"),
    probe_passingIso = cms.InputTag("probePhotonsPassingIsolation"),
    probe_passingId_EB = cms.InputTag("probePhotonsPassingIdEB"),
    probe_passingId_EE = cms.InputTag("probePhotonsPassingIdEE")
    ),
                                   probeMatches = cms.InputTag("McMatchPhoton"),
                                   allProbes = cms.InputTag("probePhotons"),
                                   )
PhotonToIsolation.variables.probe_dRjet05 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet05"
    )
PhotonToIsolation.variables.probe_dRjet09 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet09"
    )
#PhotonToIsolation.variables.probe_nJets05 = cms.InputTag("JetMultiplicity05")
#PhotonToIsolation.variables.probe_nJets09 = cms.InputTag("JetMultiplicity09")

#isolated --> ID'ed photon
IsoToIdEB = cms.EDAnalyzer("TagProbeFitTreeProducer",
                           mcTruthCommonStuff,
                           CommonStuffForPhotonProbe,
                           tagProbePairs = cms.InputTag("tagIsoPhotons"),
                           arbitration = cms.string("BestMass"),
                           massForArbitration = cms.double(91.2), #GeV
                           flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingIdEB"),
    probe_passingId = cms.InputTag("probePhotonsPassingIdEB"),
    probe_passingALL = cms.InputTag("probePhotonsPassingHLTEB")
    ),
                           probeMatches = cms.InputTag("McMatchIso"),
                           allProbes = cms.InputTag("probePhotonsPassingIsolation"),
                           )
IsoToIdEB.variables.probe_dRjet05 = cms.InputTag(
    "photonPassingIsoDRToNearestIDedUncorrectedJet05"
    )
IsoToIdEB.variables.probe_dRjet09 = cms.InputTag(
    "photonPassingIsoDRToNearestIDedUncorrectedJet09"
    )
#IsoToIdEB.variables.probe_nJets05 = cms.InputTag("JetMultiplicity05ProbePassingIso")
#IsoToIdEB.variables.probe_nJets09 = cms.InputTag("JetMultiplicity09ProbePassingIso")
IsoToIdEE = IsoToIdEB.clone()
IsoToIdEE.flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingIdEE"),
    probe_passingId = cms.InputTag("probePhotonsPassingIdEE"),
    probe_passingALL = cms.InputTag("probePhotonsPassingHLTEE")
    )

#ID'ed --> HLT photon
IdToHLTEB = cms.EDAnalyzer("TagProbeFitTreeProducer",
                           mcTruthCommonStuff,
                           CommonStuffForPhotonProbe,
                           tagProbePairs = cms.InputTag("tagIdEBPhotons"),
                           arbitration = cms.string("BestMass"),
                           massForArbitration = cms.double(91.2), #GeV
                           flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingHLTEB")
    ),
                           probeMatches = cms.InputTag("McMatchIdEB"),
                           allProbes = cms.InputTag("probePhotonsPassingIdEB"),
                           )
IdToHLTEB.variables.probe_dRjet05 = cms.InputTag(
    "photonPassingIdEBDRToNearestIDedUncorrectedJet05"
    )
IdToHLTEB.variables.probe_dRjet09 = cms.InputTag(
    "photonPassingIdEBDRToNearestIDedUncorrectedJet09"
    )
#IdToHLTEB.variables.probe_nJets05 = cms.InputTag("JetMultiplicity05ProbePassingIdEB")
#IdToHLTEB.variables.probe_nJets09 = cms.InputTag("JetMultiplicity09ProbePassingIdEB")
IdToHLTEE = IdToHLTEB.clone()
IdToHLTEE.tagProbePairs = cms.InputTag("tagIdEEPhotons")
IdToHLTEE.flags = cms.PSet(probe_passing = cms.InputTag("probePhotonsPassingHLTEE"))
IdToHLTEE.probeMatches = cms.InputTag("McMatchIdEE")
IdToHLTEE.allProbes = cms.InputTag("probePhotonsPassingIdEE")
IdToHLTEE.variables.probe_dRjet05 = cms.InputTag(
    "photonPassingIdEEDRToNearestIDedUncorrectedJet05"
    )
IdToHLTEE.variables.probe_dRjet09 = cms.InputTag(
    "photonPassingIdEEDRToNearestIDedUncorrectedJet09"
    )
#IdToHLTEE.variables.probe_nJets05 = cms.InputTag("JetMultiplicity05ProbePassingIdEE")
#IdToHLTEE.variables.probe_nJets09 = cms.InputTag("JetMultiplicity09ProbePassingIdEE")

#loose --> HLT photon
PhotonToHLTEB = cms.EDAnalyzer("TagProbeFitTreeProducer",
                               mcTruthCommonStuff,
                               CommonStuffForPhotonProbe,
                               tagProbePairs = cms.InputTag("tagPhoton"),
                               arbitration = cms.string("BestMass"),
                               massForArbitration = cms.double(91.2), #GeV
                               flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingHLTEB")
    ),
                               probeMatches = cms.InputTag("McMatchPhoton"),
                               allProbes = cms.InputTag("probePhotons"),
                               )
PhotonToHLTEB.variables.probe_dRjet05 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet05"
    )
PhotonToHLTEB.variables.probe_dRjet09 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet09"
    )
#PhotonToHLTEB.variables.probe_nJets05 = cms.InputTag("JetMultiplicity05")
#PhotonToHLTEB.variables.probe_nJets09 = cms.InputTag("JetMultiplicity09")
PhotonToHLTEE = PhotonToHLTEB.clone()
PhotonToHLTEE.flags = cms.PSet(probe_passing = cms.InputTag("probePhotonsPassingHLTEE"))

#loose --> ID'ed photon, tag required to fire specific HLT
PhotonToIDEB = cms.EDAnalyzer("TagProbeFitTreeProducer",
                              mcTruthCommonStuff,
                              CommonStuffForPhotonProbe,
                              tagProbePairs = cms.InputTag("tagPhoton"),
                              arbitration = cms.string("BestMass"),
                              massForArbitration = cms.double(91.2), #GeV
                              flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingIdEB")
    ),
                              probeMatches = cms.InputTag("McMatchPhoton"),
                              allProbes = cms.InputTag("probePhotons"),
                              )
PhotonToIDEB.variables.probe_dR1jet00 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet00"
    )
PhotonToIDEB.variables.probe_dR2jet00 = cms.InputTag(
    "photonDRTo2ndNearestIDedUncorrectedJet00"
    )
PhotonToIDEB.variables.probe_dR3jet00 = cms.InputTag(
    "photonDRTo3rdNearestIDedUncorrectedJet00"
    )
PhotonToIDEB.variables.probe_dRjet03 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet03"
    )
PhotonToIDEB.variables.probe_dRjet05 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet05"
    )
PhotonToIDEB.variables.probe_dRjet07 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet07"
    )
PhotonToIDEB.variables.probe_dRjet09 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet09"
    )
PhotonToIDEB.variables.probe_nJets03 = cms.InputTag("JetMultiplicity03")
PhotonToIDEB.variables.probe_nJets05 = cms.InputTag("JetMultiplicity05")
PhotonToIDEB.variables.probe_nJets07 = cms.InputTag("JetMultiplicity07")
PhotonToIDEB.variables.probe_nJets09 = cms.InputTag("JetMultiplicity09")
PhotonToIDEE = PhotonToIDEB.clone()
PhotonToIDEE.flags = cms.PSet(probe_passing = cms.InputTag("probePhotonsPassingIdEE"))

#loose --> ID'ed photon, no trigger requirement on tag
PhotonToIDNoHLTEB = PhotonToIDEB.clone()
PhotonToIDNoHLTEB.tagProbePairs = cms.InputTag("tagPhotonNoHLT")
PhotonToIDNoHLTEE = PhotonToIDNoHLTEB.clone()
PhotonToIDNoHLTEE.flags = cms.PSet(probe_passing = cms.InputTag("probePhotonsPassingIdEE"))

#loose --> photon passing ECAL isolation, tag required to fire specific HLT
PhotonToECALIso = PhotonToIDEB.clone()
PhotonToECALIso.flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingECALIsolation")
    )

#loose --> photon passing ECAL isolation, no trigger requirement on tag
PhotonToECALIsoNoHLT = PhotonToECALIso.clone()
PhotonToECALIsoNoHLT.tagProbePairs = cms.InputTag("tagPhotonNoHLT")

#loose --> photon passing HCAL isolation, tag required to fire specific HLT
PhotonToHCALIso = PhotonToIDEB.clone()
PhotonToHCALIso.flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingHCALIsolation"),
    )

#loose --> photon passing HCAL isolation, no trigger requirement on tag
PhotonToHCALIsoNoHLT = PhotonToHCALIso.clone()
PhotonToHCALIsoNoHLT.tagProbePairs = cms.InputTag("tagPhotonNoHLT")

#loose --> photon passing H/E, tag required to fire specific HLT
PhotonToHOverE = PhotonToIDEB.clone()
PhotonToHOverE.flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingHOverE")
    )

#loose --> photon passing H/E, no trigger requirement on tag
PhotonToHOverENoHLT = PhotonToHOverE.clone()
PhotonToHOverENoHLT.tagProbePairs = cms.InputTag("tagPhotonNoHLT")

#loose --> photon passing track isolation, tag required to fire specific HLT
PhotonToTrackIso = PhotonToIDEB.clone()
PhotonToTrackIso.flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingTrackIsolation")
    )

#loose --> photon passing track isolation, no trigger requirement on tag
PhotonToTrackIsoNoHLT = PhotonToTrackIso.clone()
PhotonToTrackIsoNoHLT.tagProbePairs = cms.InputTag("tagPhotonNoHLT")

#loose --> photon passing sigmaIetaIeta, tag required to fire specific HLT
PhotonToSigmaIetaIetaEB = PhotonToIDEB.clone()
PhotonToSigmaIetaIetaEB.flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingSigmaIetaIetaEB")
    )
PhotonToSigmaIetaIetaEE = PhotonToSigmaIetaIetaEB.clone()
PhotonToSigmaIetaIetaEE.flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingSigmaIetaIetaEE")
    )

#loose --> photon passing sigmaIetaIeta, no trigger requirement on tag
PhotonToSigmaIetaIetaNoHLTEB = PhotonToSigmaIetaIetaEB.clone()
PhotonToSigmaIetaIetaNoHLTEB.tagProbePairs = cms.InputTag("tagPhotonNoHLTEB")
PhotonToSigmaIetaIetaNoHLTEE = PhotonToSigmaIetaIetaNoHLTEB.clone()
PhotonToSigmaIetaIetaNoHLTEE.flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingSigmaIetaIetaEE")
    )

#loose --> photon passing R9, tag required to fire specific HLT
PhotonToR9 = PhotonToIDEB.clone()
PhotonToR9.flags = cms.PSet(probe_passing = cms.InputTag("probePhotonsPassingR9"))

#loose --> photon passing R9, no trigger requirement on tag
PhotonToR9NoHLT = PhotonToR9.clone()
PhotonToR9NoHLT.tagProbePairs = cms.InputTag("tagPhotonNoHLT")

#loose --> ID'ed photon, tag required to fire specific HLT, only dR < 0.9 jet cleaning
PhotonToID09EB = cms.EDAnalyzer("TagProbeFitTreeProducer",
                                mcTruthCommonStuff,
                                CommonStuffForPhotonProbe,
                                tagProbePairs = cms.InputTag("tagPhoton"),
                                arbitration = cms.string("BestMass"),
                                massForArbitration = cms.double(91.2), #GeV
                                flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingIdEB")
    ),
                                probeMatches = cms.InputTag("McMatchPhoton"),
                                allProbes = cms.InputTag("probePhotons"),
                                )
PhotonToID09EB.variables.probe_dR1jet00 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet00"
    )
PhotonToID09EB.variables.probe_dR2jet00 = cms.InputTag(
    "photonDRTo2ndNearestIDedUncorrectedJet00"
    )
PhotonToID09EB.variables.probe_dR3jet00 = cms.InputTag(
    "photonDRTo3rdNearestIDedUncorrectedJet00"
    )
PhotonToID09EB.variables.probe_dRjet09 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet09"
    )
PhotonToID09EB.variables.probe_nJets09 = cms.InputTag("JetMultiplicity09")
PhotonToID09EE = PhotonToID09EB.clone()
PhotonToID09EE.flags = cms.PSet(probe_passing = cms.InputTag("probePhotonsPassingIdEE"))

#loose --> ID'ed photon, no trigger requirement on tag, only dR < 0.9 jet cleaning
PhotonToIDNoHLT09EB = PhotonToID09EB.clone()
PhotonToIDNoHLT09EB.tagProbePairs = cms.InputTag("tagPhotonNoHLT")
PhotonToIDNoHLT09EE = PhotonToIDNoHLT09EB.clone()
PhotonToIDNoHLT09EE.flags = cms.PSet(probe_passing = cms.InputTag("probePhotonsPassingIdEE"))

#loose --> photon passing ECAL isolation, tag required to fire specific HLT, only dR < 0.9 jet
#cleaning
PhotonToECALIso09 = PhotonToID09EB.clone()
PhotonToECALIso09.flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingECALIsolation")
    )

#loose --> photon passing ECAL isolation, no trigger requirement on tag, only dR < 0.9 jet cleaning
PhotonToECALIsoNoHLT09 = PhotonToECALIso09.clone()
PhotonToECALIsoNoHLT09.tagProbePairs = cms.InputTag("tagPhotonNoHLT")

#loose --> photon passing HCAL isolation, tag required to fire specific HLT, only dR < 0.9 jet
#cleaning
PhotonToHCALIso09 = PhotonToID09EB.clone()
PhotonToHCALIso09.flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingHCALIsolation"),
    )

#loose --> photon passing HCAL isolation, no trigger requirement on tag, only dR < 0.9 jet cleaning
PhotonToHCALIsoNoHLT09 = PhotonToHCALIso09.clone()
PhotonToHCALIsoNoHLT09.tagProbePairs = cms.InputTag("tagPhotonNoHLT")

#loose --> photon passing H/E, tag required to fire specific HLT, only dR < 0.9 jet cleaning
PhotonToHOverE09 = PhotonToID09EB.clone()
PhotonToHOverE09.flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingHOverE")
    )

#loose --> photon passing H/E, no trigger requirement on tag, only dR < 0.9 jet cleaning
PhotonToHOverENoHLT09 = PhotonToHOverE09.clone()
PhotonToHOverENoHLT09.tagProbePairs = cms.InputTag("tagPhotonNoHLT")

#loose --> photon passing track isolation, tag required to fire specific HLT, only dR < 0.9 jet
#cleaning
PhotonToTrackIso09 = PhotonToID09EB.clone()
PhotonToTrackIso09.flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingTrackIsolation")
    )

#loose --> photon passing track isolation, no trigger requirement on tag, only dR < 0.9 jet
#cleaning
PhotonToTrackIsoNoHLT09 = PhotonToTrackIso09.clone()
PhotonToTrackIsoNoHLT09.tagProbePairs = cms.InputTag("tagPhotonNoHLT")

#loose --> photon passing sigmaIetaIeta, tag required to fire specific HLT, only dR < 0.9 jet
#cleaning
PhotonToSigmaIetaIeta09EB = PhotonToID09EB.clone()
PhotonToSigmaIetaIeta09EB.flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingSigmaIetaIetaEB")
    )
PhotonToSigmaIetaIeta09EE = PhotonToSigmaIetaIeta09EB.clone()
PhotonToSigmaIetaIeta09EE.flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingSigmaIetaIetaEE")
    )

#loose --> photon passing sigmaIetaIeta, no trigger requirement on tag, only dR < 0.9 jet cleaning
PhotonToSigmaIetaIetaNoHLT09EB = PhotonToSigmaIetaIeta09EB.clone()
PhotonToSigmaIetaIetaNoHLT09EB.tagProbePairs = cms.InputTag("tagPhotonNoHLTEB")
PhotonToSigmaIetaIetaNoHLT09EE = PhotonToSigmaIetaIetaNoHLT09EB.clone()
PhotonToSigmaIetaIetaNoHLT09EE.flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingSigmaIetaIetaEE")
    )

#loose --> photon passing R9, tag required to fire specific HLT, only dR < 0.9 jet cleaning
PhotonToR909 = PhotonToID09EB.clone()
PhotonToR909.flags = cms.PSet(probe_passing = cms.InputTag("probePhotonsPassingR9"))

#loose --> photon passing R9, no trigger requirement on tag, only dR < 0.9 jet cleaning
PhotonToR9NoHLT09 = PhotonToR909.clone()
PhotonToR9NoHLT09.tagProbePairs = cms.InputTag("tagPhotonNoHLT")

############################### probe: SC ##################################

#SC --> ECAL isolation
SCToECALIso = cms.EDAnalyzer("TagProbeFitTreeProducer",
                             ## pick the defaults
                             mcTruthCommonStuff,
                             CommonStuffForPhotonProbe,
                             # choice of tag and probe pairs, and arbitration
                             tagProbePairs = cms.InputTag("tagSC"),
                             arbitration = cms.string("BestMass"),
                             massForArbitration = cms.double(91.2), #GeV
                             flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingECALIsolation")
    ),
                             probeMatches = cms.InputTag("McMatchPhoton"),
                             allProbes = cms.InputTag("probePhotons"),
                             )
SCToECALIso.variables.probe_dRjet03 = cms.InputTag("photonDRToNearestIDedUncorrectedJet03")
SCToECALIso.variables.probe_nJets05 = cms.InputTag("JetMultiplicity05")

#SC --> HCAL isolation
SCToHCALIso = SCToECALIso.clone()
SCToHCALIso.flags = cms.PSet(probe_passing = cms.InputTag("probePhotonsPassingHCALIsolation"))

#SC --> track isolation
SCToTrackIso = SCToECALIso.clone()
SCToTrackIso.flags = cms.PSet(probe_passing = cms.InputTag("probePhotonsPassingTrackIsolation"))

#SC --> IsoVL only
SCToIsoVLOnly = SCToECALIso.clone()
SCToIsoVLOnly.flags = cms.PSet(probe_passing = cms.InputTag("probePhotonsPassingIsolation"))

#SC --> combined isolation
SCToCombinedIso = SCToECALIso.clone()
SCToCombinedIso.flags = cms.PSet(
    probe_passing = cms.InputTag("preCombIso", "rhoCorrected", "TagProbe")
    )

#SC --> H/E
SCToHOverE = SCToECALIso.clone()
SCToHOverE.flags = cms.PSet(probe_passing = cms.InputTag("probePhotonsPassingHOverE"))

#SC --> R9
SCToR9 = SCToECALIso.clone()
SCToR9.flags = cms.PSet(probe_passing = cms.InputTag("probePhotonsPassingR9"))

#SC --> sigmaIetaIeta
SCToSigmaIetaIeta = SCToECALIso.clone()
SCToSigmaIetaIeta.flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingSigmaIetaIetaEB")
    )

#SC --> all but trigger
SCToAll = SCToECALIso.clone()
SCToAll.flags = cms.PSet(
    probe_passing = cms.InputTag("preAll", "rhoCorrected", "TagProbe")
    )

#SC --> IsoVL && R9Id
SCToIsoVLR9Id = SCToECALIso.clone()
SCToIsoVLR9Id.flags = cms.PSet(
    probe_passing = cms.InputTag("preIsoVLR9Id", "rhoCorrected", "TagProbe")
    )

#SC --> IsoVL
SCToIsoVL = SCToECALIso.clone()
SCToIsoVL.flags = cms.PSet(
    probe_passing = cms.InputTag("preIsoVL", "rhoCorrected", "TagProbe")
    )

#SC --> R9Id
SCToR9Id = SCToECALIso.clone()
SCToR9Id.flags = cms.PSet(
    probe_passing = cms.InputTag("preR9Id", "rhoCorrected", "TagProbe")
    )

############################### probe: selected photon ##################################

#IsoVL && R9Id --> 26 / 18 leading
IsoVLR9IdTo26IsoVL18Leading = SCToECALIso.clone()
IsoVLR9IdTo26IsoVL18Leading.tagProbePairs = cms.InputTag("tagIsoVLR9Id")
IsoVLR9IdTo26IsoVL18Leading.allProbes = cms.InputTag(
    "probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLR9IdEB"
    )
IsoVLR9IdTo26IsoVL18Leading.flags = cms.PSet(
    probe_passing = cms.InputTag("selectedIsoVLR9IdPhotonsPassingHLT26IsoVL18LeadingEB")
    )
IsoVLR9IdTo26IsoVL18Leading.variables.probe_dRjet03 = cms.InputTag(
    "photonPassingIsoVLR9IdDRToNearestIDedUncorrectedJet03"
    )
IsoVLR9IdTo26IsoVL18Leading.variables.probe_nJets05 = cms.InputTag(
    "JetMultiplicity05ProbePassingIsoVLR9Id"
    )

#IsoVL --> 26 / 18 leading
IsoVLTo26IsoVL18Leading = IsoVLR9IdTo26IsoVL18Leading.clone()
IsoVLTo26IsoVL18Leading.tagProbePairs = cms.InputTag("tagIsoVL")
IsoVLTo26IsoVL18Leading.allProbes = cms.InputTag(
    "probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLEB"
    )
IsoVLTo26IsoVL18Leading.flags = cms.PSet(
    probe_passing = cms.InputTag("selectedIsoVLPhotonsPassingHLT26IsoVL18LeadingEB")
    )
IsoVLTo26IsoVL18Leading.variables.probe_dRjet03 = cms.InputTag(
    "photonPassingIsoVLDRToNearestIDedUncorrectedJet03"
    )
IsoVLTo26IsoVL18Leading.variables.probe_nJets05 = cms.InputTag(
    "JetMultiplicity05ProbePassingIsoVL"
    )

#R9Id --> 26 / 18 leading
R9IdTo26IsoVL18Leading = IsoVLR9IdTo26IsoVL18Leading.clone()
R9IdTo26IsoVL18Leading.tagProbePairs = cms.InputTag("tagR9Id")
R9IdTo26IsoVL18Leading.allProbes = cms.InputTag(
    "probePhotonsPassingPUCorrectedCombinedIsoIdR9IdEB"
    )
R9IdTo26IsoVL18Leading.flags = cms.PSet(
    probe_passing = cms.InputTag("selectedR9IdPhotonsPassingHLT26IsoVL18LeadingEB")
    )
R9IdTo26IsoVL18Leading.variables.probe_dRjet03 = cms.InputTag(
    "photonPassingR9IdDRToNearestIDedUncorrectedJet03"
    )
R9IdTo26IsoVL18Leading.variables.probe_nJets05 = cms.InputTag(
    "JetMultiplicity05ProbePassingR9Id"
    )

#IsoVL && R9Id --> 26 / 18 trailing
IsoVLR9IdTo26IsoVL18Trailing = IsoVLR9IdTo26IsoVL18Leading.clone()
IsoVLR9IdTo26IsoVL18Trailing.flags = cms.PSet(
    probe_passing = cms.InputTag("selectedIsoVLR9IdPhotonsPassingHLT26IsoVL18TrailingEB")
    )

#IsoVL --> 26 / 18 trailing
IsoVLTo26IsoVL18Trailing = IsoVLTo26IsoVL18Leading.clone()
IsoVLTo26IsoVL18Trailing.flags = cms.PSet(
    probe_passing = cms.InputTag("selectedIsoVLPhotonsPassingHLT26IsoVL18TrailingEB")
    )

#R9Id --> 26 / 18 trailing
R9IdTo26IsoVL18Trailing = R9IdTo26IsoVL18Leading.clone()
R9IdTo26IsoVL18Trailing.flags = cms.PSet(
    probe_passing = cms.InputTag("selectedR9IdPhotonsPassingHLT26IsoVL18TrailingEB")
    )

#IsoVL && R9Id --> 36 / 22 leading
IsoVLR9IdTo36CaloIdL22CaloIdLLeading = IsoVLR9IdTo26IsoVL18Leading.clone()
IsoVLR9IdTo36CaloIdL22CaloIdLLeading.flags = cms.PSet(
    probe_passing = cms.InputTag("selectedIsoVLR9IdPhotonsPassingHLT36CaloIdL22CaloIdLLeadingEB")
    )

#IsoVL --> 36 / 22 leading
IsoVLTo36CaloIdL22CaloIdLLeading = IsoVLTo26IsoVL18Leading.clone()
IsoVLTo36CaloIdL22CaloIdLLeading.flags = cms.PSet(
    probe_passing = cms.InputTag("selectedIsoVLPhotonsPassingHLT36CaloIdL22CaloIdLLeadingEB")
    )

#R9Id --> 36 / 22 leading
R9IdTo36CaloIdL22CaloIdLLeading = R9IdTo26IsoVL18Leading.clone()
R9IdTo36CaloIdL22CaloIdLLeading.flags = cms.PSet(
    probe_passing = cms.InputTag("selectedR9IdPhotonsPassingHLT36CaloIdL22CaloIdLLeadingEB")
    )

#IsoVL && R9Id --> 36 / 22 trailing
IsoVLR9IdTo36CaloIdL22CaloIdLTrailing = IsoVLR9IdTo36CaloIdL22CaloIdLLeading.clone()
IsoVLR9IdTo36CaloIdL22CaloIdLTrailing.flags = cms.PSet(
    probe_passing = cms.InputTag("selectedIsoVLR9IdPhotonsPassingHLT36CaloIdL22CaloIdLTrailingEB")
    )

#IsoVL --> 36 / 22 trailing
IsoVLTo36CaloIdL22CaloIdLTrailing = IsoVLTo36CaloIdL22CaloIdLLeading.clone()
IsoVLTo36CaloIdL22CaloIdLTrailing.flags = cms.PSet(
    probe_passing = cms.InputTag("selectedIsoVLPhotonsPassingHLT36CaloIdL22CaloIdLTrailingEB")
    )

#R9Id --> 36 / 22 trailing
R9IdTo36CaloIdL22CaloIdLTrailing = R9IdTo36CaloIdL22CaloIdLLeading.clone()
R9IdTo36CaloIdL22CaloIdLTrailing.flags = cms.PSet(
    probe_passing = cms.InputTag("selectedR9IdPhotonsPassingHLT36CaloIdL22CaloIdLTrailingEB")
    )

#IsoVL && R9Id --> 36 IsoVL / 22 IsoVL leading
IsoVLR9IdTo36CaloIdLIsoVL22CaloIdLIsoVLLeading = IsoVLR9IdTo26IsoVL18Leading.clone()
IsoVLR9IdTo36CaloIdLIsoVL22CaloIdLIsoVLLeading.flags = cms.PSet(
    probe_passing = cms.InputTag(
    "selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLLeadingEB"
    )
    )

#IsoVL --> 36 IsoVL / 22 IsoVL leading
IsoVLTo36CaloIdLIsoVL22CaloIdLIsoVLLeading = IsoVLTo26IsoVL18Leading.clone()
IsoVLTo36CaloIdLIsoVL22CaloIdLIsoVLLeading.flags = cms.PSet(
    probe_passing = cms.InputTag(
    "selectedIsoVLPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLLeadingEB"
    )
    )

#IsoVL && R9Id --> 36 IsoVL / 22 IsoVL trailing
IsoVLR9IdTo36CaloIdLIsoVL22CaloIdLIsoVLTrailing = IsoVLR9IdTo36CaloIdL22CaloIdLLeading.clone()
IsoVLR9IdTo36CaloIdLIsoVL22CaloIdLIsoVLTrailing.flags = cms.PSet(
    probe_passing = cms.InputTag(
    "selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLTrailingEB"
    )
    )

#IsoVL --> 36 IsoVL / 22 IsoVL trailing
IsoVLTo36CaloIdLIsoVL22CaloIdLIsoVLTrailing = IsoVLTo36CaloIdL22CaloIdLLeading.clone()
IsoVLTo36CaloIdLIsoVL22CaloIdLIsoVLTrailing.flags = cms.PSet(
    probe_passing = cms.InputTag(
    "selectedIsoVLPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLTrailingEB"
    )
    )

#IsoVL && R9Id --> 36 IsoVL / 22 R9Id leading
IsoVLR9IdTo36CaloIdLIsoVL22R9IdLeading = IsoVLR9IdTo26IsoVL18Leading.clone()
IsoVLR9IdTo36CaloIdLIsoVL22R9IdLeading.flags = cms.PSet(
    probe_passing = cms.InputTag(
    "selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22R9IdLeadingEB"
    )
    )

#IsoVL --> 36 IsoVL / 22 R9Id leading
IsoVLTo36CaloIdLIsoVL22R9IdLeading = IsoVLTo26IsoVL18Leading.clone()
IsoVLTo36CaloIdLIsoVL22R9IdLeading.flags = cms.PSet(
    probe_passing = cms.InputTag(
    "selectedIsoVLPhotonsPassingHLT36CaloIdLIsoVL22R9IdLeadingEB"
    )
    )

#IsoVL && R9Id --> 36 IsoVL / 22 R9Id trailing
IsoVLR9IdTo36CaloIdLIsoVL22R9IdTrailing = IsoVLR9IdTo36CaloIdL22CaloIdLLeading.clone()
IsoVLR9IdTo36CaloIdLIsoVL22R9IdTrailing.flags = cms.PSet(
    probe_passing = cms.InputTag(
    "selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22R9IdTrailingEB"
    )
    )

#R9Id --> 36 IsoVL / 22 R9Id trailing
R9IdTo36CaloIdLIsoVL22R9IdTrailing = R9IdTo36CaloIdL22CaloIdLLeading.clone()
R9IdTo36CaloIdLIsoVL22R9IdTrailing.flags = cms.PSet(
    probe_passing = cms.InputTag(
    "selectedR9IdPhotonsPassingHLT36CaloIdLIsoVL22R9IdTrailingEB"
    )
    )

#IsoVL && R9Id --> 36 R9Id / 22 IsoVL leading
IsoVLR9IdTo36R9Id22CaloIdLIsoVLLeading = IsoVLR9IdTo26IsoVL18Leading.clone()
IsoVLR9IdTo36R9Id22CaloIdLIsoVLLeading.flags = cms.PSet(
    probe_passing = cms.InputTag(
    "selectedIsoVLR9IdPhotonsPassingHLT36R9Id22CaloIdLIsoVLLeadingEB"
    )
    )

#R9Id --> 36 R9Id / 22 IsoVL leading
R9IdTo36R9Id22CaloIdLIsoVLLeading = R9IdTo26IsoVL18Leading.clone()
R9IdTo36R9Id22CaloIdLIsoVLLeading.flags = cms.PSet(
    probe_passing = cms.InputTag(
    "selectedR9IdPhotonsPassingHLT36R9Id22CaloIdLIsoVLLeadingEB"
    )
    )

#IsoVL && R9Id --> 36 R9Id / 22 IsoVL trailing
IsoVLR9IdTo36R9Id22CaloIdLIsoVLTrailing = IsoVLR9IdTo36CaloIdL22CaloIdLLeading.clone()
IsoVLR9IdTo36R9Id22CaloIdLIsoVLTrailing.flags = cms.PSet(
    probe_passing = cms.InputTag(
    "selectedIsoVLR9IdPhotonsPassingHLT36R9Id22CaloIdLIsoVLTrailingEB"
    )
    )

#IsoVL --> 36 R9Id / 22 IsoVL trailing
IsoVLTo36R9Id22CaloIdLIsoVLTrailing = IsoVLTo36CaloIdL22CaloIdLLeading.clone()
IsoVLTo36R9Id22CaloIdLIsoVLTrailing.flags = cms.PSet(
    probe_passing = cms.InputTag(
    "selectedIsoVLPhotonsPassingHLT36R9Id22CaloIdLIsoVLTrailingEB"
    )
    )

#IsoVL && R9Id --> 36 R9Id / 22 R9Id leading
IsoVLR9IdTo36R9Id22R9IdLeading = IsoVLR9IdTo26IsoVL18Leading.clone()
IsoVLR9IdTo36R9Id22R9IdLeading.flags = cms.PSet(
    probe_passing = cms.InputTag(
    "selectedIsoVLR9IdPhotonsPassingHLT36R9Id22R9IdLeadingEB"
    )
    )

#R9Id --> 36 R9Id / 22 R9Id leading
R9IdTo36R9Id22R9IdLeading = R9IdTo26IsoVL18Leading.clone()
R9IdTo36R9Id22R9IdLeading.flags = cms.PSet(
    probe_passing = cms.InputTag(
    "selectedR9IdPhotonsPassingHLT36R9Id22R9IdLeadingEB"
    )
    )

#IsoVL && R9Id --> 36 R9Id / 22 R9Id trailing
IsoVLR9IdTo36R9Id22R9IdTrailing = IsoVLR9IdTo36CaloIdL22CaloIdLLeading.clone()
IsoVLR9IdTo36R9Id22R9IdTrailing.flags = cms.PSet(
    probe_passing = cms.InputTag(
    "selectedIsoVLR9IdPhotonsPassingHLT36R9Id22R9IdTrailingEB"
    )
    )

#R9Id --> 36 R9Id / 22 R9Id trailing
R9IdTo36R9Id22R9IdTrailing = R9IdTo36CaloIdL22CaloIdLLeading.clone()
R9IdTo36R9Id22R9IdTrailing.flags = cms.PSet(
    probe_passing = cms.InputTag(
    "selectedR9IdPhotonsPassingHLT36R9Id22R9IdTrailingEB"
    )
    )

#efficiency sequences
efficiency_sequence = cms.Sequence(PhotonToIsolation + IsoToIdEB + IdToHLTEB + PhotonToHLTEB +
                                   PhotonToIDEB + PhotonToIDNoHLTEB + PhotonToECALIso +
                                   PhotonToECALIsoNoHLT + PhotonToHCALIso + PhotonToHCALIsoNoHLT +
                                   PhotonToHOverE + PhotonToHOverENoHLT + PhotonToTrackIso +
                                   PhotonToTrackIsoNoHLT + PhotonToSigmaIetaIetaEB +
                                   PhotonToSigmaIetaIetaNoHLTEB + PhotonToR9 + PhotonToR9NoHLT +
                                   IsoToIdEE + IdToHLTEE + PhotonToHLTEE + PhotonToIDEE +
                                   PhotonToIDNoHLTEE + PhotonToSigmaIetaIetaEE +
                                   PhotonToSigmaIetaIetaNoHLTEE)
efficiency_09_sequence = cms.Sequence(PhotonToIsolation + IsoToIdEB + IdToHLTEB + PhotonToHLTEB +
                                      PhotonToID09EB + PhotonToIDNoHLT09EB + PhotonToECALIso09 +
                                      PhotonToECALIsoNoHLT09 + PhotonToHCALIso09 +
                                      PhotonToHCALIsoNoHLT09 + PhotonToHOverE09 +
                                      PhotonToHOverENoHLT09 + PhotonToTrackIso09 +
                                      PhotonToTrackIsoNoHLT09 + PhotonToSigmaIetaIeta09EB +
                                      PhotonToSigmaIetaIetaNoHLT09EB + PhotonToR909 +
                                      PhotonToR9NoHLT09 + IsoToIdEE + IdToHLTEE + PhotonToHLTEE +
                                      PhotonToID09EE + PhotonToIDNoHLT09EE +
                                      PhotonToSigmaIetaIeta09EE + PhotonToSigmaIetaIetaNoHLT09EE)
no_intermediates_efficiency_sequence = cms.Sequence(PhotonToIDEB + PhotonToIDNoHLTEB +
                                                    PhotonToECALIso + PhotonToECALIsoNoHLT +
                                                    PhotonToHCALIso + PhotonToHCALIsoNoHLT +
                                                    PhotonToHOverE + PhotonToHOverENoHLT +
                                                    PhotonToTrackIso + PhotonToTrackIsoNoHLT +
                                                    PhotonToSigmaIetaIetaEB +
                                                    PhotonToSigmaIetaIetaNoHLTEB + PhotonToR9 +
                                                    PhotonToR9NoHLT + PhotonToIDEE +
                                                    PhotonToIDNoHLTEE + PhotonToSigmaIetaIetaEE +
                                                    PhotonToSigmaIetaIetaNoHLTEE)
no_intermediates_efficiency_09_sequence = cms.Sequence(PhotonToID09EB + PhotonToIDNoHLT09EB +
                                                       PhotonToECALIso09 + PhotonToECALIsoNoHLT09 +
                                                       PhotonToHCALIso09 + PhotonToHCALIsoNoHLT09 +
                                                       PhotonToHOverE09 + PhotonToHOverENoHLT09 +
                                                       PhotonToTrackIso09 +
                                                       PhotonToTrackIsoNoHLT09 +
                                                       PhotonToSigmaIetaIeta09EB +
                                                       PhotonToSigmaIetaIetaNoHLT09EB +
                                                       PhotonToR909 + PhotonToR9NoHLT09 + 
                                                       PhotonToID09EE + PhotonToIDNoHLT09EE +
                                                       PhotonToSigmaIetaIeta09EE +
                                                       PhotonToSigmaIetaIetaNoHLT09EE)
tag_HLT_efficiency_sequence = cms.Sequence(PhotonToIDEB + PhotonToECALIso + PhotonToHCALIso +
                                           PhotonToHOverE + PhotonToTrackIso +
                                           PhotonToSigmaIetaIetaEB + PhotonToR9 + PhotonToIDEE +
                                           PhotonToSigmaIetaIetaEE)
tag_HLT_efficiency_09_sequence = cms.Sequence(PhotonToID09EB + PhotonToECALIso09 +
                                              PhotonToHCALIso09 + PhotonToHOverE09 +
                                              PhotonToTrackIso09 + PhotonToSigmaIetaIeta09EB +
                                              PhotonToR909 + PhotonToID09EE +
                                              PhotonToSigmaIetaIeta09EE)
efficiency_sequence_postMay10ReReco = cms.Sequence(
    SCToECALIso + SCToHCALIso + SCToTrackIso + SCToIsoVLOnly + SCToCombinedIso + SCToHOverE + SCToR9 +
    SCToSigmaIetaIeta + SCToAll + SCToIsoVLR9Id + SCToIsoVL + SCToR9Id +
    IsoVLR9IdTo36CaloIdLIsoVL22CaloIdLIsoVLLeading + IsoVLTo36CaloIdLIsoVL22CaloIdLIsoVLLeading +
    IsoVLR9IdTo36CaloIdLIsoVL22CaloIdLIsoVLTrailing +
    IsoVLTo36CaloIdLIsoVL22CaloIdLIsoVLTrailing + IsoVLR9IdTo36CaloIdLIsoVL22R9IdLeading +
    IsoVLTo36CaloIdLIsoVL22R9IdLeading + IsoVLR9IdTo36CaloIdLIsoVL22R9IdTrailing +
    IsoVLR9IdTo36R9Id22CaloIdLIsoVLLeading +
    IsoVLR9IdTo36R9Id22CaloIdLIsoVLTrailing +
    IsoVLTo36R9Id22CaloIdLIsoVLTrailing + IsoVLR9IdTo36R9Id22R9IdLeading +
    IsoVLR9IdTo36R9Id22R9IdTrailing
    )
efficiency_sequence_2011 = cms.Sequence(
    SCToECALIso + SCToHCALIso + SCToTrackIso + SCToIsoVLOnly + SCToCombinedIso + SCToHOverE + SCToR9 +
    SCToSigmaIetaIeta + SCToAll + SCToIsoVLR9Id + SCToIsoVL + SCToR9Id +
    IsoVLR9IdTo26IsoVL18Leading + IsoVLTo26IsoVL18Leading +
    IsoVLR9IdTo26IsoVL18Trailing +
    IsoVLTo26IsoVL18Trailing +
    IsoVLR9IdTo36CaloIdL22CaloIdLLeading + IsoVLTo36CaloIdL22CaloIdLLeading +
    IsoVLR9IdTo36CaloIdL22CaloIdLTrailing +
    IsoVLTo36CaloIdL22CaloIdLTrailing +
    IsoVLR9IdTo36CaloIdLIsoVL22CaloIdLIsoVLLeading + IsoVLTo36CaloIdLIsoVL22CaloIdLIsoVLLeading +
    IsoVLR9IdTo36CaloIdLIsoVL22CaloIdLIsoVLTrailing +
    IsoVLTo36CaloIdLIsoVL22CaloIdLIsoVLTrailing + IsoVLR9IdTo36CaloIdLIsoVL22R9IdLeading +
    IsoVLTo36CaloIdLIsoVL22R9IdLeading + IsoVLR9IdTo36CaloIdLIsoVL22R9IdTrailing +
    IsoVLR9IdTo36R9Id22CaloIdLIsoVLLeading +
    IsoVLR9IdTo36R9Id22CaloIdLIsoVLTrailing +
    IsoVLTo36R9Id22CaloIdLIsoVLTrailing + IsoVLR9IdTo36R9Id22R9IdLeading +
    IsoVLR9IdTo36R9Id22R9IdTrailing
    )
