import FWCore.ParameterSet.Config as cms

#Z variables to store
ZVariablesToStore = cms.PSet(eta = cms.string("eta"),
                             pt = cms.string("pt"),
                             phi = cms.string("phi"),
                             et = cms.string("et"),
                             e = cms.string("energy"),
                             p = cms.string("p"),
                             px = cms.string("px"),
                             py = cms.string("py"),
                             pz = cms.string("pz"),
                             theta = cms.string("theta"),
                             vx = cms.string("vx"),
                             vy = cms.string("vy"),
                             vz = cms.string("vz"),
                             rapidity = cms.string("rapidity"),
                             mass = cms.string("mass"),
                             mt = cms.string("mt")
                             )

#tag variables to store
TagPhotonVariablesToStore = cms.PSet(
    photon_eta = cms.string("eta"),
    photon_pt = cms.string("pt"),
    photon_phi = cms.string("phi"),
    photon_px = cms.string("px"),
    photon_py = cms.string("py"),
    photon_pz = cms.string("pz"),
    ## super cluster quantities
    sc_energy = cms.string("superCluster.energy"),
    sc_et = cms.string("superCluster.energy*sin(superCluster.position.theta)"),
    sc_x = cms.string("superCluster.x"),
    sc_y = cms.string("superCluster.y"),
    sc_z = cms.string("superCluster.z"),
    sc_eta = cms.string("superCluster.eta"),
    sc_phi = cms.string("superCluster.phi"),
    sc_size = cms.string("superCluster.size"), # number of hits
    sc_rawEnergy = cms.string("superCluster.rawEnergy"), 
    sc_preshowerEnergy = cms.string("superCluster.preshowerEnergy"),
    sc_phiWidth = cms.string("superCluster.phiWidth"),
    sc_etaWidth = cms.string("superCluster.etaWidth"),
    ## isolation
    photon_trackiso_dr04 = cms.string("trkSumPtHollowConeDR04"),
    photon_ecaliso_dr04 = cms.string("ecalRecHitSumEtConeDR04"),
    photon_hcaliso_dr04 = cms.string("hcalTowerSumEtConeDR04"),
    photon_trackiso_dr03 = cms.string("trkSumPtHollowConeDR03"),
    photon_ecaliso_dr03 = cms.string("ecalRecHitSumEtConeDR03"),
    photon_hcaliso_dr03 = cms.string("hcalTowerSumEtConeDR03"),
    ## classification, location, etc.
    photon_isEB = cms.string("isEB"),
    photon_isEE = cms.string("isEE"),
    photon_isEBEEGap = cms.string("isEBEEGap"),
    photon_isEBEtaGap = cms.string("isEBEtaGap"),
    photon_isEBPhiGap = cms.string("isEBPhiGap"),
    photon_isEEDeeGap = cms.string("isEEDeeGap"),
    photon_isEERingGap = cms.string("isEERingGap"),
    ## Hcal energy over Ecal Energy
    photon_HoverE = cms.string("hadronicOverEm"),
    photon_HoverE_Depth1 = cms.string("hadronicDepth1OverEm"),
    photon_HoverE_Depth2 = cms.string("hadronicDepth2OverEm"),
    ## Cluster shape information
    photon_sigmaEtaEta = cms.string("sigmaEtaEta"),
    photon_sigmaIetaIeta = cms.string("sigmaIetaIeta"),
    photon_e1x5 = cms.string("e1x5"),
    photon_e2x5 = cms.string("e2x5"),
    photon_e5x5 = cms.string("e5x5"),
    photon_hasPixelSeed = cms.string("hasPixelSeed"),
    photon_R9 = cms.string("r9")
    )

