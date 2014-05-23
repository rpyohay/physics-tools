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
HLTPath1 = "HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC8_Mass30_v1" #lasts entire run
HLTPath2 = "HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC8_Mass30_v2"
HLTPath3 = "HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC8_Mass30_v3"
HLTPath4 = "HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC8_Mass30_v4"
HLTPath5 = "HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC8_Mass30_v5"
HLTPath6 = "HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC8_Mass30_v6"
HLTPath7 = "HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC8_Mass30_v7"
HLTPath8 = "HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC8_Mass30_v8"
HLTPath9 = "HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC8_Mass30_v9"
HLTPath10 = "HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC8_Mass30_v10"
HLTSUBFILTER1 = "hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8TrackIsolFilter"
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
    'file:/data2/yohay/test_dataset_files/DoubleElectron_May10ReReco.root'
    ])
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )    
process.source.inputCommands = cms.untracked.vstring("keep *","drop *_MEtoEDMConverter_*_*")

#probe
process.load('PhysicsTools.TagAndProbe.Probe_cfi')
process.probePhotons.src = cms.InputTag("photons", "", RECOProcess)
process.probePhotons.cut = cms.string("(superCluster.energy*sin(superCluster.position.theta) > 15.0) && (((abs(superCluster.eta) < 1.4442) && (hadronicOverEm < 0.15)) || ((abs(superCluster.eta) > 1.566) && (abs(superCluster.eta) < 2.5) && (hadronicOverEm < 0.1)))")

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
process.preIsoVLR9Id.PVSrc = cms.InputTag("offlinePrimaryVertices", "", RECOProcess)
process.probePhotonsPassingPUCorrectedCombinedIsoIdR9IdEB.PVSrc = cms.InputTag(
    "offlinePrimaryVertices", "", RECOProcess
    )
process.probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLEB.PVSrc = cms.InputTag(
    "offlinePrimaryVertices", "", RECOProcess
    )

#trigger
process.load('PhysicsTools.TagAndProbe.Trigger_cfi')

##################### 26 IsoVL / 18 leading #####################

#photons passing IsoVL && R9Id that fire the leading leg of 26 IsoVL / 18
process.selectedIsoVLR9IdPhotonsPassingHLT26IsoVL18LeadingEB.hltTags = cms.VInputTag(
    cms.InputTag("HLT_Photon26_IsoVL_Photon18_v1", "", InputTagProcess),
    cms.InputTag("HLT_Photon26_IsoVL_Photon18_v2", "", InputTagProcess)
    )
process.selectedIsoVLR9IdPhotonsPassingHLT26IsoVL18LeadingEB.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess)
process.selectedIsoVLR9IdPhotonsPassingHLT26IsoVL18LeadingEB.triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", InputTagProcess)

#photons passing IsoVL that fire the leading leg of 26 IsoVL / 18
process.selectedIsoVLPhotonsPassingHLT26IsoVL18LeadingEB.hltTags = cms.VInputTag(
    cms.InputTag("HLT_Photon26_IsoVL_Photon18_v1", "", InputTagProcess),
    cms.InputTag("HLT_Photon26_IsoVL_Photon18_v2", "", InputTagProcess)
    )
process.selectedIsoVLPhotonsPassingHLT26IsoVL18LeadingEB.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess)
process.selectedIsoVLPhotonsPassingHLT26IsoVL18LeadingEB.triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", InputTagProcess)

##################### 26 IsoVL / 18 trailing #####################

#photons passing IsoVL && R9Id that fire the trailing leg of 26 IsoVL / 18
process.selectedIsoVLR9IdPhotonsPassingHLT26IsoVL18TrailingEB.hltTags = cms.VInputTag(
    cms.InputTag("HLT_Photon26_IsoVL_Photon18_v1", "", InputTagProcess),
    cms.InputTag("HLT_Photon26_IsoVL_Photon18_v2", "", InputTagProcess)
    )
process.selectedIsoVLR9IdPhotonsPassingHLT26IsoVL18TrailingEB.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess)
process.selectedIsoVLR9IdPhotonsPassingHLT26IsoVL18TrailingEB.triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", InputTagProcess)

#photons passing IsoVL that fire the trailing leg of 26 IsoVL / 18
process.selectedIsoVLPhotonsPassingHLT26IsoVL18TrailingEB.hltTags = cms.VInputTag(
    cms.InputTag("HLT_Photon26_IsoVL_Photon18_v1", "", InputTagProcess),
    cms.InputTag("HLT_Photon26_IsoVL_Photon18_v2", "", InputTagProcess)
    )
process.selectedIsoVLPhotonsPassingHLT26IsoVL18TrailingEB.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess)
process.selectedIsoVLPhotonsPassingHLT26IsoVL18TrailingEB.triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", InputTagProcess)

#jet variables
process.load('PhysicsTools.TagAndProbe.PFJetVariables_cfi')

#tag
process.load('PhysicsTools.TagAndProbe.Tag_cfi')
process.trackMatchedPhotons.srcObjectsToMatch = cms.VInputTag(cms.InputTag("generalTracks", "",
                                                                           RECOProcess))
process.goodPhotons.cut = cms.string("(sigmaIetaIeta < 0.009) && (hasPixelSeed = 1.0) && (hadronicOverEm < 0.05) && (pt > 25.0) && (abs(superCluster.eta) < 1.4442) && (ecalRecHitSumEtConeDR04 < (0.006*pt + 4.2)) && (hcalTowerSumEtConeDR04 < (0.0025*pt + 2.2)) && (trkSumPtHollowConeDR04 < (0.001*pt + 2.0))")
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
    cms.InputTag(HLTPath10, "", InputTagProcess)
    )
process.Tag.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess)
process.Tag.triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", InputTagProcess)
process.Tag.HLTSubFilters = cms.untracked.VInputTag(
    cms.InputTag(HLTSUBFILTER1, "", InputTagProcess)
    )

#tag-probe pairs
process.load('PhysicsTools.TagAndProbe.TagAndProbePairs_cfi')

#efficiencies
process.load('PhysicsTools.TagAndProbe.DataEfficiencies_cfi')

#path
process.tagAndProbe = cms.Path(process.probe_sequence + process.iso_sequence + 
                               process.PU_subtracted_iso_sequence + process.ID_sequence + 
                               process.PU_corrected_ID_sequence +
                               process.trigger_sequence_May10ReReco1 + process.tag_sequence +
                               process.tag_and_probe_sequence +
                               process.jet_variable_sequence_2011 +
                               process.efficiency_sequence_May10ReReco1)

#output
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string(outputFile)
                                   )
