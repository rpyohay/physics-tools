import FWCore.ParameterSet.Config as cms

#configurable jet collection names and cuts
from PhysicsTools.TagAndProbe.JetVariables_cfi import JET_CUTS, JET_CUTS_00, probesAndTagsToRemove, probesPassingIsoAndTagsToRemove, probesPassingIdEBAndTagsToRemove, probesPassingIdEEAndTagsToRemove, probesPassingIsoVLR9IdAndTagsToRemove, probesPassingIsoVLAndTagsToRemove, probesPassingR9IdAndTagsToRemove
PF_JET_COLL_00 = "ak5PFJetsL1L2L300"
PF_JET_COLL_03 = "ak5PFJetsL1L2L303"
PF_JET_COLL_05 = "ak5PFJetsL1L2L305"
PF_JET_COLL_07 = "ak5PFJetsL1L2L307"
PF_JET_COLL_09 = "ak5PFJetsL1L2L309"
PF_JET_COLL_00_PROBE_PASSING_ISO = "ak5PFJetsL1L2L300ProbePassingIso"
PF_JET_COLL_03_PROBE_PASSING_ISO = "ak5PFJetsL1L2L303ProbePassingIso"
PF_JET_COLL_05_PROBE_PASSING_ISO = "ak5PFJetsL1L2L305ProbePassingIso"
PF_JET_COLL_07_PROBE_PASSING_ISO = "ak5PFJetsL1L2L307ProbePassingIso"
PF_JET_COLL_09_PROBE_PASSING_ISO = "ak5PFJetsL1L2L309ProbePassingIso"
PF_JET_COLL_00_PROBE_PASSING_ID_EB = "ak5PFJetsL1L2L300ProbePassingIdEB"
PF_JET_COLL_03_PROBE_PASSING_ID_EB = "ak5PFJetsL1L2L303ProbePassingIdEB"
PF_JET_COLL_05_PROBE_PASSING_ID_EB = "ak5PFJetsL1L2L305ProbePassingIdEB"
PF_JET_COLL_07_PROBE_PASSING_ID_EB = "ak5PFJetsL1L2L307ProbePassingIdEB"
PF_JET_COLL_09_PROBE_PASSING_ID_EB = "ak5PFJetsL1L2L309ProbePassingIdEB"
PF_JET_COLL_00_PROBE_PASSING_ID_EE = "ak5PFJetsL1L2L300ProbePassingIdEE"
PF_JET_COLL_03_PROBE_PASSING_ID_EE = "ak5PFJetsL1L2L303ProbePassingIdEE"
PF_JET_COLL_05_PROBE_PASSING_ID_EE = "ak5PFJetsL1L2L305ProbePassingIdEE"
PF_JET_COLL_07_PROBE_PASSING_ID_EE = "ak5PFJetsL1L2L307ProbePassingIdEE"
PF_JET_COLL_09_PROBE_PASSING_ID_EE = "ak5PFJetsL1L2L309ProbePassingIdEE"
PF_JET_COLL_03_PROBE_PASSING_ISOVL_R9ID = "ak5PFJetsL1L2L303ProbePassingIsoVLR9Id"
PF_JET_COLL_03_PROBE_PASSING_ISOVL = "ak5PFJetsL1L2L303ProbePassingIsoVL"
PF_JET_COLL_03_PROBE_PASSING_R9ID = "ak5PFJetsL1L2L303ProbePassingR9Id"
PF_JET_COLL_05_PROBE_PASSING_ISOVL_R9ID = "ak5PFJetsL1L2L305ProbePassingIsoVLR9Id"
PF_JET_COLL_05_PROBE_PASSING_ISOVL = "ak5PFJetsL1L2L305ProbePassingIsoVL"
PF_JET_COLL_05_PROBE_PASSING_R9ID = "ak5PFJetsL1L2L305ProbePassingR9Id"

#for the PF L1L2L3 corrections (L1 = PU subtraction)
from JetMETCorrections.Configuration.DefaultJEC_cff import *
ak5PFL1Fastjet.useCondDB = True

#producer of dR < 0.0 photon-cleaned jets
#passing PF jet ID (https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID)
IDedPFJetProducer00 = cms.EDProducer(
    "IDedJetProducer",
    PFJetSrc = cms.InputTag("ak5PFJets"),
    photonSrc = cms.InputTag("probesAndTagsToRemove"),
    cleaningDR = cms.double(0.0),
    maxAbsEta = cms.double(2.6)
    )
IDedPFJetProducer00ProbePassingIso = IDedPFJetProducer00.clone()
IDedPFJetProducer00ProbePassingIso.photonSrc = cms.InputTag("probesPassingIsoAndTagsToRemove")
IDedPFJetProducer00ProbePassingIdEB = IDedPFJetProducer00.clone()
IDedPFJetProducer00ProbePassingIdEB.photonSrc = cms.InputTag("probesPassingIdEBAndTagsToRemove")
IDedPFJetProducer00ProbePassingIdEE = IDedPFJetProducer00.clone()
IDedPFJetProducer00ProbePassingIdEE.photonSrc = cms.InputTag("probesPassingIdEEAndTagsToRemove")
IDedPFJetProducer00ProbePassingIsoVLR9Id = IDedPFJetProducer00.clone()
IDedPFJetProducer00ProbePassingIsoVLR9Id.photonSrc = cms.InputTag(
    "probesPassingIsoVLR9IdAndTagsToRemove"
    )
IDedPFJetProducer00ProbePassingIsoVL = IDedPFJetProducer00.clone()
IDedPFJetProducer00ProbePassingIsoVL.photonSrc = cms.InputTag(
    "probesPassingIsoVLAndTagsToRemove"
    )
IDedPFJetProducer00ProbePassingR9Id = IDedPFJetProducer00.clone()
IDedPFJetProducer00ProbePassingR9Id.photonSrc = cms.InputTag(
    "probesPassingR9IdAndTagsToRemove"
    )

#producer of dR < 0.3 photon-cleaned jets
#passing PF jet ID (https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID)
IDedPFJetProducer03 = cms.EDProducer(
    "IDedJetProducer",
    PFJetSrc = cms.InputTag("ak5PFJets"),
    photonSrc = cms.InputTag("probesAndTagsToRemove"),
    cleaningDR = cms.double(0.3),
    maxAbsEta = cms.double(2.6)
    )
