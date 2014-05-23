import FWCore.ParameterSet.Config as cms

process = cms.Process("TagProbe")

##    ___            _           _      
##   |_ _|_ __   ___| |_   _  __| | ___ 
##    | || '_ \ / __| | | | |/ _` |/ _ \
##    | || | | | (__| | |_| | (_| |  __/
##   |___|_| |_|\___|_|\__,_|\__,_|\___|

process.load('FWCore.MessageService.MessageLogger_cfi')
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True),
##                                      SkipEvent = cms.untracked.vstring('ProductNotFound')
                                     )
process.MessageLogger.cerr.FwkReport.reportEvery = 10000

############
############
########################

#configurables
MC_flag = False
HLTPath1 = "HLT_Photon32_CaloIdL_Photon26_CaloIdL_v1"
HLTPath2 = "HLT_Photon32_CaloIdL_Photon26_CaloIdL_v2"
HLTPath3 = "HLT_Photon32_CaloIdL_Photon26_CaloIdL_v3"
HLTPath4 = "HLT_Photon32_CaloIdL_Photon26_CaloIdL_v4"
#paths for >=1e33 HLT menu (deployed 13-May-2011)
## HLTPath5 = "HLT_Photon36_CaloIdL_Photon22_CaloIdL_v1"
## HLTPath6 = "HLT_Photon36_CaloIdL_Photon22_CaloIdL_v2"
## HLTPath7 = "HLT_Photon36_CaloIdL_Photon22_CaloIdL_v3"
InputTagProcess = "HLT"
RECOProcess = "RECO"
globalTag = "GR_R_42_V14::All"
outputFile = "tagProbeTree_data_photonToID.root"
probeDef = "(hadronicOverEm < 0.1) && (et > 35.0) && (abs(eta) < 1.479) && (abs(abs(superCluster.eta) - 1.479) >= 0.1)"
isoCuts = "(ecalRecHitSumEtConeDR04 < (0.006*pt + 4.2)) && (hcalTowerSumEtConeDR04 < (0.0025*pt + 2.2))"
ECALIsoCut = "ecalRecHitSumEtConeDR04 < (0.006*pt + 4.2)"
HCALIsoCut = "hcalTowerSumEtConeDR04 < (0.0025*pt + 2.2)"
IDCuts = "(hadronicOverEm < 0.05) && (trkSumPtHollowConeDR04 < (0.001*pt + 2.0)) && (sigmaIetaIeta < 0.013)"
HOverECut = "hadronicOverEm < 0.05"
trackIsoCut = "trkSumPtHollowConeDR04 < (0.001*pt + 2.0)"
sigmaIetaIetaCut013 = "sigmaIetaIeta < 0.013"
sigmaIetaIetaCut009 = "sigmaIetaIeta < 0.009"
tagDef = "(sigmaIetaIeta < 0.009) && (hasPixelSeed = 1.0) && (hadronicOverEm < 0.05) && (pt > 35.0) && (abs(eta) < 1.479) && (abs(abs(superCluster.eta) - 1.479) >= 0.1)"
ARBITRATION = "BestMass"
MZ = 91.2 #GeV

#stuff needed for prescales
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = globalTag

########################

##   ____             _ ____                           
##  |  _ \ ___   ___ | / ___|  ___  _   _ _ __ ___ ___ 
##  | |_) / _ \ / _ \| \___ \ / _ \| | | | '__/ __/ _ \
##  |  __/ (_) | (_) | |___) | (_) | |_| | | | (_|  __/
##  |_|   \___/ \___/|_|____/ \___/ \__,_|_|  \___\___|
##  

readFiles = cms.untracked.vstring()
process.source = cms.Source("PoolSource", 
                            fileNames = readFiles
                            )
readFiles.extend([
    '/store/relval/CMSSW_4_2_3/RelValZEE/GEN-SIM-RECO/START42_V12-v2/0067/7ED5B1F7-DB7B-E011-896C-0026189438BF.root',
    '/store/relval/CMSSW_4_2_3/RelValZEE/GEN-SIM-RECO/START42_V12-v2/0062/FCEBB129-397B-E011-993B-00261894394D.root',
    '/store/relval/CMSSW_4_2_3/RelValZEE/GEN-SIM-RECO/START42_V12-v2/0062/3CE75CB9-317B-E011-86BE-002618943864.root'
    ])
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )    
process.source.inputCommands = cms.untracked.vstring("keep *","drop *_MEtoEDMConverter_*_*")

#----------------------PROBE DEFINITION------------------------#
#--------------------------------------------------------------#

#basic probe photon selection
process.probePhotonsEB = cms.EDFilter("PhotonSelector",
                                      src = cms.InputTag("photons", "", RECOProcess),
                                      cut = cms.string(probeDef)
                                      )

#loose track match requirement cuts down on non-Z-electron background
## process.trackMatchedFilteredProbePhotonsEB = cms.EDProducer(
##     "TrackMatchedPhotonProducer",
##     src = cms.InputTag("probePhotonsEB"),
##     ReferenceTrackCollection = cms.untracked.InputTag("generalTracks", "", RECOProcess),
##     deltaR = cms.untracked.double(0.1),
##     trackPTMin = cms.double(30.0),
##     trackEtaMax = cms.double(1.4),
##     )
process.trackMatchedFilteredProbePhotonsEB = cms.EDProducer(
    "TrackMatchedPhotonProducer",
    srcObject = cms.InputTag("probePhotonsEB"),
    srcObjectsToMatch = cms.VInputTag(cms.InputTag("generalTracks", "", RECOProcess)),
    deltaRMax = cms.double(0.1),
    srcObjectsToMatchSelection = cms.string("(pt > 30.0) && (abs(eta) < 1.4)")
    )

#--------------------------------------------------------------#
#----------------------PROBE DEFINITION------------------------#

##   ____                         ____ _           _            
##  / ___| _   _ _ __   ___ _ __ / ___| |_   _ ___| |_ ___ _ __ 
##  \___ \| | | | '_ \ / _ \ '__| |   | | | | / __| __/ _ \ '__|
##   ___) | |_| | |_) |  __/ |  | |___| | |_| \__ \ ||  __/ |   
##  |____/ \__,_| .__/ \___|_|   \____|_|\__,_|___/\__\___|_|   
##  

