import FWCore.ParameterSet.Config as cms

#configurable jet collection names and cuts
JET_COLL_00 = "ak5JPTJetsL2L300"
JET_COLL_03 = "ak5JPTJetsL2L303"
JET_COLL_05 = "ak5JPTJetsL2L305"
JET_COLL_07 = "ak5JPTJetsL2L307"
JET_COLL_09 = "ak5JPTJetsL2L309"
JET_COLL_00_PROBE_PASSING_ISO = "ak5JPTJetsL2L300ProbePassingIso"
JET_COLL_03_PROBE_PASSING_ISO = "ak5JPTJetsL2L303ProbePassingIso"
JET_COLL_05_PROBE_PASSING_ISO = "ak5JPTJetsL2L305ProbePassingIso"
JET_COLL_07_PROBE_PASSING_ISO = "ak5JPTJetsL2L307ProbePassingIso"
JET_COLL_09_PROBE_PASSING_ISO = "ak5JPTJetsL2L309ProbePassingIso"
JET_COLL_00_PROBE_PASSING_ID_EB = "ak5JPTJetsL2L300ProbePassingIdEB"
JET_COLL_03_PROBE_PASSING_ID_EB = "ak5JPTJetsL2L303ProbePassingIdEB"
JET_COLL_05_PROBE_PASSING_ID_EB = "ak5JPTJetsL2L305ProbePassingIdEB"
JET_COLL_07_PROBE_PASSING_ID_EB = "ak5JPTJetsL2L307ProbePassingIdEB"
JET_COLL_09_PROBE_PASSING_ID_EB = "ak5JPTJetsL2L309ProbePassingIdEB"
JET_COLL_00_PROBE_PASSING_ID_EE = "ak5JPTJetsL2L300ProbePassingIdEE"
JET_COLL_03_PROBE_PASSING_ID_EE = "ak5JPTJetsL2L303ProbePassingIdEE"
JET_COLL_05_PROBE_PASSING_ID_EE = "ak5JPTJetsL2L305ProbePassingIdEE"
JET_COLL_07_PROBE_PASSING_ID_EE = "ak5JPTJetsL2L307ProbePassingIdEE"
JET_COLL_09_PROBE_PASSING_ID_EE = "ak5JPTJetsL2L309ProbePassingIdEE"
JET_CUTS = "pt > 30.0"
JET_CUTS_00 = "pt > 0.0"

#for the JPT L2L3 corrections
from JetMETCorrections.Configuration.DefaultJEC_cff import *
ak5JPTJetsL2L3 = cms.EDProducer("JPTJetCorrectionProducer",
                                src = cms.InputTag("JetPlusTrackZSPCorJetAntiKt5"),
                                correctors = cms.vstring("ak5JPTL2L3")
                                )

#photons to clean from jet collection: probes and tags in a tag-probe pair
probesAndTagsToRemove = cms.EDProducer("ProbeMaker",
                                       tagProbePairs = cms.InputTag("tagSC"),
                                       arbitration = cms.string("BestMass"),
                                       massForArbitration = cms.double(91.2) #GeV
                                       )
probesPassingIsoAndTagsToRemove = probesAndTagsToRemove.clone()
probesPassingIsoAndTagsToRemove.tagProbePairs = cms.InputTag("tagIsoPhotons")
probesPassingIdEBAndTagsToRemove = probesAndTagsToRemove.clone()
probesPassingIdEBAndTagsToRemove.tagProbePairs = cms.InputTag("tagIdEBPhotons")
probesPassingIdEEAndTagsToRemove = probesAndTagsToRemove.clone()
probesPassingIdEEAndTagsToRemove.tagProbePairs = cms.InputTag("tagIdEEPhotons")
probesPassingIsoVLR9IdAndTagsToRemove = probesAndTagsToRemove.clone()
probesPassingIsoVLR9IdAndTagsToRemove.tagProbePairs = cms.InputTag("tagIsoVLR9Id")
probesPassingIsoVLAndTagsToRemove = probesAndTagsToRemove.clone()
probesPassingIsoVLAndTagsToRemove.tagProbePairs = cms.InputTag("tagIsoVL")
probesPassingR9IdAndTagsToRemove = probesAndTagsToRemove.clone()
probesPassingR9IdAndTagsToRemove.tagProbePairs = cms.InputTag("tagR9Id")

#producer of dR < 0.0 photon-cleaned jets
#passing LOOSE PURE09 jet ID (https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID)
IDedJetProducer00 = cms.EDProducer(
    "IDedJetProducer",
    caloJetSrc = cms.InputTag("ak5CaloJets", "", "RECO"),
    jetIDSrc = cms.InputTag("ak5JetID", "", "RECO"),
    JPTJetSrc = cms.InputTag("JetPlusTrackZSPCorJetAntiKt5", "", "RECO"),
    photonSrc = cms.InputTag("probesAndTagsToRemove"),
    cleaningDR = cms.double(0.0),
    maxAbsEta = cms.double(2.6)
    )
IDedJetProducer00ProbePassingIso = IDedJetProducer00.clone()
IDedJetProducer00ProbePassingIso.photonSrc = cms.InputTag("probesPassingIsoAndTagsToRemove")
IDedJetProducer00ProbePassingIdEB = IDedJetProducer00.clone()
IDedJetProducer00ProbePassingIdEB.photonSrc = cms.InputTag("probesPassingIdEBAndTagsToRemove")
IDedJetProducer00ProbePassingIdEE = IDedJetProducer00.clone()
IDedJetProducer00ProbePassingIdEE.photonSrc = cms.InputTag("probesPassingIdEEAndTagsToRemove")

