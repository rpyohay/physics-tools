import FWCore.ParameterSet.Config as cms

process = cms.Process("TagProbe")

#message logger
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 10000

process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))

#configurables
PU_only_flag = False
if PU_only_flag:
    ECAL_RHO_EFFECTIVE_AREA_ALT = 0.2576
    ECAL_NPV_EFFECTIVE_AREA_ALT = 0.1391
    HCAL_RHO_EFFECTIVE_AREA_ALT = 0.0895
    HCAL_NPV_EFFECTIVE_AREA_ALT = 0.04818
HLTPath1 = "HLT_Ele32_CaloIdL_CaloIsoVL_SC17_v1" #only until end of 5e32 menu
HLTPath2 = "HLT_Ele32_CaloIdL_CaloIsoVL_SC17_v2"
HLTPath3 = "HLT_Ele32_CaloIdL_CaloIsoVL_SC17_v3"
HLTPath4 = "HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_v1" #beginning of 1e33 menu onwards
HLTPath5 = "HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_v2"
HLTPath6 = "HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_v3"
HLTPath7 = "HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_v4"
HLTPath8 = "HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_v5"
HLTPath9 = "HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_v6"
HLTPath10 = "HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_v7"
HLTPath11 = "HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_v8"
HLTSUBFILTER1 = "hltEle32CaloIdLCaloIsoVLSC17PixelMatchFilter"
HLTSUBFILTER2 = "hltEle32CaloIdTCaloIsoTTrkIdTTrkIsoTSC17TrackIsolFilter"
InputTagProcess = "HLT"
RECOProcess = "RECO"
globalTag = "GR_R_42_V19::All"
outputFile = "tagProbeTree.root"

#stuff needed for prescales and JEC
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = globalTag

#input
readFiles = cms.untracked.vstring()
process.source = cms.Source("PoolSource", 
                            fileNames = readFiles
                            )
readFiles.extend([
    'file:/data2/yohay/test_dataset_files/DoubleElectron_PromptRecov4_2.root',
    'file:/data2/yohay/test_dataset_files/DoubleElectron_Aug5ReReco.root',
    'file:/data2/yohay/test_dataset_files/DoubleElectron_PromptRecov6.root',
    'file:/data2/yohay/test_dataset_files/DoubleElectron_Run2011BPromptRecov1.root'
    ])
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )    
process.source.inputCommands = cms.untracked.vstring("keep *","drop *_MEtoEDMConverter_*_*")

#probe
process.load('PhysicsTools.TagAndProbe.Probe_cfi')
process.probePhotons.src = cms.InputTag("photons", "", RECOProcess)
process.probePhotons.cut = cms.string("(superCluster.energy*sin(superCluster.position.theta) > 25.0) && (((abs(superCluster.eta) < 1.4442) && (hadronicOverEm < 0.15)) || ((abs(superCluster.eta) > 1.566) && (abs(superCluster.eta) < 2.5) && (hadronicOverEm < 0.1)))")

#isolation
process.load('PhysicsTools.TagAndProbe.Isolation_cfi')

#PU-subtracted isolation
process.load('PhysicsTools.TagAndProbe.PUSubtractedIsolation_cfi')
if PU_only_flag:
    process.probePhotonsPassingPUCorrectedCombinedIsolation.rhoEffectiveArea = cms.double(
        ECAL_RHO_EFFECTIVE_AREA_ALT, HCAL_RHO_EFFECTIVE_AREA_ALT, 0.0
        )
    process.probePhotonsPassingPUCorrectedCombinedIsolation.nPVEffectiveArea = cms.double(
        ECAL_NPV_EFFECTIVE_AREA_ALT, HCAL_NPV_EFFECTIVE_AREA_ALT, 0.0
        )
process.probePhotonsPassingPUCorrectedCombinedIsolation.PVSrc = cms.InputTag(
    "offlinePrimaryVertices", "", RECOProcess
    )

#ID
process.load('PhysicsTools.TagAndProbe.ID_cfi')

#PU-corrected ID
process.load('PhysicsTools.TagAndProbe.PUCorrectedID_cfi')
process.probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLR9IdEB.PVSrc = cms.InputTag(
    "offlinePrimaryVertices", "", RECOProcess
    )
