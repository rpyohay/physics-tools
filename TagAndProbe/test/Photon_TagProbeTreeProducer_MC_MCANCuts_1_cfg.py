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
                                     SkipEvent = cms.untracked.vstring('ProductNotFound')
                                     )
process.MessageLogger.cerr.FwkReport.reportEvery = 1


############
process.load("RecoEgamma.EgammaTools.correctedElectronsProducer_cfi")
############
########################

#configurables
MC_flag = True
#MC_flag = False
HLTPath1 = "HLT_Photon30_L1R_8E29"
HLTPath2 = "HLT_Photon30_L1R"
HLTPath3 = "HLT_Photon30_Cleaned_L1R"
InputTagProcess = "REDIGI36X"
#InputTagProcess = "HLT"
#RECOProcess = "RECO"
RECOProcess = "RECOCleaned"
#globalTag = "START36_V7::All"
globalTag = "GR_R_36X_V12::All"
outputFile = "/data/yohay/tagProbeTree_MC_MCANCuts/tagProbeTree_MC_MCANCuts_201010.root"

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
    'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_100_2_Gk7.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_101_2_ofY.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_102_2_for.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_103_2_9eu.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_104_2_NCd.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_105_2_AKM.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_106_2_fRW.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_107_2_oFy.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_108_1_N6y.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_109_3_WYZ.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_10_2_hcX.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_110_2_ySE.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_111_2_kuk.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_112_2_fmv.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_113_1_6fF.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_114_2_9Bj.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_115_2_9ty.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_116_1_aSi.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_117_2_tg7.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_118_2_sEG.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_119_3_1M0.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_11_2_U5q.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_120_2_2kB.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_121_2_loe.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_122_2_SIe.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_123_2_Fjx.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_124_2_gGv.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_125_1_gtR.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_126_2_tJ1.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_127_2_7ka.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_128_2_lIp.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_129_3_TmJ.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_12_2_ZEP.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_130_2_bID.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_131_2_4wZ.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_132_2_edL.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_133_1_5pX.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_134_2_8Ur.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_135_2_CFM.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_136_2_Izr.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_137_2_5Y5.root', 'rfio:/castor/cern.ch/user/y/yohay/361p4/Zee/Skimmed_138_3_Tqo.root'
    ])

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )    
process.source.inputCommands = cms.untracked.vstring("keep *","drop *_MEtoEDMConverter_*_*")


#----------------------PROBE DEFINITION------------------------#
#--------------------------------------------------------------#

#basic probe photon selection
#keep EB and EE efficiencies separate
process.probePhotonsEB = cms.EDFilter("PhotonSelector",
                                      src = cms.InputTag("photons", "", RECOProcess),                                      
                                      cut = cms.string("hadronicOverEm<0.5"
                                                       " && pt>10"
                                                       " && (abs(eta)<1.479) && (abs(abs(superCluster.eta) - 1.479)>=0.1)")
                                      )

#process.FilteredPhotonsEB = cms.EDFilter("PhotonRefSelector",
#                                         src = cms.InputTag("probePhotonsEB"),
#                                         cut = cms.string("")
#                                         )

#loose track match requirement cuts down on non-Z-electron background
process.trackMatchedFilteredProbePhotonsEB = cms.EDProducer(
    "TrackMatchedPhotonProducer",
    src = cms.InputTag("probePhotonsEB"),
    ReferenceTrackCollection = cms.untracked.InputTag("generalTracks", "", RECOProcess),
    deltaR = cms.untracked.double(0.1),
    trackPTMin = cms.double(30.0),
    trackEtaMax = cms.double(1.4),
    )

#--------------------------------------------------------------#
#----------------------PROBE DEFINITION------------------------#




##   ____                         ____ _           _            
##  / ___| _   _ _ __   ___ _ __ / ___| |_   _ ___| |_ ___ _ __ 
##  \___ \| | | | '_ \ / _ \ '__| |   | | | | / __| __/ _ \ '__|
##   ___) | |_| | |_) |  __/ |  | |___| | |_| \__ \ ||  __/ |   
##  |____/ \__,_| .__/ \___|_|   \____|_|\__,_|___/\__\___|_|   
##  

#  SuperClusters  ################
#process.superClusters = cms.EDProducer("SuperClusterMerger",
#   src = cms.VInputTag(cms.InputTag("hybridSuperClusters","", "RECO"),
#                       cms.InputTag("multi5x5SuperClustersWithPreshower","", "RECO"))  
#)

#process.superClusterCands = cms.EDProducer("ConcreteEcalCandidateProducer",
#   src = cms.InputTag("superClusters"),
#   particleType = cms.int32(11),
#)

#   Get the above SC's Candidates and place a cut on their Et and eta
#process.goodSuperClusters = cms.EDFilter("CandViewSelector",
#      src = cms.InputTag("superClusterCands"),
#      cut = cms.string("et>20.0 && abs(eta)<2.5 && !(1.4442< abs(eta) <1.566)"),
#      filter = cms.bool(True)
#)                                         
                                         

#### remove real jets (with high hadronic energy fraction) from SC collection
##### this improves the purity of the probe sample without affecting efficiency

#process.JetsToRemoveFromSuperCluster = cms.EDFilter("CaloJetSelector",   
#    src = cms.InputTag("ak5CaloJets"),
#    cut = cms.string('pt>5 && energyFractionHadronic > 0.15')
#)


#process.goodSuperClustersClean = cms.EDProducer("CandViewCleaner",
#    srcCands = cms.InputTag("goodSuperClusters"),
#    module_label = cms.string(''),
#    srcObjects = cms.VInputTag(cms.InputTag("JetsToRemoveFromSuperCluster")),
#    deltaRMin = cms.double(0.1)
#)

## process.superClusters = cms.EDFilter("EgammaHLTRecoEcalCandidateProducers",
##    scHybridBarrelProducer =  cms.InputTag("hybridSuperClusters","", "RECO"),
##    scIslandEndcapProducer =  cms.InputTag("multi5x5SuperClustersWithPreshower","", "RECO"),    
##    recoEcalCandidateCollection = cms.string("")
## )

process.sc_sequence = cms.Sequence( process.probePhotonsEB *
                                    process.trackMatchedFilteredProbePhotonsEB
#                                    process.superClusters *
#                                    process.superClusterCands *
#                                    process.goodSuperClusters *
#                                    process.JetsToRemoveFromSuperCluster *
#                                    process.goodSuperClustersClean
                                    )


##    ____      __ _____ _           _                   
##   / ___|___ / _| ____| | ___  ___| |_ _ __ ___  _ __  
##  | |  _/ __| |_|  _| | |/ _ \/ __| __| '__/ _ \| '_ \ 
##  | |_| \__ \  _| |___| |  __/ (__| |_| | | (_) | | | |
##   \____|___/_| |_____|_|\___|\___|\__|_|  \___/|_| |_|
##  

#  GsfElectron ################ 
#process.PassingGsf = cms.EDFilter("GsfElectronRefSelector",
#    src = cms.InputTag("gsfElectrons"),
#    cut = cms.string("(abs(superCluster.eta)<2.5) && !(1.4442<abs(superCluster.eta)<1.566)"
#                     " && (ecalEnergy*sin(superClusterPosition.theta)>20.0) && (hadronicOverEm<0.15)")    
#)


#process.GsfMatchedSuperClusterCands = cms.EDProducer("ElectronMatchedCandidateProducer",
#   src     = cms.InputTag("goodSuperClustersClean"),
#   ReferenceElectronCollection = cms.untracked.InputTag("PassingGsf"),
#   deltaR =  cms.untracked.double(0.3)
#)