process.sc_sequence = cms.Sequence(process.probePhotonsEB #*
#                                   process.trackMatchedFilteredProbePhotonsEB
                                   )

##     ___           _       _   _             
##    |_ _|___  ___ | | __ _| |_(_) ___  _ __  
##     | |/ __|/ _ \| |/ _` | __| |/ _ \| '_ \ 
##     | |\__ \ (_) | | (_| | |_| | (_) | | | |
##    |___|___/\___/|_|\__,_|\__|_|\___/|_| |_|

                                         
#  Isolation ################
#ECAL and HCAL only
process.probePhotonsPassingIsolationEB = cms.EDFilter("PhotonRefSelector",
                                                      src = cms.InputTag("probePhotonsEB"),
                                                      cut = cms.string(isoCuts)
                                                      )

#ECAL only
process.probePhotonsPassingECALIsolationEB = cms.EDFilter("PhotonRefSelector",
                                                          src = cms.InputTag("probePhotonsEB"),
                                                          cut = cms.string(ECALIsoCut)
                                                          )

#HCAL only
process.probePhotonsPassingHCALIsolationEB = cms.EDFilter("PhotonRefSelector",
                                                          src = cms.InputTag("probePhotonsEB"),
                                                          cut = cms.string(HCALIsoCut)
                                                          )

##    _____ _           _                     ___    _ 
##   | ____| | ___  ___| |_ _ __ ___  _ __   |_ _|__| |
##   |  _| | |/ _ \/ __| __| '__/ _ \| '_ \   | |/ _` |
##   | |___| |  __/ (__| |_| | | (_) | | | |  | | (_| |
##   |_____|_|\___|\___|\__|_|  \___/|_| |_| |___\__,_|
##   

#photon ID

#ECAL and HCAL isolation + track isolation, H/E, and sigmaIetaIeta
process.probePhotonsPassingIdEB = cms.EDFilter(
    "PhotonRefSelector",
    src = cms.InputTag("probePhotonsEB"),
    cut = cms.string(process.probePhotonsPassingIsolationEB.cut.value() + " && " + IDCuts)
    )

#H/E
process.probePhotonsPassingHOverEEB = cms.EDFilter(
    "PhotonRefSelector",
    src = cms.InputTag("probePhotonsEB"),
    cut = cms.string(HOverECut)
    )

#track isolation
process.probePhotonsPassingTrackIsolationEB = cms.EDFilter(
    "PhotonRefSelector",
    src = cms.InputTag("probePhotonsEB"),
    cut = cms.string(trackIsoCut)
    )

#sigmaIetaIeta < 0.013 (SUS-10-002)
process.probePhotonsPassingSigmaIetaIeta013EB = cms.EDFilter(
    "PhotonRefSelector",
    src = cms.InputTag("probePhotonsEB"),
    cut = cms.string(sigmaIetaIetaCut013)
    )

#sigmaIetaIeta < 0.009 (SUS-10-002)
process.probePhotonsPassingSigmaIetaIeta009EB = cms.EDFilter(
    "PhotonRefSelector",
    src = cms.InputTag("probePhotonsEB"),
    cut = cms.string(sigmaIetaIetaCut009)
    )

##    _____     _                         __  __       _       _     _             
##   |_   _| __(_) __ _  __ _  ___ _ __  |  \/  | __ _| |_ ___| |__ (_)_ __   __ _ 
##     | || '__| |/ _` |/ _` |/ _ \ '__| | |\/| |/ _` | __/ __| '_ \| | '_ \ / _` |
##     | || |  | | (_| | (_| |  __/ |    | |  | | (_| | || (__| | | | | | | | (_| |
##     |_||_|  |_|\__, |\__, |\___|_|    |_|  |_|\__,_|\__\___|_| |_|_|_| |_|\__, |
##                |___/ |___/                                                |___/ 
##   

# Trigger  ##################

#new implementation of trgMatchedPhotonProducer that accepts multiple HLT paths
process.probePhotonsPassingHLTEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingIdEB"),
    hltTags = cms.VInputTag(
    cms.InputTag(HLTPath1, "", InputTagProcess),
    cms.InputTag(HLTPath2, "", InputTagProcess),
    cms.InputTag(HLTPath3, "", InputTagProcess),
    cms.InputTag(HLTPath4, "", InputTagProcess)#,
    #paths for >=1e33 HLT menu (deployed 13-May-2011)    
##     cms.InputTag(HLTPath5, "", InputTagProcess),
##     cms.InputTag(HLTPath6, "", InputTagProcess),
##     cms.InputTag(HLTPath7, "", InputTagProcess)
    ),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess),
    triggerResultsTag = cms.InputTag("TriggerResults", "", InputTagProcess)
    )

##    _____      _                        _  __     __             
##   | ____|_  _| |_ ___ _ __ _ __   __ _| | \ \   / /_ _ _ __ ___ 
##   |  _| \ \/ / __/ _ \ '__| '_ \ / _` | |  \ \ / / _` | '__/ __|
##   | |___ >  <| ||  __/ |  | | | | (_| | |   \ V / (_| | |  \__ \
##   |_____/_/\_\\__\___|_|  |_| |_|\__,_|_|    \_/ \__,_|_|  |___/
##   

## Here we show how to use a module to compute an external variable
process.load("JetMETCorrections.Configuration.DefaultJEC_cff")
process.ak5JPTJetsL2L3 = cms.EDProducer("JPTJetCorrectionProducer",
                                        src = cms.InputTag("JetPlusTrackZSPCorJetAntiKt5"),
                                        correctors = cms.vstring("ak5JPTL2L3")
                                        )
JET_COLL_00 = "ak5JPTJetsL2L300"
JET_COLL_03 = "ak5JPTJetsL2L303"
JET_COLL_05 = "ak5JPTJetsL2L305"
JET_COLL_07 = "ak5JPTJetsL2L307"
JET_COLL_09 = "ak5JPTJetsL2L309"
JET_CUTS = "pt > 30.0"
JET_CUTS_00 = "pt > 0.0"