process.probePhotonsPassingPUCorrectedCombinedIsoIdR9IdEB.PVSrc = cms.InputTag(
    "offlinePrimaryVertices", "", RECOProcess
    )
process.probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLEB.PVSrc = cms.InputTag(
    "offlinePrimaryVertices", "", RECOProcess
    )

#trigger
process.load('PhysicsTools.TagAndProbe.Trigger_cfi')

##################### 36 CaloIdL IsoVL / 22 CaloIdL IsoVL leading #####################

#photons passing IsoVL && R9Id that fire the leading leg of 36 CaloIdL IsoVL / 22 CaloIdL IsoVL
process.selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLLeadingEB.hltTags = cms.VInputTag(
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v1", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v2", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v3", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v4", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v5", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v6", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v7", "", InputTagProcess)
    )
process.selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLLeadingEB.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess)
process.selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLLeadingEB.triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", InputTagProcess)
process.selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLLeadingEB.HLTSubFilters = cms.untracked.VInputTag("hltEG36CaloIdLIsoVLHcalIsoLastFilter", "hltEG36CaloIdLIsoVLHcalIsolLastFilter")

#photons passing IsoVL that fire the leading leg of 36 CaloIdL IsoVL / 22 CaloIdL IsoVL
process.selectedIsoVLPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLLeadingEB.hltTags = cms.VInputTag(
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v1", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v2", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v3", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v4", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v5", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v6", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v7", "", InputTagProcess)
    )
process.selectedIsoVLPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLLeadingEB.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess)
process.selectedIsoVLPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLLeadingEB.triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", InputTagProcess)
process.selectedIsoVLPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLLeadingEB.HLTSubFilters = cms.untracked.VInputTag("hltEG36CaloIdLIsoVLHcalIsoLastFilter", "hltEG36CaloIdLIsoVLHcalIsolLastFilter")

##################### 36 CaloIdL IsoVL / 22 CaloIdL IsoVL trailing #####################

#photons passing IsoVL && R9Id that fire the trailing leg of 36 CaloIdL IsoVL / 22 CaloIdL IsoVL
process.selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLTrailingEB.hltTags = cms.VInputTag(
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v1", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v2", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v3", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v4", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v5", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v6", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v7", "", InputTagProcess)
    )
process.selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLTrailingEB.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess)
process.selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLTrailingEB.triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", InputTagProcess)
process.selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLTrailingEB.HLTSubFilters = cms.untracked.VInputTag("hltDoubleIsoEG22TrackIsolDoubleLastFilterUnseeded", "hltEG22CaloIdLTrackIsolDoubleLastFilterUnseeded")

#photons passing IsoVL that fire the trailing leg of 36 CaloIdL IsoVL / 22 CaloIdL IsoVL
process.selectedIsoVLPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLTrailingEB.hltTags = cms.VInputTag(
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v1", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v2", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v3", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v4", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v5", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v6", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v7", "", InputTagProcess)
    )
process.selectedIsoVLPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLTrailingEB.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess)
process.selectedIsoVLPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLTrailingEB.triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", InputTagProcess)
process.selectedIsoVLPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLTrailingEB.HLTSubFilters = cms.untracked.VInputTag("hltDoubleIsoEG22TrackIsolDoubleLastFilterUnseeded", "hltEG22CaloIdLTrackIsolDoubleLastFilterUnseeded")

##################### 36 CaloIdL IsoVL / 22 R9Id leading #####################

#photons passing IsoVL && R9Id that fire the leading leg of 36 CaloIdL IsoVL / 22 R9Id
process.selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22R9IdLeadingEB.hltTags = cms.VInputTag(
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v1", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloId_IsoVL_Photon22_R9Id_v1", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v2", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v3", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v4", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v5", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v6", "", InputTagProcess)
    )
process.selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22R9IdLeadingEB.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess)
process.selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22R9IdLeadingEB.triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", InputTagProcess)
process.selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22R9IdLeadingEB.HLTSubFilters = cms.untracked.VInputTag("hltEG36CaloIdLIsoVLTrackIsoLastFilter", "hltEG36CaloIdLIsoVLTrackIsolLastFilter")