#probe variables to store
ProbePhotonVariablesToStore = cms.PSet(
    probe_eta = cms.string("eta"),
    probe_SC_eta = cms.string("superCluster.eta"),
    probe_phi = cms.string("phi"),
    probe_et = cms.string("et"),
    probe_px = cms.string("px"),
    probe_py = cms.string("py"),
    probe_pz = cms.string("pz"),
    ## isolation
    probe_trkSumPtHollowConeDR03 = cms.string("trkSumPtHollowConeDR03"),
    probe_ecalRecHitSumEtConeDR03 = cms.string("ecalRecHitSumEtConeDR03"),
    probe_hcalTowerSumEtConeDR03 = cms.string("hcalTowerSumEtConeDR03"),
    probe_trkSumPtHollowConeDR04 = cms.string("trkSumPtHollowConeDR04"),
    probe_ecalRecHitSumEtConeDR04 = cms.string("ecalRecHitSumEtConeDR04"),
    probe_hcalTowerSumEtConeDR04 = cms.string("hcalTowerSumEtConeDR04"),
    ## booleans
    probe_isPhoton = cms.string("isPhoton"),
    ## Hcal energy over Ecal Energy
    probe_hadronicOverEm = cms.string("hadronicOverEm"),
    ## Cluster shape information
    probe_sigmaIetaIeta = cms.string("sigmaIetaIeta"),
    probe_sigmaIphiIphi = cms.string("superCluster.phiWidth"),
    probe_R9 = cms.string("r9"),
    ## Pixel seed
    probe_hasPixelSeed = cms.string("hasPixelSeed")
    )

#PU-subtracted probe variables to store
PUSubtractedProbePhotonVariablesToStore = cms.PSet(
    probe_PURhoSubtractedECALIso04 = cms.InputTag(
    "probePhotonsPassingPUSubtractedECALIsolation", "rhoCorrected", "TagProbe"
    ),
    probe_PUNPVSubtractedECALIso04 = cms.InputTag(
    "probePhotonsPassingPUSubtractedECALIsolation", "nPVCorrected", "TagProbe"
    ),
    probe_PURhoSubtractedHCALIso04 = cms.InputTag(
    "probePhotonsPassingPUSubtractedHCALIsolation", "rhoCorrected", "TagProbe"
    ),
    probe_PUNPVSubtractedHCALIso04 = cms.InputTag(
    "probePhotonsPassingPUSubtractedHCALIsolation", "nPVCorrected", "TagProbe"
    )
    )

#jet variables to store
## JetVariablesToStore = cms.PSet(jet_pt = cms.string("pt"))

#common stuff for probe
CommonStuffForPhotonProbe = cms.PSet(variables = cms.PSet(ProbePhotonVariablesToStore),
                                     ignoreExceptions = cms.bool(False),
                                     #fillTagTree = cms.bool(True),
                                     addRunLumiInfo = cms.bool(True),
                                     addEventVariablesInfo = cms.bool(True),
                                     pairVariables = cms.PSet(ZVariablesToStore),
                                     pairFlags = cms.PSet(
    mass60to120 = cms.string("60 < mass < 120")
    ),
                                     tagVariables = cms.PSet(TagPhotonVariablesToStore),
                                     tagFlags =  cms.PSet(flag = cms.string("pt > 0")),
                                     )

#common stuff for MC matching
mcTruthCommonStuff = cms.PSet(
    isMC = cms.bool(True),
    tagMatches = cms.InputTag("McMatchTag"),
    motherPdgId = cms.vint32(22,23),
    makeMCUnbiasTree = cms.bool(False),
    checkMotherInUnbiasEff = cms.bool(True),
##     mcVariables = cms.PSet(probe_eta = cms.string("eta"),
##                            probe_pt = cms.string("pt"),
##                            probe_phi = cms.string("phi"),
##                            probe_et = cms.string("et"),
##                            probe_e = cms.string("energy"),
##                            probe_p = cms.string("p"),
##                            probe_px = cms.string("px"),
##                            probe_py = cms.string("py"),
##                            probe_pz = cms.string("pz"),
##                            probe_theta = cms.string("theta"),
##                            probe_vx = cms.string("vx"),
##                            probe_vy = cms.string("vy"),
##                            probe_vz = cms.string("vz"),
##                            probe_charge = cms.string("charge"),
##                            probe_rapidity = cms.string("rapidity"),
##                            probe_mass = cms.string("mass"),
##                            probe_mt = cms.string("mt"),
##                            ),
##     mcFlags = cms.PSet(probe_flag = cms.string("pt > 0")),
    eventWeight = cms.double(1.0),
    PUWeight = cms.VInputTag(cms.InputTag("PUWeightProducerPostMay10ReReco")),
    xSec = cms.double(0.0),
    nEvts = cms.uint32(1)
    )

#turn off MC stuff for data
dataCommonStuff = cms.PSet(isMC = cms.bool(False))