#producer of dR < 0.3 photon-cleaned jets
#passing LOOSE PURE09 jet ID (https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID)
IDedJetProducer03 = cms.EDProducer(
    "IDedJetProducer",
    caloJetSrc = cms.InputTag("ak5CaloJets", "", "RECO"),
    jetIDSrc = cms.InputTag("ak5JetID", "", "RECO"),
    JPTJetSrc = cms.InputTag("JetPlusTrackZSPCorJetAntiKt5", "", "RECO"),
    photonSrc = cms.InputTag("probesAndTagsToRemove"),
    cleaningDR = cms.double(0.3),
    maxAbsEta = cms.double(2.6)
    )
IDedJetProducer03ProbePassingIso = IDedJetProducer00.clone()
IDedJetProducer03ProbePassingIso.photonSrc = cms.InputTag("probesPassingIsoAndTagsToRemove")
IDedJetProducer03ProbePassingIdEB = IDedJetProducer00.clone()
IDedJetProducer03ProbePassingIdEB.photonSrc = cms.InputTag("probesPassingIdEBAndTagsToRemove")
IDedJetProducer03ProbePassingIdEE = IDedJetProducer00.clone()
IDedJetProducer03ProbePassingIdEE.photonSrc = cms.InputTag("probesPassingIdEEAndTagsToRemove")

#producer of dR < 0.5 photon-cleaned jets
#passing LOOSE PURE09 jet ID (https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID)
IDedJetProducer05 = cms.EDProducer(
    "IDedJetProducer",
    caloJetSrc = cms.InputTag("ak5CaloJets", "", "RECO"),
    jetIDSrc = cms.InputTag("ak5JetID", "", "RECO"),
    JPTJetSrc = cms.InputTag("JetPlusTrackZSPCorJetAntiKt5", "", "RECO"),
    photonSrc = cms.InputTag("probesAndTagsToRemove"),
    cleaningDR = cms.double(0.5),
    maxAbsEta = cms.double(2.6)
    )
IDedJetProducer05ProbePassingIso = IDedJetProducer00.clone()
IDedJetProducer05ProbePassingIso.photonSrc = cms.InputTag("probesPassingIsoAndTagsToRemove")
IDedJetProducer05ProbePassingIdEB = IDedJetProducer00.clone()
IDedJetProducer05ProbePassingIdEB.photonSrc = cms.InputTag("probesPassingIdEBAndTagsToRemove")
IDedJetProducer05ProbePassingIdEE = IDedJetProducer00.clone()
IDedJetProducer05ProbePassingIdEE.photonSrc = cms.InputTag("probesPassingIdEEAndTagsToRemove")

#producer of dR < 0.7 photon-cleaned jets
#passing LOOSE PURE09 jet ID (https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID)
IDedJetProducer07 = cms.EDProducer(
    "IDedJetProducer",
    caloJetSrc = cms.InputTag("ak5CaloJets", "", "RECO"),
    jetIDSrc = cms.InputTag("ak5JetID", "", "RECO"),
    JPTJetSrc = cms.InputTag("JetPlusTrackZSPCorJetAntiKt5", "", "RECO"),
    photonSrc = cms.InputTag("probesAndTagsToRemove"),
    cleaningDR = cms.double(0.7),
    maxAbsEta = cms.double(2.6)
    )
IDedJetProducer07ProbePassingIso = IDedJetProducer00.clone()
IDedJetProducer07ProbePassingIso.photonSrc = cms.InputTag("probesPassingIsoAndTagsToRemove")
IDedJetProducer07ProbePassingIdEB = IDedJetProducer00.clone()
IDedJetProducer07ProbePassingIdEB.photonSrc = cms.InputTag("probesPassingIdEBAndTagsToRemove")
IDedJetProducer07ProbePassingIdEE = IDedJetProducer00.clone()
IDedJetProducer07ProbePassingIdEE.photonSrc = cms.InputTag("probesPassingIdEEAndTagsToRemove")

#producer of dR < 0.9 photon-cleaned jets
#passing LOOSE PURE09 jet ID (https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID)
IDedJetProducer09 = cms.EDProducer(
    "IDedJetProducer",
    caloJetSrc = cms.InputTag("ak5CaloJets", "", "RECO"),
    jetIDSrc = cms.InputTag("ak5JetID", "", "RECO"),
    JPTJetSrc = cms.InputTag("JetPlusTrackZSPCorJetAntiKt5", "", "RECO"),
    photonSrc = cms.InputTag("probesAndTagsToRemove"),
    cleaningDR = cms.double(0.9),
    maxAbsEta = cms.double(2.6)
    )
IDedJetProducer09ProbePassingIso = IDedJetProducer00.clone()
IDedJetProducer09ProbePassingIso.photonSrc = cms.InputTag("probesPassingIsoAndTagsToRemove")
IDedJetProducer09ProbePassingIdEB = IDedJetProducer00.clone()
IDedJetProducer09ProbePassingIdEB.photonSrc = cms.InputTag("probesPassingIdEBAndTagsToRemove")
IDedJetProducer09ProbePassingIdEE = IDedJetProducer00.clone()
IDedJetProducer09ProbePassingIdEE.photonSrc = cms.InputTag("probesPassingIdEEAndTagsToRemove")

