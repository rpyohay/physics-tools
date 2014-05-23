#include <map>
#include <iostream>
#include <sstream>
#include "TFile.h"
#include "TTree.h"
#include "FitterTree.h"
#include "MCUnbiasTree.h"
#include "PUCorrectedFitterTree.h"
#include "PUCorrectedMCUnbiasTree.h"
#include "Data.h"
#include "MC.h"

//run makeClass for all trees supplied
void makeClasses(const std::string& input, const std::string& dir, 
		 const std::vector<std::string>& trees)
{
  TFile file(input.c_str());
  if (file.IsOpen()) {
    for (std::vector<std::string>::const_iterator iTree = trees.begin(); iTree != trees.end(); 
	 ++iTree) {
      TTree* tree = NULL;
      std::stringstream name;
      name << dir << "/" << *iTree;
      file.GetObject(name.str().c_str(), tree);
      if (tree != NULL) {
	tree->MakeClass(name.str().replace(name.str().find('/'), 1, "_").c_str());
      }
      else std::cerr << "Error getting TTree " << name.str() << " from file " << input << ".\n";
    }
  }
  else std::cerr << "Error opening file " << input << ".\n";
}

/*return the real weight (if the weight saved in the ntuple is no longer valid due to CRAB 
  processing failures)*/
float weight(const std::string& fileName)
{
  float realWeight = -1.0;
  if (fileName.find("G_Pt-15to30") != std::string::npos) realWeight = 17.1485627180042;
  else if (fileName.find("G_Pt-30to50") != std::string::npos) realWeight = 1.70348517425871;
  else if (fileName.find("G_Pt-50to80") != std::string::npos) {
    realWeight = 0.272440177855987;
  }
  else if (fileName.find("G_Pt-80to120") != std::string::npos) realWeight = 0.0449947375874417;
  else if (fileName.find("G_Pt-120to170") != std::string::npos) realWeight = 0.0151495480748199;
  else if (fileName.find("G_Pt-170to300") != std::string::npos) realWeight = 0.00224989642102304;
  else if (fileName.find("G_Pt-300to470") != std::string::npos) realWeight = 0.000146354146604522;
  else if (fileName.find("G_Pt-470to800") != std::string::npos) realWeight = 0.0000129014206510886;
  else if (fileName.find("G_Pt-800to1400") != std::string::npos) realWeight = 0.70992; //incorrect
  else if (fileName.find("G_Pt-1400to1800") != std::string::npos) {
    realWeight = 0.00000000117862212031881;
  }
  else if (fileName.find("G_Pt-1800") != std::string::npos) realWeight = 2.75334E-11;
  else if (fileName.find("QCD_Pt-1400to1800") != std::string::npos) {
    realWeight = 0.00000132231208372978;
  }
  else if (fileName.find("DYToTauTau") != std::string::npos) realWeight = 0.14877679889775;
  else if (fileName.find("WToTauNu") != std::string::npos) realWeight = 0.312892427184466;
  return realWeight;
}

template<typename T>
void addTotalWeight(const std::string& fileName, TFile& out, const std::string& dir)
{
  //set up tree reader
  T treeReader(fileName, dir);
  out.cd();
  out.mkdir(dir.c_str());
  out.cd(dir.c_str());

  //add total weight = lumi weight * PU weight
  TTree* tree = treeReader.fChain->CloneTree(0);
  Float_t newWeight = -1.0;
  Float_t totalWeight;
  if (fileName.find("WJetsToLNu_17-8") != string::npos) newWeight = 1.602983169;
  tree->Branch("totalWeight", &totalWeight, "totalWeight/F");
  treeReader.Loop(tree, totalWeight, newWeight);
  tree->Write();

  //write
  out.Write();
}