##does the probe EB photon match in space to a GSF electron?
#I don't think we really care about this
#process.GsfMatchedPhotonCands = cms.EDProducer("ElectronMatchedCandidateProducer",
#   src     = cms.InputTag("FilteredPhotonsEB"),
#   ReferenceElectronCollection = cms.untracked.InputTag("PassingGsf"),
#   deltaR =  cms.untracked.double(0.3)
#)
            

##     ___           _       _   _             
##    |_ _|___  ___ | | __ _| |_(_) ___  _ __  
##     | |/ __|/ _ \| |/ _` | __| |/ _ \| '_ \ 
##     | |\__ \ (_) | | (_| | |_| | (_) | | | |
##    |___|___/\___/|_|\__,_|\__|_|\___/|_| |_|

                                         
#  Isolation ################
#ECAL and HCAL only
process.probePhotonsPassingIsolationEB = cms.EDFilter("PhotonRefSelector",
                                                      src = cms.InputTag("trackMatchedFilteredProbePhotonsEB"),
                                                      cut = cms.string("(ecalRecHitSumEtConeDR04 < (0.006*pt + 4.2)) && (hcalTowerSumEtConeDR04 < (0.0025*pt + 2.2 ))")
                                                      )

##    _____ _           _                     ___    _ 
##   | ____| | ___  ___| |_ _ __ ___  _ __   |_ _|__| |
##   |  _| | |/ _ \/ __| __| '__/ _ \| '_ \   | |/ _` |
##   | |___| |  __/ (__| |_| | | (_) | | | |  | | (_| |
##   |_____|_|\___|\___|\__|_|  \___/|_| |_| |___\__,_|
##   

# Electron ID  ######

#process.PassingId = cms.EDFilter("GsfElectronRefSelector",
#    src = cms.InputTag("gsfElectrons"),
#    cut = cms.string(process.PassingIsolation.cut.value() +
#                     " && (gsfTrack.trackerExpectedHitsInner.numberOfHits <= 1)"
#                     " && ((isEB"
#                                   " && (sigmaIetaIeta<0.01)"
#                                   " && ( -0.8<deltaPhiSuperClusterTrackAtVtx<0.8 )"
#                                   " && ( -0.007<deltaEtaSuperClusterTrackAtVtx<0.007 )"
#                                   " && (hadronicOverEm<0.15)"
#                                   ")"
#                     " || (isEE"
#                                   " && (sigmaIetaIeta<0.03)"
#                                   " && ( -0.7<deltaPhiSuperClusterTrackAtVtx<0.7 )"
                                   #" && ( -0.01<deltaEtaSuperClusterTrackAtVtx<0.01 )"
#                                   " && (hadronicOverEm<0.07) "
#                                   "))"
#                     ) 
#)


#process.PassingId80 = cms.EDFilter("GsfElectronRefSelector",
#    src = cms.InputTag("gsfElectrons"),
#    cut = cms.string(process.PassingGsf.cut.value() +
#                     " && (gsfTrack.trackerExpectedHitsInner.numberOfHits <= 0)"
#                     " && ((isEB"
#                                   " && ( (dr03TkSumPt + max(0., dr03EcalRecHitSumEt - 1.) + dr03HcalTowerSumEt)/(p4.Pt) < 0.07 )"
#                                   " && (sigmaIetaIeta<0.01)"
#                                   " && ( -0.06<deltaPhiSuperClusterTrackAtVtx<0.06 )"
#                                   " && ( -0.004<deltaEtaSuperClusterTrackAtVtx<0.004 )"
#                                   " && (hadronicOverEm<0.04)"
#                                   ")"
#                     " || (isEE"
#                                   " && ( (dr03TkSumPt + dr03EcalRecHitSumEt + dr03HcalTowerSumEt)/(p4.Pt) < 0.06 )"
#                                   " && (sigmaIetaIeta<0.03)"
#                                   " && ( -0.03<deltaPhiSuperClusterTrackAtVtx<0.03 )"
                                   #" && ( -0.007<deltaEtaSuperClusterTrackAtVtx<0.007 )"
#                                   " && (hadronicOverEm<0.025) "
#                                   "))"
#                     ) 
#)

#photon ID

#track isolation
process.probePhotonsPassingIdEB = cms.EDFilter("PhotonRefSelector",
                                               src = cms.InputTag("trackMatchedFilteredProbePhotonsEB"),
                                               cut = cms.string(process.probePhotonsPassingIsolationEB.cut.value() +
                                                                " && (hadronicOverEm < 0.05)"
                                                                " && (trkSumPtHollowConeDR04 < (0.001*pt + 2.0)"
                                                                " && (sigmaIetaIeta < 0.013))"
                                                                )
                                               )


                         
##    _____     _                         __  __       _       _     _             
##   |_   _| __(_) __ _  __ _  ___ _ __  |  \/  | __ _| |_ ___| |__ (_)_ __   __ _ 
##     | || '__| |/ _` |/ _` |/ _ \ '__| | |\/| |/ _` | __/ __| '_ \| | '_ \ / _` |
##     | || |  | | (_| | (_| |  __/ |    | |  | | (_| | || (__| | | | | | | | (_| |
##     |_||_|  |_|\__, |\__, |\___|_|    |_|  |_|\__,_|\__\___|_| |_|_|_| |_|\__, |
##                |___/ |___/                                                |___/ 
##   

# Trigger  ##################
#process.PassingHLT = cms.EDProducer("trgMatchedGsfElectronProducer",                     
#    InputProducer = cms.InputTag("PassingId"),                          
#    hltTag = cms.untracked.InputTag(HLTPath,"","HLT"),
#    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","","HLT")
#)

#new implementation of trgMatchedPhotonProducer that accepts multiple HLT paths
process.probePhotonsPassingHLTEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingIdEB"),
    hltTags = cms.VInputTag(
    cms.InputTag(HLTPath1,"",InputTagProcess),
    cms.InputTag(HLTPath2,"",InputTagProcess),
    cms.InputTag(HLTPath3,"",InputTagProcess)
    ),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",InputTagProcess),
    triggerResultsTag = cms.InputTag("TriggerResults", "", InputTagProcess)
    )

#process.badSuperClustersClean = cms.EDProducer("CandViewCleaner",
#    srcCands = cms.InputTag("goodSuperClustersClean"),
#    module_label = cms.string(''),
#    srcObjects = cms.VInputTag(cms.InputTag("PassingHLT")),
#    deltaRMin = cms.double(0.1)
#)

##    _____      _                        _  __     __             
##   | ____|_  _| |_ ___ _ __ _ __   __ _| | \ \   / /_ _ _ __ ___ 
##   |  _| \ \/ / __/ _ \ '__| '_ \ / _` | |  \ \ / / _` | '__/ __|
##   | |___ >  <| ||  __/ |  | | | | (_| | |   \ V / (_| | |  \__ \
##   |_____/_/\_\\__\___|_|  |_| |_|\__,_|_|    \_/ \__,_|_|  |___/
##   

## Here we show how to use a module to compute an external variable
process.load("JetMETCorrections.Configuration.DefaultJEC_cff")
JET_COLL_05 = "ak5JPTJetsL2L305"
JET_COLL_09 = "ak5JPTJetsL2L309"
JET_CUTS = "pt > 30.0 && abs(eta)<3.0"

#process.superClusterDRToNearestJet = cms.EDProducer("DeltaRNearestObjectComputer",
#    probes = cms.InputTag("goodSuperClusters"),
       # ^^--- NOTA BENE: if probes are defined by ref, as in this case, 
       #       this must be the full collection, not the subset by refs.