#produce corrected jet collection from IDed and dR < 0.0 cross-cleaned jet collection
ak5JPTJetsL2L300 = ak5JPTJetsL2L3.clone()
ak5JPTJetsL2L300.src = cms.InputTag("IDedJetProducer00")
ak5JPTJetsL2L300ProbePassingIso = ak5JPTJetsL2L3.clone()
ak5JPTJetsL2L300ProbePassingIso.src = cms.InputTag("IDedJetProducer00ProbePassingIso")
ak5JPTJetsL2L300ProbePassingIdEB = ak5JPTJetsL2L3.clone()
ak5JPTJetsL2L300ProbePassingIdEB.src = cms.InputTag("IDedJetProducer00ProbePassingIdEB")
ak5JPTJetsL2L300ProbePassingIdEE = ak5JPTJetsL2L3.clone()
ak5JPTJetsL2L300ProbePassingIdEE.src = cms.InputTag("IDedJetProducer00ProbePassingIdEE")

#produce corrected jet collection from IDed and dR < 0.3 cross-cleaned jet collection
ak5JPTJetsL2L303 = ak5JPTJetsL2L3.clone()
ak5JPTJetsL2L303.src = cms.InputTag("IDedJetProducer03")
ak5JPTJetsL2L303ProbePassingIso = ak5JPTJetsL2L3.clone()
ak5JPTJetsL2L303ProbePassingIso.src = cms.InputTag("IDedJetProducer00ProbePassingIso")
ak5JPTJetsL2L303ProbePassingIdEB = ak5JPTJetsL2L3.clone()
ak5JPTJetsL2L303ProbePassingIdEB.src = cms.InputTag("IDedJetProducer00ProbePassingIdEB")
ak5JPTJetsL2L303ProbePassingIdEE = ak5JPTJetsL2L3.clone()
ak5JPTJetsL2L303ProbePassingIdEE.src = cms.InputTag("IDedJetProducer00ProbePassingIdEE")

#produce corrected jet collection from IDed and dR < 0.5 cross-cleaned jet collection
ak5JPTJetsL2L305 = ak5JPTJetsL2L3.clone()
ak5JPTJetsL2L305.src = cms.InputTag("IDedJetProducer05")
ak5JPTJetsL2L305ProbePassingIso = ak5JPTJetsL2L3.clone()
ak5JPTJetsL2L305ProbePassingIso.src = cms.InputTag("IDedJetProducer00ProbePassingIso")
ak5JPTJetsL2L305ProbePassingIdEB = ak5JPTJetsL2L3.clone()
ak5JPTJetsL2L305ProbePassingIdEB.src = cms.InputTag("IDedJetProducer00ProbePassingIdEB")
ak5JPTJetsL2L305ProbePassingIdEE = ak5JPTJetsL2L3.clone()
ak5JPTJetsL2L305ProbePassingIdEE.src = cms.InputTag("IDedJetProducer00ProbePassingIdEE")

#produce corrected jet collection from IDed and dR < 0.7 cross-cleaned jet collection
ak5JPTJetsL2L307 = ak5JPTJetsL2L3.clone()
ak5JPTJetsL2L307.src = cms.InputTag("IDedJetProducer07")
ak5JPTJetsL2L307ProbePassingIso = ak5JPTJetsL2L3.clone()
ak5JPTJetsL2L307ProbePassingIso.src = cms.InputTag("IDedJetProducer00ProbePassingIso")
ak5JPTJetsL2L307ProbePassingIdEB = ak5JPTJetsL2L3.clone()
ak5JPTJetsL2L307ProbePassingIdEB.src = cms.InputTag("IDedJetProducer00ProbePassingIdEB")
ak5JPTJetsL2L307ProbePassingIdEE = ak5JPTJetsL2L3.clone()
ak5JPTJetsL2L307ProbePassingIdEE.src = cms.InputTag("IDedJetProducer00ProbePassingIdEE")

#produce corrected jet collection from IDed and dR < 0.9 cross-cleaned jet collection
ak5JPTJetsL2L309 = ak5JPTJetsL2L3.clone()
ak5JPTJetsL2L309.src = cms.InputTag("IDedJetProducer09")
ak5JPTJetsL2L309ProbePassingIso = ak5JPTJetsL2L3.clone()
ak5JPTJetsL2L309ProbePassingIso.src = cms.InputTag("IDedJetProducer00ProbePassingIso")
ak5JPTJetsL2L309ProbePassingIdEB = ak5JPTJetsL2L3.clone()
ak5JPTJetsL2L309ProbePassingIdEB.src = cms.InputTag("IDedJetProducer00ProbePassingIdEB")
ak5JPTJetsL2L309ProbePassingIdEE = ak5JPTJetsL2L3.clone()
ak5JPTJetsL2L309ProbePassingIdEE.src = cms.InputTag("IDedJetProducer00ProbePassingIdEE")

#produce dR(photon, nearest IDed uncorrected jet passing cuts on corrected eta)
#use jets cleaned with dR = 0.0 algorithm
photonDRToNearestIDedUncorrectedJet00 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(JET_COLL_00),
    objectSelection = cms.string(JET_CUTS_00),
    minDR = cms.double(0.0)
)
photonPassingIsoDRToNearestIDedUncorrectedJet00 = photonDRToNearestIDedUncorrectedJet00.clone()
photonPassingIsoDRToNearestIDedUncorrectedJet00.probes = cms.InputTag(
    "probePhotonsPassingIsolation"
    )
