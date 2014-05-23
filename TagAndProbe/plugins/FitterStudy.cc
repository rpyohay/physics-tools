/*********************WORK IN PROGRESS -- DO NOT USE!*********************/

#include <memory>
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "PhysicsTools/TagAndProbe/interface/PlotAux.h"
#include "RooRealVar.h"
#include "RooWorkspace.h"
//#include "RooDataSet.h"
#include "TFile.h"
//#include "RooCategory.h"
/*#include "RooBinning.h"
#include "RooFitResult.h"
#include "RooPlot.h"*/

class FitterStudy : public edm::EDAnalyzer {
public:
  FitterStudy(const edm::ParameterSet& pset);
  virtual ~FitterStudy();
private:
  virtual void analyze(const edm::Event& event, const edm::EventSetup& eventSetup) {};
  virtual void endRun(const edm::Run &run, const edm::EventSetup &setup) {};

  //input parameters
  STRING outputFile_;
  VSTRING genVarName_;
  VSTRING fitVarName_;
  VDOUBLE fitVarLimits_;
  edm::ParameterSet PDFParSet_;

  //gen and fit stuff
  RooRealVar* genVar_;
  RooRealVar* fitVar_;
  map<STRING, VSTRING> PDFs_;
  RooWorkspace* workspace_;

  /******MAYBE UNNECESSARY******/
  /**///graphics             /**/
  /**/VSTRING legendEntries_;/**/
  /**/VUINT plotColors_;     /**/
  /**/bool showXErrorBars_;  /**/
  /**/PlotAux plotAux_;      /**/
  /******MAYBE UNNECESSARY******/
};