IDedPFJetProducer03ProbePassingIso = IDedPFJetProducer00.clone()
IDedPFJetProducer03ProbePassingIso.photonSrc = cms.InputTag("probesPassingIsoAndTagsToRemove")
IDedPFJetProducer03ProbePassingIdEB = IDedPFJetProducer00.clone()
IDedPFJetProducer03ProbePassingIdEB.photonSrc = cms.InputTag("probesPassingIdEBAndTagsToRemove")
IDedPFJetProducer03ProbePassingIdEE = IDedPFJetProducer00.clone()
IDedPFJetProducer03ProbePassingIdEE.photonSrc = cms.InputTag("probesPassingIdEEAndTagsToRemove")
IDedPFJetProducer03ProbePassingIsoVLR9Id = IDedPFJetProducer03.clone()
IDedPFJetProducer03ProbePassingIsoVLR9Id.photonSrc = cms.InputTag(
    "probesPassingIsoVLR9IdAndTagsToRemove"
    )
IDedPFJetProducer03ProbePassingIsoVL = IDedPFJetProducer03.clone()
IDedPFJetProducer03ProbePassingIsoVL.photonSrc = cms.InputTag(
    "probesPassingIsoVLAndTagsToRemove"
    )
IDedPFJetProducer03ProbePassingR9Id = IDedPFJetProducer03.clone()
IDedPFJetProducer03ProbePassingR9Id.photonSrc = cms.InputTag(
    "probesPassingR9IdAndTagsToRemove"
    )

#producer of dR < 0.5 photon-cleaned jets
#passing PF jet ID (https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID)
IDedPFJetProducer05 = cms.EDProducer(
    "IDedJetProducer",
    PFJetSrc = cms.InputTag("ak5PFJets"),
    photonSrc = cms.InputTag("probesAndTagsToRemove"),
    cleaningDR = cms.double(0.5),
    maxAbsEta = cms.double(2.6)
    )
IDedPFJetProducer05ProbePassingIso = IDedPFJetProducer00.clone()
IDedPFJetProducer05ProbePassingIso.photonSrc = cms.InputTag("probesPassingIsoAndTagsToRemove")
IDedPFJetProducer05ProbePassingIdEB = IDedPFJetProducer00.clone()
IDedPFJetProducer05ProbePassingIdEB.photonSrc = cms.InputTag("probesPassingIdEBAndTagsToRemove")
IDedPFJetProducer05ProbePassingIdEE = IDedPFJetProducer00.clone()
IDedPFJetProducer05ProbePassingIdEE.photonSrc = cms.InputTag("probesPassingIdEEAndTagsToRemove")
IDedPFJetProducer05ProbePassingIsoVLR9Id = IDedPFJetProducer05.clone()
IDedPFJetProducer05ProbePassingIsoVLR9Id.photonSrc = cms.InputTag(
    "probesPassingIsoVLR9IdAndTagsToRemove"
    )
IDedPFJetProducer05ProbePassingIsoVL = IDedPFJetProducer05.clone()
IDedPFJetProducer05ProbePassingIsoVL.photonSrc = cms.InputTag(
    "probesPassingIsoVLAndTagsToRemove"
    )
IDedPFJetProducer05ProbePassingR9Id = IDedPFJetProducer05.clone()
IDedPFJetProducer05ProbePassingR9Id.photonSrc = cms.InputTag(
    "probesPassingR9IdAndTagsToRemove"
    )

#producer of dR < 0.7 photon-cleaned jets
#passing PF jet ID (https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID)
IDedPFJetProducer07 = cms.EDProducer(
    "IDedJetProducer",
    PFJetSrc = cms.InputTag("ak5PFJets"),
    photonSrc = cms.InputTag("probesAndTagsToRemove"),
    cleaningDR = cms.double(0.7),
    maxAbsEta = cms.double(2.6)
    )
IDedPFJetProducer07ProbePassingIso = IDedPFJetProducer00.clone()
IDedPFJetProducer07ProbePassingIso.photonSrc = cms.InputTag("probesPassingIsoAndTagsToRemove")
IDedPFJetProducer07ProbePassingIdEB = IDedPFJetProducer00.clone()
IDedPFJetProducer07ProbePassingIdEB.photonSrc = cms.InputTag("probesPassingIdEBAndTagsToRemove")
IDedPFJetProducer07ProbePassingIdEE = IDedPFJetProducer00.clone()
IDedPFJetProducer07ProbePassingIdEE.photonSrc = cms.InputTag("probesPassingIdEEAndTagsToRemove")

#producer of dR < 0.9 photon-cleaned jets
#passing PF jet ID (https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID)
IDedPFJetProducer09 = cms.EDProducer(
    "IDedJetProducer",
    PFJetSrc = cms.InputTag("ak5PFJets"),
    photonSrc = cms.InputTag("probesAndTagsToRemove"),
    cleaningDR = cms.double(0.9),
    maxAbsEta = cms.double(2.6)
    )
IDedPFJetProducer09ProbePassingIso = IDedPFJetProducer00.clone()
IDedPFJetProducer09ProbePassingIso.photonSrc = cms.InputTag("probesPassingIsoAndTagsToRemove")
IDedPFJetProducer09ProbePassingIdEB = IDedPFJetProducer00.clone()
IDedPFJetProducer09ProbePassingIdEB.photonSrc = cms.InputTag("probesPassingIdEBAndTagsToRemove")
IDedPFJetProducer09ProbePassingIdEE = IDedPFJetProducer00.clone()
IDedPFJetProducer09ProbePassingIdEE.photonSrc = cms.InputTag("probesPassingIdEEAndTagsToRemove")

#produce corrected PF jet collection from IDed and dR < 0.0 cross-cleaned PF jet collection
ak5PFJetsL1L2L300 = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L300.src = cms.InputTag("IDedPFJetProducer00")
ak5PFJetsL1L2L300ProbePassingIso = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L300ProbePassingIso.src = cms.InputTag("IDedPFJetProducer00ProbePassingIso")
ak5PFJetsL1L2L300ProbePassingIdEB = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L300ProbePassingIdEB.src = cms.InputTag("IDedPFJetProducer00ProbePassingIdEB")
ak5PFJetsL1L2L300ProbePassingIdEE = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L300ProbePassingIdEE.src = cms.InputTag("IDedPFJetProducer00ProbePassingIdEE")

