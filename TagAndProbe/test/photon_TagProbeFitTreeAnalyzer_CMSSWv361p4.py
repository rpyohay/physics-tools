import FWCore.ParameterSet.Config as cms

process = cms.Process("TagProbe")
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 1


process.TagProbeFitTreeAnalyzer = cms.EDAnalyzer(
    "TagProbeFitTreeAnalyzer",
    # IO parameters:
    InputFileNames = cms.vstring(
    "/data/yohay/tagProbeTree_MC_MCANCuts/tagProbeTree_MC_photonToID_nPVGreater0.root"
    ),
    InputDirectoryName = cms.string("PhotonToID"),
    InputTreeName = cms.string("fitter_tree"),
    OutputFileName = cms.string(
    "/data/yohay/tagProbeTree_MC_MCANCuts/efficiency_photonToID_nPVGreater0_unbinned.root"
    ),
    #numbrer of CPUs to use for fitting
    NumCPU = cms.uint32(4),
    # specifies wether to save the RooWorkspace containing the data for each bin and
    # the pdf object with the initial and final state snapshots
    SaveWorkspace = cms.bool(True),
    floatShapeParameters = cms.bool(True),
    fixVars = cms.vstring("mean"),
                                                 
    # defines all the real variables of the probes available in the input tree and intended for use in the efficiencies
    Variables = cms.PSet(
        mass = cms.vstring("Tag-Probe Mass", "77.0", "120.0", "GeV/c^{2}"),
        probe_et = cms.vstring("Probe p_{T}", "0", "1000", "GeV/c"),
        probe_eta = cms.vstring("Probe #eta", "-2.5", "2.5", ""),
        probe_dRjet05 = cms.vstring(
    "#DeltaR(probe, nearest jet), jets cross-cleaned using #DeltaR = 0.5", "0.5", "4.5", ""
    ),
        probe_dRjet09 = cms.vstring(
    "#DeltaR(probe, nearest jet), jets cross-cleaned using #DeltaR = 0.9", "0.9", "4.9", ""
    ),
        probe_nJets05 = cms.vstring(
    "N_{j}, jets cross-cleaned using #DeltaR = 0.5", "-0.5", "5.5", ""
    ),
        probe_nJets09 = cms.vstring(
    "N_{j}, jets cross-cleaned using #DeltaR = 0.9", "-0.5", "5.5", ""
    ),
        event_nPV = cms.vstring("N_{PV}", "-0.5", "8.5", "")
        ),

    # defines all the discrete variables of the probes available in the input tree and intended for use in the efficiency calculations
    Categories = cms.PSet(
        mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
        probe_passing = cms.vstring("isMuon", "dummy[pass=1,fail=0]")
    ),

    # defines all the PDFs that will be available for the efficiency calculations; uses RooFit's "factory" syntax;
    # each pdf needs to define "signal", "backgroundPass", "backgroundFail" pdfs, "efficiency[0.9,0,1]" and "signalFractionInPassing[0.9]" are used for initial values  
    PDFs = cms.PSet(
        gaussPlusLinear = cms.vstring(
            #"Gaussian::signal(mass, mean[91.2, 85.2, 97.2], sigma[2.3, 0.5, 10.0])",
            #"Gaussian::signal(mass, mean[89.0, 89.0, 89.0], sigma[2.3, 0.5, 10.0])",
    #"RooCBShape::signal(mass, mean[91.2, 85.2, 97.2], sigma[2.3, 0.5, 10.0], alpha[2.0, 1.0, 4.0], n[1.0, 0.0, 10.0])",
    "RooVoigtian::signal(mass, mean[91.2, 90.0, 92.4], width[2.5, 1.0, 4.0], sigma[2.3, 0.5, 10.0])",
            "RooExponential::backgroundPass(mass, cPass[0,-10,10])",
            "RooExponential::backgroundFail(mass, cFail[0,-10,10])",
            "efficiency[0.9,0,1]",
            #"efficiency[0.45,0,1]",
            "signalFractionInPassing[0.9]"
            #"signalFractionInPassing[0.45]"
        ),
    ),

    # defines a set of efficiency calculations, what PDF to use for fitting and how to bin the data;
    # there will be a separate output directory for each calculation that includes a simultaneous fit, side band subtraction and counting. 
    Efficiencies = cms.PSet(
    #the name of the parameter set becomes the name of the directory
    pt = cms.PSet(
    #specifies the efficiency of which category and state to measure 
    EfficiencyCategoryAndState = cms.vstring("probe_passing","pass"),
    #specifies what unbinned variables to include in the dataset, the mass is needed for the fit
    UnbinnedVariables = cms.vstring("mass"),
    #specifies the binning of parameters
    BinnedVariables = cms.PSet(
    #probe_et = cms.vdouble(
    #0, 20.0, 25.0, 30.0, 35.0, 40.0, 50.0, 60.0, 70.0, 80.0, 120.0
    #)
    probe_et = cms.vdouble(
    #30.0, 40.0, 50.0, 60.0, 90.0, 120.0
    30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 80.0, 120.0
    )
    #probe_et = cms.vdouble(35.0, 120.0)
    ),
    #first string is the default followed by binRegExp - PDFname pairs
    BinToPDFmap = cms.vstring("gaussPlusLinear")
    ),
        eta = cms.PSet(
    #specifies the efficiency of which category and state to measure 
            EfficiencyCategoryAndState = cms.vstring("probe_passing","pass"),
            #specifies what unbinned variables to include in the dataset, the mass is needed for the fit
            UnbinnedVariables = cms.vstring("mass"),
            #specifies the binning of parameters
            BinnedVariables = cms.PSet(
                #probe_eta = cms.vdouble(-1.6, -0.55, 0.0, 0.55, 1.6)
    #probe_eta = cms.vdouble(-1.6, -1.2, -0.8, -0.4, 0.0, 0.4, 0.8, 1.2, 1.6)
    #probe_eta = cms.vdouble(
    #-1.5, -1.25, -1.0, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5
    #)
    probe_eta = cms.vdouble(-1.5, 1.5)
            ),
            #first string is the default followed by binRegExp - PDFname pairs
            BinToPDFmap = cms.vstring("gaussPlusLinear")
        ),
        #dRJets05 = cms.PSet(
    #EfficiencyCategoryAndState = cms.vstring("probe_passing", "pass"),
    #UnbinnedVariables = cms.vstring("mass"),
    #BinnedVariables = cms.PSet(
    #probe_dRjet05 = cms.vdouble(0.5, 1.5, 2.5, 3.5, 4.5)
    #),
    #BinToPDFmap = cms.vstring("gaussPlusLinear")
    #),
        dRJets09 = cms.PSet(
    EfficiencyCategoryAndState = cms.vstring("probe_passing", "pass"),
    UnbinnedVariables = cms.vstring("mass"),
    BinnedVariables = cms.PSet(
    #probe_dRjet09 = cms.vdouble(0.9, 1.9, 2.9, 3.9, 4.9)
    probe_dRjet09 = cms.vdouble(0.9, 1.3, 1.7, 2.1, 2.5, 2.9, 3.3, 3.7, 4.1)
    #probe_dRjet09 = cms.vdouble(0.9, 10.0)
    ),
    BinToPDFmap = cms.vstring("gaussPlusLinear")
    ),
        #nJets05 = cms.PSet(
    #EfficiencyCategoryAndState = cms.vstring("probe_passing", "pass"),
    #UnbinnedVariables = cms.vstring("mass"),
    #BinnedVariables = cms.PSet(
    #probe_nJets05 = cms.vdouble(-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5)
    #),
    #BinToPDFmap = cms.vstring("gaussPlusLinear")
    #),
        nJets09 = cms.PSet(
    EfficiencyCategoryAndState = cms.vstring("probe_passing", "pass"),
    UnbinnedVariables = cms.vstring("mass"),
    BinnedVariables = cms.PSet(
    #probe_nJets09 = cms.vdouble(-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5)
    probe_nJets09 = cms.vdouble(-0.5, 0.5, 1.5, 2.5, 3.5, 4.5)
    #probe_nJets09 = cms.vdouble(-0.5, 10.5)
    ),
    BinToPDFmap = cms.vstring("gaussPlusLinear")
    ),
    nPV = cms.PSet(
    EfficiencyCategoryAndState = cms.vstring("probe_passing", "pass"),
    UnbinnedVariables = cms.vstring("mass"),
    BinnedVariables = cms.PSet(
    event_nPV = cms.vdouble(0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5)
    #event_nPV = cms.vdouble(0.5, 1.5)
    ),
    BinToPDFmap = cms.vstring("gaussPlusLinear")
    ),
        #pt_mcTrue = cms.PSet(
            #EfficiencyCategoryAndState = cms.vstring("probe_passing","pass"),
            #UnbinnedVariables = cms.vstring("mass"),
            #BinnedVariables = cms.PSet(
                #mcTrue = cms.vstring("true"),
                #pt = cms.vdouble(20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120)
                #probe_et = cms.vdouble(0, 39.5, 45.0, 120)
                #probe_et = cms.vdouble(0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 110.0, 120.0)
            #),
            #unspecified binToPDFmap means no fitting
            #BinToPDFmap = cms.vstring()
        #),
        #pt_eta = cms.PSet(
            #EfficiencyCategoryAndState = cms.vstring("probe_passing","pass"),
            #UnbinnedVariables = cms.vstring("mass"),
            #BinnedVariables = cms.PSet(
            #probe_et = cms.vdouble(0.0, 20.0, 30.0, 40.0, 50.0, 120.0),
    #probe_et = cms.vdouble(0, 20.0, 25.0, 30.0, 35.0, 40.0, 50.0, 60.0, 70.0, 80.0, 120.0),
            #probe_eta = cms.vdouble(-1.6, -0.55, 0.0, 0.55, 1.6)
    #probe_eta = cms.vdouble(-1.6, -1.2, -0.8, -0.4, 0.0, 0.4, 0.8, 1.2, 1.6)
            #),
            #BinToPDFmap = cms.vstring("gaussPlusLinear")
        #),
        #pt_eta_mcTrue = cms.PSet(
            #EfficiencyCategoryAndState = cms.vstring("probe_passing","pass"),
            #UnbinnedVariables = cms.vstring("mass"),
            #BinnedVariables = cms.PSet(
                #mcTrue = cms.vstring("true"),
                #probe_et = cms.vdouble(0, 39.5, 45.0, 120),
                #probe_et = cms.vdouble(0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 110.0, 120.0),
                #probe_eta = cms.vdouble(-1.6, -0.55, 0.0, 0.55, 1.6)
            #),
            #BinToPDFmap = cms.vstring()
        #)
    )
)


process.fit = cms.Path(process.TagProbeFitTreeAnalyzer)