#    objects = cms.InputTag(JET_COLL),
#    objectSelection = cms.string(JET_CUTS),
#)

#producer of dR < 0.5 photon-cleaned jets
#passing LOOSE PURE09 jet ID (https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID)
process.IDedJetProducer05 = cms.EDProducer(
    "IDedJetProducer",
    caloJetSrc = cms.InputTag("ak5CaloJets", "", "RECO"),
    jetIDSrc = cms.InputTag("ak5JetID", "", "RECO"),
    JPTJetSrc = cms.InputTag("JetPlusTrackZSPCorJetAntiKt5", "", "RECO"),
    photonSrc = cms.InputTag("photons", "", RECOProcess),
    cleaningDR = cms.double(0.5)
    )

#producer of dR < 0.9 photon-cleaned jets
#passing LOOSE PURE09 jet ID (https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID)
process.IDedJetProducer09 = cms.EDProducer(
    "IDedJetProducer",
    caloJetSrc = cms.InputTag("ak5CaloJets", "", "RECO"),
    jetIDSrc = cms.InputTag("ak5JetID", "", "RECO"),
    JPTJetSrc = cms.InputTag("JetPlusTrackZSPCorJetAntiKt5", "", "RECO"),
    photonSrc = cms.InputTag("photons", "", RECOProcess),
    cleaningDR = cms.double(0.9)
    )

#produce corrected jet collection from IDed and dR < 0.5 cross-cleaned jet collection
process.ak5JPTJetsL2L305 = process.ak5JPTJetsL2L3.clone()
process.ak5JPTJetsL2L305.src = cms.InputTag("IDedJetProducer05")

#produce corrected jet collection from IDed and dR < 0.9 cross-cleaned jet collection
process.ak5JPTJetsL2L309 = process.ak5JPTJetsL2L3.clone()
process.ak5JPTJetsL2L309.src = cms.InputTag("IDedJetProducer09")

#produce dR(photon, nearest IDed uncorrected jet passing cuts on corrected eta and pT)
#use jets cleaned with dR = 0.5 algorithm
process.photonDRToNearestIDedUncorrectedJet05 = cms.EDProducer("DeltaRNearestJetComputer",
    probes = cms.InputTag("trackMatchedFilteredProbePhotonsEB"),
       # ^^--- NOTA BENE: if probes are defined by ref, as in this case, 
       #       this must be the full collection, not the subset by refs.
    objects = cms.InputTag(JET_COLL_05),
    objectSelection = cms.string(JET_CUTS),
                                                               minDR = cms.double(0.0)
)

#produce dR(photon, nearest IDed uncorrected jet passing cuts on corrected eta and pT)
#use jets cleaned with dR = 0.9 algorithm
process.photonDRToNearestIDedUncorrectedJet09 = cms.EDProducer("DeltaRNearestJetComputer",
    probes = cms.InputTag("trackMatchedFilteredProbePhotonsEB"),
       # ^^--- NOTA BENE: if probes are defined by ref, as in this case, 
       #       this must be the full collection, not the subset by refs.
    objects = cms.InputTag(JET_COLL_09),
    objectSelection = cms.string(JET_CUTS),
                                                               minDR = cms.double(0.0)
)

#process.JetMultiplicityInSCEvents = cms.EDProducer("CandMultiplicityCounter",
#    probes = cms.InputTag("goodSuperClusters"),
#    objects = cms.InputTag(JET_COLL),
#    objectSelection = cms.string(JET_CUTS),
#)

#count IDed and dR < 0.5 cross-cleaned jets passing cuts
process.JetMultiplicity05 = cms.EDProducer(
    "CandMultiplicityCounter",
    probes = cms.InputTag("trackMatchedFilteredProbePhotonsEB"),
    objects = cms.InputTag(JET_COLL_05),
    objectSelection = cms.string(JET_CUTS),
    )

#count IDed and dR < 0.9 cross-cleaned jets passing cuts
process.JetMultiplicity09 = cms.EDProducer(
    "CandMultiplicityCounter",
    probes = cms.InputTag("trackMatchedFilteredProbePhotonsEB"),
    objects = cms.InputTag(JET_COLL_09),
    objectSelection = cms.string(JET_CUTS),
    )

#process.GsfDRToNearestJet = cms.EDProducer("DeltaRNearestObjectComputer",
#    probes = cms.InputTag("gsfElectrons"),
#    objects = cms.InputTag(JET_COLL),
#    objectSelection = cms.string(JET_CUTS),
#)



#process.JetMultiplicityInGsfEvents = cms.EDProducer("CandMultiplicityCounter",
#    probes = cms.InputTag("gsfElectrons"),
#    objects = cms.InputTag(JET_COLL),
#    objectSelection = cms.string(JET_CUTS),
#)


process.ext_ToNearestJet_sequence = cms.Sequence(
    process.IDedJetProducer05 + process.IDedJetProducer09 +
    process.ak5JPTJetsL2L305 + process.ak5JPTJetsL2L309 + 
    process.photonDRToNearestIDedUncorrectedJet05 +
    process.photonDRToNearestIDedUncorrectedJet09 +
    process.JetMultiplicity05 + process.JetMultiplicity09
#    process.GsfDRToNearestJet +
#    process.JetMultiplicityInGsfEvents
    )


##    _____             ____        __ _       _ _   _             
##   |_   _|_ _  __ _  |  _ \  ___ / _(_)_ __ (_) |_(_) ___  _ __  
##     | |/ _` |/ _` | | | | |/ _ \ |_| | '_ \| | __| |/ _ \| '_ \ 
##     | | (_| | (_| | | |_| |  __/  _| | | | | | |_| | (_) | | | |
##     |_|\__,_|\__, | |____/ \___|_| |_|_| |_|_|\__|_|\___/|_| |_|
##              |___/                                              

#step 1: tag should be tightly matched to a track
process.trackMatchedPhotons = cms.EDProducer("TrackMatchedPhotonProducer",
                                             src = cms.InputTag("probePhotonsEB"),
                                             ReferenceTrackCollection = cms.untracked.InputTag(
    "generalTracks", "", RECOProcess
    ),
                                             deltaR = cms.untracked.double(0.04),
                                             trackPTMin = cms.double(15.0),
                                             trackEtaMax = cms.double(1.479),
                                             )

#step 2: tag should have good shower shape, a pixel seed, have good H/E, be reasonably high pT, and be in EB
process.goodPhotons = cms.EDFilter("PhotonRefSelector",
                                   src = cms.InputTag("trackMatchedPhotons"),
                                   cut = cms.string("(sigmaIetaIeta < 0.009) && (hasPixelSeed = 1.0) && (hadronicOverEm < 0.05) && (pt > 30.0)"
                                                    " && (abs(eta)<1.479) && (abs(abs(superCluster.eta) - 1.479)>=0.1)"
                                                    )
                                   )

#step 3: tag should have fired the HLT path under study
process.Tag = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("goodPhotons"),
    hltTags = cms.VInputTag(
    cms.InputTag(HLTPath1,"",InputTagProcess),
    cms.InputTag(HLTPath2,"",InputTagProcess),
    cms.InputTag(HLTPath3,"",InputTagProcess)
    ),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",InputTagProcess),
    triggerResultsTag = cms.InputTag("TriggerResults", "", InputTagProcess)
    )

#process.TagMatchedSuperClusterCandsClean = cms.EDProducer("ElectronMatchedCandidateProducer",
#   src     = cms.InputTag("goodSuperClustersClean"),
#   ReferenceElectronCollection = cms.untracked.InputTag("Tag"),
#   deltaR =  cms.untracked.double(0.3)
#)

