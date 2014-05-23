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
MC_flag = True
PU_only_flag = PU_ONLY_FLAG
## PU_only_flag = False
if PU_only_flag:
    ECAL_RHO_EFFECTIVE_AREA_ALT = 0.2576
    ECAL_NPV_EFFECTIVE_AREA_ALT = 0.1391
    HCAL_RHO_EFFECTIVE_AREA_ALT = 0.0895
    HCAL_NPV_EFFECTIVE_AREA_ALT = 0.04818
HLTPath1 = "HLT_Photon32_CaloIdL_Photon26_CaloIdL_v2"
HLTSUBFILTER = "hltEG32CaloIdLClusterShapeFilter"
InputTagProcess = "HLT"
RECOProcess = "RECO"
globalTag = "START42_V12::All"
outputFile = "tagProbeTree_MC_photonToID.root"
ARBITRATION = "BestMass"
MZ = 91.2 #GeV
SAMPLE = "MY_SAMPLE"
## SAMPLE = "PhotonJet_120-170"
EVENT_WEIGHT = MY_EVENT_WEIGHT
XSEC = MY_XSEC
NEVTS = MY_NEVTS
## EVENT_WEIGHT = 1.0
## XSEC = 0.0
## NEVTS = 1
DATARECOERA = "MY_DATA_RECO_ERA"
## DATARECOERA = "May10ReReco"

#stuff needed for prescales and JEC
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = globalTag

#input
readFiles = cms.untracked.vstring()
process.source = cms.Source("PoolSource", 
                            fileNames = readFiles,
##                             skipEvents = cms.untracked.uint32(999)
                            )
readFiles.extend([
##     '/store/relval/CMSSW_4_2_3/RelValZEE/GEN-SIM-RECO/START42_V12-v2/0067/7ED5B1F7-DB7B-E011-896C-0026189438BF.root',
##     '/store/relval/CMSSW_4_2_3/RelValZEE/GEN-SIM-RECO/START42_V12-v2/0062/FCEBB129-397B-E011-993B-00261894394D.root',
##     '/store/relval/CMSSW_4_2_3/RelValZEE/GEN-SIM-RECO/START42_V12-v2/0062/3CE75CB9-317B-E011-86BE-002618943864.root'
    'file:/data2/yohay/ZeeSummer11MC.root'
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
    cms.InputTag(HLTPath1, "", InputTagProcess)
    )
process.probePhotonsPassingHLTEB.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD",
                                                                          "", InputTagProcess)
process.probePhotonsPassingHLTEB.triggerResultsTag = cms.InputTag("TriggerResults", "",
                                                                  InputTagProcess)
process.probePhotonsPassingHLTEB.HLTSubFilters = cms.untracked.VInputTag(
    cms.InputTag(HLTSUBFILTER, "", InputTagProcess)
    )
process.probePhotonsPassingHLTEE.hltTags = cms.VInputTag(
    cms.InputTag(HLTPath1, "", InputTagProcess)
    )
process.probePhotonsPassingHLTEE.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD",
                                                                          "", InputTagProcess)
process.probePhotonsPassingHLTEE.triggerResultsTag = cms.InputTag("TriggerResults", "",
                                                                  InputTagProcess)
process.probePhotonsPassingHLTEE.HLTSubFilters = cms.untracked.VInputTag(
    cms.InputTag(HLTSUBFILTER, "", InputTagProcess)
    )

#PU-corrected trigger
process.load('PhysicsTools.TagAndProbe.PUCorrectedTrigger_cfi')
process.probePhotonsPassingPURhoCorrectedHLTEB.hltTags = cms.VInputTag(
    cms.InputTag(HLTPath1, "", InputTagProcess)
    )
process.probePhotonsPassingPURhoCorrectedHLTEB.triggerEventTag = cms.untracked.InputTag(
    "hltTriggerSummaryAOD", "", InputTagProcess
    )
process.probePhotonsPassingPURhoCorrectedHLTEB.triggerResultsTag = cms.InputTag(
    "TriggerResults", "", InputTagProcess
    )
process.probePhotonsPassingPURhoCorrectedHLTEB.HLTSubFilters = cms.untracked.VInputTag(
    cms.InputTag(HLTSUBFILTER, "", InputTagProcess)
    )
