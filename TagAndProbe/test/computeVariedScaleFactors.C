#include <string>
#include <fstream>
#include <algorithm>
#include <iostream>

void readLine(vector<float>& floatPars, string& bkgPar, const string& line)
{
  size_t beginPos = 0;
  size_t endPos = line.find(' ');
  bool end = false;
  while (!end) {
    string par(line.substr(beginPos, endPos - beginPos));
    string::const_iterator iChar = par.begin();
    bool foundAlpha = false;
    while ((iChar != par.end()) && !foundAlpha) {
      if (isalpha(*iChar) != 0) foundAlpha = true;
      ++iChar;
    }
    if (foundAlpha) bkgPar = par;
    else floatPars.push_back((float)atof(par.c_str()));
    if (endPos == string::npos) end = true;
    beginPos = endPos + 1;
    endPos = line.find(' ', beginPos);
  }  
}

void computeVariedScaleFactors(const string& dataEfficienciesFileName, 
			       const string& MCEfficienciesFileName, const string& outputFile, 
			       const unsigned int numSigPars, const float nominalScaleFactor)
{
  //open data and MC efficiency text files
  ifstream dataEfficienciesFile(dataEfficienciesFileName.c_str());
  ifstream MCEfficienciesFile(MCEfficienciesFileName.c_str());
  if (!dataEfficienciesFile.is_open() || !MCEfficienciesFile.is_open()) {
    cerr << "Error opening file " << dataEfficienciesFileName << " and/or ";
    cerr << MCEfficienciesFileName << ".\n";
    return;
  }

  //quantities to be calculated and printed
  vector<float> scaleFactor;
  vector<float> error;
  vector<float> deviationFromNominal;

  //quantities to be read and re-printed
  vector<float> alphaPass;
  vector<float> nPass;
  vector<float> alphaFail;
  vector<float> nFail;
  vector<string> bkgShape;
  vector<float> dataEfficiency;
  vector<float> dataEfficiencyErrorHigh;
  vector<float> dataEfficiencyErrorLow;
  vector<float> dataEfficiencyError;
  vector<float> MCEfficiency;
  vector<float> MCEfficiencyErrorHigh;
  vector<float> MCEfficiencyErrorLow;
  vector<float> MCEfficiencyError;

  //read each file
  unsigned int lineNum = 0;
  unsigned int dataFail = 0;
  unsigned int MCFail = 0;
  while (!dataEfficienciesFile.eof() && !MCEfficienciesFile.eof()) {

    //check each line of the file to see if it is a comment
    string dataLine, MCLine;
    getline(dataEfficienciesFile, dataLine);
    getline(MCEfficienciesFile, MCLine);
    ++lineNum;
    if ((dataLine.find('#') == string::npos) && (dataLine.length() != 0) && 
	(MCLine.find('#') == string::npos) && (MCLine.length() != 0)) {

      /*grab all words  and check that signal and background shape parameters are equal for data 
	and MC*/
      vector<float> dataFloatPars, MCFloatPars;
      string dataBkgPar, MCBkgPar;
      readLine(dataFloatPars, dataBkgPar, dataLine);
      readLine(MCFloatPars, MCBkgPar, MCLine);
      if ((dataFloatPars.size() == MCFloatPars.size()) && (dataBkgPar == MCBkgPar)) {
	bool equal = true;
	unsigned int iFloatPar = 0;
	while ((iFloatPar < numSigPars) && equal) {
	  equal = equal && (dataFloatPars[iFloatPar] == MCFloatPars[iFloatPar]);
	  ++iFloatPar;
	}
	if (equal) {

	  /*if the error isn't -1, compute the scale factor, error, and deviation of scale factor 
	    from nominal*/
	  if (dataFloatPars[dataFloatPars.size() - 1] != -1.0) ++dataFail;
	  if (MCFloatPars[MCFloatPars.size() - 1] != -1.0) ++MCFail;
	  if ((dataFloatPars[dataFloatPars.size() - 1] != -1.0) && 
	      (MCFloatPars[MCFloatPars.size() - 1] != -1.0)) {
	    const unsigned int efficiencyIndex = numSigPars;
	    const unsigned int errorIndex = dataFloatPars.size() - 1;
	    scaleFactor.push_back(dataFloatPars[efficiencyIndex]/MCFloatPars[efficiencyIndex]);
	    error.push_back(scaleFactor[scaleFactor.size() - 1]*
			    sqrt(((dataFloatPars[errorIndex]*dataFloatPars[errorIndex])/
				  (dataFloatPars[efficiencyIndex]*dataFloatPars[efficiencyIndex])) 
				 + ((MCFloatPars[errorIndex]*MCFloatPars[errorIndex])/
				    (MCFloatPars[efficiencyIndex]*MCFloatPars[efficiencyIndex]))));
	    deviationFromNominal.push_back(scaleFactor[scaleFactor.size() - 1] - 
					   nominalScaleFactor);

	    //save other information
	    alphaPass.push_back(dataFloatPars[0]);
	    nPass.push_back(dataFloatPars[1]);
	    alphaFail.push_back(dataFloatPars[2]);
	    nFail.push_back(dataFloatPars[3]);
	    bkgShape.push_back(dataBkgPar);
	    dataEfficiency.push_back(dataFloatPars[4]);
	    dataEfficiencyErrorHigh.push_back(dataFloatPars[5]);
	    dataEfficiencyErrorLow.push_back(dataFloatPars[6]);
	    dataEfficiencyError.push_back(dataFloatPars[7]);
	    MCEfficiency.push_back(MCFloatPars[4]);
	    MCEfficiencyErrorHigh.push_back(MCFloatPars[5]);
	    MCEfficiencyErrorLow.push_back(MCFloatPars[6]);
	    MCEfficiencyError.push_back(MCFloatPars[7]);
	  }
	}
      }
      else {
	cerr << "Error processing " << dataEfficienciesFileName << " and ";
	cerr << MCEfficienciesFileName << " at line " << lineNum << ".\n";
      }
    }
  }

  //close files
  dataEfficienciesFile.close();
  MCEfficienciesFile.close();

  //open file for dumping scale factors, errors, and deviations from nominal
  ofstream out(outputFile.c_str());
  if (!out.is_open()) {
    cerr << "Error opening file " << outputFile << ".\n";
    return;
  }
  out << "#alphaPass nPass alphaFail nFail bkgShape dataEfficiency dataEfficiencyErrorHigh ";
  out << "dataEfficiencyErrorLow dataEfficiencyError MCEfficiency MCEfficiencyErrorHigh ";
  out << "MCEfficiencyErrorLow MCEfficiencyError scaleFactor scaleFactorError ";
  out << "scaleFactorDeviationFromNominal\n";
  vector<float> deviationFromNominalCopy;
  deviationFromNominalCopy.resize(deviationFromNominal.size());
  copy(deviationFromNominal.begin(), deviationFromNominal.end(), deviationFromNominalCopy.begin());
  sort(deviationFromNominal.begin(), deviationFromNominal.end());
  for (vector<float>::const_iterator iDeviation = deviationFromNominal.begin(); 
       iDeviation != deviationFromNominal.end(); ++iDeviation) {
    vector<float>::const_iterator p = 
      find(deviationFromNominalCopy.begin(), deviationFromNominalCopy.end(), *iDeviation);
    const unsigned int index = p - deviationFromNominalCopy.begin();
    out << alphaPass[index] << " " << nPass[index] << " " << alphaFail[index] << " ";
    out << nFail[index] << " " << bkgShape[index] << " " << dataEfficiency[index] << " ";
    out << dataEfficiencyErrorHigh[index] << " " << dataEfficiencyErrorLow[index] << " ";
    out << dataEfficiencyError[index] << " " << MCEfficiency[index] << " ";
    out << MCEfficiencyErrorHigh[index] << " " << MCEfficiencyErrorLow[index] << " ";
    out << MCEfficiencyError[index] << " " << scaleFactor[index] << " " << error[index] << " ";
    out << *iDeviation << endl;
  }
  out.close();
}
