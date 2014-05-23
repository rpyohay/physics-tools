import FWCore.ParameterSet.Config as cms

process = cms.Process("FITTERSTUDY")
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.load("FWCore.MessageService.MessageLogger_cfi")

#colors from ROOT
blue = 857
green = 834
purple = 619
PLOTCOLORS = cms.vuint32(blue, green, purple)

#gen parameters
NBKGPASSOVERNSIGPASS = 0.001
NBKGFAILOVERNSIGFAIL = 0.01
NSIGALL = 500
EFF = 0.9

#basic macros
GENID = 'Gen'
FITID = 'Fit'
VARNAME = 'mass'
GENVARNAME = VARNAME + GENID
FITVARNAME = VARNAME + FITID
VARTITLE = 'm_{tag-probe}'
VARUNITS = 'GeV/c^{2}'
FITLOWERLIM = 60.0
FITUPPERLIM = 120.0
OUTPUTFILE = '/data/yohay/fitter_study.root'



EFFVARS = cms.vstring("pt", "eta", "dRJets09", "nJets09", "nPV", "run", "run_nPV")
DIMTOBINBY = cms.vuint32(1, 1, 1, 1, 1, 1, 0)
#BRANCHNAMES = cms.vstring("probe_et", "probe_eta", "probe_dRjet09", "probe_nJets09", "event_nPV",
#                          "run"
#                          )
UNITS = cms.vstring("p_{T} (GeV)", "#eta", "#DeltaR_{#gammaj}", "N_{j}", "N_{PV}", "Run", "Run")
PARNAMES = cms.vstring("alpha", "cFail", "cPass", "efficiency", "mean", "n", "numBackgroundFail",
                       "numBackgroundPass", "numSignalAll", "width"
                       )
FITLOWERLIM = cms.vdouble(30.0, -1.5, 0.9, -0.5, 0.5, 132440)
FITUPPERLIM = cms.vdouble(120.0, 1.5, 4.1, 3.5, 7.5, 149442)
SHOWXERRORBARS = cms.bool(True)

#module definition
process.FitterStudy = cms.EDAnalyzer(
    "FitterStudy",

    #output file to store RooMCStudy histograms
    outputFile = cms.string(OUTPUTFILE),

    #name, title, and units of variable to be generated
    genVarName = cms.vstring(GENVARNAME, VARTITLE, VARUNITS),

    #name, title, and units of variable to be fit
    fitVarName = cms.vstring(FITVARNAME, VARTITLE, VARUNITS),

    #lower and upper limits of fit
    fitVarLimits = cms.vdouble(FITLOWERLIM, FITUPPERLIM),

    #all PDFs must be in RooWorkspace factory syntax
    PDFParSet = cms.PSet(

    #PDF describing the generated data
    genPDF = cms.vstring(

    #1 signal shape for tag-pass and tag-fail called "signal", or 1 "signalPass" and 1 "signalFail"
    "ZGeneratorLineShape::signalPhy" + GENID + "(" + GENVARNAME + ")",
    "RooCBShape::signalRes" + GENID + "(" + GENVARNAME + ", mean[-5.88229274420057457e-01], width[1.96930488886820232e+00], alpha[1.37873426687373990e+00], n[3.77653285661682281e+00])",
    "FCONV::signal" + GENID + "(" + GENVARNAME + ", signalPhy, signalRes)",

    #1 background shape for tag-pass and 1 for tag-fail
    "RooExponential::backgroundPass" + GENID + "(" + GENVARNAME + ", cPass[2.03937835475418439e-02])",
    "RooExponential::backgroundFail" + GENID + "(" + GENVARNAME + ", cFail[2.56419220774883883e-03])",

    #desired ratios of background to signal in tag-pass and tag-fail samples
    "NBkgPassOverNSigPass" + GENID + "[" + NBKGPASSOVERNSIGPASS + "]",
    "NBkgFailOverNSigFail" + GENID + "[" + NBKGFAILOVERNSIGFAIL + "]",

    #desired number of signal (Z) events
    "NSigAll" + GENID + "[" + NSIGALL + "]",

    #desired efficiency
    "efficiency" + GENID + "[" + EFF + "]"
    ),

    #PDF with which to fit the generated data
    fitPDF = cms.vstring(

    #1 signal shape for tag-pass and tag-fail called "signal", or 1 "signalPass" and 1 "signalFail"
    "ZGeneratorLineShape::signalPhy" + FITID + "(" + FITVARNAME + ")",
    "RooCBShape::signalRes" + FITID + "(" + FITVARNAME + ", mean[0.0, -5.0, 5.0], width[1.8, 1.0, 3.0], alpha[1.7, 0.0, 3.0], n[2, 1, 10])",
    "FCONV::signal" + FITID + "(" + FITVARNAME + ", signalPhy, signalRes)",

    #1 background shape for tag-pass and 1 for tag-fail
    "RooExponential::backgroundPass" + FITID + "(" + FITVARNAME + ", cPass[0, -5, 5])",
    "RooExponential::backgroundFail" + FITID + "(" + FITVARNAME + ", cFail[0, -5, 5])",

    #used to set initial values
    "efficiency" + FITID + "[0.9, 0, 1]",
    "signalFractionInPassing[0.9]"
    )
    ),




    inputFile = cms.string(
    "/data/yohay/efficiency_photonToID_nPVGreater0_mass60-120GeV_expBkg_CBSig_allFix.root"
    ),
    legendEntries = cms.vstring(
    "Tag-pass sample",
    "Tag-fail sample",
    "Tag-pass + tag-fail samples"
    ),
    plotColors = PLOTCOLORS,
    effVars = EFFVARS,
    dimToBinBy = DIMTOBINBY,
    #branchNames = BRANCHNAMES,
    units = UNITS,
    parNames = PARNAMES,
    doEffFits = cms.bool(False),
    showXErrorBars = SHOWXERRORBARS,
    fitLowerLim = FITLOWERLIM,
    fitUpperLim = FITUPPERLIM
    )

#run the job
process.run = cms.Path(process.FitterStudy)