#photons to clean from jet collection: probes in a tag-probe pair
process.probesToRemove = cms.EDProducer("ProbeMaker",
                                        tagProbePairs = cms.InputTag("tagPhoton"),
                                        arbitration = cms.string(ARBITRATION),
                                        massForArbitration = cms.double(MZ)
                                        )

#producer of dR < 0.0 photon-cleaned jets
#passing LOOSE PURE09 jet ID (https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID)
process.IDedJetProducer00 = cms.EDProducer(
    "IDedJetProducer",
    caloJetSrc = cms.InputTag("ak5CaloJets", "", "RECO"),
    jetIDSrc = cms.InputTag("ak5JetID", "", "RECO"),
    JPTJetSrc = cms.InputTag("JetPlusTrackZSPCorJetAntiKt5", "", "RECO"),
    photonSrc = cms.InputTag("probesToRemove"),
    cleaningDR = cms.double(0.0),
    maxAbsEta = cms.double(2.6)
    )

#producer of dR < 0.3 photon-cleaned jets
#passing LOOSE PURE09 jet ID (https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID)
process.IDedJetProducer03 = cms.EDProducer(
    "IDedJetProducer",
    caloJetSrc = cms.InputTag("ak5CaloJets", "", "RECO"),
    jetIDSrc = cms.InputTag("ak5JetID", "", "RECO"),
    JPTJetSrc = cms.InputTag("JetPlusTrackZSPCorJetAntiKt5", "", "RECO"),
    photonSrc = cms.InputTag("probesToRemove"),
    cleaningDR = cms.double(0.3),
    maxAbsEta = cms.double(2.6)
    )

#producer of dR < 0.5 photon-cleaned jets
#passing LOOSE PURE09 jet ID (https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID)
process.IDedJetProducer05 = cms.EDProducer(
    "IDedJetProducer",
    caloJetSrc = cms.InputTag("ak5CaloJets", "", "RECO"),
    jetIDSrc = cms.InputTag("ak5JetID", "", "RECO"),
    JPTJetSrc = cms.InputTag("JetPlusTrackZSPCorJetAntiKt5", "", "RECO"),
    photonSrc = cms.InputTag("probesToRemove"),
    cleaningDR = cms.double(0.5),
    maxAbsEta = cms.double(2.6)
    )

#producer of dR < 0.7 photon-cleaned jets
#passing LOOSE PURE09 jet ID (https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID)
process.IDedJetProducer07 = cms.EDProducer(
    "IDedJetProducer",
    caloJetSrc = cms.InputTag("ak5CaloJets", "", "RECO"),
    jetIDSrc = cms.InputTag("ak5JetID", "", "RECO"),
    JPTJetSrc = cms.InputTag("JetPlusTrackZSPCorJetAntiKt5", "", "RECO"),
    photonSrc = cms.InputTag("probesToRemove"),
    cleaningDR = cms.double(0.7),
    maxAbsEta = cms.double(2.6)
    )

#producer of dR < 0.9 photon-cleaned jets
#passing LOOSE PURE09 jet ID (https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID)
process.IDedJetProducer09 = cms.EDProducer(
    "IDedJetProducer",
    caloJetSrc = cms.InputTag("ak5CaloJets", "", "RECO"),
    jetIDSrc = cms.InputTag("ak5JetID", "", "RECO"),
    JPTJetSrc = cms.InputTag("JetPlusTrackZSPCorJetAntiKt5", "", "RECO"),
    photonSrc = cms.InputTag("probesToRemove"),
    cleaningDR = cms.double(0.9),
    maxAbsEta = cms.double(2.6)
    )

#produce corrected jet collection from IDed and dR < 0.0 cross-cleaned jet collection
process.ak5JPTJetsL2L300 = process.ak5JPTJetsL2L3.clone()
process.ak5JPTJetsL2L300.src = cms.InputTag("IDedJetProducer00")

#produce corrected jet collection from IDed and dR < 0.3 cross-cleaned jet collection
process.ak5JPTJetsL2L303 = process.ak5JPTJetsL2L3.clone()
process.ak5JPTJetsL2L303.src = cms.InputTag("IDedJetProducer03")

#produce corrected jet collection from IDed and dR < 0.5 cross-cleaned jet collection
process.ak5JPTJetsL2L305 = process.ak5JPTJetsL2L3.clone()
process.ak5JPTJetsL2L305.src = cms.InputTag("IDedJetProducer05")

#produce corrected jet collection from IDed and dR < 0.7 cross-cleaned jet collection
process.ak5JPTJetsL2L307 = process.ak5JPTJetsL2L3.clone()
process.ak5JPTJetsL2L307.src = cms.InputTag("IDedJetProducer07")

#produce corrected jet collection from IDed and dR < 0.9 cross-cleaned jet collection
process.ak5JPTJetsL2L309 = process.ak5JPTJetsL2L3.clone()
process.ak5JPTJetsL2L309.src = cms.InputTag("IDedJetProducer09")

#produce dR(photon, nearest IDed uncorrected jet passing cuts on corrected eta)
#use jets cleaned with dR = 0.0 algorithm
process.photonDRToNearestIDedUncorrectedJet00 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotonsEB"),
    objects = cms.InputTag(JET_COLL_00),
    objectSelection = cms.string(JET_CUTS_00),
    minDR = cms.double(0.0)
)

#produce dR(photon, 2nd nearest IDed uncorrected jet passing cuts on corrected eta)
#use jets cleaned with dR = 0.0 algorithm
process.photonDRTo2ndNearestIDedUncorrectedJet00 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotonsEB"),
    objects = cms.InputTag(JET_COLL_00),
    objectSelection = cms.string(JET_CUTS_00),
    minDR = cms.double(0.0),
    pos = cms.untracked.uint32(1)
)

#produce dR(photon, 3rd nearest IDed uncorrected jet passing cuts on corrected eta)
#use jets cleaned with dR = 0.0 algorithm
process.photonDRTo3rdNearestIDedUncorrectedJet00 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotonsEB"),
    objects = cms.InputTag(JET_COLL_00),
    objectSelection = cms.string(JET_CUTS_00),
    minDR = cms.double(0.0),
    pos = cms.untracked.uint32(2)                                                           
)