#produce corrected PF jet collection from IDed and dR < 0.3 cross-cleaned PF jet collection
ak5PFJetsL1L2L303 = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L303.src = cms.InputTag("IDedPFJetProducer03")
ak5PFJetsL1L2L303ProbePassingIso = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L303ProbePassingIso.src = cms.InputTag("IDedPFJetProducer00ProbePassingIso")
ak5PFJetsL1L2L303ProbePassingIdEB = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L303ProbePassingIdEB.src = cms.InputTag("IDedPFJetProducer00ProbePassingIdEB")
ak5PFJetsL1L2L303ProbePassingIdEE = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L303ProbePassingIdEE.src = cms.InputTag("IDedPFJetProducer00ProbePassingIdEE")
ak5PFJetsL1L2L303ProbePassingIsoVLR9Id = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L303ProbePassingIsoVLR9Id.src = cms.InputTag(
    "IDedPFJetProducer03ProbePassingIsoVLR9Id"
    )
ak5PFJetsL1L2L303ProbePassingIsoVL = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L303ProbePassingIsoVL.src = cms.InputTag(
    "IDedPFJetProducer03ProbePassingIsoVL"
    )
ak5PFJetsL1L2L303ProbePassingR9Id = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L303ProbePassingR9Id.src = cms.InputTag(
    "IDedPFJetProducer03ProbePassingR9Id"
    )

#produce corrected PF jet collection from IDed and dR < 0.5 cross-cleaned PF jet collection
ak5PFJetsL1L2L305 = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L305.src = cms.InputTag("IDedPFJetProducer05")
ak5PFJetsL1L2L305ProbePassingIso = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L305ProbePassingIso.src = cms.InputTag("IDedPFJetProducer00ProbePassingIso")
ak5PFJetsL1L2L305ProbePassingIdEB = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L305ProbePassingIdEB.src = cms.InputTag("IDedPFJetProducer00ProbePassingIdEB")
ak5PFJetsL1L2L305ProbePassingIdEE = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L305ProbePassingIdEE.src = cms.InputTag("IDedPFJetProducer00ProbePassingIdEE")
ak5PFJetsL1L2L305ProbePassingIsoVLR9Id = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L305ProbePassingIsoVLR9Id.src = cms.InputTag(
    "IDedPFJetProducer05ProbePassingIsoVLR9Id"
    )
ak5PFJetsL1L2L305ProbePassingIsoVL = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L305ProbePassingIsoVL.src = cms.InputTag(
    "IDedPFJetProducer05ProbePassingIsoVL"
    )
ak5PFJetsL1L2L305ProbePassingR9Id = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L305ProbePassingR9Id.src = cms.InputTag(
    "IDedPFJetProducer05ProbePassingR9Id"
    )

#produce corrected PF jet collection from IDed and dR < 0.7 cross-cleaned PF jet collection
ak5PFJetsL1L2L307 = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L307.src = cms.InputTag("IDedPFJetProducer07")
ak5PFJetsL1L2L307ProbePassingIso = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L307ProbePassingIso.src = cms.InputTag("IDedPFJetProducer00ProbePassingIso")
ak5PFJetsL1L2L307ProbePassingIdEB = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L307ProbePassingIdEB.src = cms.InputTag("IDedPFJetProducer00ProbePassingIdEB")
ak5PFJetsL1L2L307ProbePassingIdEE = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L307ProbePassingIdEE.src = cms.InputTag("IDedPFJetProducer00ProbePassingIdEE")

#produce corrected PF jet collection from IDed and dR < 0.9 cross-cleaned PF jet collection
ak5PFJetsL1L2L309 = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L309.src = cms.InputTag("IDedPFJetProducer09")
ak5PFJetsL1L2L309ProbePassingIso = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L309ProbePassingIso.src = cms.InputTag("IDedPFJetProducer00ProbePassingIso")
ak5PFJetsL1L2L309ProbePassingIdEB = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L309ProbePassingIdEB.src = cms.InputTag("IDedPFJetProducer00ProbePassingIdEB")
ak5PFJetsL1L2L309ProbePassingIdEE = ak5PFJetsL1FastL2L3.clone()
ak5PFJetsL1L2L309ProbePassingIdEE.src = cms.InputTag("IDedPFJetProducer00ProbePassingIdEE")

#produce dR(photon, nearest IDed uncorrected jet passing cuts on corrected eta)
#use PF jets cleaned with dR = 0.0 algorithm
photonDRToNearestIDedUncorrectedJet00 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(PF_JET_COLL_00),
    objectSelection = cms.string(JET_CUTS_00),
    minDR = cms.double(0.0)
)
photonPassingIsoDRToNearestIDedUncorrectedJet00 = photonDRToNearestIDedUncorrectedJet00.clone()
photonPassingIsoDRToNearestIDedUncorrectedJet00.probes = cms.InputTag(
    "probePhotonsPassingIsolation"
    )
photonPassingIsoDRToNearestIDedUncorrectedJet00.objects = cms.InputTag(
    PF_JET_COLL_00_PROBE_PASSING_ISO
    )
photonPassingIdEBDRToNearestIDedUncorrectedJet00 = photonDRToNearestIDedUncorrectedJet00.clone()
photonPassingIdEBDRToNearestIDedUncorrectedJet00.probes = cms.InputTag(
    "probePhotonsPassingIdEB"
    )
photonPassingIdEBDRToNearestIDedUncorrectedJet00.objects = cms.InputTag(
    PF_JET_COLL_00_PROBE_PASSING_ID_EB
    )
photonPassingIdEEDRToNearestIDedUncorrectedJet00 = photonDRToNearestIDedUncorrectedJet00.clone()
photonPassingIdEEDRToNearestIDedUncorrectedJet00.probes = cms.InputTag(
    "probePhotonsPassingIdEE"
    )
photonPassingIdEEDRToNearestIDedUncorrectedJet00.objects = cms.InputTag(
    PF_JET_COLL_00_PROBE_PASSING_ID_EE
    )

