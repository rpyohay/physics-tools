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
    INPUT_FILE_NAMES
    ),
    InputFileNamesBkg = cms.vstring(
    INPUT_BKG_FILE_NAMES
    ),
    InputDirectoryName = cms.string("INPUT_DIRECTORY_NAME"),
    InputTreeName = cms.string("fitter_tree"),
    OutputFileName = cms.string(
    "/data2/yohay/eff_MC/efficiency_INPUT_DIRECTORY_NAME_LABEL.root"
    ),

    #numbrer of CPUs to use for fitting
    NumCPU = cms.uint32(4),

    # specifies wether to save the RooWorkspace containing the data for each bin and
    # the pdf object with the initial and final state snapshots
    SaveWorkspace = cms.bool(True),
    floatShapeParameters = cms.bool(True),
    fixVars = cms.vstring(),

    #weights
    WeightVariable = cms.string("totalWeight"),
                                                 
    # defines all the real variables of the probes available in the input tree and intended for use in the efficiencies
    Variables = cms.PSet(
    totalWeight = cms.vstring("Total weight", "0.0", "20000.0", ""),
    mass = cms.vstring("Tag-Probe Mass", "60.0", "120.0", "GeV/c^{2}"),
    probe_et = cms.vstring("Probe E_{T}", "0", "1000", "GeV/c"),
    probe_SC_eta = cms.vstring("Probe SC #eta", "-1.4442", "1.4442", ""),
    probe_dR2jet00 = cms.vstring(
    "#DeltaR(probe, nearest jet), jets cross-cleaned using #DeltaR = 0.3, no jet p_{T} cut",
    "0.3", "3.9", ""
    ),
    probe_dRjet03 = cms.vstring(
    "#DeltaR(probe, nearest jet), jets cross-cleaned using #DeltaR = 0.3", "0.3", "4.5", ""
    ),
    probe_dRjet05 = cms.vstring(
    "#DeltaR(probe, nearest jet), jets cross-cleaned using #DeltaR = 0.5", "0.5", "4.5", ""
    ),
    probe_dRjet07 = cms.vstring(
    "#DeltaR(probe, nearest jet), jets cross-cleaned using #DeltaR = 0.7", "0.5", "4.5", ""
    ),
    probe_dRjet09 = cms.vstring(
    "#DeltaR(probe, nearest jet), jets cross-cleaned using #DeltaR = 0.9", "0.9", "4.9", ""
    ),
    probe_nJets03 = cms.vstring(
    "N_{j}, jets cross-cleaned using #DeltaR = 0.3", "-0.5", "5.5", ""
    ),
    probe_nJets05 = cms.vstring(
    "N_{j}, jets cross-cleaned using #DeltaR = 0.5", "-0.5", "5.5", ""
    ),
    probe_nJets07 = cms.vstring(
    "N_{j}, jets cross-cleaned using #DeltaR = 0.7", "-0.5", "5.5", ""
    ),
    probe_nJets09 = cms.vstring(
    "N_{j}, jets cross-cleaned using #DeltaR = 0.9", "-0.5", "5.5", ""
    ),
    event_nPV = cms.vstring("N_{PV}", "0.5", "15.5", ""),
    probe_R9 = cms.vstring("R9", "0.2", "0.98", "")
    ),
                     
    # defines all the discrete variables of the probes available in the input tree and intended for use in the efficiency calculations
    Categories = cms.PSet(mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
                          PASS_RHO = cms.vstring("passesRho", "dummy[pass=1,fail=0]"),
                          PASS_NPV = cms.vstring("passesNPV", "dummy[pass=1,fail=0]"),
                          ),

    # defines all the PDFs that will be available for the efficiency calculations; uses RooFit's "factory" syntax;
    # each pdf needs to define "signal", "backgroundPass", "backgroundFail" pdfs, "efficiency[0.9,0,1]" and "signalFractionInPassing[0.9]" are used for initial values  
    PDFs = cms.PSet(gaussPlusLinear = cms.vstring(
    "ZGeneratorLineShape::signalPhy(mass)",
    "RooCBShape::signalResPass(mass, meanPass[0.0, -1.0, 1.0], widthPass[1.8, 1.0, 3.0], alphaPass[1.4], nPass[138.6])",
    "RooCBShape::signalResFail(mass, meanFail[0.0, -2.0, 2.0], widthFail[1.8, 1.0, 3.0], alphaFail[1.4], nFail[138.6])",
    "FCONV::signalPass(mass, signalPhy, signalResPass)",
    "FCONV::signalFail(mass, signalPhy, signalResFail)",
    "RooCMSShape::backgroundPass(mass, aPass[79.8], bPass[0.081], gPass[0.02], peakPass[91.2])",
    "RooCMSShape::backgroundFail(mass, aFail[79.8], bFail[0.081], gFail[0.02], peakFail[91.2])",
    "efficiency[0.9,0,1]",
    "signalFractionInPassing[0.9]"
    ),
                    gaussPlusLinearBkgFloat = cms.vstring(
    "ZGeneratorLineShape::signalPhy(mass)",
    "RooCBShape::signalResPass(mass, meanPass[0.0, -1.0, 1.0], widthPass[1.8, 1.0, 3.0], alphaPass[1.4], nPass[138.6])",
    "RooCBShape::signalResFail(mass, meanFail[0.0, -1.0, 1.0], widthFail[1.8, 1.0, 3.0], alphaFail[1.4], nFail[138.6])",
    "FCONV::signalPass(mass, signalPhy, signalResPass)",
    "FCONV::signalFail(mass, signalPhy, signalResFail)",
##     "RooCMSShape::backgroundPass(mass, aPass[79.8, 50.0, 90.0], bPass[0.17, 0.16, 0.18], gPass[0.2, 0.1, 0.5], peakPass[91.2, 80.0, 100.0])",
##     "RooCMSShape::backgroundFail(mass, aFail[79.8, 50.0, 90.0], bFail[0.081, 0.05, 0.5], gFail[0.02, 0.002, 0.2], peakFail[91.2, 80.0, 100.0])",
    "RooCMSShape::backgroundPass(mass, aPass[79.8], bPass[0.081], gPass[0.02], peakPass[91.2, 50.0, 120.0])",
    "RooCMSShape::backgroundFail(mass, aFail[79.8], bFail[0.081], gFail[0.02], peakFail[91.2, 50.0, 120.0])",
    "efficiency[0.9,0,1]",
    "signalFractionInPassing[0.9]"
    )
                    ),

    # defines a set of efficiency calculations, what PDF to use for fitting and how to bin the data;
    # there will be a separate output directory for each calculation that includes a simultaneous fit, side band subtraction and counting. 
    Efficiencies = cms.PSet(

##     unbinnedRho = cms.PSet(EfficiencyCategoryAndState = cms.vstring("PASS_RHO", "pass"),
##                            UnbinnedVariables = cms.vstring("mass", "totalWeight"),
##                            BinnedVariables = cms.PSet(
##     probe_nJets05 = cms.vdouble(0.5, 15.5),
##     probe_SC_eta = cms.vdouble(-1.4442, 1.4442)),
##                            BinToPDFmap = cms.vstring("gaussPlusLinear")
##                            ),
##     unbinnedNPV = cms.PSet(EfficiencyCategoryAndState = cms.vstring("PASS_NPV", "pass"),
##                            UnbinnedVariables = cms.vstring("mass", "totalWeight"),
##                            BinnedVariables = cms.PSet(
##     probe_nJets05 = cms.vdouble(0.5, 15.5),
##     probe_SC_eta = cms.vdouble(-1.4442, 1.4442)),
##                            BinToPDFmap = cms.vstring("gaussPlusLinear")
##                            ),

##     dRJetRho = cms.PSet(EfficiencyCategoryAndState = cms.vstring("PASS_RHO","pass"),
##                         UnbinnedVariables = cms.vstring("mass", "totalWeight"),
##                         BinnedVariables = cms.PSet(
##     probe_nJets05 = cms.vdouble(0.5, 15.5),
##     probe_SC_eta = cms.vdouble(-1.4442, 1.4442),
##     probe_dR2jet00 = cms.vdouble(0.3, 0.9, 1.5, 2.1, 2.7, 3.3, 3.9)
##     ),
##                         BinToPDFmap = cms.vstring("gaussPlusLinear")
##                         ),
##     dRJetNPV = cms.PSet(EfficiencyCategoryAndState = cms.vstring("PASS_NPV","pass"),
##                         UnbinnedVariables = cms.vstring("mass", "totalWeight"),
##                         BinnedVariables = cms.PSet(
##     probe_nJets05 = cms.vdouble(0.5, 15.5),
##     probe_SC_eta = cms.vdouble(-1.4442, 1.4442),
##     probe_dR2jet00 = cms.vdouble(0.3, 0.9, 1.5, 2.1, 2.7, 3.3, 3.9)
##     ),
##                         BinToPDFmap = cms.vstring("gaussPlusLinear")
##                         ),
    
##     #the name of the parameter set becomes the name of the directory
##     ptRho = cms.PSet(
    
##     #specifies the efficiency of which category and state to measure 
##     EfficiencyCategoryAndState = cms.vstring("PASS_RHO","pass"),
    
##     #specifies what unbinned variables to include in the dataset, the mass is needed for the fit
##     UnbinnedVariables = cms.vstring("mass", "totalWeight"),
    
##     #specifies the binning of parameters
##     BinnedVariables = cms.PSet(
##     probe_nJets05 = cms.vdouble(0.5, 15.5),
##     probe_SC_eta = cms.vdouble(-1.4442, 1.4442),
##     probe_et = cms.vdouble(
##     30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 80.0, 120.0, 160.0, 200.0
##     )
##     ),
    
##     #first string is the default followed by binRegExp - PDFname pairs
##     BinToPDFmap = cms.vstring("gaussPlusLinearBkgFloat")
##     ),
    
##     ptNPV = cms.PSet(
    
##     #specifies the efficiency of which category and state to measure 
##     EfficiencyCategoryAndState = cms.vstring("PASS_NPV","pass"),
    
##     #specifies what unbinned variables to include in the dataset, the mass is needed for the fit
##     UnbinnedVariables = cms.vstring("mass", "totalWeight"),
    
##     #specifies the binning of parameters
##     BinnedVariables = cms.PSet(
##     probe_nJets05 = cms.vdouble(0.5, 15.5),
##     probe_SC_eta = cms.vdouble(-1.4442, 1.4442),
##     probe_et = cms.vdouble(
##     30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 80.0, 120.0, 160.0, 200.0
##     )
##     ),

##     #first string is the default followed by binRegExp - PDFname pairs
##     BinToPDFmap = cms.vstring("gaussPlusLinearBkgFloat")
##     ),
    
##     etaRho = cms.PSet(EfficiencyCategoryAndState = cms.vstring("PASS_RHO","pass"),
##                       UnbinnedVariables = cms.vstring("mass", "totalWeight"),
##                       BinnedVariables = cms.PSet(
##     probe_nJets05 = cms.vdouble(0.5, 15.5),
##     probe_SC_eta = cms.vdouble(
##     -1.4442, -1.25, -1.0, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.4442
##     )
##     ),
##                       BinToPDFmap = cms.vstring("gaussPlusLinear")
##                       ),
##     etaNPV = cms.PSet(EfficiencyCategoryAndState = cms.vstring("PASS_NPV","pass"),
##                       UnbinnedVariables = cms.vstring("mass", "totalWeight"),
##                       BinnedVariables = cms.PSet(
##     probe_nJets05 = cms.vdouble(0.5, 15.5),
##     probe_SC_eta = cms.vdouble(
##     -1.4442, -1.25, -1.0, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.4442
##     )
##     ),
##                       BinToPDFmap = cms.vstring("gaussPlusLinear")
##                       ),
    dRJets03Rho = cms.PSet(EfficiencyCategoryAndState = cms.vstring("PASS_RHO", "pass"),
                           UnbinnedVariables = cms.vstring("mass", "totalWeight"),
                           BinnedVariables = cms.PSet(
##     probe_nJets05 = cms.vdouble(0.5, 15.5),
    probe_SC_eta = cms.vdouble(-1.4442, 1.4442),
    probe_dRjet03 = cms.vdouble(0.3, 0.9, 1.5, 2.1, 2.7, 3.3, 3.9)
    ),
                           BinToPDFmap = cms.vstring("gaussPlusLinear")
                           ),
    dRJets03NPV = cms.PSet(EfficiencyCategoryAndState = cms.vstring("PASS_NPV", "pass"),
                           UnbinnedVariables = cms.vstring("mass", "totalWeight"),
                           BinnedVariables = cms.PSet(
##     probe_nJets05 = cms.vdouble(0.5, 15.5),
    probe_SC_eta = cms.vdouble(-1.4442, 1.4442),
    probe_dRjet03 = cms.vdouble(0.3, 0.9, 1.5, 2.1, 2.7, 3.3, 3.9)
    ),
                           BinToPDFmap = cms.vstring("gaussPlusLinear")
                           ),
    nJets05Rho = cms.PSet(EfficiencyCategoryAndState = cms.vstring("PASS_RHO", "pass"),
                          UnbinnedVariables = cms.vstring("mass", "totalWeight"),
                          BinnedVariables = cms.PSet(
    probe_SC_eta = cms.vdouble(-1.4442, 1.4442),
    probe_nJets05 = cms.vdouble(-0.5, 0.5, 1.5, 2.5, 3.5, 4.5)
    ),
                          BinToPDFmap = cms.vstring("gaussPlusLinear")
                          ),
    nJets05NPV = cms.PSet(EfficiencyCategoryAndState = cms.vstring("PASS_NPV", "pass"),
                          UnbinnedVariables = cms.vstring("mass", "totalWeight"),
                          BinnedVariables = cms.PSet(
    probe_SC_eta = cms.vdouble(-1.4442, 1.4442),
    probe_nJets05 = cms.vdouble(-0.5, 0.5, 1.5, 2.5, 3.5, 4.5)
    ),
                          BinToPDFmap = cms.vstring("gaussPlusLinear")
                          ),
##     nPVRho = cms.PSet(EfficiencyCategoryAndState = cms.vstring("PASS_RHO", "pass"),
##                       UnbinnedVariables = cms.vstring("mass", "totalWeight"),
##                       BinnedVariables = cms.PSet(
##     probe_nJets05 = cms.vdouble(0.5, 15.5),
##     probe_SC_eta = cms.vdouble(-1.4442, 1.4442),
##     event_nPV = cms.vdouble(
##     0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5
##     )
##     ),
##                       BinToPDFmap = cms.vstring("gaussPlusLinear")
##                       ),
##     nPVNPV = cms.PSet(EfficiencyCategoryAndState = cms.vstring("PASS_NPV", "pass"),
##                       UnbinnedVariables = cms.vstring("mass", "totalWeight"),
##                       BinnedVariables = cms.PSet(
##     probe_nJets05 = cms.vdouble(0.5, 15.5),
##     probe_SC_eta = cms.vdouble(-1.4442, 1.4442),
##     event_nPV = cms.vdouble(
##     0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5
##     )
##     ),
##                       BinToPDFmap = cms.vstring("gaussPlusLinear")
##                       )
    R9Rho = cms.PSet(EfficiencyCategoryAndState = cms.vstring("PASS_RHO", "pass"),
                  UnbinnedVariables = cms.vstring("mass", "totalWeight"),
                  BinnedVariables = cms.PSet(
    probe_SC_eta = cms.vdouble(-1.4442, 1.4442),
    probe_R9 = cms.vdouble(0.2, 0.4, 0.6, 0.8, 0.9, 0.92, 0.94, 0.96, 0.98)
    ),
                       BinToPDFmap = cms.vstring("gaussPlusLinear")
                  ),
    R9NPV = cms.PSet(EfficiencyCategoryAndState = cms.vstring("PASS_NPV", "pass"),
                  UnbinnedVariables = cms.vstring("mass", "totalWeight"),
                  BinnedVariables = cms.PSet(
    probe_SC_eta = cms.vdouble(-1.4442, 1.4442),
    probe_R9 = cms.vdouble(0.2, 0.4, 0.6, 0.8, 0.9, 0.92, 0.94, 0.96, 0.98)
    ),
                       BinToPDFmap = cms.vstring("gaussPlusLinear")
                  )
    )
    )

process.fit = cms.Path(process.TagProbeFitTreeAnalyzer)