photonPassingIsoDRToNearestIDedUncorrectedJet00.objects = cms.InputTag(
    JET_COLL_00_PROBE_PASSING_ISO
    )
photonPassingIdEBDRToNearestIDedUncorrectedJet00 = photonDRToNearestIDedUncorrectedJet00.clone()
photonPassingIdEBDRToNearestIDedUncorrectedJet00.probes = cms.InputTag(
    "probePhotonsPassingIdEB"
    )
photonPassingIdEBDRToNearestIDedUncorrectedJet00.objects = cms.InputTag(
    JET_COLL_00_PROBE_PASSING_ID_EB
    )
photonPassingIdEEDRToNearestIDedUncorrectedJet00 = photonDRToNearestIDedUncorrectedJet00.clone()
photonPassingIdEEDRToNearestIDedUncorrectedJet00.probes = cms.InputTag(
    "probePhotonsPassingIdEE"
    )
photonPassingIdEEDRToNearestIDedUncorrectedJet00.objects = cms.InputTag(
    JET_COLL_00_PROBE_PASSING_ID_EE
    )

#produce dR(photon, 2nd nearest IDed uncorrected jet passing cuts on corrected eta)
#use jets cleaned with dR = 0.0 algorithm
photonDRTo2ndNearestIDedUncorrectedJet00 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(JET_COLL_00),
    objectSelection = cms.string(JET_CUTS_00),
    minDR = cms.double(0.0),
    pos = cms.untracked.uint32(1)
)
photonPassingIsoDRTo2ndNearestIDedUncorrectedJet00 = photonDRTo2ndNearestIDedUncorrectedJet00.clone()
photonPassingIsoDRTo2ndNearestIDedUncorrectedJet00.probes = cms.InputTag(
    "probePhotonsPassingIsolation"
    )
photonPassingIsoDRTo2ndNearestIDedUncorrectedJet00.objects = cms.InputTag(
    JET_COLL_00_PROBE_PASSING_ISO
    )
photonPassingIdEBDRTo2ndNearestIDedUncorrectedJet00 = photonDRTo2ndNearestIDedUncorrectedJet00.clone()
photonPassingIdEBDRTo2ndNearestIDedUncorrectedJet00.probes = cms.InputTag(
    "probePhotonsPassingIdEB"
    )
photonPassingIdEBDRTo2ndNearestIDedUncorrectedJet00.objects = cms.InputTag(
    JET_COLL_00_PROBE_PASSING_ID_EB
    )
photonPassingIdEEDRTo2ndNearestIDedUncorrectedJet00 = photonDRTo2ndNearestIDedUncorrectedJet00.clone()
photonPassingIdEEDRTo2ndNearestIDedUncorrectedJet00.probes = cms.InputTag(
    "probePhotonsPassingIdEE"
    )
photonPassingIdEEDRTo2ndNearestIDedUncorrectedJet00.objects = cms.InputTag(
    JET_COLL_00_PROBE_PASSING_ID_EE
    )

#produce dR(photon, 3rd nearest IDed uncorrected jet passing cuts on corrected eta)
#use jets cleaned with dR = 0.0 algorithm
photonDRTo3rdNearestIDedUncorrectedJet00 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(JET_COLL_00),
    objectSelection = cms.string(JET_CUTS_00),
    minDR = cms.double(0.0),
    pos = cms.untracked.uint32(2)                                                           
)
photonPassingIsoDRTo3rdNearestIDedUncorrectedJet00 = photonDRTo3rdNearestIDedUncorrectedJet00.clone()
photonPassingIsoDRTo3rdNearestIDedUncorrectedJet00.probes = cms.InputTag(
    "probePhotonsPassingIsolation"
    )
photonPassingIsoDRTo3rdNearestIDedUncorrectedJet00.objects = cms.InputTag(
    JET_COLL_00_PROBE_PASSING_ISO
    )
photonPassingIdEBDRTo3rdNearestIDedUncorrectedJet00 = photonDRTo3rdNearestIDedUncorrectedJet00.clone()
photonPassingIdEBDRTo3rdNearestIDedUncorrectedJet00.probes = cms.InputTag(
    "probePhotonsPassingIdEB"
    )
photonPassingIdEBDRTo3rdNearestIDedUncorrectedJet00.objects = cms.InputTag(
    JET_COLL_00_PROBE_PASSING_ID_EB
    )
photonPassingIdEEDRTo3rdNearestIDedUncorrectedJet00 = photonDRTo3rdNearestIDedUncorrectedJet00.clone()
photonPassingIdEEDRTo3rdNearestIDedUncorrectedJet00.probes = cms.InputTag(
    "probePhotonsPassingIdEE"
    )
photonPassingIdEEDRTo3rdNearestIDedUncorrectedJet00.objects = cms.InputTag(
    JET_COLL_00_PROBE_PASSING_ID_EE
    )

#produce dR(photon, nearest IDed uncorrected jet passing cuts on corrected eta and pT)
#use jets cleaned with dR = 0.3 algorithm
photonDRToNearestIDedUncorrectedJet03 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(JET_COLL_03),
    objectSelection = cms.string(JET_CUTS),
    minDR = cms.double(0.0)
)
photonPassingIsoDRToNearestIDedUncorrectedJet03 = photonDRToNearestIDedUncorrectedJet03.clone()
photonPassingIsoDRToNearestIDedUncorrectedJet03.probes = cms.InputTag(
    "probePhotonsPassingIsolation"
    )