#produce dR(photon, 2nd nearest IDed uncorrected jet passing cuts on corrected eta)
#use PF jets cleaned with dR = 0.0 algorithm
photonDRTo2ndNearestIDedUncorrectedJet00 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(PF_JET_COLL_00),
    objectSelection = cms.string(JET_CUTS_00),
    minDR = cms.double(0.0),
    pos = cms.untracked.uint32(1)
)
photonPassingIsoDRTo2ndNearestIDedUncorrectedJet00 = photonDRTo2ndNearestIDedUncorrectedJet00.clone()
photonPassingIsoDRTo2ndNearestIDedUncorrectedJet00.probes = cms.InputTag(
    "probePhotonsPassingIsolation"
    )
photonPassingIsoDRTo2ndNearestIDedUncorrectedJet00.objects = cms.InputTag(
    PF_JET_COLL_00_PROBE_PASSING_ISO
    )
photonPassingIdEBDRTo2ndNearestIDedUncorrectedJet00 = photonDRTo2ndNearestIDedUncorrectedJet00.clone()
photonPassingIdEBDRTo2ndNearestIDedUncorrectedJet00.probes = cms.InputTag(
    "probePhotonsPassingIdEB"
    )
photonPassingIdEBDRTo2ndNearestIDedUncorrectedJet00.objects = cms.InputTag(
    PF_JET_COLL_00_PROBE_PASSING_ID_EB
    )
photonPassingIdEEDRTo2ndNearestIDedUncorrectedJet00 = photonDRTo2ndNearestIDedUncorrectedJet00.clone()
photonPassingIdEEDRTo2ndNearestIDedUncorrectedJet00.probes = cms.InputTag(
    "probePhotonsPassingIdEE"
    )
photonPassingIdEEDRTo2ndNearestIDedUncorrectedJet00.objects = cms.InputTag(
    PF_JET_COLL_00_PROBE_PASSING_ID_EE
    )

#produce dR(photon, 3rd nearest IDed uncorrected jet passing cuts on corrected eta)
#use PF jets cleaned with dR = 0.0 algorithm
photonDRTo3rdNearestIDedUncorrectedJet00 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(PF_JET_COLL_00),
    objectSelection = cms.string(JET_CUTS_00),
    minDR = cms.double(0.0),
    pos = cms.untracked.uint32(2)                                                           
)
photonPassingIsoDRTo3rdNearestIDedUncorrectedJet00 = photonDRTo3rdNearestIDedUncorrectedJet00.clone()
photonPassingIsoDRTo3rdNearestIDedUncorrectedJet00.probes = cms.InputTag(
    "probePhotonsPassingIsolation"
    )
photonPassingIsoDRTo3rdNearestIDedUncorrectedJet00.objects = cms.InputTag(
    PF_JET_COLL_00_PROBE_PASSING_ISO
    )
photonPassingIdEBDRTo3rdNearestIDedUncorrectedJet00 = photonDRTo3rdNearestIDedUncorrectedJet00.clone()
photonPassingIdEBDRTo3rdNearestIDedUncorrectedJet00.probes = cms.InputTag(
    "probePhotonsPassingIdEB"
    )
photonPassingIdEBDRTo3rdNearestIDedUncorrectedJet00.objects = cms.InputTag(
    PF_JET_COLL_00_PROBE_PASSING_ID_EB
    )
photonPassingIdEEDRTo3rdNearestIDedUncorrectedJet00 = photonDRTo3rdNearestIDedUncorrectedJet00.clone()
photonPassingIdEEDRTo3rdNearestIDedUncorrectedJet00.probes = cms.InputTag(
    "probePhotonsPassingIdEE"
    )
photonPassingIdEEDRTo3rdNearestIDedUncorrectedJet00.objects = cms.InputTag(
    PF_JET_COLL_00_PROBE_PASSING_ID_EE
    )

#produce dR(photon, nearest IDed uncorrected jet passing cuts on corrected eta and pT)
#use PF jets cleaned with dR = 0.3 algorithm
photonDRToNearestIDedUncorrectedJet03 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(PF_JET_COLL_03),
    objectSelection = cms.string(JET_CUTS),
    minDR = cms.double(0.0)
)
photonPassingIsoDRToNearestIDedUncorrectedJet03 = photonDRToNearestIDedUncorrectedJet03.clone()
photonPassingIsoDRToNearestIDedUncorrectedJet03.probes = cms.InputTag(
    "probePhotonsPassingIsolation"
    )
photonPassingIsoDRToNearestIDedUncorrectedJet03.objects = cms.InputTag(
    PF_JET_COLL_03_PROBE_PASSING_ISO
    )
photonPassingIdEBDRToNearestIDedUncorrectedJet03 = photonDRToNearestIDedUncorrectedJet03.clone()
photonPassingIdEBDRToNearestIDedUncorrectedJet03.probes = cms.InputTag(
    "probePhotonsPassingIdEB"
    )
photonPassingIdEBDRToNearestIDedUncorrectedJet03.objects = cms.InputTag(
    PF_JET_COLL_03_PROBE_PASSING_ID_EB
    )
photonPassingIdEEDRToNearestIDedUncorrectedJet03 = photonDRToNearestIDedUncorrectedJet03.clone()
photonPassingIdEEDRToNearestIDedUncorrectedJet03.probes = cms.InputTag(
    "probePhotonsPassingIdEE"
    )
photonPassingIdEEDRToNearestIDedUncorrectedJet03.objects = cms.InputTag(
    PF_JET_COLL_03_PROBE_PASSING_ID_EE
    )
photonPassingIsoVLR9IdDRToNearestIDedUncorrectedJet03 = photonDRToNearestIDedUncorrectedJet03.clone()
photonPassingIsoVLR9IdDRToNearestIDedUncorrectedJet03.probes = cms.InputTag(
    "probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLR9IdEB"
    )
photonPassingIsoVLR9IdDRToNearestIDedUncorrectedJet03.objects = cms.InputTag(
    PF_JET_COLL_03_PROBE_PASSING_ISOVL_R9ID
    )
photonPassingIsoVLDRToNearestIDedUncorrectedJet03 = photonDRToNearestIDedUncorrectedJet03.clone()
photonPassingIsoVLDRToNearestIDedUncorrectedJet03.probes = cms.InputTag(
    "probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLEB"
    )
photonPassingIsoVLDRToNearestIDedUncorrectedJet03.objects = cms.InputTag(
    PF_JET_COLL_03_PROBE_PASSING_ISOVL
    )