//save a new tree with new additional variables
template<typename T, typename U>
void addVariables(const std::string& fileName, TFile& out, const std::string& dir)
{
  //flags to set
//   float realWeight = weight(fileName);
  float realWeight = -1.0;
  bool isOldTree = (fileName.find("_G_") != std::string::npos) || 
    (fileName.find("_ZJetToEE_") != std::string::npos);
  bool isPUSubtracted = dir.find("PU") != std::string::npos;
  bool isData = fileName.find("JSON") != std::string::npos;
  bool isReallyOld = false;

  //set up tree readers
  T fitterTreeReader(fileName, dir);
  U* MCUnbiasTreeReader = NULL;
  if (!isData) MCUnbiasTreeReader = new U(fileName, dir);
  out.cd();
  out.mkdir(dir.c_str());
  out.cd(dir.c_str());

  //fitter tree
  TTree* fitterTree = fitterTreeReader.fChain->CloneTree(0);
  Float_t fitterTreeTotalWeight;
  Float_t fitterTreeSCEta;
  Int_t fitterTreeProbePassingRhoSigmaIetaIetaEB;
  Int_t fitterTreeProbePassingNPVSigmaIetaIetaEB;
  Float_t fitterTreeDRTagProbe;
  std::string fitterBranchNameRho = "probe_passing_sigmaIetaIeta_EB";
  if (isPUSubtracted) {
    fitterBranchNameRho = "probe_passing_rho_sigmaIetaIeta_EB";
    fitterTreeProbePassingNPVSigmaIetaIetaEB = -1;
  }
  const std::string fitterBranchNameNPV = "probe_passing_nPV_sigmaIetaIeta_EB";
  if (!isData) fitterTree->Branch("totalWeight", &fitterTreeTotalWeight, "totalWeight/F");
  if (isReallyOld && isOldTree) {
    fitterTree->Branch("probe_SC_eta", &fitterTreeSCEta, "probe_SC_eta/F");
  }
  if (isReallyOld) {
    fitterTree->Branch(fitterBranchNameRho.c_str(), &fitterTreeProbePassingRhoSigmaIetaIetaEB, 
		       (fitterBranchNameRho + "/I").c_str());
  }
  if (isReallyOld && isPUSubtracted) {
    fitterTree->Branch(fitterBranchNameNPV.c_str(), &fitterTreeProbePassingNPVSigmaIetaIetaEB, 
		       (fitterBranchNameNPV + "/I").c_str());
  }
  fitterTree->Branch("dRTagProbe", &fitterTreeDRTagProbe, "dRTagProbe/F");
  fitterTreeReader.Loop(fitterTree, fitterTreeTotalWeight, fitterTreeSCEta, 
			fitterTreeProbePassingRhoSigmaIetaIetaEB, 
			fitterTreeProbePassingNPVSigmaIetaIetaEB, fitterTreeDRTagProbe, 
			realWeight);
  fitterTree->Write();

  //MCUnbias tree
  if (!isData) {
    TTree* theMCUnbiasTree = MCUnbiasTreeReader->fChain->CloneTree(0);
    Float_t MCUnbiasTreeTotalWeight;
    Float_t MCUnbiasTreeSCEta;
    Int_t MCUnbiasTreeProbePassingRhoSigmaIetaIetaEB;
    Int_t MCUnbiasTreeProbePassingNPVSigmaIetaIetaEB;
    std::string MCUnbiasBranchNameRho = "probe_passing_sigmaIetaIeta_EB";
    if (isPUSubtracted) {
      MCUnbiasBranchNameRho = "probe_passing_rho_sigmaIetaIeta_EB";
      MCUnbiasTreeProbePassingNPVSigmaIetaIetaEB = -1;
    }
    const std::string MCUnbiasBranchNameNPV = "probe_passing_nPV_sigmaIetaIeta_EB";
    theMCUnbiasTree->Branch("totalWeight", &MCUnbiasTreeTotalWeight, "totalWeight/F");
    if (isReallyOld && isOldTree) {
      theMCUnbiasTree->Branch("probe_SC_eta", &MCUnbiasTreeSCEta, "probe_SC_eta/F");
    }
    if (isReallyOld) {
      theMCUnbiasTree->Branch(MCUnbiasBranchNameRho.c_str(), 
			      &MCUnbiasTreeProbePassingRhoSigmaIetaIetaEB, 
			      (MCUnbiasBranchNameRho + "/I").c_str());
    }
    if (isReallyOld && isPUSubtracted) {
      theMCUnbiasTree->Branch(MCUnbiasBranchNameNPV.c_str(), 
			      &MCUnbiasTreeProbePassingNPVSigmaIetaIetaEB, 
			      (MCUnbiasBranchNameNPV + "/I").c_str());
    }
    MCUnbiasTreeReader->Loop(theMCUnbiasTree, MCUnbiasTreeTotalWeight, MCUnbiasTreeSCEta, 
			     MCUnbiasTreeProbePassingRhoSigmaIetaIetaEB, 
			     MCUnbiasTreeProbePassingNPVSigmaIetaIetaEB, realWeight);
    theMCUnbiasTree->Write();
  }

  //write
  out.Write();
}

//add new variables to trees
void addVariables(const std::vector<std::string>& input, const std::vector<std::string>& dirs, 
		  const std::string tag)
{
  for (std::vector<std::string>::const_iterator iIn = input.begin(); iIn != input.end(); ++iIn) {
    std::string fileName(*iIn);
    cout << "Processing " << fileName << "...\n";
    TFile out(fileName.replace(fileName.find(".root"), 5, "_" + tag + ".root").c_str(), 
	      "RECREATE");
    for (std::vector<std::string>::const_iterator iDir = dirs.begin(); iDir != dirs.end(); 
	 ++iDir) {
//       if ((*iDir).find("PU") == std::string::npos) {
// 	addVariables<FitterTree, MCUnbiasTree>(*iIn, out, *iDir);
//       }
//       else {
// 	addVariables<PUCorrectedFitterTree, PUCorrectedMCUnbiasTree>(*iIn, out, *iDir);
//       }
      addTotalWeight<MC>(*iIn, out, *iDir);
    }
    out.Close();
  }
}

//mimic newest directory structure
void makeNewDirs(const std::string& fileName, const std::string& dir, TFile& out, 
		 const std::vector<std::string>& dirsToReplace)
{
  std::string newDirEB(dir);
  std::string newDirEE(dir);
  for (std::vector<std::string>::const_iterator iDirToReplace = dirsToReplace.begin(); 
       iDirToReplace != dirsToReplace.end(); ++iDirToReplace) {
    if (dir == *iDirToReplace) {
      newDirEB.append("EB");
      newDirEE.append("EE");
    }
  }
  TFile in(fileName.c_str());
  TTree* inFitterTree = NULL;
  in.GetObject((dir + "/fitter_tree").c_str(), inFitterTree);
  TTree* inMCUnbiasTree = NULL;
  bool isData = fileName.find("JSON") != std::string::npos;
  if (!isData) in.GetObject((dir + "/mcUnbias_tree").c_str(), inMCUnbiasTree);
  out.cd();
  if ((inFitterTree == NULL) || (!isData && (inMCUnbiasTree == NULL))) {
    std::cerr << "Error getting tree with name " << (dir + "/fitter_tree") << " or ";
    std::cerr << (dir + "/mcUnbias_tree") << " from file " << fileName << ".\n";
    in.Close();
    return;
  }
  TTree* fitterTree = inFitterTree->CloneTree();
  TTree* MCUnbiasTree = NULL;
  if (!isData) MCUnbiasTree = inMCUnbiasTree->CloneTree();
  out.mkdir(newDirEB.c_str());
  out.cd(newDirEB.c_str());
  fitterTree->Write();
  if (!isData) MCUnbiasTree->Write();
  if (newDirEB != newDirEE) {
    out.cd();
    out.mkdir(newDirEE.c_str());
    out.cd(newDirEE.c_str());
    fitterTree->Write();
    if (!isData) MCUnbiasTree->Write();
  }
  out.Write();
  delete fitterTree;
  if (!isData) delete MCUnbiasTree;
  in.Close();
}

//mimic newest directory structure
void makeNewDirs(const std::vector<std::string>& input, const std::vector<std::string>& dirs, 
		 const std::vector<std::string>& dirsToReplace, const std::string& tag)
{
  for (std::vector<std::string>::const_iterator iIn = input.begin(); iIn != input.end(); ++iIn) {
    std::string fileName(*iIn);
//     TFile out(fileName.replace(fileName.find(".root"), 5, "_" + tag + ".root").c_str(), 
// 	      "RECREATE");
    TFile out(fileName.replace(fileName.find("intermediatev2"), 14, tag).c_str(), 
	      "RECREATE");
    for (std::vector<std::string>::const_iterator iDir = dirs.begin(); iDir != dirs.end(); 
	 ++iDir) {
      if ((*iDir).find("PU") == std::string::npos) makeNewDirs(*iIn, *iDir, out, dirsToReplace);
      else makeNewDirs(*iIn, *iDir, out, dirsToReplace);
    }
    out.Close();
  }
}