#probes matched in space to tags -- do we care about this?  I think not
#process.TagMatchedPhotonCands = cms.EDProducer("ElectronMatchedCandidateProducer",
#   src     = cms.InputTag("FilteredPhotonsEB"),
#   ReferenceElectronCollection = cms.untracked.InputTag("Tag"),
#   deltaR =  cms.untracked.double(0.3)
#)

#process.IsoMatchedSuperClusterCandsClean = process.TagMatchedSuperClusterCandsClean.clone()
#process.IsoMatchedSuperClusterCandsClean.ReferenceElectronCollection = cms.untracked.InputTag("PassingIsolation")
#process.IdMatchedSuperClusterCandsClean = process.TagMatchedSuperClusterCandsClean.clone()
#process.IdMatchedSuperClusterCandsClean.ReferenceElectronCollection = cms.untracked.InputTag("PassingId")

#process.Id80MatchedSuperClusterCandsClean = process.TagMatchedSuperClusterCandsClean.clone()
#process.Id80MatchedSuperClusterCandsClean.ReferenceElectronCollection = cms.untracked.InputTag("PassingId80")
#process.IsoMatchedPhotonCands = process.GsfMatchedPhotonCands.clone()
#process.IsoMatchedPhotonCands.ReferenceElectronCollection = cms.untracked.InputTag("PassingIsolation")

#process.IdMatchedPhotonCands = process.GsfMatchedPhotonCands.clone()
#process.IdMatchedPhotonCands.ReferenceElectronCollection = cms.untracked.InputTag("PassingId")

#process.Id80MatchedPhotonCands = process.GsfMatchedPhotonCands.clone()
#process.Id80MatchedPhotonCands.ReferenceElectronCollection = cms.untracked.InputTag("PassingId80")



process.ele_sequence = cms.Sequence(
#    process.PassingGsf * process.GsfMatchedSuperClusterCands +
#    process.GsfMatchedPhotonCands +
    process.probePhotonsPassingIsolationEB + process.probePhotonsPassingIdEB +
#    process.PassingIsolation + process.PassingId +
#    process.PassingId80 +
    process.probePhotonsPassingHLTEB + 
    (process.trackMatchedPhotons * process.goodPhotons * process.Tag)
#    process.PassingHLT + process.Tag*
#    process.TagMatchedSuperClusterCandsClean *
#    process.badSuperClustersClean *
#    process.TagMatchedPhotonCands *
#    process.IsoMatchedSuperClusterCandsClean *
#    process.IdMatchedSuperClusterCandsClean *
#    process.Id80MatchedSuperClusterCandsClean *
#    process.IsoMatchedPhotonCands *
#    process.IdMatchedPhotonCands *
#    process.Id80MatchedPhotonCands    
    )


##    _____ ___   ____    ____       _          
##   |_   _( _ ) |  _ \  |  _ \ __ _(_)_ __ ___ 
##     | | / _ \/\ |_) | | |_) / _` | | '__/ __|
##     | || (_>  <  __/  |  __/ (_| | | |  \__ \
##     |_| \___/\/_|     |_|   \__,_|_|_|  |___/
##                                              
##   
#  Tag & probe selection ######

#process.tagSC = cms.EDProducer("CandViewShallowCloneCombiner",
#    decay = cms.string("Tag goodSuperClustersClean"), # charge coniugate states are implied
#    checkCharge = cms.bool(False),                           
#    cut   = cms.string("60 < mass < 120"),
#)

#process.tagPhoton = cms.EDProducer("CandViewShallowCloneCombiner",
#    decay = cms.string("Tag FilteredPhotonsEB"), # charge coniugate states are implied
#    checkCharge = cms.bool(False),                           
#    cut   = cms.string("60 < mass < 120"),
#)

process.tagPhoton = cms.EDProducer("CandViewShallowCloneCombiner",
                                   decay = cms.string("Tag trackMatchedFilteredProbePhotonsEB"),
                                   checkCharge = cms.bool(False),
                                   cut = cms.string("60 < mass < 120")
                                   )

#process.SCSC = cms.EDProducer("CandViewShallowCloneCombiner",
#    decay = cms.string("badSuperClustersClean badSuperClustersClean"), # charge coniugate states are implied
#    checkCharge = cms.bool(False),                           
#    cut   = cms.string("60 < mass < 120"),
#)

#process.GsfGsf = cms.EDProducer("CandViewShallowCloneCombiner",
#    decay = cms.string("PassingGsf PassingGsf"), # charge coniugate states are implied
#    checkCharge = cms.bool(False),                                   
#    cut   = cms.string("60 < mass < 120"),
#)

#process.tagGsf = cms.EDProducer("CandViewShallowCloneCombiner",
#    decay = cms.string("Tag PassingGsf"), # charge coniugate states are implied
#    checkCharge = cms.bool(False),                                   
#    cut   = cms.string("60 < mass < 120"),
#)


#process.tagIso = cms.EDProducer("CandViewShallowCloneCombiner",
#    decay = cms.string("Tag PassingIsolation"), # charge coniugate states are implied
#    checkCharge = cms.bool(False),                                   
#    cut   = cms.string("60 < mass < 120"),
#)

process.tagIsoEBPhotons = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("Tag probePhotonsPassingIsolationEB"), # charge coniugate states are implied
    checkCharge = cms.bool(False),                                   
    cut   = cms.string("60 < mass < 120"),
)


#process.tagId = cms.EDProducer("CandViewShallowCloneCombiner",
#    decay = cms.string("Tag PassingId"), # charge coniugate states are implied
#    checkCharge = cms.bool(False),                                  
#    cut   = cms.string("60 < mass < 120"),
#)

process.tagIdEBPhotons = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("Tag probePhotonsPassingIdEB"), # charge coniugate states are implied
    checkCharge = cms.bool(False),                                  
    cut   = cms.string("60 < mass < 120"),
)


#process.tagHLT = cms.EDProducer("CandViewShallowCloneCombiner",
#    decay = cms.string("Tag PassingHLT"), # charge coniugate states are implied
#    checkCharge = cms.bool(False),                                   
#    cut   = cms.string("60 < mass < 120"),
#)

process.tagHLTEBPhotons = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("Tag probePhotonsPassingHLTEB"), # charge coniugate states are implied
    checkCharge = cms.bool(False),                                   
    cut   = cms.string("60 < mass < 120"),
)

process.allTagsAndProbes = cms.Sequence(
#    process.tagSC + process.SCSC + process.tagPhoton +
#    process.tagGsf + process.GsfGsf +
#    process.tagIso + process.tagId + process.tagHLT
    process.tagPhoton + process.tagIsoEBPhotons + process.tagIdEBPhotons + process.tagHLTEBPhotons
)


##    __  __  ____   __  __       _       _               
##   |  \/  |/ ___| |  \/  | __ _| |_ ___| |__   ___  ___ 
##   | |\/| | |     | |\/| |/ _` | __/ __| '_ \ / _ \/ __|
##   | |  | | |___  | |  | | (_| | || (__| | | |  __/\__ \
##   |_|  |_|\____| |_|  |_|\__,_|\__\___|_| |_|\___||___/
##                                                        

process.McMatchTag = cms.EDFilter("MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("Tag"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
)


#process.McMatchSC = cms.EDFilter("MCTruthDeltaRMatcherNew",
#    matchPDGId = cms.vint32(11),
#    src = cms.InputTag("goodSuperClustersClean"),
#    distMin = cms.double(0.3),
#    matched = cms.InputTag("genParticles")
#)