process.probePhotonsPassingPURhoCorrectedHLTEE.hltTags = cms.VInputTag(
    cms.InputTag(HLTPath1, "", InputTagProcess)
    )
process.probePhotonsPassingPURhoCorrectedHLTEE.triggerEventTag = cms.untracked.InputTag(
    "hltTriggerSummaryAOD", "", InputTagProcess
    )
process.probePhotonsPassingPURhoCorrectedHLTEE.triggerResultsTag = cms.InputTag(
    "TriggerResults", "", InputTagProcess
    )
process.probePhotonsPassingPURhoCorrectedHLTEE.HLTSubFilters = cms.untracked.VInputTag(
    cms.InputTag(HLTSUBFILTER, "", InputTagProcess)
    )
process.probePhotonsPassingPUNPVCorrectedHLTEB.hltTags = cms.VInputTag(
    cms.InputTag(HLTPath1, "", InputTagProcess)
    )
process.probePhotonsPassingPUNPVCorrectedHLTEB.triggerEventTag = cms.untracked.InputTag(
    "hltTriggerSummaryAOD", "", InputTagProcess
    )
process.probePhotonsPassingPUNPVCorrectedHLTEB.triggerResultsTag = cms.InputTag(
    "TriggerResults", "", InputTagProcess
    )
process.probePhotonsPassingPUNPVCorrectedHLTEB.HLTSubFilters = cms.untracked.VInputTag(
    cms.InputTag(HLTSUBFILTER, "", InputTagProcess)
    )
process.probePhotonsPassingPUNPVCorrectedHLTEE.hltTags = cms.VInputTag(
    cms.InputTag(HLTPath1, "", InputTagProcess)
    )
process.probePhotonsPassingPUNPVCorrectedHLTEE.triggerEventTag = cms.untracked.InputTag(
    "hltTriggerSummaryAOD", "", InputTagProcess
    )
process.probePhotonsPassingPUNPVCorrectedHLTEE.triggerResultsTag = cms.InputTag(
    "TriggerResults", "", InputTagProcess
    )
