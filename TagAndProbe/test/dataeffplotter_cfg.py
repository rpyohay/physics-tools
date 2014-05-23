import FWCore.ParameterSet.Config as cms

#setup
process = cms.Process("DATAEFFPLOTTER")
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )
process.load("FWCore.MessageService.MessageLogger_cfi")

#colors from ROOT
blue = 857
green = 834
purple = 619

#plot names for option 1
MCTRUTH = False
PLOTNAMES = cms.vstring("")
if MCTRUTH:
    PLOTNAMES = cms.vstring("effVsPT_",
                            "effVsEta_",
                            "effVsDRPhotonJet_",
                            "effVsNJets_",
                            "effVsNPV_"
                            )
else:
    PLOTNAMES = cms.vstring(
##         "SCToIsoVL/pt/fit_eff_plots/probe_et_PLOT_probe_SC_eta_bin0",
##         "SCToIsoVL/eta/fit_eff_plots/probe_SC_eta_PLOT_probe_et_bin0",
##         "SCToIsoVL/nJets05/fit_eff_plots/probe_nJets05_PLOT_probe_SC_eta_bin0_&_probe_et_bin0",
##         "SCToIsoVL/dRJets03/fit_eff_plots/probe_dRjet03_PLOT_probe_SC_eta_bin0_&_probe_et_bin0",
##         "SCToIsoVL/nPV/fit_eff_plots/event_nPV_PLOT_probe_SC_eta_bin0_&_probe_et_bin0",
##         "SCToIsoVL/unbinned/fit_eff_plots/probe_SC_eta_PLOT_probe_et_bin0",
        "SCToIsoVLOnly/pt/fit_eff_plots/probe_et_PLOT_probe_SC_eta_bin0"
        )

#module definition
process.DataEffPlotter = cms.EDAnalyzer(
    "DataEffPlotter",
    inputFiles = cms.vstring(
    "/data2/yohay/RA3/data_tagProbeTrees/eff_SCToIsoVLOnly_ET.root",
    "/data2/yohay/RA3/MC_tagProbeTrees/eff_SCToIsoVLOnly_ET.root"
    ),
    outputFile = cms.string(
    "/data2/yohay/RA3/scale_SCToIsoVLOnly_ET.root"
    ),
##     legendEntries = cms.vstring("Photon selection efficiency (minus HLT and pixel seed veto)",
##                                 "I_{ECAL} efficiency", "I_{HCAL} efficiency", "H/E efficiency",
##                                 "I_{track} efficiency", "#sigma_{i#etai#eta} efficiency"),
    legendEntries = cms.vstring(
    "Data (runs 165088-180252)",
    "MC (Drell-Yan#rightarrowee+jet, #gamma+jet, QCD, W+jet, t#bar{t})"
    ),
    plotColors = cms.vuint32(blue, green),
##     effVars = cms.vstring("pt", "eta", "nJets05", "dRJet03", "nPV"),
    effVars = cms.vstring("pt"),
##     cuts = cms.vstring("", "", "", "", ""),
    cuts = cms.vstring(""),
##     canvasFileNames = cms.vstring("", "", "", "", ""),
    canvasFileNames = cms.vstring(""),
    plotNames = PLOTNAMES,
##     units = cms.vstring("E_{T} (GeV)", "#eta", "N_{jet}", "#DeltaR_{#gammajet}", "N_{PV}"),
    units = cms.vstring("E_{T} (GeV)"),
    MCTruth = cms.bool(False),
    doEffFits = cms.bool(False),
##     fitLowerLim = cms.vdouble(25.0, -1.4442, -0.5, 0.3, 0.5),
    fitLowerLim = cms.vdouble(25.0),
##     fitUpperLim = cms.vdouble(200.0, 1.4442, 4.5, 3.9, 20.5),
    fitUpperLim = cms.vdouble(200.0),
    opt = cms.uint32(1),
##     effDirs = cms.vstring("SCToIsoVL", "SCToIsoVL", "SCToIsoVL", "SCToIsoVL", "SCToIsoVL"),
    effDirs = cms.vstring("SCToIsoVLOnly"),
##     effVarLeaves = cms.vstring("probe_et", "probe_SC_eta", "probe_nJets05", "probe_dRjet03", "event_nPV"),
    effVarLeaves = cms.vstring("probe_et"),
##     xAxisLowerLim = cms.vdouble(15.0, -1.4442, -0.5, 0.3, 0.5),
    xAxisLowerLim = cms.vdouble(15.0),
##     xAxisUpperLim = cms.vdouble(200.0, 1.4442, 4.5, 3.9, 20.5)
    xAxisUpperLim = cms.vdouble(200.0)
    )

#run the job
process.run = cms.Path(process.DataEffPlotter)