FitterStudy::FitterStudy(const edm::ParameterSet& pset) :
  outputFile_(pset.getParameter<STRING>("outputFile")),
  genVarName_(pset.getParameter<VSTRING>("genVarName")),
  fitVarName_(pset.getParameter<VSTRING>("fitVarName")),
  fitVarLimits_(pset.getParameter<VDOUBLE>("fitVarLimits")),
  PDFParSet_(pset.getParameter<edm::ParameterSet>("PDFParSet")),

  /*************************MAYBE UNNECESSARY************************/
  /**/legendEntries_(pset.getParameter<VSTRING>("legendEntries")),/**/
  /**/plotColors_(pset.getParameter<VUINT>("plotColors")),        /**/
  /**/showXErrorBars_(pset.getParameter<bool>("showXErrorBars")), /**/
  /**/plotAux_(PlotAux(plotColors_))                              /**/
  /*************************MAYBE UNNECESSARY************************/
{
  //create the RooWorkspace, import the gen and fit variables, and import the gen and fit PDFs
  workspace_ = NULL;
  workspace_ = new RooWorkspace("workspace");
  if (workspace_ != NULL) {
    workspace_->import(*genVar_);
    workspace_->import(*fitVar_);
    VSTRING PDFTypes = PDFParSet_.getParameterNamesForType<VSTRING>();
    for (VSTRING_IT iType = PDFTypes.begin(); iType != PDFTypes.end(); ++iType) {
      VSTRING shapes = PDFParSet_.getParameter<VSTRING>(*iType);
      for (VSTRING_IT iShape = shapes.begin(); iShape != shapes.end(); ++iShape) {
	TDirectory *here = gDirectory;
	workspace_->factory((*iShape).c_str());
	here->cd();

      }//for (VSTRING_IT iShape = shapes.begin(); iShape != shapes.end(); ++iShape)
    }//for (VSTRING_IT iType = PDFTypes.begin(); iType != PDFTypes.end(); ++iType)
  }//if (workspace_ != NULL)
  else cout << "Error: unable to allocate memory for RooWorkspace.\n";

  //create the simultaneous gen PDF out of the individual gen PDFs already imported
  workspace_->factory("expr::numSignalPassGen('efficiencyGen*numSignalAllGen', efficiencyGen, NSigAllGen)");
  workspace_->factory("expr::numSignalFailGen('(1-efficiencyGen)*NSigAllGen', efficiencyGen, NSigAllGen)");
  TString sPass = "signal", sFail = "signal";
  if (workspace_->pdf("signalPassGen") != 0 && workspace_->pdf("signalFailGen") != 0) {
    if (workspace_->pdf("signalGen") != 0) throw std::logic_error("You must either define one 'signal' PDF or two PDFs ('signalPass', 'signalFail'), not both!"); 
    sPass = "signalPassGen";
    sFail = "signalFailGen";
  }
  else if (workspace_->pdf("signalGen") != 0) {
    if (workspace_->pdf("signalPassGen") != 0 || workspace_->pdf("signalFailGen") != 0) throw std::logic_error("You must either define one 'signal' PDF or two PDFs ('signalPass', 'signalFail'), not both!"); 
  }
  else throw std::logic_error("You must either define one 'signal' PDF or two PDFs ('signalPass', 'signalFail')");
  workspace_->factory("SUM::PDFPassGen(numSignalPassGen*" + sPass + ", NBkgPassOverNSigPass*numSignalPassGen*backgroundPassGen)");
  workspace_->factory("SUM::PDFFailGen(numSignalFailGen*" + sFail + ", NBkgFailOverNSigFail*numSignalFailGen*backgroundFailGen)");
  workspace_->factory("SIMUL::PDFGen(effCategory,Passed=PDFPassGen,Failed=PDFFailGen)");

  //create the simultaneous fit PDF out of the individual fit PDFs already imported
  /*workspace_->factory("expr::numSignalPassFit('efficiencyFit*numSignalAllFit', efficiencyFit, NSigAllFit)");
  workspace_->factory("expr::numSignalFailFit('(1-efficiencyFit)*NSigAllFit', efficiencyFit, NSigAllFit)");
  TString sPass = "signal", sFail = "signal";
  if (workspace_->pdf("signalPassFit") != 0 && workspace_->pdf("signalFailFit") != 0) {
    if (workspace_->pdf("signalFit") != 0) throw std::logic_error("You must either define one 'signal' PDF or two PDFs ('signalPass', 'signalFail'), not both!"); 
    sPass = "signalPassFit";
    sFail = "signalFailFit";
  }
  else if (workspace_->pdf("signalFit") != 0) {
    if (workspace_->pdf("signalPassFit") != 0 || workspace_->pdf("signalFailFit") != 0) throw std::logic_error("You must either define one 'signal' PDF or two PDFs ('signalPass', 'signalFail'), not both!"); 
  }
  else throw std::logic_error("You must either define one 'signal' PDF or two PDFs ('signalPass', 'signalFail')");
  workspace_->factory("SUM::PDFPassFit(numSignalPassFit*" + sPass + ", NBkgPassOverNSigPass*numSignalPassFit*backgroundPassFit)");
  workspace_->factory("SUM::PDFFailFit(numSignalFailFit*" + sFail + ", NBkgFailOverNSigFail*numSignalFailFit*backgroundFailFit)");
  workspace_->factory("SIMUL::PDFFit(effCategory,Passed=PDFPassFit,Failed=PDFFailFit)");*/

  /*

  //sanity checks
  if (dimToBinBy_.size() != effVars_.size()) {
    cerr << "Error: dimToBinBy_.size() = " << dimToBinBy_.size() << " but effVars_.size() = ";
    cerr << effVars_.size() << ".\n";
    if (dimToBinBy_.size() < effVars_.size()) {
      cerr << "Truncating effVars_ after element " << dimToBinBy_.size() - 1 << ".\n";
      effVars_.erase(effVars_.begin() + dimToBinBy_.size(), effVars_.end());
    }
    else {
      cerr << "Truncating dimToBinBy_ after element " << effVars_.size() - 1 << ".\n";
      dimToBinBy_.erase(dimToBinBy_.begin() + effVars_.size(), dimToBinBy_.end());
    }
  }

  //define dimensions of RooDataSet
  effVar_ = new RooCategory("effVar", "");
  for (VSTRING_IT iEffVar = effVars_.begin(); iEffVar != effVars_.end(); ++iEffVar) {
    effVar_->defineType((*iEffVar).c_str());
  }
  binNumber0_ = new RooRealVar("binNumber0", "Bin number 0", -1.0);
  binNumber1_ = new RooRealVar("binNumber1", "Bin number 1", -1.0);
  parName_ = new RooCategory("parName", "");
  for (VSTRING_IT iParName = parNames_.begin(); iParName != parNames_.end(); ++iParName) {
    parName_->defineType((*iParName).c_str());
  }
  parVal_ = new RooRealVar("parVal", "", -1.0);
  parData_ = new RooDataSet("parData", "", 
			    RooArgSet(*effVar_, *binNumber0_, *binNumber1_, *parName_, *parVal_), 
			    RooFit::StoreAsymError(RooArgSet(*parVal_)));

  //go!
  fillParDataset();
  makePlots();

  */
}

