import FWCore.ParameterSet.Config as cms

process = cms.Process("TagProbe")

#message logger
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 10000

#for MC matching
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(False)## ,
##                                      SkipEvent = cms.untracked.vstring('ProductNotFound')
                                     )

#configurables
MC_flag = False
PU_only_flag = False
if PU_only_flag:
    ECAL_RHO_EFFECTIVE_AREA_ALT = 0.2576
    ECAL_NPV_EFFECTIVE_AREA_ALT = 0.1391
    HCAL_RHO_EFFECTIVE_AREA_ALT = 0.0895
    HCAL_NPV_EFFECTIVE_AREA_ALT = 0.04818
## HLTPath1 = "HLT_Ele32_CaloIdL_CaloIsoVL_SC17_v1"
## HLTPath2 = "HLT_Ele32_CaloIdL_CaloIsoVL_SC17_v2"
## HLTPath3 = "HLT_Ele32_CaloIdL_CaloIsoVL_SC17_v3"
## HLTPath4 = "HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_v1"
## HLTPath5 = "HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_v2"
## HLTPath6 = "HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_v3"
## HLTPath7 = "HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_v4"
HLTPath1 = "HLT_Photon32_CaloIdL_Photon26_CaloIdL_v1"
HLTPath2 = "HLT_Photon32_CaloIdL_Photon26_CaloIdL_v2"
HLTPath3 = "HLT_Photon32_CaloIdL_Photon26_CaloIdL_v3"
HLTPath4 = "HLT_Photon32_CaloIdL_Photon26_CaloIdL_v4"
HLTPath5 = "HLT_Photon36_CaloIdL_Photon22_CaloIdL_v1"
HLTPath6 = "HLT_Photon36_CaloIdL_Photon22_CaloIdL_v2"
HLTPath7 = "HLT_Photon36_CaloIdL_Photon22_CaloIdL_v3"
HLTPath8 = "HLT_Photon36_CaloIdL_Photon22_CaloIdL_v4"
HLTPath9 = "HLT_Photon40_CaloIdL_Photon28_CaloIdL_v1"
HLTPath10 = "HLT_Photon40_CaloIdL_Photon28_CaloIdL_v2"
HLTPath11 = "HLT_Photon40_CaloIdL_Photon28_CaloIdL_v3"
HLTSUBFILTER1 = "hltEG32CaloIdLClusterShapeFilter"
HLTSUBFILTER2 = "hltEG36CaloIdLClusterShapeFilter"
HLTSUBFILTER3 = "hltEG40CaloIdLClusterShapeFilter"
InputTagProcess = "HLT"
RECOProcess = "RECO"
globalTag = "GR_R_42_V14::All"
outputFile = "tagProbeTree_data_photonToID.root"
ARBITRATION = "BestMass"
MZ = 91.2 #GeV

#stuff needed for prescales and JEC
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = globalTag

#input
readFiles = cms.untracked.vstring()
process.source = cms.Source("PoolSource", 
                            fileNames = readFiles
                            )
readFiles.extend([
##     '/store/relval/CMSSW_4_2_3/RelValZEE/GEN-SIM-RECO/START42_V12-v2/0067/7ED5B1F7-DB7B-E011-896C-0026189438BF.root',
##     '/store/relval/CMSSW_4_2_3/RelValZEE/GEN-SIM-RECO/START42_V12-v2/0062/FCEBB129-397B-E011-993B-00261894394D.root',
##     '/store/relval/CMSSW_4_2_3/RelValZEE/GEN-SIM-RECO/START42_V12-v2/0062/3CE75CB9-317B-E011-86BE-002618943864.root'
    'file:/data2/yohay/May10ReRecoDoublePhotonSkim.root'
    ])
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )    
process.source.inputCommands = cms.untracked.vstring("keep *","drop *_MEtoEDMConverter_*_*")