photonPassingR9IdDRToNearestIDedUncorrectedJet03 = photonDRToNearestIDedUncorrectedJet03.clone()
photonPassingR9IdDRToNearestIDedUncorrectedJet03.probes = cms.InputTag(
    "probePhotonsPassingPUCorrectedCombinedIsoIdR9IdEB"
    )
photonPassingR9IdDRToNearestIDedUncorrectedJet03.objects = cms.InputTag(
    PF_JET_COLL_03_PROBE_PASSING_R9ID
    )

#produce dR(photon, nearest IDed uncorrected jet passing cuts on corrected eta and pT)
#use PF jets cleaned with dR = 0.5 algorithm
photonDRToNearestIDedUncorrectedJet05 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(PF_JET_COLL_05),
    objectSelection = cms.string(JET_CUTS),
    minDR = cms.double(0.0)
)
photonPassingIsoDRToNearestIDedUncorrectedJet05 = photonDRToNearestIDedUncorrectedJet05.clone()
photonPassingIsoDRToNearestIDedUncorrectedJet05.probes = cms.InputTag(
    "probePhotonsPassingIsolation"
    )
photonPassingIsoDRToNearestIDedUncorrectedJet05.objects = cms.InputTag(
    PF_JET_COLL_05_PROBE_PASSING_ISO
    )
photonPassingIdEBDRToNearestIDedUncorrectedJet05 = photonDRToNearestIDedUncorrectedJet05.clone()
photonPassingIdEBDRToNearestIDedUncorrectedJet05.probes = cms.InputTag(
    "probePhotonsPassingIdEB"
    )
photonPassingIdEBDRToNearestIDedUncorrectedJet05.objects = cms.InputTag(
    PF_JET_COLL_05_PROBE_PASSING_ID_EB
    )
photonPassingIdEEDRToNearestIDedUncorrectedJet05 = photonDRToNearestIDedUncorrectedJet05.clone()
photonPassingIdEEDRToNearestIDedUncorrectedJet05.probes = cms.InputTag(
    "probePhotonsPassingIdEE"
    )
photonPassingIdEEDRToNearestIDedUncorrectedJet05.objects = cms.InputTag(
    PF_JET_COLL_05_PROBE_PASSING_ID_EE
    )
photonPassingIsoVLR9IdDRToNearestIDedUncorrectedJet05 = photonDRToNearestIDedUncorrectedJet05.clone()
photonPassingIsoVLR9IdDRToNearestIDedUncorrectedJet05.probes = cms.InputTag(
    "probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLR9IdEB"
    )
photonPassingIsoVLR9IdDRToNearestIDedUncorrectedJet05.objects = cms.InputTag(
    PF_JET_COLL_05_PROBE_PASSING_ISOVL_R9ID
    )
photonPassingIsoVLDRToNearestIDedUncorrectedJet05 = photonDRToNearestIDedUncorrectedJet05.clone()
photonPassingIsoVLDRToNearestIDedUncorrectedJet05.probes = cms.InputTag(
    "probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLEB"
    )
photonPassingIsoVLDRToNearestIDedUncorrectedJet05.objects = cms.InputTag(
    PF_JET_COLL_05_PROBE_PASSING_ISOVL
    )
photonPassingR9IdDRToNearestIDedUncorrectedJet05 = photonDRToNearestIDedUncorrectedJet05.clone()
photonPassingR9IdDRToNearestIDedUncorrectedJet05.probes = cms.InputTag(
    "probePhotonsPassingPUCorrectedCombinedIsoIdR9IdEB"
    )
photonPassingR9IdDRToNearestIDedUncorrectedJet05.objects = cms.InputTag(
    PF_JET_COLL_05_PROBE_PASSING_R9ID
    )

#produce dR(photon, nearest IDed uncorrected jet passing cuts on corrected eta and pT)
#use PF jets cleaned with dR = 0.7 algorithm
photonDRToNearestIDedUncorrectedJet07 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(PF_JET_COLL_07),
    objectSelection = cms.string(JET_CUTS),
    minDR = cms.double(0.0)
)
photonPassingIsoDRToNearestIDedUncorrectedJet07 = photonDRToNearestIDedUncorrectedJet07.clone()
photonPassingIsoDRToNearestIDedUncorrectedJet07.probes = cms.InputTag(
    "probePhotonsPassingIsolation"
    )
photonPassingIsoDRToNearestIDedUncorrectedJet07.objects = cms.InputTag(
    PF_JET_COLL_07_PROBE_PASSING_ISO
    )
photonPassingIdEBDRToNearestIDedUncorrectedJet07 = photonDRToNearestIDedUncorrectedJet07.clone()
photonPassingIdEBDRToNearestIDedUncorrectedJet07.probes = cms.InputTag(
    "probePhotonsPassingIdEB"
    )
photonPassingIdEBDRToNearestIDedUncorrectedJet07.objects = cms.InputTag(
    PF_JET_COLL_07_PROBE_PASSING_ID_EB
    )
photonPassingIdEEDRToNearestIDedUncorrectedJet07 = photonDRToNearestIDedUncorrectedJet07.clone()
photonPassingIdEEDRToNearestIDedUncorrectedJet07.probes = cms.InputTag(
    "probePhotonsPassingIdEE"
    )
photonPassingIdEEDRToNearestIDedUncorrectedJet07.objects = cms.InputTag(
    PF_JET_COLL_07_PROBE_PASSING_ID_EE
    )

#produce dR(photon, nearest IDed uncorrected jet passing cuts on corrected eta and pT)
#use PF jets cleaned with dR = 0.9 algorithm
photonDRToNearestIDedUncorrectedJet09 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(PF_JET_COLL_09),
    objectSelection = cms.string(JET_CUTS),
    minDR = cms.double(0.0)
)
photonPassingIsoDRToNearestIDedUncorrectedJet09 = photonDRToNearestIDedUncorrectedJet09.clone()
photonPassingIsoDRToNearestIDedUncorrectedJet09.probes = cms.InputTag(
    "probePhotonsPassingIsolation"
    )
photonPassingIsoDRToNearestIDedUncorrectedJet09.objects = cms.InputTag(
    PF_JET_COLL_09_PROBE_PASSING_ISO
    )
photonPassingIdEBDRToNearestIDedUncorrectedJet09 = photonDRToNearestIDedUncorrectedJet09.clone()
photonPassingIdEBDRToNearestIDedUncorrectedJet09.probes = cms.InputTag(
    "probePhotonsPassingIdEB"
    )
