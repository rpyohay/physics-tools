#include <iostream>
#include "TFile.h"
#include "RooFitResult.h"
#include "RooRealVar.h"
#include "RooPlot.h"
#include "RooHist.h"
#include "RooWorkspace.h"
#include "RooAbsPdf.h"
#include "TCanvas.h"

//const string efficiencyFile = "/data2/yohay/analysis_golden_JSON_24052011_defaultPU_01072011_Photon-Run2011A-DoublePhoton-May10ReReco-v1/efficiency_data_PhotonToIDEB_v2.root";
const string efficiencyFile = "/data2/yohay/eff_MC/efficiency_PhotonToIDEB_v2.root";

void estimateSignalFitPerformance()
{
  //open the ROOT efficiency file
  TFile ROOTFile(efficiencyFile.c_str());
  if (!ROOTFile.IsOpen()) {
    cerr << "Error opening file " << efficiencyFile << ".\n";
    return;
  }

  //get numBackgroundFail, numBackgroundPass, numSignalAll, and efficiency
  RooFitResult* fitResult = NULL;
  ROOTFile.GetObject("PhotonToIDEB/unbinned/probe_eta_bin0__probe_nJets05_bin0__gaussPlusLinear/fitresults", fitResult);
  Double_t efficiency = 0.0;
  Double_t efficiencyError = 0.0;
  Double_t numBackgroundFail = 0.0;
  Double_t numBackgroundFailError = 0.0;
  Double_t numBackgroundPass = 0.0;
  Double_t numBackgroundPassError = 0.0;
  Double_t numSignalAll = 0.0;
  Double_t numSignalAllError = 0.0;
  if (fitResult != NULL) {
    RooRealVar* theEfficiency = (RooRealVar*)fitResult->floatParsFinal().find("efficiency");
    efficiency = theEfficiency->getVal();
    efficiencyError = theEfficiency->getError();
    RooRealVar* theNumBackgroundFail = (RooRealVar*)fitResult->floatParsFinal().find("numBackgroundFail");
    numBackgroundFail = theNumBackgroundFail->getVal();
    numBackgroundFailError = theNumBackgroundFail->getError();
    RooRealVar* theNumBackgroundPass = (RooRealVar*)fitResult->floatParsFinal().find("numBackgroundPass");
    numBackgroundPass = theNumBackgroundPass->getVal();
    numBackgroundPassError = theNumBackgroundPass->getError();
    RooRealVar* theNumSignalAll = (RooRealVar*)fitResult->floatParsFinal().find("numSignalAll");
    numSignalAll = theNumSignalAll->getVal();
    numSignalAllError = theNumSignalAll->getError();
  }
  else {
    cerr << "Error getting RooFitResult PhotonToIDEB/unbinned/probe_eta_bin0__probe_nJets05_bin0__gaussPlusLinear/fitresults from file ";
    cerr << efficiencyFile << ".\n";
  }

  //get integrals of tag-pass and tag-fail distributions
  TCanvas* fitCanvas = NULL;
  ROOTFile.GetObject("PhotonToIDEB/unbinned/probe_eta_bin0__probe_nJets05_bin0__gaussPlusLinear/fit_canvas", fitCanvas);
  Double_t tagPassIntegral = 0;
  Double_t tagFailIntegral = 0;
  if (fitCanvas != NULL) {
    fitCanvas->cd(1);
    RooHist* tagPassDistribution = NULL;
    tagPassDistribution = (RooHist*)((TCanvas*)fitCanvas->GetPrimitive("fit_canvas_1"))->GetPrimitive("h_data");
    fitCanvas->cd(2);
    RooHist* tagFailDistribution = NULL;
    tagFailDistribution = (RooHist*)((TCanvas*)fitCanvas->GetPrimitive("fit_canvas_2"))->GetPrimitive("h_data");
    RooHist* blah = NULL;
    blah = (RooHist*)((TCanvas*)fitCanvas->GetPrimitive("fit_canvas_3"))->GetPrimitive("h_data");
    cerr << blah->Integral() << endl;
    if ((tagPassDistribution != NULL) && (tagFailDistribution != NULL)) {
      tagPassIntegral = tagPassDistribution->Integral()*/*1.796*/1.844;
      tagFailIntegral = tagFailDistribution->Integral()*/*1.796*/1.844;
    }
    else cerr << "Error: could not get RooPlots.\n";
  }
  else {
    cerr << "Error getting TCanvas PhotonToIDEB/unbinned/probe_eta_bin0__probe_nJets05_bin0__gaussPlusLinear/fit_canvas from file ";
    cerr << efficiencyFile << ".\n";
  }

  //close file
  ROOTFile.Close();

  //subtract fitted background from integral
  Double_t tagPassNumBkgSubtractedEvts = tagPassIntegral - numBackgroundPass;
  Double_t tagPassNumBkgSubtractedEvtsError = numBackgroundPassError;
  Double_t tagFailNumBkgSubtractedEvts = tagFailIntegral - numBackgroundFail;
  Double_t tagFailNumBkgSubtractedEvtsError = numBackgroundFailError;

  //calculate fitted signal
  Double_t tagPassNumFittedSignal = efficiency*numSignalAll;
  Double_t tagPassNumFittedSignalError = tagPassNumFittedSignal*sqrt(((efficiencyError*efficiencyError)/(efficiency*efficiency)) + 
								     ((numSignalAllError*numSignalAllError)/(numSignalAll*numSignalAll)));
  Double_t tagFailNumFittedSignal = (1.0 - efficiency)*numSignalAll;
  Double_t tagFailNumFittedSignalError = tagFailNumFittedSignal*
    sqrt(((efficiencyError*efficiencyError)/((1.0 - efficiency)*(1.0 - efficiency))) + 
	 ((numSignalAllError*numSignalAllError)/(numSignalAll*numSignalAll)));

  //calculate difference between signal fit result and background subtracted integral
  Double_t tagPassDifference = tagPassNumBkgSubtractedEvts - tagPassNumFittedSignal;
  Double_t tagPassDifferenceError = sqrt(tagPassNumBkgSubtractedEvtsError*tagPassNumBkgSubtractedEvtsError + 
					 tagPassNumFittedSignalError*tagPassNumFittedSignalError);
  Double_t tagFailDifference = tagFailNumBkgSubtractedEvts - tagFailNumFittedSignal;
  Double_t tagFailDifferenceError = sqrt(tagFailNumBkgSubtractedEvtsError*tagFailNumBkgSubtractedEvtsError + 
					 tagFailNumFittedSignalError*tagFailNumFittedSignalError);

  //compare signal fit result to background subtracted integral
  cout << "Tag pass signal fit: " << tagPassNumFittedSignal << " +/- " << tagPassNumFittedSignalError << endl;
  cout << "Tag pass background subtracted integral: " <<  tagPassNumBkgSubtractedEvts << " +/- " << tagPassNumBkgSubtractedEvtsError;
  cout << endl;
  cout << "Difference: " << tagPassDifference << " +/- " << tagPassDifferenceError << endl;
  cout << "Tag fail signal fit: " << tagFailNumFittedSignal << " +/- " << tagFailNumFittedSignalError << endl;
  cout << "Tag fail background subtracted integral: " <<  tagFailNumBkgSubtractedEvts << " +/- " << tagFailNumBkgSubtractedEvtsError;
  cout << endl;
  cout << "Difference: " << tagFailDifference << " +/- " << tagFailDifferenceError << endl;
}