#probe
process.load('PhysicsTools.TagAndProbe.Probe_cfi')
process.probePhotons.src = cms.InputTag("photons", "", RECOProcess)

#isolation
process.load('PhysicsTools.TagAndProbe.Isolation_cfi')

#PU-subtracted isolation
process.load('PhysicsTools.TagAndProbe.PUSubtractedIsolation_cfi')
if PU_only_flag:
    process.probePhotonsPassingPUSubtractedECALIsolation.rhoEffectiveArea = cms.double(
        ECAL_RHO_EFFECTIVE_AREA_ALT
        )
    process.probePhotonsPassingPUSubtractedECALIsolation.nPVEffectiveArea = cms.double(
        ECAL_NPV_EFFECTIVE_AREA_ALT
        )
    process.probePhotonsPassingPUSubtractedHCALIsolation.rhoEffectiveArea = cms.double(
        HCAL_RHO_EFFECTIVE_AREA_ALT
        )
    process.probePhotonsPassingPUSubtractedHCALIsolation.nPVEffectiveArea = cms.double(
        HCAL_NPV_EFFECTIVE_AREA_ALT
        )
    process.probePhotonsPassingPUCorrectedIsolation.rhoEffectiveArea = cms.double(
        ECAL_RHO_EFFECTIVE_AREA_ALT, HCAL_RHO_EFFECTIVE_AREA_ALT
        )
    process.probePhotonsPassingPUCorrectedIsolation.nPVEffectiveArea = cms.double(
        ECAL_NPV_EFFECTIVE_AREA_ALT, HCAL_NPV_EFFECTIVE_AREA_ALT
        )
process.probePhotonsPassingPUSubtractedECALIsolation.rhoSrc = cms.InputTag("kt6PFJets", "rho",
                                                                           "TagProbe")
process.probePhotonsPassingPUSubtractedECALIsolation.PVSrc = cms.InputTag(
    "offlinePrimaryVertices", "", RECOProcess
    )
process.probePhotonsPassingPUSubtractedHCALIsolation.rhoSrc = cms.InputTag("kt6PFJets", "rho",
                                                                           "TagProbe")
process.probePhotonsPassingPUSubtractedHCALIsolation.PVSrc = cms.InputTag(
    "offlinePrimaryVertices", "", RECOProcess
    )
process.probePhotonsPassingPUCorrectedIsolation.rhoSrc = cms.InputTag("kt6PFJets", "rho",
                                                                      "TagProbe")
process.probePhotonsPassingPUCorrectedIsolation.PVSrc = cms.InputTag(
    "offlinePrimaryVertices", "", RECOProcess
    )

#ID
process.load('PhysicsTools.TagAndProbe.ID_cfi')

#PU-corrected ID
process.load('PhysicsTools.TagAndProbe.PUCorrectedID_cfi')
process.probePhotonsPassingPUCorrectedIdEB.rhoSrc = cms.InputTag("kt6PFJets", "rho", "TagProbe")
process.probePhotonsPassingPUCorrectedIdEB.PVSrc = cms.InputTag("offlinePrimaryVertices",
                                                                "", RECOProcess)
process.probePhotonsPassingPUCorrectedIdEE.rhoSrc = cms.InputTag("kt6PFJets", "rho", "TagProbe")
process.probePhotonsPassingPUCorrectedIdEE.PVSrc = cms.InputTag("offlinePrimaryVertices",
                                                                "", RECOProcess)

#trigger
process.load('PhysicsTools.TagAndProbe.Trigger_cfi')
process.probePhotonsPassingHLTEB.hltTags = cms.VInputTag(
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
process.probePhotonsPassingHLTEB.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD",
                                                                          "", InputTagProcess)
process.probePhotonsPassingHLTEB.triggerResultsTag = cms.InputTag("TriggerResults", "",
                                                                  InputTagProcess)
