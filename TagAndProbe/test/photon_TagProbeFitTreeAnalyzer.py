import FWCore.ParameterSet.Config as cms

process = cms.Process("TagProbe")
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 1


process.TagProbeFitTreeAnalyzer = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
    # IO parameters:
    #InputFileNames = cms.vstring("/data/yohay/tagProbeTree_data_MCANCuts_Photon30Cleaned_noJetInfo/tagProbeTree_data_MCANCuts_Photon30Cleaned_noJetInfo.root"),
    InputFileNames = cms.vstring("/data/yohay/tagProbeTree_data_MCANCuts_Photon308E29_noJetInfo/tagProbeTree_data_MCANCuts_Photon308E29_noJetInfo.root", "/data/yohay/tagProbeTree_data_MCANCuts_Photon30_noJetInfo/tagProbeTree_data_MCANCuts_Photon30_noJetInfo.root", "/data/yohay/tagProbeTree_data_MCANCuts_Photon30Cleaned_noJetInfo/tagProbeTree_data_MCANCuts_Photon30Cleaned_noJetInfo.root"),
    InputDirectoryName = cms.string("PhotonToHLT"),
    InputTreeName = cms.string("fitter_tree"),
    OutputFileName = cms.string("/data/yohay/tagProbeTree_data_MCANCuts_Photon30Cleaned_noJetInfo/efficiency_081010_Photon308E29PlusPhoton30PlusPhoton30Cleaned.root"),
    #numbrer of CPUs to use for fitting
    NumCPU = cms.uint32(1),
    # specifies wether to save the RooWorkspace containing the data for each bin and
    # the pdf object with the initial and final state snapshots
    SaveWorkspace = cms.bool(True),
    floatShapeParameters = cms.bool(True),
    fixVars = cms.vstring("mean"),
                                                 
    # defines all the real variables of the probes available in the input tree and intended for use in the efficiencies
    Variables = cms.PSet(
        mass = cms.vstring("Tag-Probe Mass", "60.0", "120.0", "GeV/c^{2}"),
        probe_et = cms.vstring("Probe p_{T}", "0", "1000", "GeV/c"),
        probe_eta = cms.vstring("Probe #eta", "-2.5", "2.5", "")
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
            "Gaussian::signal(mass, mean[89.0, 89.0, 89.0], sigma[2.3, 0.5, 10.0])",
            "RooExponential::backgroundPass(mass, cPass[0,-10,10])",
            "RooExponential::backgroundFail(mass, cFail[0,-10,10])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
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
                probe_et = cms.vdouble(0, 39.5, 45.0, 120)
                #probe_et = cms.vdouble(0, 120)
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
                probe_eta = cms.vdouble(-1.6, -0.55, 0.0, 0.55, 1.6)
            ),
            #first string is the default followed by binRegExp - PDFname pairs
            BinToPDFmap = cms.vstring("gaussPlusLinear")
        ),
        pt_mcTrue = cms.PSet(
            EfficiencyCategoryAndState = cms.vstring("probe_passing","pass"),
            UnbinnedVariables = cms.vstring("mass"),
            BinnedVariables = cms.PSet(
                mcTrue = cms.vstring("true"),
                #pt = cms.vdouble(20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120)
                probe_et = cms.vdouble(0, 39.5, 45.0, 120)
            ),
            #unspecified binToPDFmap means no fitting
            BinToPDFmap = cms.vstring()
        ),
        pt_eta = cms.PSet(
            EfficiencyCategoryAndState = cms.vstring("probe_passing","pass"),
            UnbinnedVariables = cms.vstring("mass"),
            BinnedVariables = cms.PSet(
            probe_et = cms.vdouble(0, 39.5, 45.0, 120),
            probe_eta = cms.vdouble(-1.6, -0.55, 0.0, 0.55, 1.6)
            ),
            BinToPDFmap = cms.vstring("gaussPlusLinear")
        ),
        pt_eta_mcTrue = cms.PSet(
            EfficiencyCategoryAndState = cms.vstring("probe_passing","pass"),
            UnbinnedVariables = cms.vstring("mass"),
            BinnedVariables = cms.PSet(
                mcTrue = cms.vstring("true"),
                probe_et = cms.vdouble(0, 39.5, 45.0, 120),
                probe_eta = cms.vdouble(-1.6, -0.55, 0.0, 0.55, 1.6)
            ),
            BinToPDFmap = cms.vstring()
        )
    )
)


process.fit = cms.Path(process.TagProbeFitTreeAnalyzer)