#produce dR(photon, nearest IDed uncorrected jet passing cuts on corrected eta and pT)
#use jets cleaned with dR = 0.3 algorithm
process.photonDRToNearestIDedUncorrectedJet03 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotonsEB"),
    objects = cms.InputTag(JET_COLL_03),
    objectSelection = cms.string(JET_CUTS),
    minDR = cms.double(0.0)
)

#produce dR(photon, nearest IDed uncorrected jet passing cuts on corrected eta and pT)
#use jets cleaned with dR = 0.5 algorithm
process.photonDRToNearestIDedUncorrectedJet05 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotonsEB"),
    objects = cms.InputTag(JET_COLL_05),
    objectSelection = cms.string(JET_CUTS),
    minDR = cms.double(0.0)
)

#produce dR(photon, nearest IDed uncorrected jet passing cuts on corrected eta and pT)
#use jets cleaned with dR = 0.7 algorithm
process.photonDRToNearestIDedUncorrectedJet07 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotonsEB"),
    objects = cms.InputTag(JET_COLL_07),
    objectSelection = cms.string(JET_CUTS),
    minDR = cms.double(0.0)
)

#produce dR(photon, nearest IDed uncorrected jet passing cuts on corrected eta and pT)
#use jets cleaned with dR = 0.9 algorithm
process.photonDRToNearestIDedUncorrectedJet09 = cms.EDProducer(
    "DeltaRNearestJetDRSortComputer",
    probes = cms.InputTag("probePhotonsEB"),
    objects = cms.InputTag(JET_COLL_09),
    objectSelection = cms.string(JET_CUTS),
    minDR = cms.double(0.0)
)

#count IDed and dR < 0.0 cross-cleaned jets passing cuts
process.JetMultiplicity00 = cms.EDProducer(
    "CandMultiplicityCounter",
    probes = cms.InputTag("probePhotonsEB"),
    objects = cms.InputTag(JET_COLL_00),
    objectSelection = cms.string(JET_CUTS),
    )

#count IDed and dR < 0.3 cross-cleaned jets passing cuts
process.JetMultiplicity03 = cms.EDProducer(
    "CandMultiplicityCounter",
    probes = cms.InputTag("probePhotonsEB"),
    objects = cms.InputTag(JET_COLL_03),
    objectSelection = cms.string(JET_CUTS),
    )

#count IDed and dR < 0.5 cross-cleaned jets passing cuts
process.JetMultiplicity05 = cms.EDProducer(
    "CandMultiplicityCounter",
    probes = cms.InputTag("probePhotonsEB"),
    objects = cms.InputTag(JET_COLL_05),
    objectSelection = cms.string(JET_CUTS),
    )

#count IDed and dR < 0.7 cross-cleaned jets passing cuts
process.JetMultiplicity07 = cms.EDProducer(
    "CandMultiplicityCounter",
    probes = cms.InputTag("probePhotonsEB"),
    objects = cms.InputTag(JET_COLL_07),
    objectSelection = cms.string(JET_CUTS),
    )

#count IDed and dR < 0.9 cross-cleaned jets passing cuts
process.JetMultiplicity09 = cms.EDProducer(
    "CandMultiplicityCounter",
    probes = cms.InputTag("probePhotonsEB"),
    objects = cms.InputTag(JET_COLL_09),
    objectSelection = cms.string(JET_CUTS),
    )

process.ext_ToNearestJet_sequence = cms.Sequence(
    process.probesToRemove + process.IDedJetProducer00 + process.IDedJetProducer03 +
    process.IDedJetProducer05 + process.IDedJetProducer07 + process.IDedJetProducer09 +
    process.ak5JPTJetsL2L300 + process.ak5JPTJetsL2L303 + process.ak5JPTJetsL2L305 +
    process.ak5JPTJetsL2L307 + process.ak5JPTJetsL2L309 +
    process.photonDRToNearestIDedUncorrectedJet00 +
    process.photonDRTo2ndNearestIDedUncorrectedJet00 +
    process.photonDRTo3rdNearestIDedUncorrectedJet00 +
    process.photonDRToNearestIDedUncorrectedJet03 +
    process.photonDRToNearestIDedUncorrectedJet05 +
    process.photonDRToNearestIDedUncorrectedJet07 +
    process.photonDRToNearestIDedUncorrectedJet09 +
    process.JetMultiplicity03 + process.JetMultiplicity05 + process.JetMultiplicity07 +
    process.JetMultiplicity09
    )

##    _____             ____        __ _       _ _   _             
##   |_   _|_ _  __ _  |  _ \  ___ / _(_)_ __ (_) |_(_) ___  _ __  
##     | |/ _` |/ _` | | | | |/ _ \ |_| | '_ \| | __| |/ _ \| '_ \ 
##     | | (_| | (_| | | |_| |  __/  _| | | | | | |_| | (_) | | | |
##     |_|\__,_|\__, | |____/ \___|_| |_|_| |_|_|\__|_|\___/|_| |_|
##              |___/                                              

#step 1: tag should be tightly matched to a track
## process.trackMatchedPhotons = cms.EDProducer(
##     "TrackMatchedPhotonProducer",
##     src = cms.InputTag("probePhotonsEB"),
##     ReferenceTrackCollection = cms.untracked.InputTag("generalTracks", "", RECOProcess),
##     deltaR = cms.untracked.double(0.04),
##     trackPTMin = cms.double(15.0),
##     trackEtaMax = cms.double(1.479),
##     )
process.trackMatchedPhotons = cms.EDProducer(
    "TrackMatchedPhotonProducer",
    srcObject = cms.InputTag("probePhotonsEB"),
    srcObjectsToMatch = cms.VInputTag(cms.InputTag("generalTracks", "", RECOProcess)),
    deltaRMax = cms.double(0.04),
    srcObjectsToMatchSelection = cms.string("(pt > 15.0) && (abs(eta) < 1.479)")
    )

#step 2: tag should have good shower shape, a pixel seed, have good H/E, be reasonably high pT, and be in EB
process.goodPhotons = cms.EDFilter("PhotonRefSelector",
                                   src = cms.InputTag("trackMatchedPhotons"),
                                   cut = cms.string(tagDef)
                                   )