process.probePhotonsPassingPUNPVCorrectedHLTEE.HLTSubFilters = cms.untracked.VInputTag(
    cms.InputTag(HLTSUBFILTER, "", InputTagProcess)
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
process.Tag.hltTags = cms.VInputTag(cms.InputTag(HLTPath1, "", InputTagProcess))
process.Tag.triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", InputTagProcess)
process.Tag.triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", InputTagProcess)
process.Tag.HLTSubFilters = cms.untracked.VInputTag(
    cms.InputTag(HLTSUBFILTER, "", InputTagProcess)
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
if SAMPLE == "PhotonJet_80-120" or SAMPLE == "PhotonJet_170-300" or SAMPLE == "PhotonJet_800-1400":
    process.PUWeightProducer.PU = cms.string("S4")
else:
    process.PUWeightProducer.PU = cms.string("S3")
process.PUWeightProducer.dataRecoEra = cms.string(DATARECOERA)

#efficiencies
if MC_flag:
    process.load('PhysicsTools.TagAndProbe.Efficiencies_cfi')
    process.load('PhysicsTools.TagAndProbe.PUCorrectedEfficiencies_cfi')
else:
    process.load('PhysicsTools.TagAndProbe.DataEfficiencies_cfi')
    process.load('PhysicsTools.TagAndProbe.PUCorrectedDataEfficiencies_cfi')
process.PhotonToIsolation.arbitration = cms.string(ARBITRATION)
process.PhotonToIsolation.massForArbitration = cms.double(MZ)
process.PhotonToIsolation.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToIsolation.xSec = cms.double(XSEC)
process.PhotonToIsolation.nEvts = cms.uint32(NEVTS)
process.IsoToIdEB.arbitration = cms.string(ARBITRATION)
process.IsoToIdEB.massForArbitration = cms.double(MZ)
process.IsoToIdEB.eventWeight = cms.double(EVENT_WEIGHT)
process.IsoToIdEB.xSec = cms.double(XSEC)
process.IsoToIdEB.nEvts = cms.uint32(NEVTS)
process.IsoToIdEE.arbitration = cms.string(ARBITRATION)
process.IsoToIdEE.massForArbitration = cms.double(MZ)
process.IsoToIdEE.eventWeight = cms.double(EVENT_WEIGHT)
process.IsoToIdEE.xSec = cms.double(XSEC)
process.IsoToIdEE.nEvts = cms.uint32(NEVTS)
process.IdToHLTEB.arbitration = cms.string(ARBITRATION)
process.IdToHLTEB.massForArbitration = cms.double(MZ)
process.IdToHLTEB.eventWeight = cms.double(EVENT_WEIGHT)
process.IdToHLTEB.xSec = cms.double(XSEC)
process.IdToHLTEB.nEvts = cms.uint32(NEVTS)
process.IdToHLTEE.arbitration = cms.string(ARBITRATION)
process.IdToHLTEE.massForArbitration = cms.double(MZ)
process.IdToHLTEE.eventWeight = cms.double(EVENT_WEIGHT)
process.IdToHLTEE.xSec = cms.double(XSEC)
process.IdToHLTEE.nEvts = cms.uint32(NEVTS)
process.PhotonToHLTEB.arbitration = cms.string(ARBITRATION)
process.PhotonToHLTEB.massForArbitration = cms.double(MZ)
process.PhotonToHLTEB.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToHLTEB.xSec = cms.double(XSEC)
process.PhotonToHLTEB.nEvts = cms.uint32(NEVTS)
process.PhotonToHLTEE.arbitration = cms.string(ARBITRATION)
process.PhotonToHLTEE.massForArbitration = cms.double(MZ)
process.PhotonToHLTEE.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToHLTEE.xSec = cms.double(XSEC)
process.PhotonToHLTEE.nEvts = cms.uint32(NEVTS)
process.PhotonToIDEB.arbitration = cms.string(ARBITRATION)
process.PhotonToIDEB.massForArbitration = cms.double(MZ)
process.PhotonToIDEB.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToIDEB.xSec = cms.double(XSEC)
process.PhotonToIDEB.nEvts = cms.uint32(NEVTS)
process.PhotonToIDEE.arbitration = cms.string(ARBITRATION)
process.PhotonToIDEE.massForArbitration = cms.double(MZ)
process.PhotonToIDEE.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToIDEE.xSec = cms.double(XSEC)
process.PhotonToIDEE.nEvts = cms.uint32(NEVTS)
process.PhotonToIDNoHLTEB.arbitration = cms.string(ARBITRATION)
process.PhotonToIDNoHLTEB.massForArbitration = cms.double(MZ)
process.PhotonToIDNoHLTEB.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToIDNoHLTEB.xSec = cms.double(XSEC)
process.PhotonToIDNoHLTEB.nEvts = cms.uint32(NEVTS)
process.PhotonToIDNoHLTEE.arbitration = cms.string(ARBITRATION)
process.PhotonToIDNoHLTEE.massForArbitration = cms.double(MZ)
process.PhotonToIDNoHLTEE.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToIDNoHLTEE.xSec = cms.double(XSEC)
process.PhotonToIDNoHLTEE.nEvts = cms.uint32(NEVTS)
process.PhotonToECALIso.arbitration = cms.string(ARBITRATION)
process.PhotonToECALIso.massForArbitration = cms.double(MZ)
process.PhotonToECALIso.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToECALIso.xSec = cms.double(XSEC)
process.PhotonToECALIso.nEvts = cms.uint32(NEVTS)
process.PhotonToECALIsoNoHLT.arbitration = cms.string(ARBITRATION)
process.PhotonToECALIsoNoHLT.massForArbitration = cms.double(MZ)
process.PhotonToECALIsoNoHLT.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToECALIsoNoHLT.xSec = cms.double(XSEC)
process.PhotonToECALIsoNoHLT.nEvts = cms.uint32(NEVTS)
process.PhotonToHCALIso.arbitration = cms.string(ARBITRATION)
process.PhotonToHCALIso.massForArbitration = cms.double(MZ)
process.PhotonToHCALIso.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToHCALIso.xSec = cms.double(XSEC)
process.PhotonToHCALIso.nEvts = cms.uint32(NEVTS)
process.PhotonToHCALIsoNoHLT.arbitration = cms.string(ARBITRATION)
process.PhotonToHCALIsoNoHLT.massForArbitration = cms.double(MZ)
process.PhotonToHCALIsoNoHLT.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToHCALIsoNoHLT.xSec = cms.double(XSEC)
process.PhotonToHCALIsoNoHLT.nEvts = cms.uint32(NEVTS)
process.PhotonToHOverE.arbitration = cms.string(ARBITRATION)
process.PhotonToHOverE.massForArbitration = cms.double(MZ)
process.PhotonToHOverE.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToHOverE.xSec = cms.double(XSEC)
process.PhotonToHOverE.nEvts = cms.uint32(NEVTS)
process.PhotonToHOverENoHLT.arbitration = cms.string(ARBITRATION)
process.PhotonToHOverENoHLT.massForArbitration = cms.double(MZ)
process.PhotonToHOverENoHLT.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToHOverENoHLT.xSec = cms.double(XSEC)
process.PhotonToHOverENoHLT.nEvts = cms.uint32(NEVTS)
process.PhotonToTrackIso.arbitration = cms.string(ARBITRATION)
process.PhotonToTrackIso.massForArbitration = cms.double(MZ)
process.PhotonToTrackIso.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToTrackIso.xSec = cms.double(XSEC)
process.PhotonToTrackIso.nEvts = cms.uint32(NEVTS)
process.PhotonToTrackIsoNoHLT.arbitration = cms.string(ARBITRATION)
process.PhotonToTrackIsoNoHLT.massForArbitration = cms.double(MZ)
process.PhotonToTrackIsoNoHLT.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToTrackIsoNoHLT.xSec = cms.double(XSEC)
process.PhotonToTrackIsoNoHLT.nEvts = cms.uint32(NEVTS)
process.PhotonToSigmaIetaIetaEB.arbitration = cms.string(ARBITRATION)
process.PhotonToSigmaIetaIetaEB.massForArbitration = cms.double(MZ)
process.PhotonToSigmaIetaIetaEB.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToSigmaIetaIetaEB.xSec = cms.double(XSEC)
process.PhotonToSigmaIetaIetaEB.nEvts = cms.uint32(NEVTS)
process.PhotonToSigmaIetaIetaEE.arbitration = cms.string(ARBITRATION)
process.PhotonToSigmaIetaIetaEE.massForArbitration = cms.double(MZ)
process.PhotonToSigmaIetaIetaEE.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToSigmaIetaIetaEE.xSec = cms.double(XSEC)
process.PhotonToSigmaIetaIetaEE.nEvts = cms.uint32(NEVTS)
process.PhotonToSigmaIetaIetaNoHLTEB.arbitration = cms.string(ARBITRATION)
process.PhotonToSigmaIetaIetaNoHLTEB.massForArbitration = cms.double(MZ)
process.PhotonToSigmaIetaIetaNoHLTEB.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToSigmaIetaIetaNoHLTEB.xSec = cms.double(XSEC)
process.PhotonToSigmaIetaIetaNoHLTEB.nEvts = cms.uint32(NEVTS)
process.PhotonToSigmaIetaIetaNoHLTEE.arbitration = cms.string(ARBITRATION)
process.PhotonToSigmaIetaIetaNoHLTEE.massForArbitration = cms.double(MZ)
process.PhotonToSigmaIetaIetaNoHLTEE.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToSigmaIetaIetaNoHLTEE.xSec = cms.double(XSEC)
process.PhotonToSigmaIetaIetaNoHLTEE.nEvts = cms.uint32(NEVTS)
process.PhotonToR9.arbitration = cms.string(ARBITRATION)
process.PhotonToR9.massForArbitration = cms.double(MZ)
process.PhotonToR9NoHLT.arbitration = cms.string(ARBITRATION)
process.PhotonToR9NoHLT.massForArbitration = cms.double(MZ)
process.PhotonToID09EB.arbitration = cms.string(ARBITRATION)
process.PhotonToID09EB.massForArbitration = cms.double(MZ)
process.PhotonToID09EB.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToID09EB.xSec = cms.double(XSEC)
process.PhotonToID09EB.nEvts = cms.uint32(NEVTS)
process.PhotonToID09EE.arbitration = cms.string(ARBITRATION)
process.PhotonToID09EE.massForArbitration = cms.double(MZ)
process.PhotonToID09EE.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToID09EE.xSec = cms.double(XSEC)
process.PhotonToID09EE.nEvts = cms.uint32(NEVTS)
process.PhotonToIDNoHLT09EB.arbitration = cms.string(ARBITRATION)
process.PhotonToIDNoHLT09EB.massForArbitration = cms.double(MZ)
process.PhotonToIDNoHLT09EB.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToIDNoHLT09EB.xSec = cms.double(XSEC)
process.PhotonToIDNoHLT09EB.nEvts = cms.uint32(NEVTS)
process.PhotonToIDNoHLT09EE.arbitration = cms.string(ARBITRATION)
process.PhotonToIDNoHLT09EE.massForArbitration = cms.double(MZ)
process.PhotonToIDNoHLT09EE.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToIDNoHLT09EE.xSec = cms.double(XSEC)
process.PhotonToIDNoHLT09EE.nEvts = cms.uint32(NEVTS)
process.PhotonToECALIso09.arbitration = cms.string(ARBITRATION)
process.PhotonToECALIso09.massForArbitration = cms.double(MZ)
process.PhotonToECALIso09.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToECALIso09.xSec = cms.double(XSEC)
process.PhotonToECALIso09.nEvts = cms.uint32(NEVTS)
process.PhotonToECALIsoNoHLT09.arbitration = cms.string(ARBITRATION)
process.PhotonToECALIsoNoHLT09.massForArbitration = cms.double(MZ)
process.PhotonToECALIsoNoHLT09.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToECALIsoNoHLT09.xSec = cms.double(XSEC)
process.PhotonToECALIsoNoHLT09.nEvts = cms.uint32(NEVTS)
process.PhotonToHCALIso09.arbitration = cms.string(ARBITRATION)
process.PhotonToHCALIso09.massForArbitration = cms.double(MZ)
process.PhotonToHCALIso09.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToHCALIso09.xSec = cms.double(XSEC)
process.PhotonToHCALIso09.nEvts = cms.uint32(NEVTS)
process.PhotonToHCALIsoNoHLT09.arbitration = cms.string(ARBITRATION)
process.PhotonToHCALIsoNoHLT09.massForArbitration = cms.double(MZ)
process.PhotonToHCALIsoNoHLT09.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToHCALIsoNoHLT09.xSec = cms.double(XSEC)
process.PhotonToHCALIsoNoHLT09.nEvts = cms.uint32(NEVTS)
process.PhotonToHOverE09.arbitration = cms.string(ARBITRATION)
process.PhotonToHOverE09.massForArbitration = cms.double(MZ)
process.PhotonToHOverE09.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToHOverE09.xSec = cms.double(XSEC)
process.PhotonToHOverE09.nEvts = cms.uint32(NEVTS)
process.PhotonToHOverENoHLT09.arbitration = cms.string(ARBITRATION)
process.PhotonToHOverENoHLT09.massForArbitration = cms.double(MZ)
process.PhotonToHOverENoHLT09.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToHOverENoHLT09.xSec = cms.double(XSEC)
process.PhotonToHOverENoHLT09.nEvts = cms.uint32(NEVTS)
process.PhotonToTrackIso09.arbitration = cms.string(ARBITRATION)
process.PhotonToTrackIso09.massForArbitration = cms.double(MZ)
process.PhotonToTrackIso09.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToTrackIso09.xSec = cms.double(XSEC)
process.PhotonToTrackIso09.nEvts = cms.uint32(NEVTS)
process.PhotonToTrackIsoNoHLT09.arbitration = cms.string(ARBITRATION)
process.PhotonToTrackIsoNoHLT09.massForArbitration = cms.double(MZ)
process.PhotonToTrackIsoNoHLT09.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToTrackIsoNoHLT09.xSec = cms.double(XSEC)
process.PhotonToTrackIsoNoHLT09.nEvts = cms.uint32(NEVTS)
process.PhotonToSigmaIetaIeta09EB.arbitration = cms.string(ARBITRATION)
process.PhotonToSigmaIetaIeta09EB.massForArbitration = cms.double(MZ)
process.PhotonToSigmaIetaIeta09EB.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToSigmaIetaIeta09EB.xSec = cms.double(XSEC)
process.PhotonToSigmaIetaIeta09EB.nEvts = cms.uint32(NEVTS)
process.PhotonToSigmaIetaIeta09EE.arbitration = cms.string(ARBITRATION)
process.PhotonToSigmaIetaIeta09EE.massForArbitration = cms.double(MZ)
process.PhotonToSigmaIetaIeta09EE.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToSigmaIetaIeta09EE.xSec = cms.double(XSEC)
process.PhotonToSigmaIetaIeta09EE.nEvts = cms.uint32(NEVTS)
process.PhotonToSigmaIetaIetaNoHLT09EB.arbitration = cms.string(ARBITRATION)
process.PhotonToSigmaIetaIetaNoHLT09EB.massForArbitration = cms.double(MZ)
process.PhotonToSigmaIetaIetaNoHLT09EB.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToSigmaIetaIetaNoHLT09EB.xSec = cms.double(XSEC)
process.PhotonToSigmaIetaIetaNoHLT09EB.nEvts = cms.uint32(NEVTS)
process.PhotonToSigmaIetaIetaNoHLT09EE.arbitration = cms.string(ARBITRATION)
process.PhotonToSigmaIetaIetaNoHLT09EE.massForArbitration = cms.double(MZ)
process.PhotonToSigmaIetaIetaNoHLT09EE.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToSigmaIetaIetaNoHLT09EE.xSec = cms.double(XSEC)
process.PhotonToSigmaIetaIetaNoHLT09EE.nEvts = cms.uint32(NEVTS)
process.PhotonToR909.arbitration = cms.string(ARBITRATION)
process.PhotonToR909.massForArbitration = cms.double(MZ)
process.PhotonToR9NoHLT09.arbitration = cms.string(ARBITRATION)
process.PhotonToR9NoHLT09.massForArbitration = cms.double(MZ)

#PU-corrected efficiencies
process.PhotonToIDPUCorrectedEB.arbitration = cms.string(ARBITRATION)
process.PhotonToIDPUCorrectedEB.massForArbitration = cms.double(MZ)
process.PhotonToIDPUCorrectedEB.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToIDPUCorrectedEB.xSec = cms.double(XSEC)
process.PhotonToIDPUCorrectedEB.nEvts = cms.uint32(NEVTS)
process.PhotonToIDPUCorrectedEE.arbitration = cms.string(ARBITRATION)
process.PhotonToIDPUCorrectedEE.massForArbitration = cms.double(MZ)
process.PhotonToIDPUCorrectedEE.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToIDPUCorrectedEE.xSec = cms.double(XSEC)
process.PhotonToIDPUCorrectedEE.nEvts = cms.uint32(NEVTS)
process.PhotonToIDNoHLTPUCorrectedEB.arbitration = cms.string(ARBITRATION)
process.PhotonToIDNoHLTPUCorrectedEB.massForArbitration = cms.double(MZ)
process.PhotonToIDNoHLTPUCorrectedEB.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToIDNoHLTPUCorrectedEB.xSec = cms.double(XSEC)
process.PhotonToIDNoHLTPUCorrectedEB.nEvts = cms.uint32(NEVTS)
process.PhotonToIDNoHLTPUCorrectedEE.arbitration = cms.string(ARBITRATION)
process.PhotonToIDNoHLTPUCorrectedEE.massForArbitration = cms.double(MZ)
process.PhotonToIDNoHLTPUCorrectedEE.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToIDNoHLTPUCorrectedEE.xSec = cms.double(XSEC)
process.PhotonToIDNoHLTPUCorrectedEE.nEvts = cms.uint32(NEVTS)
process.PhotonToECALIsoPUCorrected.arbitration = cms.string(ARBITRATION)
process.PhotonToECALIsoPUCorrected.massForArbitration = cms.double(MZ)
process.PhotonToECALIsoPUCorrected.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToECALIsoPUCorrected.xSec = cms.double(XSEC)
process.PhotonToECALIsoPUCorrected.nEvts = cms.uint32(NEVTS)
process.PhotonToECALIsoNoHLTPUCorrected.arbitration = cms.string(ARBITRATION)
process.PhotonToECALIsoNoHLTPUCorrected.massForArbitration = cms.double(MZ)
process.PhotonToECALIsoNoHLTPUCorrected.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToECALIsoNoHLTPUCorrected.xSec = cms.double(XSEC)
process.PhotonToECALIsoNoHLTPUCorrected.nEvts = cms.uint32(NEVTS)
process.PhotonToHCALIsoPUCorrected.arbitration = cms.string(ARBITRATION)
process.PhotonToHCALIsoPUCorrected.massForArbitration = cms.double(MZ)
process.PhotonToHCALIsoPUCorrected.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToHCALIsoPUCorrected.xSec = cms.double(XSEC)
process.PhotonToHCALIsoPUCorrected.nEvts = cms.uint32(NEVTS)
process.PhotonToHCALIsoNoHLTPUCorrected.arbitration = cms.string(ARBITRATION)
process.PhotonToHCALIsoNoHLTPUCorrected.massForArbitration = cms.double(MZ)
process.PhotonToHCALIsoNoHLTPUCorrected.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToHCALIsoNoHLTPUCorrected.xSec = cms.double(XSEC)
process.PhotonToHCALIsoNoHLTPUCorrected.nEvts = cms.uint32(NEVTS)
process.PhotonToIDPUCorrected09EB.arbitration = cms.string(ARBITRATION)
process.PhotonToIDPUCorrected09EB.massForArbitration = cms.double(MZ)
process.PhotonToIDPUCorrected09EB.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToIDPUCorrected09EB.xSec = cms.double(XSEC)
process.PhotonToIDPUCorrected09EB.nEvts = cms.uint32(NEVTS)
process.PhotonToIDPUCorrected09EE.arbitration = cms.string(ARBITRATION)
process.PhotonToIDPUCorrected09EE.massForArbitration = cms.double(MZ)
process.PhotonToIDPUCorrected09EE.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToIDPUCorrected09EE.xSec = cms.double(XSEC)
process.PhotonToIDPUCorrected09EE.nEvts = cms.uint32(NEVTS)
process.PhotonToIDNoHLTPUCorrected09EB.arbitration = cms.string(ARBITRATION)
process.PhotonToIDNoHLTPUCorrected09EB.massForArbitration = cms.double(MZ)
process.PhotonToIDNoHLTPUCorrected09EB.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToIDNoHLTPUCorrected09EB.xSec = cms.double(XSEC)
process.PhotonToIDNoHLTPUCorrected09EB.nEvts = cms.uint32(NEVTS)
process.PhotonToIDNoHLTPUCorrected09EE.arbitration = cms.string(ARBITRATION)
process.PhotonToIDNoHLTPUCorrected09EE.massForArbitration = cms.double(MZ)
process.PhotonToIDNoHLTPUCorrected09EE.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToIDNoHLTPUCorrected09EE.xSec = cms.double(XSEC)
process.PhotonToIDNoHLTPUCorrected09EE.nEvts = cms.uint32(NEVTS)
process.PhotonToECALIsoPUCorrected09.arbitration = cms.string(ARBITRATION)
process.PhotonToECALIsoPUCorrected09.massForArbitration = cms.double(MZ)
process.PhotonToECALIsoPUCorrected09.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToECALIsoPUCorrected09.xSec = cms.double(XSEC)
process.PhotonToECALIsoPUCorrected09.nEvts = cms.uint32(NEVTS)
process.PhotonToECALIsoNoHLTPUCorrected09.arbitration = cms.string(ARBITRATION)
process.PhotonToECALIsoNoHLTPUCorrected09.massForArbitration = cms.double(MZ)
process.PhotonToECALIsoNoHLTPUCorrected09.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToECALIsoNoHLTPUCorrected09.xSec = cms.double(XSEC)
process.PhotonToECALIsoNoHLTPUCorrected09.nEvts = cms.uint32(NEVTS)
process.PhotonToHCALIsoPUCorrected09.arbitration = cms.string(ARBITRATION)
process.PhotonToHCALIsoPUCorrected09.massForArbitration = cms.double(MZ)
process.PhotonToHCALIsoPUCorrected09.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToHCALIsoPUCorrected09.xSec = cms.double(XSEC)
process.PhotonToHCALIsoPUCorrected09.nEvts = cms.uint32(NEVTS)
process.PhotonToHCALIsoNoHLTPUCorrected09.arbitration = cms.string(ARBITRATION)
process.PhotonToHCALIsoNoHLTPUCorrected09.massForArbitration = cms.double(MZ)
process.PhotonToHCALIsoNoHLTPUCorrected09.eventWeight = cms.double(EVENT_WEIGHT)
process.PhotonToHCALIsoNoHLTPUCorrected09.xSec = cms.double(XSEC)
process.PhotonToHCALIsoNoHLTPUCorrected09.nEvts = cms.uint32(NEVTS)

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