#photons passing IsoVL that fire the leading leg of 36 CaloIdL IsoVL / 22 R9Id
process.selectedIsoVLPhotonsPassingHLT36CaloIdLIsoVL22R9IdLeadingEB.hltTags = cms.VInputTag(
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v1", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloId_IsoVL_Photon22_R9Id_v1", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v2", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v3", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v4", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v5", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v6", "", InputTagProcess)
    )
process.selectedIsoVLPhotonsPassingHLT36CaloIdLIsoVL22R9IdLeadingEB.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess)
process.selectedIsoVLPhotonsPassingHLT36CaloIdLIsoVL22R9IdLeadingEB.triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", InputTagProcess)
process.selectedIsoVLPhotonsPassingHLT36CaloIdLIsoVL22R9IdLeadingEB.HLTSubFilters = cms.untracked.VInputTag("hltEG36CaloIdLIsoVLTrackIsoLastFilter", "hltEG36CaloIdLIsoVLTrackIsolLastFilter")

##################### 36 CaloIdL IsoVL / 22 R9Id trailing #####################

#photons passing IsoVL && R9Id that fire the trailing leg of 36 CaloIdL IsoVL / 22 R9Id
process.selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22R9IdTrailingEB.hltTags = cms.VInputTag(
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v1", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloId_IsoVL_Photon22_R9Id_v1", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v2", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v3", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v4", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v5", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v6", "", InputTagProcess)
    )
process.selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22R9IdTrailingEB.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess)
process.selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22R9IdTrailingEB.triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", InputTagProcess)
process.selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22R9IdTrailingEB.HLTSubFilters = cms.untracked.VInputTag("hltDoubleIsoEG22TrackIsolLastFilterUnseeded", "hltEG22CaloIdLTrackIsolLastFilterUnseeded")

#photons passing R9Id that fire the trailing leg of 36 CaloIdL IsoVL / 22 R9Id
process.selectedR9IdPhotonsPassingHLT36CaloIdLIsoVL22R9IdTrailingEB.hltTags = cms.VInputTag(
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v1", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloId_IsoVL_Photon22_R9Id_v1", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v2", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v3", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v4", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v5", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v6", "", InputTagProcess)
    )
process.selectedR9IdPhotonsPassingHLT36CaloIdLIsoVL22R9IdTrailingEB.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess)
process.selectedR9IdPhotonsPassingHLT36CaloIdLIsoVL22R9IdTrailingEB.triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", InputTagProcess)
process.selectedR9IdPhotonsPassingHLT36CaloIdLIsoVL22R9IdTrailingEB.HLTSubFilters = cms.untracked.VInputTag("hltDoubleIsoEG22TrackIsolLastFilterUnseeded", "hltEG22CaloIdLTrackIsolLastFilterUnseeded")

##################### 36 R9Id / 22 CaloIdL IsoVL leading #####################

#photons passing IsoVL && R9Id that fire the leading leg of 36 R9Id / 22 CaloIdL IsoVL
process.selectedIsoVLR9IdPhotonsPassingHLT36R9Id22CaloIdLIsoVLLeadingEB.hltTags = cms.VInputTag(
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v1", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v2", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v3", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v4", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v5", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v6", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v7", "", InputTagProcess)
    )
process.selectedIsoVLR9IdPhotonsPassingHLT36R9Id22CaloIdLIsoVLLeadingEB.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess)
process.selectedIsoVLR9IdPhotonsPassingHLT36R9Id22CaloIdLIsoVLLeadingEB.triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", InputTagProcess)

#photons passing R9Id that fire the leading leg of 36 R9Id / 22 CaloIdL IsoVL
process.selectedR9IdPhotonsPassingHLT36R9Id22CaloIdLIsoVLLeadingEB.hltTags = cms.VInputTag(
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v1", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v2", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v3", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v4", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v5", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v6", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v7", "", InputTagProcess)
    )