process.McMatchPhoton = cms.EDFilter("MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("trackMatchedFilteredProbePhotonsEB"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles")
)


#process.McMatchSCbad = cms.EDFilter("MCTruthDeltaRMatcherNew",
#    matchPDGId = cms.vint32(11),
#    src = cms.InputTag("badSuperClustersClean"),
#    distMin = cms.double(0.3),
#    matched = cms.InputTag("genParticles")
#)


#process.McMatchGsf = cms.EDFilter("MCTruthDeltaRMatcherNew",
#    matchPDGId = cms.vint32(11),
#    src = cms.InputTag("PassingGsf"),
#    distMin = cms.double(0.3),
#    matched = cms.InputTag("genParticles"),
#    checkCharge = cms.bool(True)
#)

process.McMatchIso = cms.EDFilter("MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("probePhotonsPassingIsolationEB"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
)

process.McMatchId = cms.EDFilter("MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("probePhotonsPassingIdEB"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
)

process.McMatchHLT = cms.EDFilter("MCTruthDeltaRMatcherNew",
    matchPDGId = cms.vint32(11),
    src = cms.InputTag("probePhotonsPassingHLTEB"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles"),
    checkCharge = cms.bool(True)
)




#process.mc_sequence = cms.Sequence(
#   process.McMatchTag + process.McMatchSC + process.McMatchPhoton +
#   process.McMatchGsf + process.McMatchIso +
#   process.McMatchId  + process.McMatchHLT
#)
process.mc_sequence = cms.Sequence(
   process.McMatchTag +  process.McMatchPhoton +
   process.McMatchIso +
   process.McMatchId  + process.McMatchHLT
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



#ProbeVariablesToStore = cms.PSet(
#    probe_gsfEle_eta = cms.string("eta"),
#    probe_gsfEle_pt  = cms.string("pt"),
#    probe_gsfEle_phi  = cms.string("phi"),
#    probe_gsfEle_et  = cms.string("et"),
#    probe_gsfEle_e  = cms.string("energy"),
#    probe_gsfEle_p  = cms.string("p"),
#    probe_gsfEle_px  = cms.string("px"),
#    probe_gsfEle_py  = cms.string("py"),
#    probe_gsfEle_pz  = cms.string("pz"),
#    probe_gsfEle_theta  = cms.string("theta"),    
#    probe_gsfEle_charge = cms.string("charge"),
#    probe_gsfEle_vx     = cms.string("vx"),
#    probe_gsfEle_vy     = cms.string("vy"),
#    probe_gsfEle_vz     = cms.string("vz"),
#    probe_gsfEle_rapidity  = cms.string("rapidity"),
#    probe_gsfEle_missingHits = cms.string("gsfTrack.trackerExpectedHitsInner.numberOfHits"),
#    probe_gsfEle_hasValidHitInFirstPixelBarrel = cms.string("gsfTrack.hitPattern.hasValidHitInFirstPixelBarrel"),
    ## super cluster quantities
#    probe_sc_energy = cms.string("superCluster.energy"),
#    probe_sc_et    = cms.string("superCluster.energy*sin(superClusterPosition.theta)"),    
#    probe_sc_x      = cms.string("superCluster.x"),
#    probe_sc_y      = cms.string("superCluster.y"),
#    probe_sc_z      = cms.string("superCluster.z"),
#    probe_sc_eta    = cms.string("superCluster.eta"),
#    probe_sc_theta  = cms.string("superClusterPosition.theta"),   
#    probe_sc_phi    = cms.string("superCluster.phi"),
#    probe_sc_size   = cms.string("superCluster.size"), # number of hits
#    probe_sc_rawEnergy = cms.string("superCluster.rawEnergy"), 
#    probe_sc_preshowerEnergy   = cms.string("superCluster.preshowerEnergy"), 
#    probe_sc_phiWidth   = cms.string("superCluster.phiWidth"), 
#    probe_sc_etaWidth   = cms.string("superCluster.etaWidth"),         
    ## isolation 
#    probe_gsfEle_trackiso_dr04 = cms.string("dr04TkSumPt"),
#    probe_gsfEle_ecaliso_dr04  = cms.string("dr04EcalRecHitSumEt"),
#    probe_gsfEle_hcaliso_dr04  = cms.string("dr04HcalTowerSumEt"),
#    probe_gsfEle_trackiso_dr03 = cms.string("dr03TkSumPt"),
#    probe_gsfEle_ecaliso_dr03  = cms.string("dr03EcalRecHitSumEt"),
#    probe_gsfEle_hcaliso_dr03  = cms.string("dr03HcalTowerSumEt"),
    ## classification, location, etc.    
#    probe_gsfEle_classification = cms.string("classification"),
#    probe_gsfEle_numberOfBrems  = cms.string("numberOfBrems"),     
#    probe_gsfEle_bremFraction   = cms.string("fbrem"),
#    probe_gsfEle_mva            = cms.string("mva"),        
#    probe_gsfEle_deltaEta       = cms.string("deltaEtaSuperClusterTrackAtVtx"),
#    probe_gsfEle_deltaPhi       = cms.string("deltaPhiSuperClusterTrackAtVtx"),
#    probe_gsfEle_deltaPhiOut    = cms.string("deltaPhiSeedClusterTrackAtCalo"),
#    probe_gsfEle_deltaEtaOut    = cms.string("deltaEtaSeedClusterTrackAtCalo"),
#    probe_gsfEle_isEB           = cms.string("isEB"),
#    probe_gsfEle_isEE           = cms.string("isEE"),
#    probe_gsfEle_isGap          = cms.string("isGap"),
#    probe_gsfEle_isEBEEGap      = cms.string("isEBEEGap"),
#    probe_gsfEle_isEBGap        = cms.string("isEBGap"),
#    probe_gsfEle_isEBEtaGap     = cms.string("isEBEtaGap"),
#    probe_gsfEle_isEBPhiGap     = cms.string("isEBPhiGap"),
#    probe_gsfEle_isEEGap        = cms.string("isEEGap"),
#    probe_gsfEle_isEEDeeGap     = cms.string("isEEDeeGap"),
#    probe_gsfEle_isEERingGap    = cms.string("isEERingGap"),
    ## Hcal energy over Ecal Energy
#    probe_gsfEle_HoverE         = cms.string("hcalOverEcal"),
#    probe_gsfEle_EoverP         = cms.string("eSuperClusterOverP"),        
#    probe_gsfEle_EoverPout      = cms.string("eSeedClusterOverPout"),
#    probe_gsfEle_HoverE_Depth1  = cms.string("hcalDepth1OverEcal"),
#    probe_gsfEle_HoverE_Depth2  = cms.string("hcalDepth2OverEcal"),
    ## Cluster shape information
#    probe_gsfEle_sigmaEtaEta  = cms.string("sigmaEtaEta"),
#    probe_gsfEle_sigmaIetaIeta = cms.string("sigmaIetaIeta"),
#    probe_gsfEle_e1x5               = cms.string("e1x5"),
#    probe_gsfEle_e2x5Max            = cms.string("e2x5Max"),
#    probe_gsfEle_e5x5               = cms.string("e5x5"),
    ## is ECAL driven ? is Track driven ?
#    probe_gsfEle_ecalDrivenSeed     = cms.string("ecalDrivenSeed"),
#    probe_gsfEle_trackerDrivenSeed  = cms.string("trackerDrivenSeed"),
    ## fraction of common hits between the GSF and CTF tracks
#    probe_gsfEle_shFracInnerHits    = cms.string("shFracInnerHits"),  
#)


#TagVariablesToStore = cms.PSet(
#    gsfEle_eta = cms.string("eta"),
#    gsfEle_pt  = cms.string("pt"),
#    gsfEle_phi  = cms.string("phi"),
#    gsfEle_et  = cms.string("et"),
#    gsfEle_e  = cms.string("energy"),
#    gsfEle_p  = cms.string("p"),
#    gsfEle_px  = cms.string("px"),
#    gsfEle_py  = cms.string("py"),
#    gsfEle_pz  = cms.string("pz"),
#    gsfEle_theta  = cms.string("theta"),    
#    gsfEle_charge = cms.string("charge"),
#    gsfEle_vx     = cms.string("vx"),
#    gsfEle_vy     = cms.string("vy"),
#    gsfEle_vz     = cms.string("vz"),
#    gsfEle_rapidity  = cms.string("rapidity"),
#    gsfEle_missingHits = cms.string("gsfTrack.trackerExpectedHitsInner.numberOfHits"),
#    gsfEle_hasValidHitInFirstPixelBarrel = cms.string("gsfTrack.hitPattern.hasValidHitInFirstPixelBarrel"),
    ## super cluster quantities
#    sc_energy = cms.string("superCluster.energy"),
#    sc_et     = cms.string("superCluster.energy*sin(superClusterPosition.theta)"),    
#    sc_x      = cms.string("superCluster.x"),
#    sc_y      = cms.string("superCluster.y"),
#    sc_z      = cms.string("superCluster.z"),
#    sc_eta    = cms.string("superCluster.eta"),
#    sc_theta  = cms.string("superClusterPosition.theta"),      
#    sc_phi    = cms.string("superCluster.phi"),
#    sc_size   = cms.string("superCluster.size"), # number of hits
#    sc_rawEnergy = cms.string("superCluster.rawEnergy"), 
#    sc_preshowerEnergy   = cms.string("superCluster.preshowerEnergy"), 
#    sc_phiWidth   = cms.string("superCluster.phiWidth"), 
#    sc_etaWidth   = cms.string("superCluster.etaWidth"),         
    ## isolation 
#    gsfEle_trackiso_dr04 = cms.string("dr04TkSumPt"),
#    gsfEle_ecaliso_dr04  = cms.string("dr04EcalRecHitSumEt"),
#    gsfEle_hcaliso_dr04  = cms.string("dr04HcalTowerSumEt"),
#    gsfEle_trackiso_dr03 = cms.string("dr03TkSumPt"),
#    gsfEle_ecaliso_dr03  = cms.string("dr03EcalRecHitSumEt"),
#    gsfEle_hcaliso_dr03  = cms.string("dr03HcalTowerSumEt"),
    ## classification, location, etc.    
#    gsfEle_classification = cms.string("classification"),
#    gsfEle_numberOfBrems  = cms.string("numberOfBrems"),     
#    gsfEle_bremFraction   = cms.string("fbrem"),
#    gsfEle_mva            = cms.string("mva"),        
#    gsfEle_deltaEta       = cms.string("deltaEtaSuperClusterTrackAtVtx"),
#    gsfEle_deltaPhi       = cms.string("deltaPhiSuperClusterTrackAtVtx"),
#    gsfEle_deltaPhiOut    = cms.string("deltaPhiSeedClusterTrackAtCalo"),
#    gsfEle_deltaEtaOut    = cms.string("deltaEtaSeedClusterTrackAtCalo"),
#    gsfEle_isEB           = cms.string("isEB"),
#    gsfEle_isEE           = cms.string("isEE"),
#    gsfEle_isGap          = cms.string("isGap"),
#    gsfEle_isEBEEGap      = cms.string("isEBEEGap"),
#    gsfEle_isEBGap        = cms.string("isEBGap"),
#    gsfEle_isEBEtaGap     = cms.string("isEBEtaGap"),
#    gsfEle_isEBPhiGap     = cms.string("isEBPhiGap"),
#    gsfEle_isEEGap        = cms.string("isEEGap"),
#    gsfEle_isEEDeeGap     = cms.string("isEEDeeGap"),
#    gsfEle_isEERingGap    = cms.string("isEERingGap"),
    ## Hcal energy over Ecal Energy
#    gsfEle_HoverE         = cms.string("hcalOverEcal"),
#    gsfEle_EoverP         = cms.string("eSuperClusterOverP"),        
#    gsfEle_EoverPout      = cms.string("eSeedClusterOverPout"),
#    gsfEle_HoverE_Depth1  = cms.string("hcalDepth1OverEcal"),
#    gsfEle_HoverE_Depth2  = cms.string("hcalDepth2OverEcal"),
    ## Cluster shape information
#    gsfEle_sigmaEtaEta  = cms.string("sigmaEtaEta"),
#    gsfEle_sigmaIetaIeta = cms.string("sigmaIetaIeta"),
#    gsfEle_e1x5               = cms.string("e1x5"),
#    gsfEle_e2x5Max            = cms.string("e2x5Max"),
#    gsfEle_e5x5               = cms.string("e5x5"),
    ## is ECAL driven ? is Track driven ?
#    gsfEle_ecalDrivenSeed     = cms.string("ecalDrivenSeed"),
#    gsfEle_trackerDrivenSeed  = cms.string("trackerDrivenSeed"),
    ## fraction of common hits between the GSF and CTF tracks
#    gsfEle_shFracInnerHits    = cms.string("shFracInnerHits"),  
#)

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
        ## Pixel seed
        probe_hasPixelSeed = cms.string("hasPixelSeed")
)


#ProbeSuperClusterVariablesToStore = cms.PSet(
#    probe_sc_eta = cms.string("eta"),
#    probe_sc_pt  = cms.string("pt"),
#    probe_sc_phi  = cms.string("phi"),
#    probe_sc_et  = cms.string("et"),
#    probe_sc_e  = cms.string("energy"),
#    probe_sc_p  = cms.string("p"),
#    probe_sc_px  = cms.string("px"),
#    probe_sc_py  = cms.string("py"),
#    probe_sc_pz  = cms.string("pz"),
#    probe_sc_theta  = cms.string("theta"),
#)


#TagSuperClusterVariablesToStore = cms.PSet(
#    sc_eta = cms.string("eta"),
#    sc_pt  = cms.string("pt"),
#    sc_phi  = cms.string("phi"),
#    sc_et  = cms.string("et"),
#    sc_e  = cms.string("energy"),
#    sc_p  = cms.string("p"),
#    sc_px  = cms.string("px"),
#    sc_py  = cms.string("py"),
#        sc_pz  = cms.string("pz"),
#    sc_theta  = cms.string("theta"),
#)





#CommonStuffForSuperClusterProbe = cms.PSet(
#   variables = cms.PSet(ProbeSuperClusterVariablesToStore),
#   ignoreExceptions =  cms.bool (False),
   #fillTagTree      =  cms.bool (True),
#   addRunLumiInfo   =  cms.bool (True),
#   addEventVariablesInfo   =  cms.bool (True),
#   pairVariables =  cms.PSet(ZVariablesToStore),
#   pairFlags     =  cms.PSet(
#          mass60to120 = cms.string("60 < mass < 120")
#    ),
#    tagVariables   =  cms.PSet(TagVariablesToStore),
#    tagFlags     =  cms.PSet(
#          flag = cms.string("pt>0")
#    ),    
#)

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




#CommonStuffForGsfElectronProbe = cms.PSet(
#    variables = cms.PSet(ProbeVariablesToStore),
#    ignoreExceptions =  cms.bool (False),
    #fillTagTree      =  cms.bool (True),
#    addRunLumiInfo   =  cms.bool (True),
#    addEventVariablesInfo   =  cms.bool (True),
#    pairVariables =  cms.PSet(ZVariablesToStore),
#    pairFlags     =  cms.PSet(
#          mass60to120 = cms.string("60 < mass < 120")
#    ),
#    tagVariables   =  cms.PSet(TagVariablesToStore),
#    tagFlags     =  cms.PSet(
#          flag = cms.string("pt>0")
#    ),    
#)


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




##    ____   ____       __     ____      __ 
##   / ___| / ___|      \ \   / ___|___ / _|
##   \___ \| |      _____\ \ | |  _/ __| |_ 
##    ___) | |___  |_____/ / | |_| \__ \  _|
##   |____/ \____|      /_/   \____|___/_|  

## super cluster --> gsf electron
#process.SCToGsf = cms.EDAnalyzer("TagProbeFitTreeProducer",
    ## pick the defaults
#    CommonStuffForSuperClusterProbe, mcTruthCommonStuff,
    # choice of tag and probe pairs, and arbitration                 
#    tagProbePairs = cms.InputTag("tagSC"),
#    arbitration   = cms.string("Random2"),                      
#    flags = cms.PSet(
#        probe_passing = cms.InputTag("GsfMatchedSuperClusterCands"),
#        probe_passingGsf = cms.InputTag("GsfMatchedSuperClusterCands"),        
#        probe_passingIso = cms.InputTag("IsoMatchedSuperClusterCandsClean"),
#        probe_passingId = cms.InputTag("IdMatchedSuperClusterCandsClean"),
#        probe_passingId80 = cms.InputTag("Id80MatchedSuperClusterCandsClean"),
#        probe_passingALL = cms.InputTag("TagMatchedSuperClusterCandsClean")
#    ),
#    probeMatches  = cms.InputTag("McMatchSC"),
#    allProbes     = cms.InputTag("goodSuperClustersClean")
#)
#process.SCToGsf.variables.probe_dRjet = cms.InputTag("superClusterDRToNearestJet")
#process.SCToGsf.variables.probe_nJets = cms.InputTag("JetMultiplicityInSCEvents")





#process.SCSCtoTagSC = cms.EDAnalyzer("TagProbeFitTreeProducer",
    ## pick the defaults
#   variables = cms.PSet(ProbeSuperClusterVariablesToStore),
#   ignoreExceptions =  cms.bool (False),
#   addRunLumiInfo   =  cms.bool (True),
#   addEventVariablesInfo   =  cms.bool (True),
#   pairVariables =  cms.PSet(ZVariablesToStore),
#   pairFlags     =  cms.PSet(
#          mass60to120 = cms.string("60 < mass < 120")
#    ),
#    tagVariables   =  cms.PSet(TagSuperClusterVariablesToStore),
#    tagFlags     =  cms.PSet(
#          flag = cms.string("pt>0")
#    ),                                         
#    isMC = cms.bool(False),
    #mcTruthCommonStuff,
    # choice of tag and probe pairs, and arbitration                      
#    tagProbePairs = cms.InputTag("SCSC"),
#    arbitration   = cms.string("Random2"),
#    massForArbitration = cms.double(91.1876),
#    flags = cms.PSet(
#          probe_passing = cms.InputTag("TagMatchedSuperClusterCandsClean")
#    ),
#    probeMatches  = cms.InputTag("McMatchSCbad"),         
#    allProbes     = cms.InputTag("badSuperClustersClean")
#)


## good photon --> gsf electron
#process.PhotonToGsf = cms.EDAnalyzer("TagProbeFitTreeProducer",
    ## pick the defaults
#    mcTruthCommonStuff,
#    CommonStuffForSuperClusterProbe,
    # choice of tag and probe pairs, and arbitration                 
#    tagProbePairs = cms.InputTag("tagPhoton"),
#    arbitration   = cms.string("Random2"),                      
#    flags = cms.PSet(
#        probe_passing = cms.InputTag("GsfMatchedPhotonCands"),
#        probe_passingALL = cms.InputTag("TagMatchedPhotonCands"),
#        probe_passingIso = cms.InputTag("IsoMatchedPhotonCands"),
#        probe_passingId = cms.InputTag("IdMatchedPhotonCands"),
#        probe_passingId80 = cms.InputTag("Id80MatchedPhotonCands")        
#    ),
#    probeMatches  = cms.InputTag("McMatchPhoton"),
#    allProbes     = cms.InputTag("FilteredPhotonsEB")
#)
#process.PhotonToGsf.variables=ProbePhotonVariablesToStore

#process.SCSCbad = cms.EDAnalyzer("TagProbeFitTreeProducer",
    ## pick the defaults
   #######mcTruthCommonStuff,
#   variables = cms.PSet(ProbeSuperClusterVariablesToStore),
#   ignoreExceptions =  cms.bool (False),
#   addRunLumiInfo   =  cms.bool (True),
#   addEventVariablesInfo   =  cms.bool (True),
#   pairVariables =  cms.PSet(ZVariablesToStore),
#   pairFlags     =  cms.PSet(
#          mass60to120 = cms.string("60 < mass < 120")
#          ),
#   tagVariables   =  cms.PSet(TagSuperClusterVariablesToStore),
#   tagFlags     =  cms.PSet(
#          flag = cms.string("pt>0")
#   ),                                         
#   isMC = cms.bool(False),
   # choice of tag and probe pairs, and arbitration                      
#   tagProbePairs = cms.InputTag("SCSC"),
#   arbitration   = cms.string("Random2"),
#   massForArbitration = cms.double(91.1876),
#   flags = cms.PSet(
#          probe_passing = cms.InputTag("TagMatchedSuperClusterCandsClean")
#   ),
   #probeMatches  = cms.InputTag("McMatchSCbad"),         
#   allProbes     = cms.InputTag("badSuperClustersClean")
#)

#process.GsfGsfToIso = cms.EDAnalyzer("TagProbeFitTreeProducer",
    ########mcTruthCommonStuff,
#    CommonStuffForGsfElectronProbe,
#    isMC = cms.bool(False), 
#    tagProbePairs = cms.InputTag("GsfGsf"),
#    arbitration   = cms.string("Random2"),
#    flags = cms.PSet(
#        probe_passing = cms.InputTag("PassingIsolation")
#    ),
    #probeMatches  = cms.InputTag("McMatchGsf"),
#    allProbes     = cms.InputTag("PassingGsf")
#)


##     ____      __       __    ___           
##    / ___|___ / _|      \ \  |_ _|___  ___  
##   | |  _/ __| |_   _____\ \  | |/ __|/ _ \ 
##   | |_| \__ \  _| |_____/ /  | |\__ \ (_) |
##    \____|___/_|        /_/  |___|___/\___/ 
##   
##  gsf electron --> isolation

#process.GsfToIso = cms.EDAnalyzer("TagProbeFitTreeProducer",
#    mcTruthCommonStuff, CommonStuffForGsfElectronProbe,                        
#    tagProbePairs = cms.InputTag("tagGsf"),
#    arbitration   = cms.string("Random2"),
#    flags = cms.PSet(
#        probe_passing = cms.InputTag("PassingIsolation"),
#        probe_passingIso = cms.InputTag("PassingIsolation"),
#        probe_passingId = cms.InputTag("PassingId"),
#        probe_passingId80 = cms.InputTag("PassingId80"),        
#        probe_passingALL = cms.InputTag("PassingHLT")        
#    ),
#    probeMatches  = cms.InputTag("McMatchGsf"),
#    allProbes     = cms.InputTag("PassingGsf")
#)
#process.GsfToIso.variables.probe_dRjet = cms.InputTag("GsfDRToNearestJet")
#process.GsfToIso.variables.probe_nJets = cms.InputTag("JetMultiplicityInGsfEvents")

## loose photon --> isolation
process.PhotonToIsolation = cms.EDAnalyzer("TagProbeFitTreeProducer",
    ## pick the defaults
    mcTruthCommonStuff,
    CommonStuffForPhotonProbe,
    # choice of tag and probe pairs, and arbitration                 
    tagProbePairs = cms.InputTag("tagPhoton"),
    arbitration   = cms.string("None"),                      
    flags = cms.PSet(
        probe_passing = cms.InputTag("probePhotonsPassingIsolationEB"),
        probe_passingALL = cms.InputTag("probePhotonsPassingHLTEB"),
        probe_passingIso = cms.InputTag("probePhotonsPassingIsolationEB"),
        probe_passingId = cms.InputTag("probePhotonsPassingIdEB"),
    ),
    probeMatches  = cms.InputTag("McMatchPhoton"),
    allProbes     = cms.InputTag("trackMatchedFilteredProbePhotonsEB")
)
process.PhotonToIsolation.variables.probe_dRjet05 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet05"
    )