#step 3: tag should have fired the HLT path under study
process.Tag = cms.EDProducer(
    "trgMatchedPhotonProducer",
    InputProducer = cms.InputTag("goodPhotons"),
    hltTags = cms.VInputTag(
    cms.InputTag(HLTPath1, "", InputTagProcess),
    cms.InputTag(HLTPath2, "", InputTagProcess),
    cms.InputTag(HLTPath3, "", InputTagProcess),
    cms.InputTag(HLTPath4, "", InputTagProcess),
    #paths for >=1e33 HLT menu (deployed 13-May-2011)
##     cms.InputTag(HLTPath5, "", InputTagProcess),
##     cms.InputTag(HLTPath6, "", InputTagProcess),
##     cms.InputTag(HLTPath7, "", InputTagProcess)
    ),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", InputTagProcess)
    )

process.ele_sequence = cms.Sequence(process.probePhotonsPassingIsolationEB +
                                    process.probePhotonsPassingECALIsolationEB +
                                    process.probePhotonsPassingHCALIsolationEB + 
                                    process.probePhotonsPassingIdEB +
                                    process.probePhotonsPassingHOverEEB +
                                    process.probePhotonsPassingTrackIsolationEB +
                                    process.probePhotonsPassingSigmaIetaIeta013EB +
                                    process.probePhotonsPassingSigmaIetaIeta009EB + 
                                    (process.trackMatchedPhotons * process.goodPhotons *
                                     #trigger requirement for tag when it's a double-photon trigger?
                                     process.Tag)
                                    )


##    _____ ___   ____    ____       _          
##   |_   _( _ ) |  _ \  |  _ \ __ _(_)_ __ ___ 
##     | | / _ \/\ |_) | | |_) / _` | | '__/ __|
##     | || (_>  <  __/  |  __/ (_| | | |  \__ \
##     |_| \___/\/_|     |_|   \__,_|_|_|  |___/
##                                              
##   
#  Tag & probe selection ######

#tag required to fire specific HLT
process.tagPhoton = cms.EDProducer("CandViewShallowCloneCombiner",
                                   decay = cms.string("Tag probePhotonsEB"),
                                   checkCharge = cms.bool(False),
                                   cut = cms.string("60 < mass < 120")
                                   )

#no trigger requirement on tag
process.tagPhotonNoHLT = cms.EDProducer("CandViewShallowCloneCombiner",
                                        decay = cms.string("goodPhotons probePhotonsEB"),
                                        checkCharge = cms.bool(False),
                                        cut = cms.string("60 < mass < 120")
                                        )

process.tagIsoEBPhotons = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("Tag probePhotonsPassingIsolationEB"), # charge coniugate states are implied
    checkCharge = cms.bool(False),                                   
    cut   = cms.string("60 < mass < 120"),
)

process.tagIdEBPhotons = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("Tag probePhotonsPassingIdEB"), # charge coniugate states are implied
    checkCharge = cms.bool(False),                                  
    cut   = cms.string("60 < mass < 120"),
)

process.tagHLTEBPhotons = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("Tag probePhotonsPassingHLTEB"), # charge coniugate states are implied
    checkCharge = cms.bool(False),                                   
    cut   = cms.string("60 < mass < 120"),
)

process.allTagsAndProbes = cms.Sequence(process.tagPhoton + process.tagPhotonNoHLT +
                                        process.tagIsoEBPhotons + process.tagIdEBPhotons
                                        )


##    __  __  ____   __  __       _       _               
##   |  \/  |/ ___| |  \/  | __ _| |_ ___| |__   ___  ___ 
##   | |\/| | |     | |\/| |/ _` | __/ __| '_ \ / _ \/ __|
##   | |  | | |___  | |  | | (_| | || (__| | | |  __/\__ \
##   |_|  |_|\____| |_|  |_|\__,_|\__\___|_| |_|\___||___/
##                                                        

process.McMatchTag = cms.EDProducer("MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("Tag"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
)

process.McMatchPhoton = cms.EDProducer("MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("probePhotonsEB"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles")
)

process.McMatchIso = cms.EDProducer("MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("probePhotonsPassingIsolationEB"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
)

process.McMatchId = cms.EDProducer("MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("probePhotonsPassingIdEB"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
)

process.McMatchHLT = cms.EDProducer("MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("probePhotonsPassingHLTEB"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
)

process.mc_sequence = cms.Sequence(process.McMatchTag +  process.McMatchPhoton +
                                   process.McMatchIso + process.McMatchId
                                   )

############################################################################
##    _____           _       _ ____            _            _   _  ____  ##
##   |_   _|_ _  __ _( )_ __ ( )  _ \ _ __ ___ | |__   ___  | \ | |/ ___| ##
##     | |/ _` |/ _` |/| '_ \|/| |_) | '__/ _ \| '_ \ / _ \ |  \| | |  _  ##
##     | | (_| | (_| | | | | | |  __/| | | (_) | |_) |  __/ | |\  | |_| | ##
##     |_|\__,_|\__, | |_| |_| |_|   |_|  \___/|_.__/ \___| |_| \_|\____| ##
##              |___/                                                     ##
##                                                                        ##
############################################################################
##    ____                      _     _           
##   |  _ \ ___ _   _ ___  __ _| |__ | | ___  ___ 
##   | |_) / _ \ | | / __|/ _` | '_ \| |/ _ \/ __|
##   |  _ <  __/ |_| \__ \ (_| | |_) | |  __/\__ \
##   |_| \_\___|\__,_|___/\__,_|_.__/|_|\___||___/


## I define some common variables for re-use later.
## This will save us repeating the same code for each efficiency category

ZVariablesToStore = cms.PSet(
    eta = cms.string("eta"),
    pt  = cms.string("pt"),
    phi  = cms.string("phi"),
    et  = cms.string("et"),
    e  = cms.string("energy"),
    p  = cms.string("p"),
    px  = cms.string("px"),
    py  = cms.string("py"),
    pz  = cms.string("pz"),
    theta  = cms.string("theta"),    
    vx     = cms.string("vx"),
    vy     = cms.string("vy"),
    vz     = cms.string("vz"),
    rapidity  = cms.string("rapidity"),
    mass  = cms.string("mass"),
    mt  = cms.string("mt"),    
)   