photonPassingIsoDRToNearestIDedUncorrectedJet03.objects = cms.InputTag(
    JET_COLL_03_PROBE_PASSING_ISO
    )
photonPassingIdEBDRToNearestIDedUncorrectedJet03 = photonDRToNearestIDedUncorrectedJet03.clone()
photonPassingIdEBDRToNearestIDedUncorrectedJet03.probes = cms.InputTag(
    "probePhotonsPassingIdEB"
    )
photonPassingIdEBDRToNearestIDedUncorrectedJet03.objects = cms.InputTag(
    JET_COLL_03_PROBE_PASSING_ID_EB
    )
photonPassingIdEEDRToNearestIDedUncorrectedJet03 = photonDRToNearestIDedUncorrectedJet03.clone()
photonPassingIdEEDRToNearestIDedUncorrectedJet03.probes = cms.InputTag(
    "probePhotonsPassingIdEE"
    )
photonPassingIdEEDRToNearestIDedUncorrectedJet03.objects = cms.InputTag(
    JET_COLL_03_PROBE_PASSING_ID_EE
    )

#produce dR(photon, nearest IDed uncorrected jet passing cuts on corrected eta and pT)
#use jets cleaned with dR = 0.5 algorithm
photonDRToNearestIDedUncorrectedJet05 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(JET_COLL_05),
    objectSelection = cms.string(JET_CUTS),
    minDR = cms.double(0.0)
)
photonPassingIsoDRToNearestIDedUncorrectedJet05 = photonDRToNearestIDedUncorrectedJet05.clone()
photonPassingIsoDRToNearestIDedUncorrectedJet05.probes = cms.InputTag(
    "probePhotonsPassingIsolation"
    )
photonPassingIsoDRToNearestIDedUncorrectedJet05.objects = cms.InputTag(
    JET_COLL_05_PROBE_PASSING_ISO
    )
photonPassingIdEBDRToNearestIDedUncorrectedJet05 = photonDRToNearestIDedUncorrectedJet05.clone()
photonPassingIdEBDRToNearestIDedUncorrectedJet05.probes = cms.InputTag(
    "probePhotonsPassingIdEB"
    )
photonPassingIdEBDRToNearestIDedUncorrectedJet05.objects = cms.InputTag(
    JET_COLL_05_PROBE_PASSING_ID_EB
    )
photonPassingIdEEDRToNearestIDedUncorrectedJet05 = photonDRToNearestIDedUncorrectedJet05.clone()
photonPassingIdEEDRToNearestIDedUncorrectedJet05.probes = cms.InputTag(
    "probePhotonsPassingIdEE"
    )
photonPassingIdEEDRToNearestIDedUncorrectedJet05.objects = cms.InputTag(
    JET_COLL_05_PROBE_PASSING_ID_EE
    )

#produce dR(photon, nearest IDed uncorrected jet passing cuts on corrected eta and pT)
#use jets cleaned with dR = 0.7 algorithm
photonDRToNearestIDedUncorrectedJet07 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(JET_COLL_07),
    objectSelection = cms.string(JET_CUTS),
    minDR = cms.double(0.0)
)
photonPassingIsoDRToNearestIDedUncorrectedJet07 = photonDRToNearestIDedUncorrectedJet07.clone()
photonPassingIsoDRToNearestIDedUncorrectedJet07.probes = cms.InputTag(
    "probePhotonsPassingIsolation"
    )
photonPassingIsoDRToNearestIDedUncorrectedJet07.objects = cms.InputTag(
    JET_COLL_07_PROBE_PASSING_ISO
    )
photonPassingIdEBDRToNearestIDedUncorrectedJet07 = photonDRToNearestIDedUncorrectedJet07.clone()
photonPassingIdEBDRToNearestIDedUncorrectedJet07.probes = cms.InputTag(
    "probePhotonsPassingIdEB"
    )
photonPassingIdEBDRToNearestIDedUncorrectedJet07.objects = cms.InputTag(
    JET_COLL_07_PROBE_PASSING_ID_EB
    )
photonPassingIdEEDRToNearestIDedUncorrectedJet07 = photonDRToNearestIDedUncorrectedJet07.clone()
photonPassingIdEEDRToNearestIDedUncorrectedJet07.probes = cms.InputTag(
    "probePhotonsPassingIdEE"
    )
photonPassingIdEEDRToNearestIDedUncorrectedJet07.objects = cms.InputTag(
    JET_COLL_07_PROBE_PASSING_ID_EE
    )

#produce dR(photon, nearest IDed uncorrected jet passing cuts on corrected eta and pT)
#use jets cleaned with dR = 0.9 algorithm
photonDRToNearestIDedUncorrectedJet09 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(JET_COLL_09),
    objectSelection = cms.string(JET_CUTS),
    minDR = cms.double(0.0)
)
photonPassingIsoDRToNearestIDedUncorrectedJet09 = photonDRToNearestIDedUncorrectedJet09.clone()
photonPassingIsoDRToNearestIDedUncorrectedJet09.probes = cms.InputTag(
    "probePhotonsPassingIsolation"
    )