process.PhotonToIsolation.variables.probe_dRjet09 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet09"
    )
process.PhotonToIsolation.variables.probe_nJets05 = cms.InputTag("JetMultiplicity05")
process.PhotonToIsolation.variables.probe_nJets09 = cms.InputTag("JetMultiplicity09")

##    ___                 __    ___    _ 
##   |_ _|___  ___        \ \  |_ _|__| |
##    | |/ __|/ _ \   _____\ \  | |/ _` |
##    | |\__ \ (_) | |_____/ /  | | (_| |
##   |___|___/\___/       /_/  |___\__,_|
##   
##  isolation --> Id

#process.IsoToId = cms.EDAnalyzer("TagProbeFitTreeProducer",
#    mcTruthCommonStuff, CommonStuffForGsfElectronProbe,                              
#    tagProbePairs = cms.InputTag("tagIso"),
#    arbitration   = cms.string("Random2"),
#    flags = cms.PSet(
#        probe_passing = cms.InputTag("PassingId"),
#        probe_passingId = cms.InputTag("PassingId"),
#        probe_passingId80 = cms.InputTag("PassingId80"),        
#        probe_passingALL = cms.InputTag("PassingHLT")         
#    ),
#    probeMatches  = cms.InputTag("McMatchIso"),
#    allProbes     = cms.InputTag("PassingIsolation")
#)
#process.IsoToId.variables.probe_dRjet = cms.InputTag("GsfDRToNearestJet")
#process.IsoToId.variables.probe_nJets = cms.InputTag("JetMultiplicityInGsfEvents")