TagPhotonVariablesToStore = cms.PSet(
    photon_eta = cms.string("eta"),
    photon_pt  = cms.string("pt"),
    photon_phi  = cms.string("phi"),
    photon_px  = cms.string("px"),
    photon_py  = cms.string("py"),
    photon_pz  = cms.string("pz"),
    ## super cluster quantities
    sc_energy = cms.string("superCluster.energy"),
    sc_et     = cms.string("superCluster.energy*sin(superCluster.position.theta)"),    
    sc_x      = cms.string("superCluster.x"),
    sc_y      = cms.string("superCluster.y"),
    sc_z      = cms.string("superCluster.z"),
    sc_eta    = cms.string("superCluster.eta"),
    sc_phi    = cms.string("superCluster.phi"),
    sc_size   = cms.string("superCluster.size"), # number of hits
    sc_rawEnergy = cms.string("superCluster.rawEnergy"), 
    sc_preshowerEnergy   = cms.string("superCluster.preshowerEnergy"), 
    sc_phiWidth   = cms.string("superCluster.phiWidth"), 
    sc_etaWidth   = cms.string("superCluster.etaWidth"),         
    ## isolation 
    photon_trackiso_dr04 = cms.string("trkSumPtHollowConeDR04"),
    photon_ecaliso_dr04  = cms.string("ecalRecHitSumEtConeDR04"),
    photon_hcaliso_dr04  = cms.string("hcalTowerSumEtConeDR04"),
    photon_trackiso_dr03 = cms.string("trkSumPtHollowConeDR03"),
    photon_ecaliso_dr03  = cms.string("ecalRecHitSumEtConeDR03"),
    photon_hcaliso_dr03  = cms.string("hcalTowerSumEtConeDR04"),
    ## classification, location, etc.    
    photon_isEB           = cms.string("isEB"),
    photon_isEE           = cms.string("isEE"),
    photon_isEBEEGap      = cms.string("isEBEEGap"),
    photon_isEBEtaGap     = cms.string("isEBEtaGap"),
    photon_isEBPhiGap     = cms.string("isEBPhiGap"),
    photon_isEEDeeGap     = cms.string("isEEDeeGap"),
    photon_isEERingGap    = cms.string("isEERingGap"),
    ## Hcal energy over Ecal Energy
    photon_HoverE         = cms.string("hadronicOverEm"),
    photon_HoverE_Depth1  = cms.string("hadronicDepth1OverEm"),
    photon_HoverE_Depth2  = cms.string("hadronicDepth2OverEm"),
    ## Cluster shape information
    photon_sigmaEtaEta  = cms.string("sigmaEtaEta"),
    photon_sigmaIetaIeta = cms.string("sigmaIetaIeta"),
    photon_e1x5               = cms.string("e1x5"),
    photon_e2x5            = cms.string("e2x5"),
    photon_e5x5               = cms.string("e5x5"),
    photon_hasPixelSeed = cms.string("hasPixelSeed")
)

ProbePhotonVariablesToStore = cms.PSet(
        probe_eta = cms.string("eta"),
        probe_phi  = cms.string("phi"),
        probe_et  = cms.string("et"),
        probe_px  = cms.string("px"),
        probe_py  = cms.string("py"),
        probe_pz  = cms.string("pz"),
        ## isolation 
        probe_trkSumPtHollowConeDR03 = cms.string("trkSumPtHollowConeDR03"),
        probe_ecalRecHitSumEtConeDR03  = cms.string("ecalRecHitSumEtConeDR03"),
        probe_hcalTowerSumEtConeDR03  = cms.string("hcalTowerSumEtConeDR03"),
        probe_trkSumPtHollowConeDR04 = cms.string("trkSumPtHollowConeDR04"),
        probe_ecalRecHitSumEtConeDR04  = cms.string("ecalRecHitSumEtConeDR04"),
        probe_hcalTowerSumEtConeDR04  = cms.string("hcalTowerSumEtConeDR04"),
        ## booleans
        probe_isPhoton  = cms.string("isPhoton"),     
        ## Hcal energy over Ecal Energy
        probe_hadronicOverEm = cms.string("hadronicOverEm"),
        ## Cluster shape information
        probe_sigmaIetaIeta = cms.string("sigmaIetaIeta"),
        probe_sigmaIphiIphi = cms.string("superCluster.phiWidth"),
        ## Pixel seed
        probe_hasPixelSeed = cms.string("hasPixelSeed")
)

CommonStuffForPhotonProbe = cms.PSet(
   variables = cms.PSet(ProbePhotonVariablesToStore),
   ignoreExceptions =  cms.bool (False),
   #fillTagTree      =  cms.bool (True),
   addRunLumiInfo   =  cms.bool (True),
   addEventVariablesInfo   =  cms.bool (True),
   pairVariables =  cms.PSet(ZVariablesToStore),
   pairFlags     =  cms.PSet(
          mass60to120 = cms.string("60 < mass < 120")
    ),
    tagVariables   =  cms.PSet(TagPhotonVariablesToStore),
    tagFlags     =  cms.PSet(
          flag = cms.string("pt>0")
    ),    
)

if MC_flag:
    mcTruthCommonStuff = cms.PSet(
        isMC = cms.bool(MC_flag),
        tagMatches = cms.InputTag("McMatchTag"),
        motherPdgId = cms.vint32(22,23),
        makeMCUnbiasTree = cms.bool(MC_flag),
        checkMotherInUnbiasEff = cms.bool(MC_flag),
        mcVariables = cms.PSet(
        probe_eta = cms.string("eta"),
        probe_pt  = cms.string("pt"),
        probe_phi  = cms.string("phi"),
        probe_et  = cms.string("et"),
        probe_e  = cms.string("energy"),
        probe_p  = cms.string("p"),
        probe_px  = cms.string("px"),
        probe_py  = cms.string("py"),
        probe_pz  = cms.string("pz"),
        probe_theta  = cms.string("theta"),    
        probe_vx     = cms.string("vx"),
        probe_vy     = cms.string("vy"),
        probe_vz     = cms.string("vz"),   
        probe_charge = cms.string("charge"),
        probe_rapidity  = cms.string("rapidity"),    
        probe_mass  = cms.string("mass"),
        probe_mt  = cms.string("mt"),    
        ),
        mcFlags     =  cms.PSet(
        probe_flag = cms.string("pt>0")
        ),      
        )