photonPassingIsoDRToNearestIDedUncorrectedJet09.objects = cms.InputTag(
    JET_COLL_09_PROBE_PASSING_ISO
    )
photonPassingIdEBDRToNearestIDedUncorrectedJet09 = photonDRToNearestIDedUncorrectedJet09.clone()
photonPassingIdEBDRToNearestIDedUncorrectedJet09.probes = cms.InputTag(
    "probePhotonsPassingIdEB"
    )
photonPassingIdEBDRToNearestIDedUncorrectedJet09.objects = cms.InputTag(
    JET_COLL_09_PROBE_PASSING_ID_EB
    )
photonPassingIdEEDRToNearestIDedUncorrectedJet09 = photonDRToNearestIDedUncorrectedJet09.clone()
photonPassingIdEEDRToNearestIDedUncorrectedJet09.probes = cms.InputTag(
    "probePhotonsPassingIdEE"
    )
photonPassingIdEEDRToNearestIDedUncorrectedJet09.objects = cms.InputTag(
    JET_COLL_09_PROBE_PASSING_ID_EE
    )

#count IDed and dR < 0.0 cross-cleaned jets passing cuts
JetMultiplicity00 = cms.EDProducer(
    "CandMultiplicityCounter",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(JET_COLL_00),
    objectSelection = cms.string(JET_CUTS),
    )
JetMultiplicity00ProbePassingIso = JetMultiplicity00.clone()
JetMultiplicity00ProbePassingIso.probes = cms.InputTag("probePhotonsPassingIsolation")
JetMultiplicity00ProbePassingIso.objects = cms.InputTag(JET_COLL_00_PROBE_PASSING_ISO)
JetMultiplicity00ProbePassingIdEB = JetMultiplicity00.clone()
JetMultiplicity00ProbePassingIdEB.probes = cms.InputTag("probePhotonsPassingIdEB")
JetMultiplicity00ProbePassingIdEB.objects = cms.InputTag(JET_COLL_00_PROBE_PASSING_ID_EB)
JetMultiplicity00ProbePassingIdEE = JetMultiplicity00.clone()
JetMultiplicity00ProbePassingIdEE.probes = cms.InputTag("probePhotonsPassingIdEE")
JetMultiplicity00ProbePassingIdEE.objects = cms.InputTag(JET_COLL_00_PROBE_PASSING_ID_EE)

#count IDed and dR < 0.3 cross-cleaned jets passing cuts
JetMultiplicity03 = cms.EDProducer(
    "CandMultiplicityCounter",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(JET_COLL_03),
    objectSelection = cms.string(JET_CUTS),
    )
JetMultiplicity03ProbePassingIso = JetMultiplicity03.clone()
JetMultiplicity03ProbePassingIso.probes = cms.InputTag("probePhotonsPassingIsolation")
JetMultiplicity03ProbePassingIso.objects = cms.InputTag(JET_COLL_03_PROBE_PASSING_ISO)
JetMultiplicity03ProbePassingIdEB = JetMultiplicity03.clone()
JetMultiplicity03ProbePassingIdEB.probes = cms.InputTag("probePhotonsPassingIdEB")
JetMultiplicity03ProbePassingIdEB.objects = cms.InputTag(JET_COLL_03_PROBE_PASSING_ID_EB)
JetMultiplicity03ProbePassingIdEE = JetMultiplicity03.clone()
JetMultiplicity03ProbePassingIdEE.probes = cms.InputTag("probePhotonsPassingIdEE")
JetMultiplicity03ProbePassingIdEE.objects = cms.InputTag(JET_COLL_03_PROBE_PASSING_ID_EE)

#count IDed and dR < 0.5 cross-cleaned jets passing cuts
JetMultiplicity05 = cms.EDProducer(
    "CandMultiplicityCounter",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(JET_COLL_05),
    objectSelection = cms.string(JET_CUTS),
    )
JetMultiplicity05ProbePassingIso = JetMultiplicity05.clone()
JetMultiplicity05ProbePassingIso.probes = cms.InputTag("probePhotonsPassingIsolation")
JetMultiplicity05ProbePassingIso.objects = cms.InputTag(JET_COLL_05_PROBE_PASSING_ISO)
JetMultiplicity05ProbePassingIdEB = JetMultiplicity05.clone()
JetMultiplicity05ProbePassingIdEB.probes = cms.InputTag("probePhotonsPassingIdEB")
JetMultiplicity05ProbePassingIdEB.objects = cms.InputTag(JET_COLL_05_PROBE_PASSING_ID_EB)
JetMultiplicity05ProbePassingIdEE = JetMultiplicity05.clone()
JetMultiplicity05ProbePassingIdEE.probes = cms.InputTag("probePhotonsPassingIdEE")
JetMultiplicity05ProbePassingIdEE.objects = cms.InputTag(JET_COLL_05_PROBE_PASSING_ID_EE)

#count IDed and dR < 0.7 cross-cleaned jets passing cuts
JetMultiplicity07 = cms.EDProducer(
    "CandMultiplicityCounter",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(JET_COLL_07),
    objectSelection = cms.string(JET_CUTS),
    )