#isolated --> ID'ed photon
process.IsoToId = cms.EDAnalyzer("TagProbeFitTreeProducer",
    mcTruthCommonStuff, CommonStuffForPhotonProbe,                              
    tagProbePairs = cms.InputTag("tagIsoEBPhotons"),
    arbitration   = cms.string("None"),
    flags = cms.PSet(
        probe_passing = cms.InputTag("probePhotonsPassingIdEB"),
        probe_passingId = cms.InputTag("probePhotonsPassingIdEB"),
        probe_passingALL = cms.InputTag("probePhotonsPassingHLTEB")         
    ),
    probeMatches  = cms.InputTag("McMatchIso"),
    allProbes     = cms.InputTag("probePhotonsPassingIsolationEB")
)

##    ___    _       __    _   _ _   _____ 
##   |_ _|__| |      \ \  | | | | | |_   _|
##    | |/ _` |  _____\ \ | |_| | |   | |  
##    | | (_| | |_____/ / |  _  | |___| |  
##   |___\__,_|      /_/  |_| |_|_____|_|  

##  Id --> HLT
#process.IdToHLT = cms.EDAnalyzer("TagProbeFitTreeProducer",
#    mcTruthCommonStuff, CommonStuffForGsfElectronProbe,                             
#    tagProbePairs = cms.InputTag("tagId"),
#    arbitration   = cms.string("Random2"),
#    flags = cms.PSet(
#        probe_passing = cms.InputTag("PassingHLT"),
#        probe_passingId80 = cms.InputTag("PassingId80")        
#    ),
#    probeMatches  = cms.InputTag("McMatchId"),
#    allProbes     = cms.InputTag("PassingId")
#)
#process.IdToHLT.variables.probe_dRjet = cms.InputTag("GsfDRToNearestJet")
#process.IdToHLT.variables.probe_nJets = cms.InputTag("JetMultiplicityInGsfEvents")