else:
     mcTruthCommonStuff = cms.PSet(
         isMC = cms.bool(False)
         )

## loose photon --> isolation
process.PhotonToIsolation = cms.EDAnalyzer("TagProbeFitTreeProducer",
                                           ## pick the defaults
                                           mcTruthCommonStuff,
                                           CommonStuffForPhotonProbe,
                                           # choice of tag and probe pairs, and arbitration
                                           tagProbePairs = cms.InputTag("tagPhoton"),
                                           arbitration   = cms.string(ARBITRATION),
                                           massForArbitration = cms.double(MZ),
                                           flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingIsolationEB"),
    probe_passingALL = cms.InputTag("probePhotonsPassingHLTEB"),
    probe_passingIso = cms.InputTag("probePhotonsPassingIsolationEB"),
    probe_passingId = cms.InputTag("probePhotonsPassingIdEB")
    ),
                                           probeMatches = cms.InputTag("McMatchPhoton"),
                                           allProbes = cms.InputTag("probePhotonsEB")
                                           )
process.PhotonToIsolation.variables.probe_dRjet05 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet05"
    )
process.PhotonToIsolation.variables.probe_dRjet09 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet09"
    )
#process.PhotonToIsolation.variables.probe_nJets05 = cms.InputTag("JetMultiplicity05")
#process.PhotonToIsolation.variables.probe_nJets09 = cms.InputTag("JetMultiplicity09")

##    ___                 __    ___    _ 
##   |_ _|___  ___        \ \  |_ _|__| |
##    | |/ __|/ _ \   _____\ \  | |/ _` |
##    | |\__ \ (_) | |_____/ /  | | (_| |
##   |___|___/\___/       /_/  |___\__,_|
##   
##  isolation --> Id

#isolated --> ID'ed photon
process.IsoToId = cms.EDAnalyzer("TagProbeFitTreeProducer",
                                 mcTruthCommonStuff,
                                 CommonStuffForPhotonProbe,
                                 tagProbePairs = cms.InputTag("tagIsoEBPhotons"),
                                 arbitration = cms.string(ARBITRATION),
                                 massForArbitration = cms.double(MZ),
                                 flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingIdEB"),
    probe_passingId = cms.InputTag("probePhotonsPassingIdEB"),
    probe_passingALL = cms.InputTag("probePhotonsPassingHLTEB")         
    ),
                                 probeMatches = cms.InputTag("McMatchIso"),
                                 allProbes = cms.InputTag("probePhotonsPassingIsolationEB")
                                 )
process.IsoToId.variables.probe_dRjet05 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet05"
    )
process.IsoToId.variables.probe_dRjet09 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet09"
    )
#process.IsoToId.variables.probe_nJets05 = cms.InputTag("JetMultiplicity05")
#process.IsoToId.variables.probe_nJets09 = cms.InputTag("JetMultiplicity09")

##    ___    _       __    _   _ _   _____ 
##   |_ _|__| |      \ \  | | | | | |_   _|
##    | |/ _` |  _____\ \ | |_| | |   | |  
##    | | (_| | |_____/ / |  _  | |___| |  
##   |___\__,_|      /_/  |_| |_|_____|_|  

##  Id --> HLT

#ID'ed --> HLT photon
process.IdToHLT = cms.EDAnalyzer("TagProbeFitTreeProducer",
                                 mcTruthCommonStuff,
                                 CommonStuffForPhotonProbe,
                                 tagProbePairs = cms.InputTag("tagIdEBPhotons"),
                                 arbitration = cms.string(ARBITRATION),
                                 massForArbitration = cms.double(MZ),
                                 flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingHLTEB")
    ),
                                 probeMatches = cms.InputTag("McMatchId"),
                                 allProbes = cms.InputTag("probePhotonsPassingIdEB")
                                 )
process.IdToHLT.variables.probe_dRjet05 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet05"
    )
process.IdToHLT.variables.probe_dRjet09 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet09"
    )
#process.IdToHLT.variables.probe_nJets05 = cms.InputTag("JetMultiplicity05")
#process.IdToHLT.variables.probe_nJets09 = cms.InputTag("JetMultiplicity09")

#loose --> HLT photon
process.PhotonToHLT = cms.EDAnalyzer("TagProbeFitTreeProducer",
                                     mcTruthCommonStuff,
                                     CommonStuffForPhotonProbe,
                                     tagProbePairs = cms.InputTag("tagPhoton"),
                                     arbitration = cms.string(ARBITRATION),
                                     massForArbitration = cms.double(MZ),
                                     flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingHLTEB")
    ),
                                     probeMatches = cms.InputTag("McMatchPhoton"),
                                     allProbes = cms.InputTag("probePhotonsEB")
                                     )
process.PhotonToHLT.variables.probe_dRjet05 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet05"
    )
process.PhotonToHLT.variables.probe_dRjet09 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet09"
    )
#process.PhotonToHLT.variables.probe_nJets05 = cms.InputTag("JetMultiplicity05")
#process.PhotonToHLT.variables.probe_nJets09 = cms.InputTag("JetMultiplicity09")

#loose --> ID'ed photon, tag required to fire specific HLT
process.PhotonToID = cms.EDAnalyzer("TagProbeFitTreeProducer",
                                    mcTruthCommonStuff,
                                    CommonStuffForPhotonProbe,
                                    tagProbePairs = cms.InputTag("tagPhoton"),
                                    arbitration   = cms.string(ARBITRATION),
                                    massForArbitration = cms.double(MZ),
                                    flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingIdEB")
    ),
                                    probeMatches = cms.InputTag("McMatchPhoton"),
                                    allProbes = cms.InputTag("probePhotonsEB")
                                    )
process.PhotonToID.variables.probe_dR1jet00 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet00"
    )