process.selectedR9IdPhotonsPassingHLT36R9Id22CaloIdLIsoVLLeadingEB.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess)
process.selectedR9IdPhotonsPassingHLT36R9Id22CaloIdLIsoVLLeadingEB.triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", InputTagProcess)

##################### 36 R9Id / 22 CaloIdL IsoVL trailing #####################

#photons passing IsoVL && R9Id that fire the trailing leg of 36 R9Id / 22 CaloIdL IsoVL
process.selectedIsoVLR9IdPhotonsPassingHLT36R9Id22CaloIdLIsoVLTrailingEB.hltTags = cms.VInputTag(
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v1", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v2", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v3", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v4", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v5", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v6", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v7", "", InputTagProcess)
    )
process.selectedIsoVLR9IdPhotonsPassingHLT36R9Id22CaloIdLIsoVLTrailingEB.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess)
process.selectedIsoVLR9IdPhotonsPassingHLT36R9Id22CaloIdLIsoVLTrailingEB.triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", InputTagProcess)
process.selectedIsoVLR9IdPhotonsPassingHLT36R9Id22CaloIdLIsoVLTrailingEB.HLTSubFilters = cms.untracked.VInputTag("hltDoubleIsoEG22TrackIsolLastFilterUnseeded", "hltEG22CaloIdLTrackIsolLastFilterUnseeded")

#photons passing IsoVL that fire the trailing leg of 36 R9Id / 22 CaloIdL IsoVL
process.selectedIsoVLPhotonsPassingHLT36R9Id22CaloIdLIsoVLTrailingEB.hltTags = cms.VInputTag(
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v1", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v2", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v3", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v4", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v5", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v6", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v7", "", InputTagProcess)
    )
process.selectedIsoVLPhotonsPassingHLT36R9Id22CaloIdLIsoVLTrailingEB.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess)
process.selectedIsoVLPhotonsPassingHLT36R9Id22CaloIdLIsoVLTrailingEB.triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", InputTagProcess)
process.selectedIsoVLPhotonsPassingHLT36R9Id22CaloIdLIsoVLTrailingEB.HLTSubFilters = cms.untracked.VInputTag("hltDoubleIsoEG22TrackIsolLastFilterUnseeded", "hltEG22CaloIdLTrackIsolLastFilterUnseeded")

##################### 36 R9Id / 22 R9Id leading #####################

#photons passing IsoVL && R9Id that fire the leading leg of 36 R9Id / 22 R9Id
process.selectedIsoVLR9IdPhotonsPassingHLT36R9Id22R9IdLeadingEB.hltTags = cms.VInputTag(
    cms.InputTag("HLT_Photon36_R9Id_Photon22_R9Id_v1", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_R9Id_v2", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_R9Id_v3", "", InputTagProcess)
    )
process.selectedIsoVLR9IdPhotonsPassingHLT36R9Id22R9IdLeadingEB.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess)
process.selectedIsoVLR9IdPhotonsPassingHLT36R9Id22R9IdLeadingEB.triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", InputTagProcess)

#photons passing R9Id that fire the leading leg of 36 R9Id / 22 R9Id
process.selectedR9IdPhotonsPassingHLT36R9Id22R9IdLeadingEB.hltTags = cms.VInputTag(
    cms.InputTag("HLT_Photon36_R9Id_Photon22_R9Id_v1", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_R9Id_v2", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_R9Id_v3", "", InputTagProcess)
    )
process.selectedR9IdPhotonsPassingHLT36R9Id22R9IdLeadingEB.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess)
process.selectedR9IdPhotonsPassingHLT36R9Id22R9IdLeadingEB.triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", InputTagProcess)

##################### 36 R9Id / 22 R9Id trailing #####################

#photons passing IsoVL && R9Id that fire the trailing leg of 36 R9Id / 22 R9Id
process.selectedIsoVLR9IdPhotonsPassingHLT36R9Id22R9IdTrailingEB.hltTags = cms.VInputTag(
    cms.InputTag("HLT_Photon36_R9Id_Photon22_R9Id_v1", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_R9Id_v2", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_R9Id_v3", "", InputTagProcess)
    )