FitterStudy::~FitterStudy()
{
  /*
  delete parData_;
  delete effVar_;
  delete binNumber0_;
  delete binNumber1_;
  delete parName_;
  delete parVal_;
  */
}

/*
void FitterStudy::fillParDataset()
{
  //open file
  TFile* file = NULL;
  bool fileErr = false;
  try { file = new TFile(inputFile_.c_str()); }
  catch (cms::Exception& ex) { fileErr = true; }
  if (!fileErr && (file != NULL)) {

    //loop over efficiency variables
    for (VSTRING_IT iEffVar = effVars_.begin(); iEffVar != effVars_.end(); ++iEffVar) {
      Bool_t effVarDirExists = file->cd(plotAux_.name("PhotonToID/", (*iEffVar).c_str()).c_str());
      if (effVarDirExists) {
*/

	/*loop over keys in TDirectory corresponding to efficiency variable
	 *
	 *test whether the key is to a TDirectory by casting it to a TDirectory and calling 
	 *IsFolder()
	 *
	 *exclude cnt_eff_plots and fit_eff_plots TDirectories, which don't contain fit information
	 */
/*
	for (int iKey = 0; iKey < gDirectory->GetNkeys(); ++iKey) {
	  TDirectory* dir = NULL;
	  dir = (TDirectory*)gDirectory->GetListOfKeys()->At(iKey);
	  string dirName(dir->GetName());
	  if ((dir != NULL) && dir->IsFolder() && (dirName != "cnt_eff_plots") && 
	      (dirName != "fit_eff_plots")) {
	    Int_t binNumber0 = bin(binDirSubstring(dirName, 0));
	    Int_t binNumber1 = bin(binDirSubstring(dirName, 1));
	    stringstream name1;
	    name1 << "PhotonToID/" << *iEffVar << "/" << dir->GetName() << "/";

	    //get RooFitResult for parameters and their errors
	    RooFitResult* fitRes = NULL;
	    file->GetObject(plotAux_.name(name1.str(), "fitresults").c_str(), fitRes);

*/
	    //get RooWorkspace for binning
	    /*RooWorkspace* workspace = NULL;
	      file->GetObject(plotAux_.name(name1.str(), "w").c_str(), workspace);*/

//	    if /*(*/(fitRes != NULL)/* && (workspace != NULL))*/ {

	      //get bin low edge, high edge, and average value
	      /*const RooArgSet vars = workspace->allVars();
		RooRealVar* binRealAttributes = 
		(RooRealVar*)&vars[branchNames_[effVarIndex].c_str()];
		const Double_t binAvg = binRealAttributes->getVal();
		stringstream binName;
		binName << branchNames_[effVarIndex] << "_bins";
		RooBinning* binning = 
		(RooBinning*)&binRealAttributes->getBinning(binName.str().c_str());
		const Double_t binLowEdge = binning->binLow(iBin);
		const Double_t binHighEdge = binning->binHigh(iBin);*/

	      //loop over parameters in the RooFitResult