photonPassingIdEBDRToNearestIDedUncorrectedJet09.objects = cms.InputTag(
    PF_JET_COLL_09_PROBE_PASSING_ID_EB
    )
photonPassingIdEEDRToNearestIDedUncorrectedJet09 = photonDRToNearestIDedUncorrectedJet09.clone()
photonPassingIdEEDRToNearestIDedUncorrectedJet09.probes = cms.InputTag(
    "probePhotonsPassingIdEE"
    )
photonPassingIdEEDRToNearestIDedUncorrectedJet09.objects = cms.InputTag(
    PF_JET_COLL_09_PROBE_PASSING_ID_EE
    )

#count IDed and dR < 0.0 cross-cleaned PF jets passing cuts
JetMultiplicity00 = cms.EDProducer(
    "CandMultiplicityCounter",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(PF_JET_COLL_00),
    objectSelection = cms.string(JET_CUTS),
    )
JetMultiplicity00ProbePassingIso = JetMultiplicity00.clone()
JetMultiplicity00ProbePassingIso.probes = cms.InputTag("probePhotonsPassingIsolation")
JetMultiplicity00ProbePassingIso.objects = cms.InputTag(PF_JET_COLL_00_PROBE_PASSING_ISO)
JetMultiplicity00ProbePassingIdEB = JetMultiplicity00.clone()
JetMultiplicity00ProbePassingIdEB.probes = cms.InputTag("probePhotonsPassingIdEB")
JetMultiplicity00ProbePassingIdEB.objects = cms.InputTag(PF_JET_COLL_00_PROBE_PASSING_ID_EB)
JetMultiplicity00ProbePassingIdEE = JetMultiplicity00.clone()
JetMultiplicity00ProbePassingIdEE.probes = cms.InputTag("probePhotonsPassingIdEE")
JetMultiplicity00ProbePassingIdEE.objects = cms.InputTag(PF_JET_COLL_00_PROBE_PASSING_ID_EE)

#count IDed and dR < 0.3 cross-cleaned PF jets passing cuts
JetMultiplicity03 = cms.EDProducer(
    "CandMultiplicityCounter",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(PF_JET_COLL_03),
    objectSelection = cms.string(JET_CUTS),
    )
JetMultiplicity03ProbePassingIso = JetMultiplicity03.clone()
JetMultiplicity03ProbePassingIso.probes = cms.InputTag("probePhotonsPassingIsolation")
JetMultiplicity03ProbePassingIso.objects = cms.InputTag(PF_JET_COLL_03_PROBE_PASSING_ISO)
JetMultiplicity03ProbePassingIdEB = JetMultiplicity03.clone()
JetMultiplicity03ProbePassingIdEB.probes = cms.InputTag("probePhotonsPassingIdEB")
JetMultiplicity03ProbePassingIdEB.objects = cms.InputTag(PF_JET_COLL_03_PROBE_PASSING_ID_EB)
JetMultiplicity03ProbePassingIdEE = JetMultiplicity03.clone()
JetMultiplicity03ProbePassingIdEE.probes = cms.InputTag("probePhotonsPassingIdEE")
JetMultiplicity03ProbePassingIdEE.objects = cms.InputTag(PF_JET_COLL_03_PROBE_PASSING_ID_EE)

#count IDed and dR < 0.5 cross-cleaned PF jets passing cuts
JetMultiplicity05 = cms.EDProducer(
    "CandMultiplicityCounter",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(PF_JET_COLL_05),
    objectSelection = cms.string(JET_CUTS),
    )
JetMultiplicity05ProbePassingIso = JetMultiplicity05.clone()
JetMultiplicity05ProbePassingIso.probes = cms.InputTag("probePhotonsPassingIsolation")
JetMultiplicity05ProbePassingIso.objects = cms.InputTag(PF_JET_COLL_05_PROBE_PASSING_ISO)
JetMultiplicity05ProbePassingIdEB = JetMultiplicity05.clone()
JetMultiplicity05ProbePassingIdEB.probes = cms.InputTag("probePhotonsPassingIdEB")
JetMultiplicity05ProbePassingIdEB.objects = cms.InputTag(PF_JET_COLL_05_PROBE_PASSING_ID_EB)
JetMultiplicity05ProbePassingIdEE = JetMultiplicity05.clone()
JetMultiplicity05ProbePassingIdEE.probes = cms.InputTag("probePhotonsPassingIdEE")
JetMultiplicity05ProbePassingIdEE.objects = cms.InputTag(PF_JET_COLL_05_PROBE_PASSING_ID_EE)
JetMultiplicity05ProbePassingIsoVLR9Id = JetMultiplicity05.clone()
JetMultiplicity05ProbePassingIsoVLR9Id.probes = cms.InputTag(
    "probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLR9IdEB"
    )
JetMultiplicity05ProbePassingIsoVLR9Id.objects = cms.InputTag(
    PF_JET_COLL_05_PROBE_PASSING_ISOVL_R9ID
    )
JetMultiplicity05ProbePassingIsoVL = JetMultiplicity05.clone()
JetMultiplicity05ProbePassingIsoVL.probes = cms.InputTag(
    "probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLEB"
    )
JetMultiplicity05ProbePassingIsoVL.objects = cms.InputTag(PF_JET_COLL_05_PROBE_PASSING_ISOVL)
JetMultiplicity05ProbePassingR9Id = JetMultiplicity05.clone()
JetMultiplicity05ProbePassingR9Id.probes = cms.InputTag(
    "probePhotonsPassingPUCorrectedCombinedIsoIdR9IdEB"
    )
JetMultiplicity05ProbePassingR9Id.objects = cms.InputTag(PF_JET_COLL_05_PROBE_PASSING_R9ID)

#count IDed and dR < 0.7 cross-cleaned PF jets passing cuts
JetMultiplicity07 = cms.EDProducer(
    "CandMultiplicityCounter",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(PF_JET_COLL_07),
    objectSelection = cms.string(JET_CUTS),
    )
