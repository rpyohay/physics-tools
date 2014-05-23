#include <map>
#include <vector>
#include <iostream>
#include <fstream>

void recursiveVary(vector<vector<float> >& variations, vector<float>& variation, 
		   const vector<float>& nominal, unsigned int i, 
		   vector<unsigned int>& numPushbacks, int elementOfNumPushbacks, 
		   const vector<float> variations1Sigma)
{
  if (i < nominal.size()) {
    variation.push_back(nominal[i] + variations1Sigma[i]);
    ++numPushbacks[variation.size() - 1];
    recursiveVary(variations, variation, nominal, i + 1, numPushbacks, elementOfNumPushbacks, 
		  variations1Sigma);
    variation.push_back(nominal[i]);
    ++numPushbacks[variation.size() - 1];
    recursiveVary(variations, variation, nominal, i + 1, numPushbacks, elementOfNumPushbacks, 
		  variations1Sigma);
    variation.push_back(nominal[i] - variations1Sigma[i]);
    ++numPushbacks[variation.size() - 1];
    recursiveVary(variations, variation, nominal, i + 1, numPushbacks, elementOfNumPushbacks, 
		  variations1Sigma);
  }
  else {
    if (elementOfNumPushbacks == 3) variations.push_back(variation);
    if (elementOfNumPushbacks >= 0) {
      variation.pop_back();
      if ((numPushbacks[elementOfNumPushbacks] % 3) == 0) {
	recursiveVary(variations, variation, nominal, i, numPushbacks, elementOfNumPushbacks - 1, 
		      variations1Sigma);
      }
    }
  }
}

void generateSignalShapeVariations(vector<vector<float> >& variations, 
				   const vector<float>& nominal, 
				   const vector<float> variations1Sigma)
{
  //vector to hold a single variation
  vector<float> variation;

  //vector to hold the number of times each element of variation was filled
  vector<unsigned int> numPushbacks;
  for (unsigned int i = 0; i < nominal.size(); ++i) { numPushbacks.push_back(0); }

  //generate the variations recursively (3 variations ^ # of signal parameters * 2)
  recursiveVary(variations, variation, nominal, 0, numPushbacks, 3, variations1Sigma);
}

void systematics()
{
  /*vectors of nominal signal shape parameters and their names, background shapes, and 1 sigma 
    variations on signal shape parameters*/
  vector<float> nominal;
  nominal.push_back(1.4);
  nominal.push_back(138.6);
  nominal.push_back(1.4);
  nominal.push_back(138.6);
  vector<float> variations1Sigma;
  variations1Sigma.push_back(0.6);
  variations1Sigma.push_back(2.0);
  variations1Sigma.push_back(0.6);
  variations1Sigma.push_back(2.0);
  vector<string> sigPars;
  sigPars.push_back("alphaPass");
  sigPars.push_back("nPass");
  sigPars.push_back("alphaFail");
  sigPars.push_back("nFail");
  vector<string> bkgShapes;
  bkgShapes.push_back("RooCMSShape");
  bkgShapes.push_back("polynomial");
  bkgShapes.push_back("exponential");
  bkgShapes.push_back("powerLaw");

  //generate the signal shape variations
  vector<vector<float> > signalVariations;
  generateSignalShapeVariations(signalVariations, nominal, variations1Sigma);

  //open a text file to save a list of the variations
  ofstream out("model_variations_1Sigma.txt");
  if (!out.is_open()) {
    cerr << "Error opening file model_variations_1Sigma.txt.\n";
    return;
  }

  //print the variation names to the file (commented out by #)
  out << "#";
  for (vector<string>::const_iterator iPar = sigPars.begin(); iPar != sigPars.end(); ++iPar) {
    out << *iPar << " ";
  }
  out << "bkgShape\n";

  //print the variations
  for (vector<string>::const_iterator iShape = bkgShapes.begin(); iShape != bkgShapes.end(); 
       ++iShape) {
    for (vector<vector<float> >::const_iterator iVariation = signalVariations.begin(); 
	 iVariation != signalVariations.end(); ++iVariation) {
      for (vector<float>::const_iterator iNum = iVariation->begin(); iNum != iVariation->end(); 
	   ++iNum) { out << *iNum << " "; }
      out << *iShape << endl;
    }
  }

  //exit
  out.close();
}