JetMultiplicity07ProbePassingIso = JetMultiplicity07.clone()
JetMultiplicity07ProbePassingIso.probes = cms.InputTag("probePhotonsPassingIsolation")
JetMultiplicity07ProbePassingIso.objects = cms.InputTag(JET_COLL_07_PROBE_PASSING_ISO)
JetMultiplicity07ProbePassingIdEB = JetMultiplicity07.clone()
JetMultiplicity07ProbePassingIdEB.probes = cms.InputTag("probePhotonsPassingIdEB")
JetMultiplicity07ProbePassingIdEB.objects = cms.InputTag(JET_COLL_07_PROBE_PASSING_ID_EB)
JetMultiplicity07ProbePassingIdEE = JetMultiplicity07.clone()
JetMultiplicity07ProbePassingIdEE.probes = cms.InputTag("probePhotonsPassingIdEE")
JetMultiplicity07ProbePassingIdEE.objects = cms.InputTag(JET_COLL_07_PROBE_PASSING_ID_EE)

#count IDed and dR < 0.9 cross-cleaned jets passing cuts
JetMultiplicity09 = cms.EDProducer(
    "CandMultiplicityCounter",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(JET_COLL_09),
    objectSelection = cms.string(JET_CUTS),
    )
JetMultiplicity09ProbePassingIso = JetMultiplicity09.clone()
JetMultiplicity09ProbePassingIso.probes = cms.InputTag("probePhotonsPassingIsolation")
JetMultiplicity09ProbePassingIso.objects = cms.InputTag(JET_COLL_09_PROBE_PASSING_ISO)
JetMultiplicity09ProbePassingIdEB = JetMultiplicity09.clone()
JetMultiplicity09ProbePassingIdEB.probes = cms.InputTag("probePhotonsPassingIdEB")
JetMultiplicity09ProbePassingIdEB.objects = cms.InputTag(JET_COLL_09_PROBE_PASSING_ID_EB)
JetMultiplicity09ProbePassingIdEE = JetMultiplicity09.clone()
JetMultiplicity09ProbePassingIdEE.probes = cms.InputTag("probePhotonsPassingIdEE")
JetMultiplicity09ProbePassingIdEE.objects = cms.InputTag(JET_COLL_09_PROBE_PASSING_ID_EE)

#produce dR(photon, nearest IDed uncorrected jet passing cuts on corrected eta and pT)
#use jets cleaned with dR = 0.3 algorithm
photonDRToNearestIDedUncorrectedJet03PT10 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(JET_COLL_03),
    objectSelection = cms.string("pt > 10.0"),
    minDR = cms.double(0.0)
)

#produce dR(photon, nearest IDed uncorrected jet passing cuts on corrected eta and pT)
#use jets cleaned with dR = 0.3 algorithm
photonDRToNearestIDedUncorrectedJet03PT20 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(JET_COLL_03),
    objectSelection = cms.string("pt > 20.0"),
    minDR = cms.double(0.0)
)

#jet variable sequences
jet_variable_sequence = cms.Sequence(probesAndTagsToRemove + IDedJetProducer00 +
                                     IDedJetProducer03 + IDedJetProducer05 + IDedJetProducer07 +
                                     IDedJetProducer09 + ak5JPTJetsL2L300 + ak5JPTJetsL2L303 +
                                     ak5JPTJetsL2L305 + ak5JPTJetsL2L307 + ak5JPTJetsL2L309 +
                                     photonDRToNearestIDedUncorrectedJet00 +
                                     photonDRTo2ndNearestIDedUncorrectedJet00 +
                                     photonDRTo3rdNearestIDedUncorrectedJet00 +
                                     photonDRToNearestIDedUncorrectedJet03 +
                                     photonDRToNearestIDedUncorrectedJet05 +
                                     photonDRToNearestIDedUncorrectedJet07 +
                                     photonDRToNearestIDedUncorrectedJet09 + JetMultiplicity03 +
                                     JetMultiplicity05 + JetMultiplicity07 + JetMultiplicity09 +
                                     photonDRToNearestIDedUncorrectedJet03PT10 +
                                     photonDRToNearestIDedUncorrectedJet03PT20)
jet_variable_09_sequence = cms.Sequence(probesAndTagsToRemove + IDedJetProducer00 +
                                        IDedJetProducer09 + ak5JPTJetsL2L300 + ak5JPTJetsL2L309 +
                                        photonDRToNearestIDedUncorrectedJet00 +
                                        photonDRTo2ndNearestIDedUncorrectedJet00 +
                                        photonDRTo3rdNearestIDedUncorrectedJet00 +
                                        photonDRToNearestIDedUncorrectedJet09 + JetMultiplicity09)
jet_variable_sequence_probe_passing_iso = cms.Sequence(
    probesPassingIsoAndTagsToRemove + IDedJetProducer00ProbePassingIso +
    IDedJetProducer03ProbePassingIso + IDedJetProducer05ProbePassingIso +
    IDedJetProducer07ProbePassingIso + IDedJetProducer09ProbePassingIso +
    ak5JPTJetsL2L300ProbePassingIso + ak5JPTJetsL2L303ProbePassingIso +
    ak5JPTJetsL2L305ProbePassingIso + ak5JPTJetsL2L307ProbePassingIso +
    ak5JPTJetsL2L309ProbePassingIso + photonPassingIsoDRToNearestIDedUncorrectedJet00 +
    photonPassingIsoDRTo2ndNearestIDedUncorrectedJet00 +
    photonPassingIsoDRTo3rdNearestIDedUncorrectedJet00 +
    photonPassingIsoDRToNearestIDedUncorrectedJet03 +
    photonPassingIsoDRToNearestIDedUncorrectedJet05 +
    photonPassingIsoDRToNearestIDedUncorrectedJet07 +
    photonPassingIsoDRToNearestIDedUncorrectedJet09 + JetMultiplicity03ProbePassingIso +
    JetMultiplicity05ProbePassingIso + JetMultiplicity07ProbePassingIso +
    JetMultiplicity09ProbePassingIso
    )