JetMultiplicity07ProbePassingIso = JetMultiplicity07.clone()
JetMultiplicity07ProbePassingIso.probes = cms.InputTag("probePhotonsPassingIsolation")
JetMultiplicity07ProbePassingIso.objects = cms.InputTag(PF_JET_COLL_07_PROBE_PASSING_ISO)
JetMultiplicity07ProbePassingIdEB = JetMultiplicity07.clone()
JetMultiplicity07ProbePassingIdEB.probes = cms.InputTag("probePhotonsPassingIdEB")
JetMultiplicity07ProbePassingIdEB.objects = cms.InputTag(PF_JET_COLL_07_PROBE_PASSING_ID_EB)
JetMultiplicity07ProbePassingIdEE = JetMultiplicity07.clone()
JetMultiplicity07ProbePassingIdEE.probes = cms.InputTag("probePhotonsPassingIdEE")
JetMultiplicity07ProbePassingIdEE.objects = cms.InputTag(PF_JET_COLL_07_PROBE_PASSING_ID_EE)

#count IDed and dR < 0.9 cross-cleaned PF jets passing cuts
JetMultiplicity09 = cms.EDProducer(
    "CandMultiplicityCounter",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(PF_JET_COLL_09),
    objectSelection = cms.string(JET_CUTS),
    )
JetMultiplicity09ProbePassingIso = JetMultiplicity09.clone()
JetMultiplicity09ProbePassingIso.probes = cms.InputTag("probePhotonsPassingIsolation")
JetMultiplicity09ProbePassingIso.objects = cms.InputTag(PF_JET_COLL_09_PROBE_PASSING_ISO)
JetMultiplicity09ProbePassingIdEB = JetMultiplicity09.clone()
JetMultiplicity09ProbePassingIdEB.probes = cms.InputTag("probePhotonsPassingIdEB")
JetMultiplicity09ProbePassingIdEB.objects = cms.InputTag(PF_JET_COLL_09_PROBE_PASSING_ID_EB)
JetMultiplicity09ProbePassingIdEE = JetMultiplicity09.clone()
JetMultiplicity09ProbePassingIdEE.probes = cms.InputTag("probePhotonsPassingIdEE")
JetMultiplicity09ProbePassingIdEE.objects = cms.InputTag(PF_JET_COLL_09_PROBE_PASSING_ID_EE)

#produce dR(photon, nearest IDed uncorrected jet passing cuts on corrected eta and pT)
#use PF jets cleaned with dR = 0.3 algorithm
photonDRToNearestIDedUncorrectedJet03PT10 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(PF_JET_COLL_03),
    objectSelection = cms.string("pt > 10.0"),
    minDR = cms.double(0.0)
)

#produce dR(photon, nearest IDed uncorrected jet passing cuts on corrected eta and pT)
#use PF jets cleaned with dR = 0.3 algorithm
photonDRToNearestIDedUncorrectedJet03PT20 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotons"),
    objects = cms.InputTag(PF_JET_COLL_03),
    objectSelection = cms.string("pt > 20.0"),
    minDR = cms.double(0.0)
)

#jet variable sequences
jet_variable_sequence = cms.Sequence(probesAndTagsToRemove + IDedPFJetProducer00 +
                                     IDedPFJetProducer03 + IDedPFJetProducer05 +
                                     IDedPFJetProducer07 + IDedPFJetProducer09 +
                                     ak5PFJetsL1L2L300 + ak5PFJetsL1L2L303 + ak5PFJetsL1L2L305 +
                                     ak5PFJetsL1L2L307 + ak5PFJetsL1L2L309 +
                                     photonDRToNearestIDedUncorrectedJet00 +
                                     photonDRTo2ndNearestIDedUncorrectedJet00 +
                                     photonDRTo3rdNearestIDedUncorrectedJet00 +
                                     photonDRToNearestIDedUncorrectedJet03 +
                                     photonDRToNearestIDedUncorrectedJet05 +
                                     photonDRToNearestIDedUncorrectedJet07 +
                                     photonDRToNearestIDedUncorrectedJet09 +
                                     JetMultiplicity03 + JetMultiplicity05 +
                                     JetMultiplicity07 + JetMultiplicity09 +
                                     photonDRToNearestIDedUncorrectedJet03PT10 +
                                     photonDRToNearestIDedUncorrectedJet03PT20)
jet_variable_09_sequence = cms.Sequence(probesAndTagsToRemove + IDedPFJetProducer00 +
                                        IDedPFJetProducer09 + ak5PFJetsL1L2L300 +
                                        ak5PFJetsL1L2L309 +
                                        photonDRToNearestIDedUncorrectedJet00 +
                                        photonDRTo2ndNearestIDedUncorrectedJet00 +
                                        photonDRTo3rdNearestIDedUncorrectedJet00 +
                                        photonDRToNearestIDedUncorrectedJet09 +
                                        JetMultiplicity09)
jet_variable_sequence_probe_passing_iso = cms.Sequence(
    probesPassingIsoAndTagsToRemove + IDedPFJetProducer00ProbePassingIso +
    IDedPFJetProducer03ProbePassingIso + IDedPFJetProducer05ProbePassingIso +
    IDedPFJetProducer07ProbePassingIso + IDedPFJetProducer09ProbePassingIso +
    ak5PFJetsL1L2L300ProbePassingIso + ak5PFJetsL1L2L303ProbePassingIso +
    ak5PFJetsL1L2L305ProbePassingIso + ak5PFJetsL1L2L307ProbePassingIso +
    ak5PFJetsL1L2L309ProbePassingIso + photonPassingIsoDRToNearestIDedUncorrectedJet00 +
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
    probesPassingIsoAndTagsToRemove + IDedPFJetProducer00ProbePassingIso +
    IDedPFJetProducer09ProbePassingIso + ak5PFJetsL1L2L300ProbePassingIso +
    ak5PFJetsL1L2L309ProbePassingIso + photonPassingIsoDRToNearestIDedUncorrectedJet00 +
    photonPassingIsoDRTo2ndNearestIDedUncorrectedJet00 +
    photonPassingIsoDRTo3rdNearestIDedUncorrectedJet00 +
    photonPassingIsoDRToNearestIDedUncorrectedJet09 + JetMultiplicity09ProbePassingIso
    )