process.PhotonToID.variables.probe_dR2jet00 = cms.InputTag(
    "photonDRTo2ndNearestIDedUncorrectedJet00"
    )
process.PhotonToID.variables.probe_dR3jet00 = cms.InputTag(
    "photonDRTo3rdNearestIDedUncorrectedJet00"
    )
process.PhotonToID.variables.probe_dRjet03 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet03"
    )
process.PhotonToID.variables.probe_dRjet05 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet05"
    )
process.PhotonToID.variables.probe_dRjet07 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet07"
    )
process.PhotonToID.variables.probe_dRjet09 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet09"
    )
process.PhotonToID.variables.probe_nJets03 = cms.InputTag("JetMultiplicity03")
process.PhotonToID.variables.probe_nJets05 = cms.InputTag("JetMultiplicity05")
process.PhotonToID.variables.probe_nJets07 = cms.InputTag("JetMultiplicity07")
process.PhotonToID.variables.probe_nJets09 = cms.InputTag("JetMultiplicity09")

#loose --> ID'ed photon, no trigger requirement on tag
process.PhotonToIDNoHLT = process.PhotonToID.clone()
process.PhotonToIDNoHLT.tagProbePairs = cms.InputTag("tagPhotonNoHLT")

#loose --> photon passing ECAL isolation, tag required to fire specific HLT
process.PhotonToECALIso = process.PhotonToID.clone()
process.PhotonToECALIso.flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingECALIsolationEB")
    )

#loose --> photon passing ECAL isolation, no trigger requirement on tag
process.PhotonToECALIsoNoHLT = process.PhotonToECALIso.clone()
process.PhotonToECALIsoNoHLT.tagProbePairs = cms.InputTag("tagPhotonNoHLT")

#loose --> photon passing HCAL isolation, tag required to fire specific HLT
process.PhotonToHCALIso = process.PhotonToID.clone()
process.PhotonToHCALIso.flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingHCALIsolationEB")
    )

#loose --> photon passing HCAL isolation, no trigger requirement on tag
process.PhotonToHCALIsoNoHLT = process.PhotonToHCALIso.clone()
process.PhotonToHCALIsoNoHLT.tagProbePairs = cms.InputTag("tagPhotonNoHLT")

#loose --> photon passing H/E, tag required to fire specific HLT
process.PhotonToHOverE = process.PhotonToID.clone()
process.PhotonToHOverE.flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingHOverEEB")
    )

#loose --> photon passing H/E, no trigger requirement on tag
process.PhotonToHOverENoHLT = process.PhotonToHOverE.clone()
process.PhotonToHOverENoHLT.tagProbePairs = cms.InputTag("tagPhotonNoHLT")

#loose --> photon passing track isolation, tag required to fire specific HLT
process.PhotonToTrackIso = process.PhotonToID.clone()
process.PhotonToTrackIso.flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingTrackIsolationEB")
    )

#loose --> photon passing track isolation, no trigger requirement on tag
process.PhotonToTrackIsoNoHLT = process.PhotonToTrackIso.clone()
process.PhotonToTrackIsoNoHLT.tagProbePairs = cms.InputTag("tagPhotonNoHLT")

#loose --> photon passing sigmaIetaIeta < 0.013, tag required to fire specific HLT
process.PhotonToSigmaIetaIeta013 = process.PhotonToID.clone()
process.PhotonToSigmaIetaIeta013.flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingSigmaIetaIeta013EB")
    )

#loose --> photon passing sigmaIetaIeta < 0.013, no trigger requirement on tag
process.PhotonToSigmaIetaIeta013NoHLT = process.PhotonToSigmaIetaIeta013.clone()
process.PhotonToSigmaIetaIeta013NoHLT.tagProbePairs = cms.InputTag("tagPhotonNoHLT")

#loose --> photon passing sigmaIetaIeta < 0.009, tag required to fire specific HLT
process.PhotonToSigmaIetaIeta009 = process.PhotonToID.clone()
process.PhotonToSigmaIetaIeta009.flags = cms.PSet(
    probe_passing = cms.InputTag("probePhotonsPassingSigmaIetaIeta009EB")
    )

#loose --> photon passing sigmaIetaIeta < 0.009, no trigger requirement on tag
process.PhotonToSigmaIetaIeta009NoHLT = process.PhotonToSigmaIetaIeta009.clone()
process.PhotonToSigmaIetaIeta009NoHLT.tagProbePairs = cms.InputTag("tagPhotonNoHLT")
 
process.tree_sequence = cms.Sequence(
##     process.PhotonToIsolation + process.IsoToId + process.IdToHLT + process.PhotonToHLT + 
##     process.PhotonToID + process.PhotonToIDNoHLT + process.PhotonToECALIso +
##     process.PhotonToECALIsoNoHLT + process.PhotonToHCALIso + process.PhotonToHCALIsoNoHLT +
##     process.PhotonToHOverE + process.PhotonToHOverENoHLT + process.PhotonToTrackIso +
##     process.PhotonToTrackIsoNoHLT + process.PhotonToSigmaIetaIeta013 +
##     process.PhotonToSigmaIetaIeta013NoHLT + process.PhotonToSigmaIetaIeta009 +
##     process.PhotonToSigmaIetaIeta009NoHLT
    process.PhotonToID + process.PhotonToECALIso + process.PhotonToHCALIso + 
    process.PhotonToHOverE + process.PhotonToTrackIso + process.PhotonToSigmaIetaIeta013
    )

##    ____       _   _     
##   |  _ \ __ _| |_| |__  
##   | |_) / _` | __| '_ \ 
##   |  __/ (_| | |_| | | |
##   |_|   \__,_|\__|_| |_|
##

if MC_flag:
    process.tagAndProbe = cms.Path(
        process.sc_sequence + process.ele_sequence +
        process.allTagsAndProbes +
        process.ext_ToNearestJet_sequence + 
        process.mc_sequence + 
        process.tree_sequence
        )
else:
    process.tagAndProbe = cms.Path(
        process.sc_sequence + process.ele_sequence +
        process.allTagsAndProbes +
        process.ext_ToNearestJet_sequence + 
        process.tree_sequence
        )

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string(outputFile)
                                   )