process.probePhotonsPassingHLTEB.HLTSubFilters = cms.untracked.VInputTag(
    cms.InputTag(HLTSUBFILTER1, "", InputTagProcess),
    cms.InputTag(HLTSUBFILTER2, "", InputTagProcess),
    cms.InputTag(HLTSUBFILTER3, "", InputTagProcess)
    )

process.probePhotonsPassingHLTEE.hltTags = cms.VInputTag(
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
process.probePhotonsPassingHLTEE.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD",
                                                                          "", InputTagProcess)
process.probePhotonsPassingHLTEE.triggerResultsTag = cms.InputTag("TriggerResults", "",
                                                                  InputTagProcess)
process.probePhotonsPassingHLTEE.HLTSubFilters = cms.untracked.VInputTag(
    cms.InputTag(HLTSUBFILTER1, "", InputTagProcess),
    cms.InputTag(HLTSUBFILTER2, "", InputTagProcess),
    cms.InputTag(HLTSUBFILTER3, "", InputTagProcess)
    )

#PU-corrected trigger
process.load('PhysicsTools.TagAndProbe.PUCorrectedTrigger_cfi')
process.probePhotonsPassingPURhoCorrectedHLTEB.hltTags = cms.VInputTag(
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
process.probePhotonsPassingPURhoCorrectedHLTEB.triggerEventTag = cms.untracked.InputTag(
    "hltTriggerSummaryAOD", "", InputTagProcess
    )
process.probePhotonsPassingPURhoCorrectedHLTEB.triggerResultsTag = cms.InputTag(
    "TriggerResults", "", InputTagProcess
    )
process.probePhotonsPassingPURhoCorrectedHLTEB.HLTSubFilters = cms.untracked.VInputTag(
    cms.InputTag(HLTSUBFILTER1, "", InputTagProcess),
    cms.InputTag(HLTSUBFILTER2, "", InputTagProcess),
    cms.InputTag(HLTSUBFILTER3, "", InputTagProcess)
    )
process.probePhotonsPassingPURhoCorrectedHLTEE.hltTags = cms.VInputTag(
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
process.probePhotonsPassingPURhoCorrectedHLTEE.triggerEventTag = cms.untracked.InputTag(
    "hltTriggerSummaryAOD", "", InputTagProcess
    )
process.probePhotonsPassingPURhoCorrectedHLTEE.triggerResultsTag = cms.InputTag(
    "TriggerResults", "", InputTagProcess
    )
process.probePhotonsPassingPURhoCorrectedHLTEE.HLTSubFilters = cms.untracked.VInputTag(
    cms.InputTag(HLTSUBFILTER1, "", InputTagProcess),
    cms.InputTag(HLTSUBFILTER2, "", InputTagProcess),
    cms.InputTag(HLTSUBFILTER3, "", InputTagProcess)
    )
process.probePhotonsPassingPUNPVCorrectedHLTEB.hltTags = cms.VInputTag(
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
process.probePhotonsPassingPUNPVCorrectedHLTEB.triggerEventTag = cms.untracked.InputTag(
    "hltTriggerSummaryAOD", "", InputTagProcess
    )
process.probePhotonsPassingPUNPVCorrectedHLTEB.triggerResultsTag = cms.InputTag(
    "TriggerResults", "", InputTagProcess
    )
process.probePhotonsPassingPUNPVCorrectedHLTEB.HLTSubFilters = cms.untracked.VInputTag(
    cms.InputTag(HLTSUBFILTER1, "", InputTagProcess),
    cms.InputTag(HLTSUBFILTER2, "", InputTagProcess),
    cms.InputTag(HLTSUBFILTER3, "", InputTagProcess)
    )
process.probePhotonsPassingPUNPVCorrectedHLTEE.hltTags = cms.VInputTag(
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
process.probePhotonsPassingPUNPVCorrectedHLTEE.triggerEventTag = cms.untracked.InputTag(
    "hltTriggerSummaryAOD", "", InputTagProcess
    )
process.probePhotonsPassingPUNPVCorrectedHLTEE.triggerResultsTag = cms.InputTag(
    "TriggerResults", "", InputTagProcess
    )
process.probePhotonsPassingPUNPVCorrectedHLTEE.HLTSubFilters = cms.untracked.VInputTag(
    cms.InputTag(HLTSUBFILTER1, "", InputTagProcess),
    cms.InputTag(HLTSUBFILTER2, "", InputTagProcess),
    cms.InputTag(HLTSUBFILTER3, "", InputTagProcess)
    )

#jet variables
process.load('PhysicsTools.TagAndProbe.PFJetVariables_cfi')
process.probesAndTagsToRemove.arbitration = cms.string(ARBITRATION)
process.probesAndTagsToRemove.massForArbitration = cms.double(MZ)
process.probesPassingIsoAndTagsToRemove.arbitration = cms.string(ARBITRATION)
process.probesPassingIsoAndTagsToRemove.massForArbitration = cms.double(MZ)
process.probesPassingIdEBAndTagsToRemove.arbitration = cms.string(ARBITRATION)
process.probesPassingIdEBAndTagsToRemove.massForArbitration = cms.double(MZ)
process.probesPassingIdEEAndTagsToRemove.arbitration = cms.string(ARBITRATION)
process.probesPassingIdEEAndTagsToRemove.massForArbitration = cms.double(MZ)

#tag
process.load('PhysicsTools.TagAndProbe.Tag_cfi')
process.trackMatchedPhotons.srcObjectsToMatch = cms.VInputTag(cms.InputTag("generalTracks", "",
                                                                           RECOProcess))
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
    cms.InputTag(HLTSUBFILTER2, "", InputTagProcess),
    cms.InputTag(HLTSUBFILTER3, "", InputTagProcess)
    )

#tag-probe pairs
process.load('PhysicsTools.TagAndProbe.TagAndProbePairs_cfi')

#PU-corrected tag-probe pairs
process.load('PhysicsTools.TagAndProbe.PUCorrectedTagAndProbePairs_cfi')

#MC matching
process.load('PhysicsTools.TagAndProbe.MCMatch_cfi')

#PU-corrected MC matching
process.load('PhysicsTools.TagAndProbe.PUCorrectedMCMatch_cfi')

#PU weight producer
process.load('PhysicsTools.TagAndProbe.PUWeights_cfi')

#efficiencies
if MC_flag:
    process.load('PhysicsTools.TagAndProbe.Efficiencies_cfi')
    process.load('PhysicsTools.TagAndProbe.PUCorrectedEfficiencies_cfi')
else:
    process.load('PhysicsTools.TagAndProbe.DataEfficiencies_cfi')
    process.load('PhysicsTools.TagAndProbe.PUCorrectedDataEfficiencies_cfi')
process.PhotonToIsolation.arbitration = cms.string(ARBITRATION)
process.PhotonToIsolation.massForArbitration = cms.double(MZ)
process.IsoToIdEB.arbitration = cms.string(ARBITRATION)
process.IsoToIdEB.massForArbitration = cms.double(MZ)
process.IsoToIdEE.arbitration = cms.string(ARBITRATION)
process.IsoToIdEE.massForArbitration = cms.double(MZ)
process.IdToHLTEB.arbitration = cms.string(ARBITRATION)
process.IdToHLTEB.massForArbitration = cms.double(MZ)
process.IdToHLTEE.arbitration = cms.string(ARBITRATION)
process.IdToHLTEE.massForArbitration = cms.double(MZ)
process.PhotonToHLTEB.arbitration = cms.string(ARBITRATION)
process.PhotonToHLTEB.massForArbitration = cms.double(MZ)
process.PhotonToHLTEE.arbitration = cms.string(ARBITRATION)
process.PhotonToHLTEE.massForArbitration = cms.double(MZ)
process.PhotonToIDEB.arbitration = cms.string(ARBITRATION)
process.PhotonToIDEB.massForArbitration = cms.double(MZ)
process.PhotonToIDEE.arbitration = cms.string(ARBITRATION)
process.PhotonToIDEE.massForArbitration = cms.double(MZ)
process.PhotonToIDNoHLTEB.arbitration = cms.string(ARBITRATION)
process.PhotonToIDNoHLTEB.massForArbitration = cms.double(MZ)
process.PhotonToIDNoHLTEE.arbitration = cms.string(ARBITRATION)
process.PhotonToIDNoHLTEE.massForArbitration = cms.double(MZ)
process.PhotonToECALIso.arbitration = cms.string(ARBITRATION)
process.PhotonToECALIso.massForArbitration = cms.double(MZ)
process.PhotonToECALIsoNoHLT.arbitration = cms.string(ARBITRATION)
process.PhotonToECALIsoNoHLT.massForArbitration = cms.double(MZ)
process.PhotonToHCALIso.arbitration = cms.string(ARBITRATION)
process.PhotonToHCALIso.massForArbitration = cms.double(MZ)
process.PhotonToHCALIsoNoHLT.arbitration = cms.string(ARBITRATION)
process.PhotonToHCALIsoNoHLT.massForArbitration = cms.double(MZ)
process.PhotonToHOverE.arbitration = cms.string(ARBITRATION)
process.PhotonToHOverE.massForArbitration = cms.double(MZ)
process.PhotonToHOverENoHLT.arbitration = cms.string(ARBITRATION)
process.PhotonToHOverENoHLT.massForArbitration = cms.double(MZ)
process.PhotonToTrackIso.arbitration = cms.string(ARBITRATION)
process.PhotonToTrackIso.massForArbitration = cms.double(MZ)
process.PhotonToTrackIsoNoHLT.arbitration = cms.string(ARBITRATION)
process.PhotonToTrackIsoNoHLT.massForArbitration = cms.double(MZ)
process.PhotonToSigmaIetaIetaEB.arbitration = cms.string(ARBITRATION)
process.PhotonToSigmaIetaIetaEB.massForArbitration = cms.double(MZ)
process.PhotonToSigmaIetaIetaEE.arbitration = cms.string(ARBITRATION)
process.PhotonToSigmaIetaIetaEE.massForArbitration = cms.double(MZ)
process.PhotonToSigmaIetaIetaNoHLTEB.arbitration = cms.string(ARBITRATION)
process.PhotonToSigmaIetaIetaNoHLTEB.massForArbitration = cms.double(MZ)
process.PhotonToSigmaIetaIetaNoHLTEE.arbitration = cms.string(ARBITRATION)
process.PhotonToSigmaIetaIetaNoHLTEE.massForArbitration = cms.double(MZ)
process.PhotonToR9.arbitration = cms.string(ARBITRATION)
process.PhotonToR9.massForArbitration = cms.double(MZ)
process.PhotonToR9NoHLT.arbitration = cms.string(ARBITRATION)
process.PhotonToR9NoHLT.massForArbitration = cms.double(MZ)
process.PhotonToID09EB.arbitration = cms.string(ARBITRATION)
process.PhotonToID09EB.massForArbitration = cms.double(MZ)
process.PhotonToID09EE.arbitration = cms.string(ARBITRATION)
process.PhotonToID09EE.massForArbitration = cms.double(MZ)
process.PhotonToIDNoHLT09EB.arbitration = cms.string(ARBITRATION)
process.PhotonToIDNoHLT09EB.massForArbitration = cms.double(MZ)
process.PhotonToIDNoHLT09EE.arbitration = cms.string(ARBITRATION)
process.PhotonToIDNoHLT09EE.massForArbitration = cms.double(MZ)
process.PhotonToECALIso09.arbitration = cms.string(ARBITRATION)
process.PhotonToECALIso09.massForArbitration = cms.double(MZ)
process.PhotonToECALIsoNoHLT09.arbitration = cms.string(ARBITRATION)
process.PhotonToECALIsoNoHLT09.massForArbitration = cms.double(MZ)
process.PhotonToHCALIso09.arbitration = cms.string(ARBITRATION)
process.PhotonToHCALIso09.massForArbitration = cms.double(MZ)
process.PhotonToHCALIsoNoHLT09.arbitration = cms.string(ARBITRATION)
process.PhotonToHCALIsoNoHLT09.massForArbitration = cms.double(MZ)
process.PhotonToHOverE09.arbitration = cms.string(ARBITRATION)
process.PhotonToHOverE09.massForArbitration = cms.double(MZ)
process.PhotonToHOverENoHLT09.arbitration = cms.string(ARBITRATION)
process.PhotonToHOverENoHLT09.massForArbitration = cms.double(MZ)
process.PhotonToTrackIso09.arbitration = cms.string(ARBITRATION)
process.PhotonToTrackIso09.massForArbitration = cms.double(MZ)
process.PhotonToTrackIsoNoHLT09.arbitration = cms.string(ARBITRATION)
process.PhotonToTrackIsoNoHLT09.massForArbitration = cms.double(MZ)
process.PhotonToSigmaIetaIeta09EB.arbitration = cms.string(ARBITRATION)
process.PhotonToSigmaIetaIeta09EB.massForArbitration = cms.double(MZ)
process.PhotonToSigmaIetaIeta09EE.arbitration = cms.string(ARBITRATION)
process.PhotonToSigmaIetaIeta09EE.massForArbitration = cms.double(MZ)
process.PhotonToSigmaIetaIetaNoHLT09EB.arbitration = cms.string(ARBITRATION)
process.PhotonToSigmaIetaIetaNoHLT09EB.massForArbitration = cms.double(MZ)
process.PhotonToSigmaIetaIetaNoHLT09EE.arbitration = cms.string(ARBITRATION)
process.PhotonToSigmaIetaIetaNoHLT09EE.massForArbitration = cms.double(MZ)
process.PhotonToR909.arbitration = cms.string(ARBITRATION)
process.PhotonToR909.massForArbitration = cms.double(MZ)
process.PhotonToR9NoHLT09.arbitration = cms.string(ARBITRATION)
process.PhotonToR9NoHLT09.massForArbitration = cms.double(MZ)

#PU-corrected efficiencies
process.PhotonToIDPUCorrectedEB.arbitration = cms.string(ARBITRATION)
process.PhotonToIDPUCorrectedEB.massForArbitration = cms.double(MZ)
process.PhotonToIDPUCorrectedEE.arbitration = cms.string(ARBITRATION)
process.PhotonToIDPUCorrectedEE.massForArbitration = cms.double(MZ)
process.PhotonToIDNoHLTPUCorrectedEB.arbitration = cms.string(ARBITRATION)
process.PhotonToIDNoHLTPUCorrectedEB.massForArbitration = cms.double(MZ)
process.PhotonToIDNoHLTPUCorrectedEE.arbitration = cms.string(ARBITRATION)
process.PhotonToIDNoHLTPUCorrectedEE.massForArbitration = cms.double(MZ)
process.PhotonToECALIsoPUCorrected.arbitration = cms.string(ARBITRATION)
process.PhotonToECALIsoPUCorrected.massForArbitration = cms.double(MZ)
process.PhotonToECALIsoNoHLTPUCorrected.arbitration = cms.string(ARBITRATION)
process.PhotonToECALIsoNoHLTPUCorrected.massForArbitration = cms.double(MZ)
process.PhotonToHCALIsoPUCorrected.arbitration = cms.string(ARBITRATION)
process.PhotonToHCALIsoPUCorrected.massForArbitration = cms.double(MZ)
process.PhotonToHCALIsoNoHLTPUCorrected.arbitration = cms.string(ARBITRATION)
process.PhotonToHCALIsoNoHLTPUCorrected.massForArbitration = cms.double(MZ)
process.PhotonToIDPUCorrected09EB.arbitration = cms.string(ARBITRATION)
process.PhotonToIDPUCorrected09EB.massForArbitration = cms.double(MZ)
process.PhotonToIDPUCorrected09EE.arbitration = cms.string(ARBITRATION)
process.PhotonToIDPUCorrected09EE.massForArbitration = cms.double(MZ)
process.PhotonToIDNoHLTPUCorrected09EB.arbitration = cms.string(ARBITRATION)
process.PhotonToIDNoHLTPUCorrected09EB.massForArbitration = cms.double(MZ)
process.PhotonToIDNoHLTPUCorrected09EE.arbitration = cms.string(ARBITRATION)
process.PhotonToIDNoHLTPUCorrected09EE.massForArbitration = cms.double(MZ)
process.PhotonToECALIsoPUCorrected09.arbitration = cms.string(ARBITRATION)
process.PhotonToECALIsoPUCorrected09.massForArbitration = cms.double(MZ)
process.PhotonToECALIsoNoHLTPUCorrected09.arbitration = cms.string(ARBITRATION)
process.PhotonToECALIsoNoHLTPUCorrected09.massForArbitration = cms.double(MZ)
process.PhotonToHCALIsoPUCorrected09.arbitration = cms.string(ARBITRATION)
process.PhotonToHCALIsoPUCorrected09.massForArbitration = cms.double(MZ)
process.PhotonToHCALIsoNoHLTPUCorrected09.arbitration = cms.string(ARBITRATION)
process.PhotonToHCALIsoNoHLTPUCorrected09.massForArbitration = cms.double(MZ)

#path
if MC_flag:
    if PU_only_flag:
        process.tagAndProbe = cms.Path(process.probe_sequence +
                                       process.PU_subtracted_iso_sequence +
                                       process.PU_corrected_ID_sequence + process.tag_sequence + 
                                       process.loose_probe_tag_and_probe_sequence +
                                       process.jet_variable_sequence +
                                       ###special for MC###
                                       ####################
                                       process.no_intermediates_mc_match_sequence +
                                       process.PU_weight_sequence +
                                       ####################
                                       ###special for MC###
                                       process.PU_corrected_tag_HLT_efficiency_sequence)
    else:
        process.tagAndProbe = cms.Path(process.probe_sequence +
                                       process.iso_sequence + process.PU_subtracted_iso_sequence +
                                       process.ID_sequence + process.PU_corrected_ID_sequence +
                                       process.tag_sequence +
                                       process.loose_probe_tag_and_probe_sequence +
                                       process.jet_variable_sequence +
                                       ###special for MC###
                                       ####################
                                       process.no_intermediates_mc_match_sequence +
                                       process.PU_weight_sequence +
                                       ####################
                                       ###special for MC###
                                       process.tag_HLT_efficiency_sequence +
                                       process.PU_corrected_tag_HLT_efficiency_sequence)
else:
    if PU_only_flag:
        process.tagAndProbe = cms.Path(process.probe_sequence +
                                       process.PU_subtracted_iso_sequence +
                                       process.PU_corrected_ID_sequence + process.tag_sequence + 
                                       process.loose_probe_tag_and_probe_sequence +
                                       process.jet_variable_sequence +
                                       process.PU_corrected_tag_HLT_efficiency_sequence)
    else:
        process.tagAndProbe = cms.Path(process.probe_sequence +
                                       process.iso_sequence + process.PU_subtracted_iso_sequence +
                                       process.ID_sequence + process.PU_corrected_ID_sequence +
                                       process.tag_sequence +
                                       process.loose_probe_tag_and_probe_sequence +
                                       process.jet_variable_sequence +
                                       process.tag_HLT_efficiency_sequence +
                                       process.PU_corrected_tag_HLT_efficiency_sequence)

#output
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string(outputFile)
                                   )
