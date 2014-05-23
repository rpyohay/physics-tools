#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include "TFile.h"
#include "RooFitResult.h"
#include "RooRealVar.h"

//input parameters
const string systematicsFile = "model_variations_1Sigma.txt";
const string efficiency = "PhotonToIDEB";
const string version = "2";
const string outputFile = "MC_efficiency_variations_1Sigma.txt";
const string directory = "eff_MC";

void dumpSystematics()
{
  //open systematics file
  ifstream systematics(systematicsFile.c_str());
  if (!systematics.is_open()) {
    cerr << "Error opening file " << systematicsFile << ".\n";
    return;
  }

  //vectors to hold the parameters, the efficiency, and its error
  vector<float> alphaPass;
  vector<float> nPass;
  vector<float> alphaFail;
  vector<float> nFail;
  vector<string> bkgShape;
  vector<float> eff;
  vector<float> errHigh;
  vector<float> errLow;
  vector<float> err;

  //loop over listed shape variations
  unsigned int lineNum = 0;
  bool breakCondition = false;
  while (!systematics.eof() && !breakCondition) {

    //check each line of the file to see if it is a comment
    string line;
    getline(systematics, line);
    ++lineNum;
    cout << lineNum << endl;
    if ((line.find('#') == string::npos) && (line.length() != 0)) {

      //if not a comment, get the signal and background variations stored in the line
      vector<float> sigPars;
      string bkgPar;
      size_t beginPos = 0;
      size_t endPos = line.find(' ');
      bool foundString = false;
      while (!foundString) {
	string par(line.substr(beginPos, endPos - beginPos));
	string::const_iterator iChar = par.begin();
	bool foundAlpha = false;
	while ((iChar != par.end()) && !foundAlpha) {
	  if (isalpha(*iChar) != 0) foundAlpha = true;
	  ++iChar;
	}
	if (foundAlpha) {
	  foundString = true;
	  bkgPar = par;
	}
	else sigPars.push_back((float)atof(par.c_str()));
	beginPos = endPos + 1;
	endPos = line.find(' ', beginPos);
      }

      /*form the name of the corresponding ROOT efficiency file from the signal and background 
	variations given in the line*/
      //efficiency_PhotonToIDEB_alphaPass21_nPass2079_alphaFail21_nFail2079_bkgpowerLaw_v1.root
      stringstream ROOTFileName;
      ROOTFileName << "/data2/yohay/" << directory << "/shape_model_systematic/efficiency_";
      ROOTFileName << efficiency << "_alphaPass";
      for (vector<float>::const_iterator iSigPar = sigPars.begin(); iSigPar != sigPars.end(); 
	   ++iSigPar) {
	const unsigned int index = iSigPar - sigPars.begin();
	switch (index) {
	case 0:
	  ROOTFileName << *iSigPar << "_nPass";
	  break;
	case 1:
	  ROOTFileName << *iSigPar << "_alphaFail";
	  break;
	case 2:
	  ROOTFileName << *iSigPar << "_nFail";
	  break;
	case 3:
	  ROOTFileName << *iSigPar << "_bkg" << bkgPar << "_v" << version << ".root";
	  break;
	default:
	  cerr << "Error reading file " << systematicsFile << " at line " << lineNum << ".\n";
	  breakCondition = true;
	  break;
	}
      }
      if (!breakCondition) {
	string efficiencyFile(ROOTFileName.str());
	endPos = efficiencyFile.find('.');
	while (endPos != (efficiencyFile.size() - 5)) {
	  efficiencyFile.erase(endPos, 1);
	  endPos = efficiencyFile.find('.');
	}

	//open the ROOT efficiency file
	bool skipCondition = false;
	TFile ROOTFile(efficiencyFile.c_str());
	if (!ROOTFile.IsOpen()) {
	  cerr << "Error opening file " << efficiencyFile << ".\n";
	  skipCondition = true;
	}

	//get the value of the efficiency and its error
	if (!skipCondition) {
	  RooFitResult* fitResult = NULL;
	  string fitResultName = efficiency + 
	    "/unbinned/probe_eta_bin0__probe_nJets05_bin0__gaussPlusLinear/fitresults";
	  ROOTFile.GetObject(fitResultName.c_str(), fitResult);
	  if (fitResult != NULL) {
	    alphaPass.push_back(sigPars[0]);
	    nPass.push_back(sigPars[1]);
	    alphaFail.push_back(sigPars[2]);
	    nFail.push_back(sigPars[3]);
	    bkgShape.push_back(bkgPar);
	    RooRealVar* theEfficiency = 
	      (RooRealVar*)fitResult->floatParsFinal().find("efficiency");
	    eff.push_back((float)theEfficiency->getVal());
	    Double_t theErrHigh = theEfficiency->getAsymErrorHi();
	    Double_t theErrLow = theEfficiency->getAsymErrorLo();
	    errHigh.push_back(theErrHigh);
	    errLow.push_back(theErrLow);

	    /*if the low and high errors agree to the desired precision, save the error at that 
	      precision for Gaussian error propagation later*/
	    unsigned int power = 0;
	    float absErrLow = fabs(theErrLow);
	    float absErrHigh = fabs(theErrHigh);
	    if ((fitResult->minNll() < -2000000.0) || (absErrLow == 0.0) || (absErrHigh == 0.0)) {
	      err.push_back(-1.0);
	    }
	    else {
	      while ((absErrLow < 1.0) && (absErrHigh < 1.0)) {
		absErrLow*=10.0;
		absErrHigh*=10.0;
		++power;
	      }
	      if ((ceil(absErrLow) > 1.0) && (ceil(absErrHigh) > 1.0)) {
		float diffHigh = ceil(absErrHigh) - absErrHigh;
		float diffLow = ceil(absErrLow) - absErrLow;
		float roundedHigh, roundedLow;
		if (diffHigh <= 0.5) roundedHigh = ceil(absErrHigh);
		else roundedHigh = floor(absErrHigh);
		if (diffLow <= 0.5) roundedLow = ceil(absErrLow);
		else roundedLow = floor(absErrLow);
		if (roundedHigh == roundedLow) {
		  float theErr = roundedHigh;
		  for (unsigned int iPower = 0; iPower < power; ++iPower) { theErr/=10; }
		  err.push_back(theErr);
		}
		else err.push_back(-1.0);
	      }
	      else err.push_back(-1.0);
	    }
	  }
	  else {
	    cerr << "Error getting RooFitResult object " << efficiency;
	    cerr << "/unbinned/probe_eta_bin0__probe_nJets05_bin0__gaussPlusLinear/fitresults ";
	    cerr << "from file efficiencyFile.\n";
	  }
	  ROOTFile.Close();
	}
      }
    }
  }

  //close file
  systematics.close();

  //open file for dumping parameters, efficiencies, and errors
  ofstream out(outputFile.c_str());
  if (!out.is_open()) {
    cerr << "Error opening file " << outputFile << ".\n";
    return;
  }
  out << "#alphaPass nPass alphaFail nFail bkgShape efficiency errorHigh errorLow error\n";
  for (vector<float>::const_iterator iVariation = alphaPass.begin(); 
       iVariation != alphaPass.end(); ++iVariation) {
    const unsigned int index = iVariation - alphaPass.begin();
    out << *iVariation << " " << nPass[index] << " " << alphaFail[index] << " " << nFail[index];
    out << " " << bkgShape[index] << " " << eff[index] << " " << errHigh[index] << " ";
    out << errLow[index] << " " << err[index] << endl;
  }
  out.close();
}
