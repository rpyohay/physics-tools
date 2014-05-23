#include <vector>
#include <iostream>
#include <sstream>
#include "RooFitResult.h"
#include "TFile.h"
#include "TH1D.h"

//extract one fitted parameter and its asymmetric error from one fit
vector<Double_t> getParAndErr(RooArgList* pars, const Int_t parIndex)
{
  vector<Double_t> parAndErr(3, 0.0);
  if ((parIndex < pars->getSize()) && (parIndex >= 0)) {
    parAndErr[0] = ((RooRealVar*)(pars->at(parIndex)))->getVal();
    parAndErr[1] = ((RooRealVar*)(pars->at(parIndex)))->getAsymErrorLo();
    parAndErr[2] = ((RooRealVar*)(pars->at(parIndex)))->getAsymErrorHi();
  }
  return parAndErr;
}

//fill the fit parameter distributions with the results from one fit
void fillParHists(RooFitResult* res, vector<TH1D*> parHists, vector<TH1D*> errLoHists, 
		  vector<TH1D*> errHiHists)
{
  const RooArgList& pars = res->floatParsFinal();
  if (parHists.size() != pars->getSize()) {
    cerr << "Error: parHists.size() = " << parHists.size() << ", pars->getSize() = ";
    cerr << pars->getSize() << ".\n";
    return;
  }
  for (Int_t iPar = 0; iPar < pars->getSize(); ++iPar) {
    vector<Double_t> parAndErr = getParAndErr(pars, iPar);
    parHists[iPar]->Fill(parAndErr[0]);
    errLoHists[iPar]->Fill(parAndErr[1]);
    errHiHists[iPar]->Fill(parAndErr[2]);
  }
}

//analyze the distributions of fitted parameters
void analyze(const string& inputFile, const string& outputFile)
{
  //open input efficiency file
  TFile* in = new TFile(inputFile.c_str());
  if (!in->IsOpen()) {
    cerr << "Error opening file " << inputFile << ".\n";
    return;
  }

  //define fitted parameters
  vector<string> pars;
  pars.push_back("mean");
  pars.push_back("sigma");
  pars.push_back("alpha");
  pars.push_back("n");
  pars.push_back("sigma_2");
  pars.push_back("frac");
  pars.push_back("cPass");
  pars.push_back("cFail");

  //define histogram limits for the distributions of fitted parameters
  vector<Double_t> lowEdges;
  lowEdges.push_back(-1.0);
  lowEdges.push_back(1.0);
  lowEdges.push_back(1.0);
  lowEdges.push_back(0.0);
  lowEdges.push_back(1.0);
  lowEdges.push_back(0.2);
  lowEdges.push_back(-1.0);
  lowEdges.push_back(-1.0);
  vector<Double_t> highEdges;
  highEdges.push_back(1.0);
  highEdges.push_back(3.0);
  highEdges.push_back(3.0);
  highEdges.push_back(1.0);
  highEdges.push_back(3.0);
  highEdges.push_back(0.8);
  highEdges.push_back(1.0);
  highEdges.push_back(1.0);

  //book histograms
  vector<TH1D*> parHists;
  vector<TH1D*> errLoHists;
  vector<TH1D*> errHiHists;
  for (vector<string>::const_iterator iPar = pars.begin(); iPar != pars.end(); ++iPar) {
    const unsigned int parIndex = iPar - pars.begin();
    stringstream name;
    name << *iPar << "_val";
    parHists.push_back(new TH1D(name.str().c_str(), "", 4, lowEdges[parIndex], 
				highEdges[parIndex]));
    name.str("");
    name << *iPar << "_errLo";
    errLoHists.push_back(new TH1D(name.str().c_str(), "", 4, lowEdges[parIndex], 
				  highEdges[parIndex]));
    name.str("");
    name << *iPar << "_errHi";
    errHiHists.push_back(new TH1D(name.str().c_str(), "", 4, lowEdges[parIndex], 
				  highEdges[parIndex]));
  }

  //define efficiency categories
  vector<string> categories;
  categories.push_back("pt");
  categories.push_back("eta");
  categories.push_back("dRJets09");
  categories.push_back("nJets09");
  categories.push_back("nPV");
  vector<string> probeVars;
  probeVars.push_back("probe_et");
  probeVars.push_back("probe_eta");
  probeVars.push_back("probe_dRjet09");
  probeVars.push_back("probe_nJets09");
  probeVars.push_back("event_nPV");

  //loop over efficiency categories and their bins
  for (vector<string>::const_iterator iCategory = categories.begin(); 
       iCategory != categories.end(); ++iCategory) {
    stringstream dirName;
    dirName << "PhotonToID/" << *iCategory;
    in->cd(dirName.str().c_str());
    bool lastBin = false;
    unsigned int iBin = 0;
    while (!lastBin) {

      //get the fit result and fill the histograms
      stringstream name;
      name << probeVars[iCategory - categories.begin()] << "_bin" << iBin << "__gaussPlusLinear";
      TDirectory* binDir = NULL;
      binDir = (TDirectory*)(in->FindObjectAny(name.str().c_str()));
      if (binDir != NULL) {
	RooFitResult* res = NULL;
	stringstream resName;
	resName << dirName.str() << "/" << name.str() << "fitresult";
	in->GetObject(resName.str().c_str(), res);
	if (res != NULL) fillParHists(res, parHists, errLoHists, errHiHists);
	else {
	  cerr << "Error getting RooFitResult object " << resName.str() << " from file ";
	  cerr << inputFile << ".\n";
	}
      }
      else {
	cerr << "No bin " << iBin << ".\n";
	lastBin = true;
      }
      ++iBin;
    }
    in->cd(inputFile.c_str());
  }

  //write to output file
  TFile* out = new TFile(outputFile.c_str(), "RECREATE");
  if (out->IsOpen()) {
    out->cd();
    for (vector<TH1D*>::iterator iParHist = parHists.begin(); iParHist != parHists.end(); 
	 ++iParHist) { (*iParHist)->Write(); }
    for (vector<TH1D*>::iterator iErrLoHist = errLoHists.begin(); iErrLoHist != errLoHists.end(); 
	 ++iErrLoHist) { (*iErrLoHist)->Write(); }
    for (vector<TH1D*>::iterator iErrHiHist = errHiHists.begin(); iErrHiHist != errHiHists.end(); 
	 ++iErrHiHist) { (*iErrHiHist)->Write(); }
    out->Write();
    out->Close();
  }
  else cerr << "Error opening file " << outputFile << ".\n";
  delete out;

  //clean up
  for (vector<TH1D*>::iterator iParHist = parHists.begin(); iParHist != parHists.end(); 
       ++iParHist) { delete *iParHist; }
  for (vector<TH1D*>::iterator iErrLoHist = errLoHists.begin(); iErrLoHist != errLoHists.end(); 
       ++iErrLoHist) { delete *iErrLoHist; }
  for (vector<TH1D*>::iterator iErrHiHist = errHiHists.begin(); iErrHiHist != errHiHists.end(); 
       ++iErrHiHist) { delete *iErrHiHist; }
  in->Close();
  delete in;
}