map<pair<string, float>, pair<string, string> > makeCutMap(const vector<string>& branchNames, 
							   const vector<float>& cutVals, 
							   const vector<string>& comparators, 
							   const vector<string>& branchTypes)
{
  //sanity checks
  map<pair<string, float>, pair<string, string> > cutMap;
  if (!((branchNames.size() == cutVals.size()) && (cutVals.size() == comparators.size()) && 
	(comparators.size() == branchTypes.size()))) {
    cerr << "Error: " << branchNames.size() << " branch names, " << cutVals.size();
    cerr << " cut values, " << comparators.size() << " comparators, " << branchTypes.size();
    cerr << " branch types.\n";
    return cutMap;
  }

  //make cut map
  for (unsigned int i = 0; i < branchNames.size(); ++i) {
    cutMap[make_pair(branchNames[i], cutVals[i])] = make_pair(comparators[i], branchTypes[i]);
  }
  return cutMap;
}

void applyCuts(const vector<string>& inputFiles, 
	       const map<pair<string, float>, pair<string, string> >& cuts, 
	       const vector<string>& trees, const vector<string>& outputFiles)
{
  //sanity checks
  if (inputFiles.size() != outputFiles.size()) {
    cerr << "Error: " << inputFiles.size() << " input files, " << outputFiles.size();
    cerr << " output files.\n";
    return;
  }

  //open input files
  vector<TFile*> inputStreams;
  for (vector<string>::const_iterator iInputFile = inputFiles.begin(); 
       iInputFile != inputFiles.end(); ++iInputFile) {
    TFile* in = new TFile((*iInputFile).c_str());
    if (in->IsOpen()) inputStreams.push_back(in);
    else inputStreams.push_back(NULL);
  }

  //leaf variables
  Float_t probe_ecalRecHitSumEtConeDR03;
  Float_t probe_ecalRecHitSumEtConeDR04;
  Float_t probe_et;
  Float_t probe_eta;
  Float_t probe_hadronicOverEm;
  Float_t probe_hasPixelSeed;
  Float_t probe_hcalTowerSumEtConeDR03;
  Float_t probe_hcalTowerSumEtConeDR04;
  Float_t probe_isPhoton;
  Float_t probe_phi;
  Float_t probe_px;
  Float_t probe_py;
  Float_t probe_pz;
  Float_t probe_sigmaIetaIeta;
  Float_t probe_sigmaIphiIphi;
  Float_t probe_trkSumPtHollowConeDR03;
  Float_t probe_trkSumPtHollowConeDR04;
  Float_t probe_dRjet05;
  Float_t probe_dRjet09;
  Float_t probe_nJets05;
  Float_t probe_nJets09;
  Int_t probe_passing;
  UInt_t run;
  UInt_t lumi;
  UInt_t event;
  Int_t event_nPV;
  Float_t event_met_calomet;
  Float_t event_met_calosumet;
  Float_t event_met_calometsignificance;
  Float_t event_met_tcmet;
  Float_t event_met_tcsumet;
  Float_t event_met_tcmetsignificance;
  Float_t event_met_pfmet;
  Float_t event_met_pfsumet;
  Float_t event_met_pfmetsignificance;
  Float_t event_PrimaryVertex_x;
  Float_t event_PrimaryVertex_y;
  Float_t event_PrimaryVertex_z;
  Float_t event_BeamSpot_x;
  Float_t event_BeamSpot_y;
  Float_t event_BeamSpot_z;
  Float_t mass;
  Float_t tag_photon_HoverE;
  Float_t tag_photon_HoverE_Depth1;
  Float_t tag_photon_HoverE_Depth2;
  Float_t tag_photon_e1x5;
  Float_t tag_photon_e2x5;
  Float_t tag_photon_e5x5;
  Float_t tag_photon_ecaliso_dr03;
  Float_t tag_photon_ecaliso_dr04;
  Float_t tag_photon_eta;
  Float_t tag_photon_hasPixelSeed;
  Float_t tag_photon_hcaliso_dr03;
  Float_t tag_photon_hcaliso_dr04;
  Float_t tag_photon_isEB;
  Float_t tag_photon_isEBEEGap;
  Float_t tag_photon_isEBEtaGap;
  Float_t tag_photon_isEBPhiGap;
  Float_t tag_photon_isEE;
  Float_t tag_photon_isEEDeeGap;
  Float_t tag_photon_isEERingGap;
  Float_t tag_photon_phi;
  Float_t tag_photon_pt;
  Float_t tag_photon_px;
  Float_t tag_photon_py;
  Float_t tag_photon_pz;
  Float_t tag_photon_sigmaEtaEta;
  Float_t tag_photon_sigmaIetaIeta;
  Float_t tag_photon_trackiso_dr03;
  Float_t tag_photon_trackiso_dr04;
  Float_t tag_sc_energy;
  Float_t tag_sc_et;
  Float_t tag_sc_eta;
  Float_t tag_sc_etaWidth;
  Float_t tag_sc_phi;
  Float_t tag_sc_phiWidth;
  Float_t tag_sc_preshowerEnergy;
  Float_t tag_sc_rawEnergy;
  Float_t tag_sc_size;
  Float_t tag_sc_x;
  Float_t tag_sc_y;
  Float_t tag_sc_z;
  Int_t tag_flag;
  Float_t pair_e;
  Float_t pair_et;
  Float_t pair_eta;
  Float_t pair_mass;
  Float_t pair_mt;
  Float_t pair_p;
  Float_t pair_phi;
  Float_t pair_pt;
  Float_t pair_px;
  Float_t pair_py;
  Float_t pair_pz;
  Float_t pair_rapidity;
  Float_t pair_theta;
  Float_t pair_vx;
  Float_t pair_vy;
  Float_t pair_vz;
  Int_t pair_mass60to120;

  //branches
  TBranch* b_probe_ecalRecHitSumEtConeDR03;
  TBranch* b_probe_ecalRecHitSumEtConeDR04;
  TBranch* b_probe_et;
  TBranch* b_probe_eta;
  TBranch* b_probe_hadronicOverEm;
  TBranch* b_probe_hasPixelSeed;
  TBranch* b_probe_hcalTowerSumEtConeDR03;
  TBranch* b_probe_hcalTowerSumEtConeDR04;
  TBranch* b_probe_isPhoton;
  TBranch* b_probe_phi;
  TBranch* b_probe_px;
  TBranch* b_probe_py;
  TBranch* b_probe_pz;
  TBranch* b_probe_sigmaIetaIeta;
  TBranch* b_probe_sigmaIphiIphi;
  TBranch* b_probe_trkSumPtHollowConeDR03;
  TBranch* b_probe_trkSumPtHollowConeDR04;
  TBranch* b_probe_dRjet05;
  TBranch* b_probe_dRjet09;
  TBranch* b_probe_nJets05;
  TBranch* b_probe_nJets09;
  TBranch* b_probe_passing;
  TBranch* b_run;
  TBranch* b_lumi;
  TBranch* b_event;
  TBranch* b_mNPV;
  TBranch* b_mMET;
  TBranch* b_mSumET;
  TBranch* b_mMETSign;
  TBranch* b_mtcMET;
  TBranch* b_mtcSumET;
  TBranch* b_mtcMETSign;
  TBranch* b_mpfMET;
  TBranch* b_mpfSumET;
  TBranch* b_mpfMETSign;
  TBranch* b_mPVx;
  TBranch* b_mPVy;
  TBranch* b_mPVz;
  TBranch* b_mBSx;
  TBranch* b_mBSy;
  TBranch* b_mBSz;
  TBranch* b_mass;
  TBranch* b_tag_photon_HoverE;
  TBranch* b_tag_photon_HoverE_Depth1;
  TBranch* b_tag_photon_HoverE_Depth2;
  TBranch* b_tag_photon_e1x5;
  TBranch* b_tag_photon_e2x5;
  TBranch* b_tag_photon_e5x5;
  TBranch* b_tag_photon_ecaliso_dr03;
  TBranch* b_tag_photon_ecaliso_dr04;
  TBranch* b_tag_photon_eta;
  TBranch* b_tag_photon_hasPixelSeed;
  TBranch* b_tag_photon_hcaliso_dr03;
  TBranch* b_tag_photon_hcaliso_dr04;
  TBranch* b_tag_photon_isEB;
  TBranch* b_tag_photon_isEBEEGap;
  TBranch* b_tag_photon_isEBEtaGap;
  TBranch* b_tag_photon_isEBPhiGap;
  TBranch* b_tag_photon_isEE;
  TBranch* b_tag_photon_isEEDeeGap;
  TBranch* b_tag_photon_isEERingGap;
  TBranch* b_tag_photon_phi;
  TBranch* b_tag_photon_pt;
  TBranch* b_tag_photon_px;
  TBranch* b_tag_photon_py;
  TBranch* b_tag_photon_pz;
  TBranch* b_tag_photon_sigmaEtaEta;
  TBranch* b_tag_photon_sigmaIetaIeta;
  TBranch* b_tag_photon_trackiso_dr03;
  TBranch* b_tag_photon_trackiso_dr04;
  TBranch* b_tag_sc_energy;
  TBranch* b_tag_sc_et;
  TBranch* b_tag_sc_eta;
  TBranch* b_tag_sc_etaWidth;
  TBranch* b_tag_sc_phi;
  TBranch* b_tag_sc_phiWidth;
  TBranch* b_tag_sc_preshowerEnergy;
  TBranch* b_tag_sc_rawEnergy;
  TBranch* b_tag_sc_size;
  TBranch* b_tag_sc_x;
  TBranch* b_tag_sc_y;
  TBranch* b_tag_sc_z;
  TBranch* b_tag_flag;
  TBranch* b_pair_e;
  TBranch* b_pair_et;
  TBranch* b_pair_eta;
  TBranch* b_pair_mass;
  TBranch* b_pair_mt;
  TBranch* b_pair_p;
  TBranch* b_pair_phi;
  TBranch* b_pair_pt;
  TBranch* b_pair_px;
  TBranch* b_pair_py;
  TBranch* b_pair_pz;
  TBranch* b_pair_rapidity;
  TBranch* b_pair_theta;
  TBranch* b_pair_vx;
  TBranch* b_pair_vy;
  TBranch* b_pair_vz;
  TBranch* b_pair_mass60to120;

  //loop over input files
  for (vector<TFile*>::const_iterator iInput = inputStreams.begin(); iInput != inputStreams.end(); 
       ++iInput) {
    if (*iInput != NULL) {

      cerr << "Input file: " << (*iInput)->GetName() << endl;

      //open output file
      TFile* out = new TFile(outputFiles[iInput - inputStreams.begin()].c_str(), "RECREATE");
      cerr << "Output file: " << out->GetName() << endl;

      //loop over trees
      for (vector<string>::const_iterator iTree = trees.begin(); iTree != trees.end(); ++iTree) {
	stringstream dir;
	dir << *iTree << "/fitter_tree";
	TTree* inputTree = NULL;
	(*iInput)->GetObject(dir.str().c_str(), inputTree);
	if (inputTree != NULL) {
	  cerr << "Tree name: " << *iTree << "/" << inputTree->GetName() << endl;
	  if (out->IsOpen()) {

	    //clone input tree branch structure but not individual entries
	    out->mkdir((*iTree).c_str());
	    out->cd((*iTree).c_str());
	    TTree* outputTree = inputTree->CloneTree(0);

	    //set branch addresses
	    inputTree->SetBranchAddress("probe_ecalRecHitSumEtConeDR03", 
				     &probe_ecalRecHitSumEtConeDR03, 
				     &b_probe_ecalRecHitSumEtConeDR03);
	    inputTree->SetBranchAddress("probe_ecalRecHitSumEtConeDR04", 
				     &probe_ecalRecHitSumEtConeDR04, 
				     &b_probe_ecalRecHitSumEtConeDR04);
	    inputTree->SetBranchAddress("probe_et", &probe_et, &b_probe_et);
	    inputTree->SetBranchAddress("probe_eta", &probe_eta, &b_probe_eta);
	    inputTree->SetBranchAddress("probe_hadronicOverEm", &probe_hadronicOverEm, 
				     &b_probe_hadronicOverEm);
	    inputTree->SetBranchAddress("probe_hasPixelSeed", &probe_hasPixelSeed, 
				     &b_probe_hasPixelSeed);
	    inputTree->SetBranchAddress("probe_hcalTowerSumEtConeDR03", 
				     &probe_hcalTowerSumEtConeDR03, 
				     &b_probe_hcalTowerSumEtConeDR03);
	    inputTree->SetBranchAddress("probe_hcalTowerSumEtConeDR04", 
				     &probe_hcalTowerSumEtConeDR04, 
				     &b_probe_hcalTowerSumEtConeDR04);
	    inputTree->SetBranchAddress("probe_isPhoton", &probe_isPhoton, &b_probe_isPhoton);
	    inputTree->SetBranchAddress("probe_phi", &probe_phi, &b_probe_phi);
	    inputTree->SetBranchAddress("probe_px", &probe_px, &b_probe_px);
	    inputTree->SetBranchAddress("probe_py", &probe_py, &b_probe_py);
	    inputTree->SetBranchAddress("probe_pz", &probe_pz, &b_probe_pz);
	    inputTree->SetBranchAddress("probe_sigmaIetaIeta", &probe_sigmaIetaIeta, 
				     &b_probe_sigmaIetaIeta);
	    inputTree->SetBranchAddress("probe_sigmaIphiIphi", &probe_sigmaIphiIphi, 
				     &b_probe_sigmaIphiIphi);
	    inputTree->SetBranchAddress("probe_trkSumPtHollowConeDR03", 
				     &probe_trkSumPtHollowConeDR03, 
				     &b_probe_trkSumPtHollowConeDR03);
	    inputTree->SetBranchAddress("probe_trkSumPtHollowConeDR04", 
				     &probe_trkSumPtHollowConeDR04, 
				     &b_probe_trkSumPtHollowConeDR04);
	    inputTree->SetBranchAddress("probe_dRjet05", &probe_dRjet05, &b_probe_dRjet05);
	    inputTree->SetBranchAddress("probe_dRjet09", &probe_dRjet09, &b_probe_dRjet09);
	    inputTree->SetBranchAddress("probe_nJets05", &probe_nJets05, &b_probe_nJets05);
	    inputTree->SetBranchAddress("probe_nJets09", &probe_nJets09, &b_probe_nJets09);
	    inputTree->SetBranchAddress("probe_passing", &probe_passing, &b_probe_passing);
	    inputTree->SetBranchAddress("run", &run, &b_run);
	    inputTree->SetBranchAddress("lumi", &lumi, &b_lumi);
	    inputTree->SetBranchAddress("event", &event, &b_event);
	    inputTree->SetBranchAddress("event_nPV", &event_nPV, &b_mNPV);
	    inputTree->SetBranchAddress("event_met_calomet", &event_met_calomet, &b_mMET);
	    inputTree->SetBranchAddress("event_met_calosumet", &event_met_calosumet, &b_mSumET);
	    inputTree->SetBranchAddress("event_met_calometsignificance", 
				     &event_met_calometsignificance, &b_mMETSign);
	    inputTree->SetBranchAddress("event_met_tcmet", &event_met_tcmet, &b_mtcMET);
	    inputTree->SetBranchAddress("event_met_tcsumet", &event_met_tcsumet, &b_mtcSumET);
	    inputTree->SetBranchAddress("event_met_tcmetsignificance", 
					&event_met_tcmetsignificance, &b_mtcMETSign);
	    inputTree->SetBranchAddress("event_met_pfmet", &event_met_pfmet, &b_mpfMET);
	    inputTree->SetBranchAddress("event_met_pfsumet", &event_met_pfsumet, &b_mpfSumET);
	    inputTree->SetBranchAddress("event_met_pfmetsignificance", 
					&event_met_pfmetsignificance, &b_mpfMETSign);
	    inputTree->SetBranchAddress("event_PrimaryVertex_x", &event_PrimaryVertex_x, &b_mPVx);
	    inputTree->SetBranchAddress("event_PrimaryVertex_y", &event_PrimaryVertex_y, &b_mPVy);
	    inputTree->SetBranchAddress("event_PrimaryVertex_z", &event_PrimaryVertex_z, &b_mPVz);
	    inputTree->SetBranchAddress("event_BeamSpot_x", &event_BeamSpot_x, &b_mBSx);
	    inputTree->SetBranchAddress("event_BeamSpot_y", &event_BeamSpot_y, &b_mBSy);
	    inputTree->SetBranchAddress("event_BeamSpot_z", &event_BeamSpot_z, &b_mBSz);
	    inputTree->SetBranchAddress("mass", &mass, &b_mass);
	    inputTree->SetBranchAddress("tag_photon_HoverE", &tag_photon_HoverE, 
				     &b_tag_photon_HoverE);
	    inputTree->SetBranchAddress("tag_photon_HoverE_Depth1", &tag_photon_HoverE_Depth1, 
				     &b_tag_photon_HoverE_Depth1);
	    inputTree->SetBranchAddress("tag_photon_HoverE_Depth2", &tag_photon_HoverE_Depth2, 
				     &b_tag_photon_HoverE_Depth2);
	    inputTree->SetBranchAddress("tag_photon_e1x5", &tag_photon_e1x5, &b_tag_photon_e1x5);
	    inputTree->SetBranchAddress("tag_photon_e2x5", &tag_photon_e2x5, &b_tag_photon_e2x5);
	    inputTree->SetBranchAddress("tag_photon_e5x5", &tag_photon_e5x5, &b_tag_photon_e5x5);
	    inputTree->SetBranchAddress("tag_photon_ecaliso_dr03", &tag_photon_ecaliso_dr03, 
				     &b_tag_photon_ecaliso_dr03);
	    inputTree->SetBranchAddress("tag_photon_ecaliso_dr04", &tag_photon_ecaliso_dr04, 
				     &b_tag_photon_ecaliso_dr04);
	    inputTree->SetBranchAddress("tag_photon_eta", &tag_photon_eta, &b_tag_photon_eta);
	    inputTree->SetBranchAddress("tag_photon_hasPixelSeed", &tag_photon_hasPixelSeed, 
				     &b_tag_photon_hasPixelSeed);
	    inputTree->SetBranchAddress("tag_photon_hcaliso_dr03", &tag_photon_hcaliso_dr03, 
				     &b_tag_photon_hcaliso_dr03);
	    inputTree->SetBranchAddress("tag_photon_hcaliso_dr04", &tag_photon_hcaliso_dr04, 
				     &b_tag_photon_hcaliso_dr04);
	    inputTree->SetBranchAddress("tag_photon_isEB", &tag_photon_isEB, &b_tag_photon_isEB);
	    inputTree->SetBranchAddress("tag_photon_isEBEEGap", &tag_photon_isEBEEGap, 
				     &b_tag_photon_isEBEEGap);
	    inputTree->SetBranchAddress("tag_photon_isEBEtaGap", &tag_photon_isEBEtaGap, 
				     &b_tag_photon_isEBEtaGap);
	    inputTree->SetBranchAddress("tag_photon_isEBPhiGap", &tag_photon_isEBPhiGap, 
				     &b_tag_photon_isEBPhiGap);
	    inputTree->SetBranchAddress("tag_photon_isEE", &tag_photon_isEE, &b_tag_photon_isEE);
	    inputTree->SetBranchAddress("tag_photon_isEEDeeGap", &tag_photon_isEEDeeGap, 
				     &b_tag_photon_isEEDeeGap);
	    inputTree->SetBranchAddress("tag_photon_isEERingGap", &tag_photon_isEERingGap, 
				     &b_tag_photon_isEERingGap);
	    inputTree->SetBranchAddress("tag_photon_phi", &tag_photon_phi, &b_tag_photon_phi);
	    inputTree->SetBranchAddress("tag_photon_pt", &tag_photon_pt, &b_tag_photon_pt);
	    inputTree->SetBranchAddress("tag_photon_px", &tag_photon_px, &b_tag_photon_px);
	    inputTree->SetBranchAddress("tag_photon_py", &tag_photon_py, &b_tag_photon_py);
	    inputTree->SetBranchAddress("tag_photon_pz", &tag_photon_pz, &b_tag_photon_pz);
	    inputTree->SetBranchAddress("tag_photon_sigmaEtaEta", &tag_photon_sigmaEtaEta, 
				     &b_tag_photon_sigmaEtaEta);
	    inputTree->SetBranchAddress("tag_photon_sigmaIetaIeta", &tag_photon_sigmaIetaIeta, 
				     &b_tag_photon_sigmaIetaIeta);
	    inputTree->SetBranchAddress("tag_photon_trackiso_dr03", &tag_photon_trackiso_dr03, 
				     &b_tag_photon_trackiso_dr03);
	    inputTree->SetBranchAddress("tag_photon_trackiso_dr04", &tag_photon_trackiso_dr04, 
				     &b_tag_photon_trackiso_dr04);
	    inputTree->SetBranchAddress("tag_sc_energy", &tag_sc_energy, &b_tag_sc_energy);
	    inputTree->SetBranchAddress("tag_sc_et", &tag_sc_et, &b_tag_sc_et);
	    inputTree->SetBranchAddress("tag_sc_eta", &tag_sc_eta, &b_tag_sc_eta);
	    inputTree->SetBranchAddress("tag_sc_etaWidth", &tag_sc_etaWidth, &b_tag_sc_etaWidth);
	    inputTree->SetBranchAddress("tag_sc_phi", &tag_sc_phi, &b_tag_sc_phi);
	    inputTree->SetBranchAddress("tag_sc_phiWidth", &tag_sc_phiWidth, &b_tag_sc_phiWidth);
	    inputTree->SetBranchAddress("tag_sc_preshowerEnergy", &tag_sc_preshowerEnergy, 
				     &b_tag_sc_preshowerEnergy);
	    inputTree->SetBranchAddress("tag_sc_rawEnergy", &tag_sc_rawEnergy, 
					&b_tag_sc_rawEnergy);
	    inputTree->SetBranchAddress("tag_sc_size", &tag_sc_size, &b_tag_sc_size);
	    inputTree->SetBranchAddress("tag_sc_x", &tag_sc_x, &b_tag_sc_x);
	    inputTree->SetBranchAddress("tag_sc_y", &tag_sc_y, &b_tag_sc_y);
	    inputTree->SetBranchAddress("tag_sc_z", &tag_sc_z, &b_tag_sc_z);
	    inputTree->SetBranchAddress("tag_flag", &tag_flag, &b_tag_flag);
	    inputTree->SetBranchAddress("pair_e", &pair_e, &b_pair_e);
	    inputTree->SetBranchAddress("pair_et", &pair_et, &b_pair_et);
	    inputTree->SetBranchAddress("pair_eta", &pair_eta, &b_pair_eta);
	    inputTree->SetBranchAddress("pair_mass", &pair_mass, &b_pair_mass);
	    inputTree->SetBranchAddress("pair_mt", &pair_mt, &b_pair_mt);
	    inputTree->SetBranchAddress("pair_p", &pair_p, &b_pair_p);
	    inputTree->SetBranchAddress("pair_phi", &pair_phi, &b_pair_phi);
	    inputTree->SetBranchAddress("pair_pt", &pair_pt, &b_pair_pt);
	    inputTree->SetBranchAddress("pair_px", &pair_px, &b_pair_px);
	    inputTree->SetBranchAddress("pair_py", &pair_py, &b_pair_py);
	    inputTree->SetBranchAddress("pair_pz", &pair_pz, &b_pair_pz);
	    inputTree->SetBranchAddress("pair_rapidity", &pair_rapidity, &b_pair_rapidity);
	    inputTree->SetBranchAddress("pair_theta", &pair_theta, &b_pair_theta);
	    inputTree->SetBranchAddress("pair_vx", &pair_vx, &b_pair_vx);
	    inputTree->SetBranchAddress("pair_vy", &pair_vy, &b_pair_vy);
	    inputTree->SetBranchAddress("pair_vz", &pair_vz, &b_pair_vz);
	    inputTree->SetBranchAddress("pair_mass60to120", &pair_mass60to120, 
					&b_pair_mass60to120);

	    //loop over input tree
	    cerr << "Entries (input): " << inputTree->GetEntries() << endl;
	    for (Long64_t iEvt = 0; iEvt < inputTree->GetEntries(); ++iEvt) {
	      inputTree->GetEntry(iEvt);

	      //loop over cuts
	      vector<bool> passCuts;
	      for (map<pair<string, float>, pair<string, string> >::const_iterator 
		     iCut = cuts.begin(); iCut != cuts.end(); ++iCut) {

		//parse cut map
		string branchName = iCut->first.first;
		float cutValue = iCut->first.second;
		string comparator = iCut->second.first;

		//get the appropriate tree leaf
		Float_t valFloat = -999.0;
		Int_t valInt = -999;
		UInt_t valUInt = 999;
		if (branchName == "probe_ecalRecHitSumEtConeDR03") {
		  valFloat = probe_ecalRecHitSumEtConeDR03;
		}
		if (branchName == "probe_ecalRecHitSumEtConeDR04") {
		  valFloat = probe_ecalRecHitSumEtConeDR04;
		}
		if (branchName == "probe_et") valFloat = probe_et;
		if (branchName == "probe_eta") valFloat = probe_eta;
		if (branchName == "probe_hadronicOverEm") valFloat = probe_hadronicOverEm;
		if (branchName == "probe_hasPixelSeed") valFloat = probe_hasPixelSeed;
		if (branchName == "probe_hcalTowerSumEtConeDR03") {
		  valFloat = probe_hcalTowerSumEtConeDR03;
		}
		if (branchName == "probe_hcalTowerSumEtConeDR04") {
		  valFloat = probe_hcalTowerSumEtConeDR04;
		}
		if (branchName == "probe_isPhoton") valFloat = probe_isPhoton;
		if (branchName == "probe_phi") valFloat = probe_phi;
		if (branchName == "probe_px") valFloat = probe_px;
		if (branchName == "probe_py") valFloat = probe_py;
		if (branchName == "probe_pz") valFloat = probe_pz;
		if (branchName == "probe_sigmaIetaIeta") valFloat = probe_sigmaIetaIeta;
		if (branchName == "probe_sigmaIphiIphi") valFloat = probe_sigmaIphiIphi;
		if (branchName == "probe_trkSumPtHollowConeDR03") {
		  valFloat = probe_trkSumPtHollowConeDR03;
		}
		if (branchName == "probe_trkSumPtHollowConeDR04") {
		  valFloat = probe_trkSumPtHollowConeDR04;
		}
		if (branchName == "probe_dRjet05") valFloat = probe_dRjet05;
		if (branchName == "probe_dRjet09") valFloat = probe_dRjet09;
		if (branchName == "probe_nJets05") valFloat = probe_nJets05;
		if (branchName == "probe_nJets09") valFloat = probe_nJets09;
		if (branchName == "probe_passing") valInt = probe_passing;
		if (branchName == "run") valUInt = run;
		if (branchName == "lumi") valUInt = lumi;
		if (branchName == "event") valUInt = event;
		if (branchName == "event_nPV") valInt = event_nPV;
		if (branchName == "event_met_calomet") valFloat = event_met_calomet;
		if (branchName == "event_met_calosumet") valFloat = event_met_calosumet;
		if (branchName == "event_met_calometsignificance") {
		  valFloat = event_met_calometsignificance;
		}
		if (branchName == "event_met_tcmet") valFloat = event_met_tcmet;
		if (branchName == "event_met_tcsumet") valFloat = event_met_tcsumet;
		if (branchName == "event_met_tcmetsignificance") {
		  valFloat = event_met_tcmetsignificance;
		}
		if (branchName == "event_met_pfmet") valFloat = event_met_pfmet;
		if (branchName == "event_met_pfsumet") valFloat = event_met_pfsumet;
		if (branchName == "event_met_pfmetsignificance") {
		  valFloat = event_met_pfmetsignificance;
		}
		if (branchName == "event_PrimaryVertex_x") valFloat = event_PrimaryVertex_x;
		if (branchName == "event_PrimaryVertex_y") valFloat = event_PrimaryVertex_y;
		if (branchName == "event_PrimaryVertex_z") valFloat = event_PrimaryVertex_z;
		if (branchName == "event_BeamSpot_x") valFloat = event_BeamSpot_x;
		if (branchName == "event_BeamSpot_y") valFloat = event_BeamSpot_y;
		if (branchName == "event_BeamSpot_z") valFloat = event_BeamSpot_z;
		if (branchName == "mass") valFloat = mass;
		if (branchName == "tag_photon_HoverE") valFloat = tag_photon_HoverE;
		if (branchName == "tag_photon_HoverE_Depth1") valFloat = tag_photon_HoverE_Depth1;
		if (branchName == "tag_photon_HoverE_Depth2") valFloat = tag_photon_HoverE_Depth2;
		if (branchName == "tag_photon_e1x5") valFloat = tag_photon_e1x5;
		if (branchName == "tag_photon_e2x5") valFloat = tag_photon_e2x5;
		if (branchName == "tag_photon_e5x5") valFloat = tag_photon_e5x5;
		if (branchName == "tag_photon_ecaliso_dr03") valFloat = tag_photon_ecaliso_dr03;
		if (branchName == "tag_photon_ecaliso_dr04") valFloat = tag_photon_ecaliso_dr04;
		if (branchName == "tag_photon_eta") valFloat = tag_photon_eta;
		if (branchName == "tag_photon_hasPixelSeed") valFloat = tag_photon_hasPixelSeed;
		if (branchName == "tag_photon_hcaliso_dr03") valFloat = tag_photon_hcaliso_dr03;
		if (branchName == "tag_photon_hcaliso_dr04") valFloat = tag_photon_hcaliso_dr04;
		if (branchName == "tag_photon_isEB") valFloat = tag_photon_isEB;
		if (branchName == "tag_photon_isEBEEGap") valFloat = tag_photon_isEBEEGap;
		if (branchName == "tag_photon_isEBEtaGap") valFloat = tag_photon_isEBEtaGap;
		if (branchName == "tag_photon_isEBPhiGap") valFloat = tag_photon_isEBPhiGap;
		if (branchName == "tag_photon_isEE") valFloat = tag_photon_isEE;
		if (branchName == "tag_photon_isEEDeeGap") valFloat = tag_photon_isEEDeeGap;
		if (branchName == "tag_photon_isEERingGap") valFloat = tag_photon_isEERingGap;
		if (branchName == "tag_photon_phi") valFloat = tag_photon_phi;
		if (branchName == "tag_photon_pt") valFloat = tag_photon_pt;
		if (branchName == "tag_photon_px") valFloat = tag_photon_px;
		if (branchName == "tag_photon_py") valFloat = tag_photon_py;
		if (branchName == "tag_photon_pz") valFloat = tag_photon_pz;
		if (branchName == "tag_photon_sigmaEtaEta") valFloat = tag_photon_sigmaEtaEta;
		if (branchName == "tag_photon_sigmaIetaIeta") valFloat = tag_photon_sigmaIetaIeta;
		if (branchName == "tag_photon_trackiso_dr03") valFloat = tag_photon_trackiso_dr03;
		if (branchName == "tag_photon_trackiso_dr04") valFloat = tag_photon_trackiso_dr04;
		if (branchName == "tag_sc_energy") valFloat = tag_sc_energy;
		if (branchName == "tag_sc_et") valFloat = tag_sc_et;
		if (branchName == "tag_sc_eta") valFloat = tag_sc_eta;
		if (branchName == "tag_sc_etaWidth") valFloat = tag_sc_etaWidth;
		if (branchName == "tag_sc_phi") valFloat = tag_sc_phi;
		if (branchName == "tag_sc_phiWidth") valFloat = tag_sc_phiWidth;
		if (branchName == "tag_sc_preshowerEnergy") valFloat = tag_sc_preshowerEnergy;
		if (branchName == "tag_sc_rawEnergy") valFloat = tag_sc_rawEnergy;
		if (branchName == "tag_sc_size") valFloat = tag_sc_size;
		if (branchName == "tag_sc_x") valFloat = tag_sc_x;
		if (branchName == "tag_sc_y") valFloat = tag_sc_y;
		if (branchName == "tag_sc_z") valFloat = tag_sc_z;
		if (branchName == "tag_flag") valInt = tag_flag;
		if (branchName == "pair_e") valFloat = pair_e;
		if (branchName == "pair_et") valFloat = pair_et;
		if (branchName == "pair_eta") valFloat = pair_eta;
		if (branchName == "pair_mass") valFloat = pair_mass;
		if (branchName == "pair_mt") valFloat = pair_mt;
		if (branchName == "pair_p") valFloat = pair_p;
		if (branchName == "pair_phi") valFloat = pair_phi;
		if (branchName == "pair_pt") valFloat = pair_pt;
		if (branchName == "pair_px") valFloat = pair_px;
		if (branchName == "pair_py") valFloat = pair_py;
		if (branchName == "pair_pz") valFloat = pair_pz;
		if (branchName == "pair_rapidity") valFloat = pair_rapidity;
		if (branchName == "pair_theta") valFloat = pair_theta;
		if (branchName == "pair_vx") valFloat = pair_vx;
		if (branchName == "pair_vy") valFloat = pair_vy;
		if (branchName == "pair_vz") valFloat = pair_vz;
		if (branchName == "pair_mass60to120") valInt = pair_mass60to120;

		//apply cut
		bool passCut = 
		  ((valInt != -999) && 
		   (((comparator == ">") && (valInt > cutValue)) || 
		    ((comparator == ">=") && (valInt >= cutValue)) || 
		    ((comparator == "<") && (valInt < cutValue)) || 
		    ((comparator == "<=") && (valInt <= cutValue)) || 
		    ((comparator == "==") && (valInt == cutValue)))) || 
		  ((valUInt != 999) && 
		   (((comparator == ">") && (valUInt > cutValue)) || 
		    ((comparator == ">=") && (valUInt >= cutValue)) || 
		    ((comparator == "<") && (valUInt < cutValue)) || 
		    ((comparator == "<=") && (valUInt <= cutValue)) || 
		    ((comparator == "==") && (valUInt == cutValue)))) || 
		  ((valFloat != -999.0) && 
		   (((comparator == ">") && (valFloat > cutValue)) || 
		    ((comparator == ">=") && (valFloat >= cutValue)) || 
		    ((comparator == "<") && (valFloat < cutValue)) || 
		    ((comparator == "<=") && (valFloat <= cutValue)) || 
		    ((comparator == "==") && (valFloat == cutValue))));
		passCuts.push_back(passCut);
	      }
	      bool passedAllCuts = true;
	      for (vector<bool>::const_iterator iPassFlag = passCuts.begin(); 
		   iPassFlag != passCuts.end(); ++iPassFlag) {
		passedAllCuts = passedAllCuts && *iPassFlag;
	      }

	      //fill the output tree with passing entries
	      if (passedAllCuts) {
		//out->cd();
		outputTree->Fill();
	      }

	    }//for (Long64_t iEvt = 0; iEvt < inputTree->GetEntries(); ++iEvt)

	    //write the output tree
	    outputTree->Write();
	    cerr << "outputTree: " << outputTree << endl;
	    cerr << "Entries (output): " << outputTree->GetEntries() << endl;
	    out->cd("..");

	  }//if (out->IsOpen())

	  else {
	    cerr << "Error opening file " << outputFiles[iInput - inputStreams.begin()] << ".\n";
	  }

	}//if (inputTree != NULL)

	else {
	  cerr << "Error getting tree " << dir.str() << " from file ";
	  cerr << inputFiles[iInput - inputStreams.begin()] << ".\n";
	}

      }//for (vector<string>::const_iterator iTree = trees.begin(); iTree != trees.end(); ++iTree)

      //write output file
      out->Write();
      out->Close();
      delete out;

    }//if (*iInput != NULL)

    else cerr << "Error opening file " << inputFiles[iInput - inputStreams.begin()] << ".\n";

    //close input file
    (*iInput)->Close();
    delete *iInput;

  }/*for (vector<TFile*>::const_iterator iInput = inputStreams.begin(); 
     iInput != inputStreams.end(); ++iInput)*/
  
}