#ID'ed --> HLT photon
process.IdToHLT = cms.EDAnalyzer("TagProbeFitTreeProducer",
    mcTruthCommonStuff, CommonStuffForPhotonProbe,                             
    tagProbePairs = cms.InputTag("tagIdEBPhotons"),
    arbitration   = cms.string("None"),
    flags = cms.PSet(
        probe_passing = cms.InputTag("probePhotonsPassingHLTEB")
    ),
    probeMatches  = cms.InputTag("McMatchId"),
    allProbes     = cms.InputTag("probePhotonsPassingIdEB")
)

#loose --> HLT photon
process.PhotonToHLT = cms.EDAnalyzer("TagProbeFitTreeProducer",
    mcTruthCommonStuff, CommonStuffForPhotonProbe,                             
    tagProbePairs = cms.InputTag("tagPhoton"),
    arbitration   = cms.string("None"),
    flags = cms.PSet(
        probe_passing = cms.InputTag("probePhotonsPassingHLTEB")
    ),
    probeMatches  = cms.InputTag("McMatchPhoton"),
    allProbes     = cms.InputTag("trackMatchedFilteredProbePhotonsEB")
)
process.PhotonToHLT.variables.probe_dRjet05 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet05"
    )
process.PhotonToHLT.variables.probe_dRjet09 = cms.InputTag(
    "photonDRToNearestIDedUncorrectedJet09"
    )
process.PhotonToHLT.variables.probe_nJets05 = cms.InputTag("JetMultiplicity05")
process.PhotonToHLT.variables.probe_nJets09 = cms.InputTag("JetMultiplicity09")
 
process.tree_sequence = cms.Sequence(
#    process.SCToGsf +
#    process.SCSCbad +
#    process.PhotonToGsf +
#    process.GsfToIso +
#    process.GsfGsfToIso +
    process.PhotonToIsolation +
    process.IsoToId + process.IdToHLT + process.PhotonToHLT
)    



##    ____       _   _     
##   |  _ \ __ _| |_| |__  
##   | |_) / _` | __| '_ \ 
##   |  __/ (_| | |_| | | |
##   |_|   \__,_|\__|_| |_|
##

if MC_flag:
    process.tagAndProbe = cms.Path(
        #    process.checkTriggerMenuSequence *
        #    process.gsfElectrons +
        process.sc_sequence + process.ele_sequence +
        process.ext_ToNearestJet_sequence + 
        process.allTagsAndProbes +
        process.mc_sequence + 
        process.tree_sequence
        )
else:
    process.tagAndProbe = cms.Path(
        #    process.checkTriggerMenuSequence *
        #    process.gsfElectrons +
        process.sc_sequence + process.ele_sequence +
        process.ext_ToNearestJet_sequence + 
        process.allTagsAndProbes +
        process.tree_sequence
        )

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string(outputFile)
                                   )