process.selectedIsoVLR9IdPhotonsPassingHLT36R9Id22R9IdTrailingEB.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess)
process.selectedIsoVLR9IdPhotonsPassingHLT36R9Id22R9IdTrailingEB.triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", InputTagProcess)
process.selectedIsoVLR9IdPhotonsPassingHLT36R9Id22R9IdTrailingEB.HLTSubFilters = cms.untracked.VInputTag("hltDoubleIsoEG22R9IdDoubleLastFilterUnseeded", "hltEG22R9IdDoubleLastFilterUnseeded")

#photons passing R9Id that fire the trailing leg of 36 R9Id / 22 R9Id
process.selectedR9IdPhotonsPassingHLT36R9Id22R9IdTrailingEB.hltTags = cms.VInputTag(
    cms.InputTag("HLT_Photon36_R9Id_Photon22_R9Id_v1", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_R9Id_v2", "", InputTagProcess),
    cms.InputTag("HLT_Photon36_R9Id_Photon22_R9Id_v3", "", InputTagProcess)
    )
process.selectedR9IdPhotonsPassingHLT36R9Id22R9IdTrailingEB.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess)
process.selectedR9IdPhotonsPassingHLT36R9Id22R9IdTrailingEB.triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", InputTagProcess)
process.selectedR9IdPhotonsPassingHLT36R9Id22R9IdTrailingEB.HLTSubFilters = cms.untracked.VInputTag("hltDoubleIsoEG22R9IdDoubleLastFilterUnseeded", "hltEG22R9IdDoubleLastFilterUnseeded")

#jet variables
process.load('PhysicsTools.TagAndProbe.PFJetVariables_cfi')

#tag
process.load('PhysicsTools.TagAndProbe.Tag_cfi')
process.trackMatchedPhotons.srcObjectsToMatch = cms.VInputTag(cms.InputTag("generalTracks", "",
                                                                           RECOProcess))
process.goodPhotons.cut = cms.string("(sigmaIetaIeta < 0.009) && (hasPixelSeed = 1.0) && (hadronicOverEm < 0.05) && (pt > 40.0) && (abs(superCluster.eta) < 1.4442) && (ecalRecHitSumEtConeDR04 < (0.006*pt + 4.2)) && (hcalTowerSumEtConeDR04 < (0.0025*pt + 2.2)) && (trkSumPtHollowConeDR04 < (0.001*pt + 2.0))")
process.Tag.hltTags = cms.VInputTag(
    cms.InputTag(HLTPath1, "", InputTagProcess),
    cms.InputTag(HLTPath2, "", InputTagProcess),
    cms.InputTag(HLTPath3, "", InputTagProcess),
    cms.InputTag(HLTPath4, "", InputTagProcess),
    cms.InputTag(HLTPath5, "", InputTagProcess),
    cms.InputTag(HLTPath6, "", InputTagProcess),
    cms.InputTag(HLTPath7, "", InputTagProcess),
    cms.InputTag(HLTPath8, "", InputTagProcess),
    cms.InputTag(HLTPath9, "", InputTagProcess),
    cms.InputTag(HLTPath10, "", InputTagProcess),
    cms.InputTag(HLTPath11, "", InputTagProcess)
    )
process.Tag.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess)
process.Tag.triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", InputTagProcess)
process.Tag.HLTSubFilters = cms.untracked.VInputTag(
    cms.InputTag(HLTSUBFILTER1, "", InputTagProcess),
    cms.InputTag(HLTSUBFILTER2, "", InputTagProcess)
    )

#tag-probe pairs
process.load('PhysicsTools.TagAndProbe.TagAndProbePairs_cfi')

#efficiencies
process.load('PhysicsTools.TagAndProbe.DataEfficiencies_cfi')

#path
process.tagAndProbe = cms.Path(process.probe_sequence + process.iso_sequence + 
                               process.PU_subtracted_iso_sequence + process.ID_sequence + 
                               process.PU_corrected_ID_sequence +
                               process.trigger_sequence_postMay10ReReco +
                               process.tag_sequence + process.tag_and_probe_sequence +
                               process.jet_variable_sequence_2011 +
                               process.efficiency_sequence_postMay10ReReco)

#output
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string(outputFile)
                                   )