/*
	      RooArgList pars = fitRes->floatParsFinal();
	      for (VSTRING_IT iParName = parNames_.begin(); iParName != parNames_.end(); 
		   ++iParName) {
		const Int_t parIndex = pars.index((*iParName).c_str());
		if (parIndex == -1) {
		  cerr << "Error: in bin " << dirName << ", ";
		  cerr << "there is no parameter with name " << *iParName << ".\n";
		}
		else {

		  //fill RooDataSet
		  effVar_->setLabel((*iEffVar).c_str());
		  *binNumber0_ = binNumber0;
		  *binNumber1_ = binNumber1;
		  parName_->setLabel(pars[parIndex].GetName());
		  *parVal_ = ((RooRealVar&)pars[parIndex]).getVal();
		  parVal_->setAsymError(((RooRealVar&)pars[parIndex]).getErrorLo(), 
					((RooRealVar&)pars[parIndex]).getErrorHi());
		  parData_->add(RooArgSet(*effVar_, *binNumber0_, *binNumber1_, *parName_, 
					  *parVal_));

		}//else
*/

//	      }/*for (VSTRING_IT iParName = parNames_.begin(); iParName != parNames_.end(); 
//		 ++iParName)*/

/*
	    }//if ((fitRes != NULL) && (workspace != NULL))
	    else {
	      cout << "Error getting RooFitResult with name ";
	      cout << plotAux_.name(name1.str(), "fitresults") << ".\n";
*/
	      /*cout << "Error getting RooWorkspace with name ";
		cout << plotAux_.name(name1.str(), "w") << ".\n";*/

//	    }//else

//	  }/*if ((dir != NULL) && dir->IsFolder() && (string(dir->GetName()) != "cnt_eff_plots") 
//	     && (string(dir->GetName()) != "fit_eff_plots"))*/

/*
	}//for (int iKey = 0; iKey < gDirectory->GetNkeys(); ++iKey)

      }//if (effVarDirExists)
      else cerr << "Error cding to " << "PhotonToID/" << *iEffVar << ".\n";

    }//for (VSTRING_IT iEffVar = effVars_.begin(); iEffVar != effVars_.end(); ++iEffVar)
    file->Close();

  }//if (!fileErr)
  else cerr << "Error opening file " << inputFile_ << ".\n";
  delete file;
}
*/