jet_variable_sequence_probe_passing_ID = cms.Sequence(
    probesPassingIdEBAndTagsToRemove + IDedPFJetProducer00ProbePassingIdEB +
    IDedPFJetProducer03ProbePassingIdEB + IDedPFJetProducer05ProbePassingIdEB +
    IDedPFJetProducer07ProbePassingIdEB + IDedPFJetProducer09ProbePassingIdEB +
    ak5PFJetsL1L2L300ProbePassingIdEB + ak5PFJetsL1L2L303ProbePassingIdEB +
    ak5PFJetsL1L2L305ProbePassingIdEB + ak5PFJetsL1L2L307ProbePassingIdEB +
    ak5PFJetsL1L2L309ProbePassingIdEB + photonPassingIdEBDRToNearestIDedUncorrectedJet00 +
    photonPassingIdEBDRTo2ndNearestIDedUncorrectedJet00 +
    photonPassingIdEBDRTo3rdNearestIDedUncorrectedJet00 +
    photonPassingIdEBDRToNearestIDedUncorrectedJet03 +
    photonPassingIdEBDRToNearestIDedUncorrectedJet05 +
    photonPassingIdEBDRToNearestIDedUncorrectedJet07 +
    photonPassingIdEBDRToNearestIDedUncorrectedJet09 + JetMultiplicity03ProbePassingIdEB +
    JetMultiplicity05ProbePassingIdEB + JetMultiplicity07ProbePassingIdEB +
    JetMultiplicity09ProbePassingIdEB + probesPassingIdEEAndTagsToRemove +
    IDedPFJetProducer00ProbePassingIdEE + IDedPFJetProducer03ProbePassingIdEE +
    IDedPFJetProducer05ProbePassingIdEE + IDedPFJetProducer07ProbePassingIdEE +
    IDedPFJetProducer09ProbePassingIdEE + ak5PFJetsL1L2L300ProbePassingIdEE +
    ak5PFJetsL1L2L303ProbePassingIdEE + ak5PFJetsL1L2L305ProbePassingIdEE +
    ak5PFJetsL1L2L307ProbePassingIdEE + ak5PFJetsL1L2L309ProbePassingIdEE +
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
    probesPassingIdEBAndTagsToRemove + IDedPFJetProducer00ProbePassingIdEB +
    IDedPFJetProducer09ProbePassingIdEB + ak5PFJetsL1L2L300ProbePassingIdEB +
    ak5PFJetsL1L2L309ProbePassingIdEB + photonPassingIdEBDRToNearestIDedUncorrectedJet00 +
    photonPassingIdEBDRTo2ndNearestIDedUncorrectedJet00 +
    photonPassingIdEBDRTo3rdNearestIDedUncorrectedJet00 +
    photonPassingIdEBDRToNearestIDedUncorrectedJet09 + JetMultiplicity09ProbePassingIdEB +
    probesPassingIdEEAndTagsToRemove + IDedPFJetProducer00ProbePassingIdEE +
    IDedPFJetProducer09ProbePassingIdEE + ak5PFJetsL1L2L300ProbePassingIdEE +
    ak5PFJetsL1L2L309ProbePassingIdEE + photonPassingIdEEDRToNearestIDedUncorrectedJet00 +
    photonPassingIdEEDRTo2ndNearestIDedUncorrectedJet00 +
    photonPassingIdEEDRTo3rdNearestIDedUncorrectedJet00 +
    photonPassingIdEEDRToNearestIDedUncorrectedJet09 + JetMultiplicity09ProbePassingIdEE
    )
jet_variable_sequence_2011 = cms.Sequence(
    probesAndTagsToRemove + IDedPFJetProducer00 + IDedPFJetProducer03 + IDedPFJetProducer05 +
    IDedPFJetProducer07 + IDedPFJetProducer09 + ak5PFJetsL1L2L300 + ak5PFJetsL1L2L303 +
    ak5PFJetsL1L2L305 + ak5PFJetsL1L2L307 + ak5PFJetsL1L2L309 +
    photonDRToNearestIDedUncorrectedJet00 + photonDRTo2ndNearestIDedUncorrectedJet00 +
    photonDRTo3rdNearestIDedUncorrectedJet00 + photonDRToNearestIDedUncorrectedJet03 +
    photonDRToNearestIDedUncorrectedJet05 + photonDRToNearestIDedUncorrectedJet07 +
    photonDRToNearestIDedUncorrectedJet09 + JetMultiplicity03 + JetMultiplicity05 +
    JetMultiplicity07 + JetMultiplicity09 + photonDRToNearestIDedUncorrectedJet03PT10 +
    photonDRToNearestIDedUncorrectedJet03PT20 + probesPassingIsoVLR9IdAndTagsToRemove +
    IDedPFJetProducer00ProbePassingIsoVLR9Id + IDedPFJetProducer05ProbePassingIsoVLR9Id + 
    ak5PFJetsL1L2L305ProbePassingIsoVLR9Id +
    photonPassingIsoVLR9IdDRToNearestIDedUncorrectedJet05 +
    JetMultiplicity05ProbePassingIsoVLR9Id + probesPassingIsoVLAndTagsToRemove +
    IDedPFJetProducer00ProbePassingIsoVL + IDedPFJetProducer05ProbePassingIsoVL + 
    ak5PFJetsL1L2L305ProbePassingIsoVL + photonPassingIsoVLDRToNearestIDedUncorrectedJet05 +
    JetMultiplicity05ProbePassingIsoVL + probesPassingR9IdAndTagsToRemove +
    IDedPFJetProducer00ProbePassingR9Id + IDedPFJetProducer05ProbePassingR9Id + 
    ak5PFJetsL1L2L305ProbePassingR9Id + photonPassingR9IdDRToNearestIDedUncorrectedJet05 +
    JetMultiplicity05ProbePassingR9Id +
    IDedPFJetProducer03ProbePassingIsoVLR9Id + 
    ak5PFJetsL1L2L303ProbePassingIsoVLR9Id +
    photonPassingIsoVLR9IdDRToNearestIDedUncorrectedJet03 +
    probesPassingIsoVLAndTagsToRemove +
    IDedPFJetProducer03ProbePassingIsoVL + 
    ak5PFJetsL1L2L303ProbePassingIsoVL + photonPassingIsoVLDRToNearestIDedUncorrectedJet03 +
    probesPassingR9IdAndTagsToRemove +
    IDedPFJetProducer03ProbePassingR9Id + 
    ak5PFJetsL1L2L303ProbePassingR9Id + photonPassingR9IdDRToNearestIDedUncorrectedJet03
    )