jet_variable_09_sequence_probe_passing_iso = cms.Sequence(
    probesPassingIsoAndTagsToRemove + IDedJetProducer00ProbePassingIso +
    IDedJetProducer09ProbePassingIso + ak5JPTJetsL2L300ProbePassingIso +
    ak5JPTJetsL2L309ProbePassingIso + photonPassingIsoDRToNearestIDedUncorrectedJet00 +
    photonPassingIsoDRTo2ndNearestIDedUncorrectedJet00 +
    photonPassingIsoDRTo3rdNearestIDedUncorrectedJet00 +
    photonPassingIsoDRToNearestIDedUncorrectedJet09 + JetMultiplicity09ProbePassingIso
    )
jet_variable_sequence_probe_passing_ID = cms.Sequence(
    probesPassingIdEBAndTagsToRemove + IDedJetProducer00ProbePassingIdEB +
    IDedJetProducer03ProbePassingIdEB + IDedJetProducer05ProbePassingIdEB +
    IDedJetProducer07ProbePassingIdEB + IDedJetProducer09ProbePassingIdEB +
    ak5JPTJetsL2L300ProbePassingIdEB + ak5JPTJetsL2L303ProbePassingIdEB +
    ak5JPTJetsL2L305ProbePassingIdEB + ak5JPTJetsL2L307ProbePassingIdEB +
    ak5JPTJetsL2L309ProbePassingIdEB + photonPassingIdEBDRToNearestIDedUncorrectedJet00 +
    photonPassingIdEBDRTo2ndNearestIDedUncorrectedJet00 +
    photonPassingIdEBDRTo3rdNearestIDedUncorrectedJet00 +
    photonPassingIdEBDRToNearestIDedUncorrectedJet03 +
    photonPassingIdEBDRToNearestIDedUncorrectedJet05 +
    photonPassingIdEBDRToNearestIDedUncorrectedJet07 +
    photonPassingIdEBDRToNearestIDedUncorrectedJet09 + JetMultiplicity03ProbePassingIdEB +
    JetMultiplicity05ProbePassingIdEB + JetMultiplicity07ProbePassingIdEB +
    JetMultiplicity09ProbePassingIdEB + probesPassingIdEEAndTagsToRemove +
    IDedJetProducer00ProbePassingIdEE + IDedJetProducer03ProbePassingIdEE +
    IDedJetProducer05ProbePassingIdEE + IDedJetProducer07ProbePassingIdEE +
    IDedJetProducer09ProbePassingIdEE + ak5JPTJetsL2L300ProbePassingIdEE +
    ak5JPTJetsL2L303ProbePassingIdEE + ak5JPTJetsL2L305ProbePassingIdEE +
    ak5JPTJetsL2L307ProbePassingIdEE + ak5JPTJetsL2L309ProbePassingIdEE +
    photonPassingIdEEDRToNearestIDedUncorrectedJet00 +
    photonPassingIdEEDRTo2ndNearestIDedUncorrectedJet00 +
    photonPassingIdEEDRTo3rdNearestIDedUncorrectedJet00 +
    photonPassingIdEEDRToNearestIDedUncorrectedJet03 +
    photonPassingIdEEDRToNearestIDedUncorrectedJet05 +
    photonPassingIdEEDRToNearestIDedUncorrectedJet07 +
    photonPassingIdEEDRToNearestIDedUncorrectedJet09 + JetMultiplicity03ProbePassingIdEE +
    JetMultiplicity05ProbePassingIdEE + JetMultiplicity07ProbePassingIdEE +
    JetMultiplicity09ProbePassingIdEE
    )
jet_variable_09_sequence_probe_passing_ID = cms.Sequence(
    probesPassingIdEBAndTagsToRemove + IDedJetProducer00ProbePassingIdEB +
    IDedJetProducer09ProbePassingIdEB + ak5JPTJetsL2L300ProbePassingIdEB +
    ak5JPTJetsL2L309ProbePassingIdEB + photonPassingIdEBDRToNearestIDedUncorrectedJet00 +
    photonPassingIdEBDRTo2ndNearestIDedUncorrectedJet00 +
    photonPassingIdEBDRTo3rdNearestIDedUncorrectedJet00 +
    photonPassingIdEBDRToNearestIDedUncorrectedJet09 + JetMultiplicity09ProbePassingIdEB +
    probesPassingIdEEAndTagsToRemove + IDedJetProducer00ProbePassingIdEE +
    IDedJetProducer09ProbePassingIdEE + ak5JPTJetsL2L300ProbePassingIdEE +
    ak5JPTJetsL2L309ProbePassingIdEE + photonPassingIdEEDRToNearestIDedUncorrectedJet00 +
    photonPassingIdEEDRTo2ndNearestIDedUncorrectedJet00 +
    photonPassingIdEEDRTo3rdNearestIDedUncorrectedJet00 +
    photonPassingIdEEDRToNearestIDedUncorrectedJet09 + JetMultiplicity09ProbePassingIdEE
    )