//plot fit parameters vs. bin number, in each efficiency category
//N_effCats * N_pars total plots
/*
void FitterStudy::makePlots()
{
  //open output file
  TFile* file = NULL;
  bool fileErr = false;
  try { file = new TFile(outputFile_.c_str(), "RECREATE"); }
  catch (cms::Exception& ex) { fileErr = true; }
  if (!fileErr && (file != NULL)) {
    file->cd();

    //deal with one (efficiency variable, parameter, dim) bin at a time
    for (VSTRING_IT iEffVar = effVars_.begin(); iEffVar != effVars_.end(); ++iEffVar) {
      const unsigned int index = iEffVar - effVars_.begin();
      for (VSTRING_IT iParName = parNames_.begin(); iParName != parNames_.end(); ++iParName) {
	int i = 0;
	while (i != -1) {
	  stringstream cut;
	  cut << "(effVar == " << iEffVar - effVars_.begin() << ") && (parName == ";
	  cut << iParName - parNames_.begin() << ") && (binNumber";
	  cut << dimToBinBy_[index] << " == " << i << ")";
	  RooDataSet* parDataCut = (RooDataSet*)parData_->reduce(cut.str().c_str());

	  //create parameter vs. bin plots
	  if (parDataCut->numEntries() > 0) {
	    RooPlot* binFrame = NULL;
	    if (dimToBinBy_[index] == 0) binFrame = 
	      binNumber1_->frame(-0.5, parDataCut->numEntries() - 0.5, parDataCut->numEntries());
	    else binFrame = binNumber0_->frame(-0.5, parDataCut->numEntries() - 0.5, 
					       parDataCut->numEntries());
	    stringstream name;
	    string effVar = *iEffVar;
	    size_t underscorePos = effVar.find('_');
	    if (underscorePos != string::npos) effVar.replace(underscorePos, 1, 1, '-');
	    name << effVar << "_" << *iParName << "_" << i;
	    binFrame->SetName(name.str().c_str());
	    parDataCut->plotOnXY(binFrame, RooFit::YVar(*parVal_));
	    TCanvas canvas(name.str().c_str(), "", 600, 600);
	    //binFrame->Write();
	    canvas.cd();
	    binFrame->Draw();
	    canvas.Write();
	    ++i;
	  }
	  else {
	    cerr << "No data survived the cut \"" << cut.str() << "\".\n";
	    i = -1;

	  }//else

	}//while (i != -1)

      }//for (VSTRING_IT iParName = parNames_.begin(); iParName != parNames_.end(); ++iParName)

    }//for (VSTRING_IT iEffVar = effVars_.begin(); iEffVar != effVars_.end(); ++iEffVar)
    file->Write();
    file->Close();

  }//if (!fileErr && (file != NULL))
  else cerr << "Error opening file " << outputFile_ << ".\n";
  delete file;
}
*/

	  /*
string FitterStudy::binDirSubstring(const string& dirName, const unsigned int binNum) const
{
  int begPos = 0;
  int endPos = -2;
  unsigned int i = 0;
  while ((endPos != (int)string::npos) && (i != (binNum + 1))) {
    begPos = endPos + 2;
    endPos = dirName.find("__", begPos);
    ++i;
  }
  return dirName.substr(begPos, endPos + 2 - begPos);
}
*/

	     /*
Int_t FitterStudy::bin(const string& dirNameSubstring) const
{
  size_t begPos = dirNameSubstring.find("bin") + 3;
  size_t endPos = dirNameSubstring.find("__");
  Int_t theInt = 0;
  if ((begPos != string::npos) && (endPos != string::npos)) {
    string theString = dirNameSubstring.substr(begPos, endPos - begPos);
    stringstream theStream;
    theStream << theString;
    theStream >> theInt;
  }
  //cout << "dirNameSubstring = " << dirNameSubstring << ", theInt = " << theInt << endl;
  return theInt;
}
*/

		/*
void FitterStudy::addObservable()
{
  genVar_ = NULL;
  fitVar_ = NULL;
  if ((fitVarName_.size() >= 3) && (fitVarLimits_.size() >= 2) && (genVarName_.size() >= 3)) {
    fitVar_ = new RooRealVar(fitVarName_[0].c_str(), fitVarName_[1].c_str(), fitVarLimits_[0], 
			     fitVarLimits_[1], fitVarName_[2].c_str());
    genVar_ = new RooRealVar(genVarName_[0].c_str(), genVarName_[1].c_str(), genVarLimits_[0], 
			     genVarLimits_[1], genVarName_[2].c_str());

			     }*//*if ((fitVarName_.size() >= 3) && (fitVarLimits_.size() >= 2) && 
     (genVarName_.size() >= 3) && (genVarLimits_.size() >= 2))*/
  /*
  else {
    cout << "Error: fitVarName_.size() = " << fitVarName_.size() << ", fitVarLimits_.size() = ";
    cout << fitVarLimits_.size() << ", " << "genVarName_.size() = " << genVarName_.size() << ".\n";

  }//else
}
*/

//define this as a plug-in
DEFINE_FWK_MODULE(FitterStudy);
