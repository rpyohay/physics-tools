#ifndef FitterTree_h
#define FitterTree_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

class FitterTree {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   // Declaration of leaf types
   Float_t         probe_ecalRecHitSumEtConeDR03;
   Float_t         probe_ecalRecHitSumEtConeDR04;
   Float_t         probe_et;
   Float_t         probe_eta;
   Float_t         probe_hadronicOverEm;
   Float_t         probe_hasPixelSeed;
   Float_t         probe_hcalTowerSumEtConeDR03;
   Float_t         probe_hcalTowerSumEtConeDR04;
   Float_t         probe_isPhoton;
   Float_t         probe_phi;
   Float_t         probe_px;
   Float_t         probe_py;
   Float_t         probe_pz;
   Float_t         probe_sigmaIetaIeta;
   Float_t         probe_sigmaIphiIphi;
   Float_t         probe_trkSumPtHollowConeDR03;
   Float_t         probe_trkSumPtHollowConeDR04;
   Float_t         probe_dR1jet00;
   Float_t         probe_dR2jet00;
   Float_t         probe_dR3jet00;
   Float_t         probe_dRjet03;
   Float_t         probe_dRjet05;
   Float_t         probe_dRjet07;
   Float_t         probe_dRjet09;
   Float_t         probe_nJets03;
   Float_t         probe_nJets05;
   Float_t         probe_nJets07;
   Float_t         probe_nJets09;
   Int_t           probe_passing;
   Float_t         weight;
   Double_t        PUWeight;
   UInt_t          run;
   UInt_t          lumi;
   UInt_t          event;
   Int_t           event_nPV;
   Float_t         event_met_calomet;
   Float_t         event_met_calosumet;
   Float_t         event_met_calometsignificance;
   Float_t         event_met_tcmet;
   Float_t         event_met_tcsumet;
   Float_t         event_met_tcmetsignificance;
   Float_t         event_met_pfmet;
   Float_t         event_met_pfsumet;
   Float_t         event_met_pfmetsignificance;
   Float_t         event_PrimaryVertex_x;
   Float_t         event_PrimaryVertex_y;
   Float_t         event_PrimaryVertex_z;
   Float_t         event_BeamSpot_x;
   Float_t         event_BeamSpot_y;
   Float_t         event_BeamSpot_z;
   Float_t         xsec;
   Int_t           nEvts;
   Float_t         mass;
   Int_t           mcTrue;
   Float_t         tag_photon_HoverE;
   Float_t         tag_photon_HoverE_Depth1;
   Float_t         tag_photon_HoverE_Depth2;
   Float_t         tag_photon_e1x5;
   Float_t         tag_photon_e2x5;
   Float_t         tag_photon_e5x5;
   Float_t         tag_photon_ecaliso_dr03;
   Float_t         tag_photon_ecaliso_dr04;
   Float_t         tag_photon_eta;
   Float_t         tag_photon_hasPixelSeed;
   Float_t         tag_photon_hcaliso_dr03;
   Float_t         tag_photon_hcaliso_dr04;
   Float_t         tag_photon_isEB;
   Float_t         tag_photon_isEBEEGap;
   Float_t         tag_photon_isEBEtaGap;
   Float_t         tag_photon_isEBPhiGap;
   Float_t         tag_photon_isEE;
   Float_t         tag_photon_isEEDeeGap;
   Float_t         tag_photon_isEERingGap;
   Float_t         tag_photon_phi;
   Float_t         tag_photon_pt;
   Float_t         tag_photon_px;
   Float_t         tag_photon_py;
   Float_t         tag_photon_pz;
   Float_t         tag_photon_sigmaEtaEta;
   Float_t         tag_photon_sigmaIetaIeta;
   Float_t         tag_photon_trackiso_dr03;
   Float_t         tag_photon_trackiso_dr04;
   Float_t         tag_sc_energy;
   Float_t         tag_sc_et;
   Float_t         tag_sc_eta;
   Float_t         tag_sc_etaWidth;
   Float_t         tag_sc_phi;
   Float_t         tag_sc_phiWidth;
   Float_t         tag_sc_preshowerEnergy;
   Float_t         tag_sc_rawEnergy;
   Float_t         tag_sc_size;
   Float_t         tag_sc_x;
   Float_t         tag_sc_y;
   Float_t         tag_sc_z;
   Int_t           tag_flag;
   Float_t         mc_probe_charge;
   Float_t         mc_probe_e;
   Float_t         mc_probe_et;
   Float_t         mc_probe_eta;
   Float_t         mc_probe_mass;
   Float_t         mc_probe_mt;
   Float_t         mc_probe_p;
   Float_t         mc_probe_phi;
   Float_t         mc_probe_pt;
   Float_t         mc_probe_px;
   Float_t         mc_probe_py;
   Float_t         mc_probe_pz;
   Float_t         mc_probe_rapidity;
   Float_t         mc_probe_theta;
   Float_t         mc_probe_vx;
   Float_t         mc_probe_vy;
   Float_t         mc_probe_vz;
   Int_t           mc_probe_flag;
   Float_t         pair_e;
   Float_t         pair_et;
   Float_t         pair_eta;
   Float_t         pair_mass;
   Float_t         pair_mt;
   Float_t         pair_p;
   Float_t         pair_phi;
   Float_t         pair_pt;
   Float_t         pair_px;
   Float_t         pair_py;
   Float_t         pair_pz;
   Float_t         pair_rapidity;
   Float_t         pair_theta;
   Float_t         pair_vx;
   Float_t         pair_vy;
   Float_t         pair_vz;
   Int_t           pair_mass60to120;

   // List of branches
   TBranch        *b_probe_ecalRecHitSumEtConeDR03;   //!
   TBranch        *b_probe_ecalRecHitSumEtConeDR04;   //!
   TBranch        *b_probe_et;   //!
   TBranch        *b_probe_eta;   //!
   TBranch        *b_probe_hadronicOverEm;   //!
   TBranch        *b_probe_hasPixelSeed;   //!
   TBranch        *b_probe_hcalTowerSumEtConeDR03;   //!
   TBranch        *b_probe_hcalTowerSumEtConeDR04;   //!
   TBranch        *b_probe_isPhoton;   //!
   TBranch        *b_probe_phi;   //!
   TBranch        *b_probe_px;   //!
   TBranch        *b_probe_py;   //!
   TBranch        *b_probe_pz;   //!
   TBranch        *b_probe_sigmaIetaIeta;   //!
   TBranch        *b_probe_sigmaIphiIphi;   //!
   TBranch        *b_probe_trkSumPtHollowConeDR03;   //!
   TBranch        *b_probe_trkSumPtHollowConeDR04;   //!
   TBranch        *b_probe_dR1jet00;   //!
   TBranch        *b_probe_dR2jet00;   //!
   TBranch        *b_probe_dR3jet00;   //!
   TBranch        *b_probe_dRjet03;   //!
   TBranch        *b_probe_dRjet05;   //!
   TBranch        *b_probe_dRjet07;   //!
   TBranch        *b_probe_dRjet09;   //!
   TBranch        *b_probe_nJets03;   //!
   TBranch        *b_probe_nJets05;   //!
   TBranch        *b_probe_nJets07;   //!
   TBranch        *b_probe_nJets09;   //!
   TBranch        *b_probe_passing;   //!
   TBranch        *b_weight;   //!
   TBranch        *b_PUWeight;   //!
   TBranch        *b_run;   //!
   TBranch        *b_lumi;   //!
   TBranch        *b_event;   //!
   TBranch        *b_mNPV;   //!
   TBranch        *b_mMET;   //!
   TBranch        *b_mSumET;   //!
   TBranch        *b_mMETSign;   //!
   TBranch        *b_mtcMET;   //!
   TBranch        *b_mtcSumET;   //!
   TBranch        *b_mtcMETSign;   //!
   TBranch        *b_mpfMET;   //!
   TBranch        *b_mpfSumET;   //!
   TBranch        *b_mpfMETSign;   //!
   TBranch        *b_mPVx;   //!
   TBranch        *b_mPVy;   //!
   TBranch        *b_mPVz;   //!
   TBranch        *b_mBSx;   //!
   TBranch        *b_mBSy;   //!
   TBranch        *b_mBSz;   //!
   TBranch        *b_mXsec;   //!
   TBranch        *b_mNEvts;   //!
   TBranch        *b_mass;   //!
   TBranch        *b_mcTrue;   //!
   TBranch        *b_tag_photon_HoverE;   //!
   TBranch        *b_tag_photon_HoverE_Depth1;   //!
   TBranch        *b_tag_photon_HoverE_Depth2;   //!
   TBranch        *b_tag_photon_e1x5;   //!
   TBranch        *b_tag_photon_e2x5;   //!
   TBranch        *b_tag_photon_e5x5;   //!
   TBranch        *b_tag_photon_ecaliso_dr03;   //!
   TBranch        *b_tag_photon_ecaliso_dr04;   //!
   TBranch        *b_tag_photon_eta;   //!
   TBranch        *b_tag_photon_hasPixelSeed;   //!
   TBranch        *b_tag_photon_hcaliso_dr03;   //!
   TBranch        *b_tag_photon_hcaliso_dr04;   //!
   TBranch        *b_tag_photon_isEB;   //!
   TBranch        *b_tag_photon_isEBEEGap;   //!
   TBranch        *b_tag_photon_isEBEtaGap;   //!
   TBranch        *b_tag_photon_isEBPhiGap;   //!
   TBranch        *b_tag_photon_isEE;   //!
   TBranch        *b_tag_photon_isEEDeeGap;   //!
   TBranch        *b_tag_photon_isEERingGap;   //!
   TBranch        *b_tag_photon_phi;   //!
   TBranch        *b_tag_photon_pt;   //!
   TBranch        *b_tag_photon_px;   //!
   TBranch        *b_tag_photon_py;   //!
   TBranch        *b_tag_photon_pz;   //!
   TBranch        *b_tag_photon_sigmaEtaEta;   //!
   TBranch        *b_tag_photon_sigmaIetaIeta;   //!
   TBranch        *b_tag_photon_trackiso_dr03;   //!
   TBranch        *b_tag_photon_trackiso_dr04;   //!
   TBranch        *b_tag_sc_energy;   //!
   TBranch        *b_tag_sc_et;   //!
   TBranch        *b_tag_sc_eta;   //!
   TBranch        *b_tag_sc_etaWidth;   //!
   TBranch        *b_tag_sc_phi;   //!
   TBranch        *b_tag_sc_phiWidth;   //!
   TBranch        *b_tag_sc_preshowerEnergy;   //!
   TBranch        *b_tag_sc_rawEnergy;   //!
   TBranch        *b_tag_sc_size;   //!
   TBranch        *b_tag_sc_x;   //!
   TBranch        *b_tag_sc_y;   //!
   TBranch        *b_tag_sc_z;   //!
   TBranch        *b_tag_flag;   //!
   TBranch        *b_mc_probe_charge;   //!
   TBranch        *b_mc_probe_e;   //!
   TBranch        *b_mc_probe_et;   //!
   TBranch        *b_mc_probe_eta;   //!
   TBranch        *b_mc_probe_mass;   //!
   TBranch        *b_mc_probe_mt;   //!
   TBranch        *b_mc_probe_p;   //!
   TBranch        *b_mc_probe_phi;   //!
   TBranch        *b_mc_probe_pt;   //!
   TBranch        *b_mc_probe_px;   //!
   TBranch        *b_mc_probe_py;   //!
   TBranch        *b_mc_probe_pz;   //!
   TBranch        *b_mc_probe_rapidity;   //!
   TBranch        *b_mc_probe_theta;   //!
   TBranch        *b_mc_probe_vx;   //!
   TBranch        *b_mc_probe_vy;   //!
   TBranch        *b_mc_probe_vz;   //!
   TBranch        *b_mc_probe_flag;   //!
   TBranch        *b_pair_e;   //!
   TBranch        *b_pair_et;   //!
   TBranch        *b_pair_eta;   //!
   TBranch        *b_pair_mass;   //!
   TBranch        *b_pair_mt;   //!
   TBranch        *b_pair_p;   //!
   TBranch        *b_pair_phi;   //!
   TBranch        *b_pair_pt;   //!
   TBranch        *b_pair_px;   //!
   TBranch        *b_pair_py;   //!
   TBranch        *b_pair_pz;   //!
   TBranch        *b_pair_rapidity;   //!
   TBranch        *b_pair_theta;   //!
   TBranch        *b_pair_vx;   //!
   TBranch        *b_pair_vy;   //!
   TBranch        *b_pair_vz;   //!
   TBranch        *b_pair_mass60to120;   //!

   FitterTree(const std::string&, const std::string&, TTree *tree=0);
   virtual ~FitterTree();
   virtual Int_t    Cut(/*Long64_t entry*/);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop(TTree*, Float_t&, Float_t&, Int_t&, Int_t&, Float_t&, 
			 float realWeight = -1.0);
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef FitterTree_cxx
FitterTree::FitterTree(const std::string& file, const std::string& dir, TTree *tree)
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
     TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject(file.c_str());
      if (!f) {
	f = new TFile(file.c_str());
      }
      f->cd(dir.c_str());
      tree = (TTree*)gDirectory->Get("fitter_tree");

   }
   Init(tree);
}

FitterTree::~FitterTree()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t FitterTree::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t FitterTree::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (!fChain->InheritsFrom(TChain::Class()))  return centry;
   TChain *chain = (TChain*)fChain;
   if (chain->GetTreeNumber() != fCurrent) {
      fCurrent = chain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void FitterTree::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("probe_ecalRecHitSumEtConeDR03", &probe_ecalRecHitSumEtConeDR03, &b_probe_ecalRecHitSumEtConeDR03);
   fChain->SetBranchAddress("probe_ecalRecHitSumEtConeDR04", &probe_ecalRecHitSumEtConeDR04, &b_probe_ecalRecHitSumEtConeDR04);
   fChain->SetBranchAddress("probe_et", &probe_et, &b_probe_et);
   fChain->SetBranchAddress("probe_eta", &probe_eta, &b_probe_eta);
   fChain->SetBranchAddress("probe_hadronicOverEm", &probe_hadronicOverEm, &b_probe_hadronicOverEm);
   fChain->SetBranchAddress("probe_hasPixelSeed", &probe_hasPixelSeed, &b_probe_hasPixelSeed);
   fChain->SetBranchAddress("probe_hcalTowerSumEtConeDR03", &probe_hcalTowerSumEtConeDR03, &b_probe_hcalTowerSumEtConeDR03);
   fChain->SetBranchAddress("probe_hcalTowerSumEtConeDR04", &probe_hcalTowerSumEtConeDR04, &b_probe_hcalTowerSumEtConeDR04);
   fChain->SetBranchAddress("probe_isPhoton", &probe_isPhoton, &b_probe_isPhoton);
   fChain->SetBranchAddress("probe_phi", &probe_phi, &b_probe_phi);
   fChain->SetBranchAddress("probe_px", &probe_px, &b_probe_px);
   fChain->SetBranchAddress("probe_py", &probe_py, &b_probe_py);
   fChain->SetBranchAddress("probe_pz", &probe_pz, &b_probe_pz);
   fChain->SetBranchAddress("probe_sigmaIetaIeta", &probe_sigmaIetaIeta, &b_probe_sigmaIetaIeta);
   fChain->SetBranchAddress("probe_sigmaIphiIphi", &probe_sigmaIphiIphi, &b_probe_sigmaIphiIphi);
   fChain->SetBranchAddress("probe_trkSumPtHollowConeDR03", &probe_trkSumPtHollowConeDR03, &b_probe_trkSumPtHollowConeDR03);
   fChain->SetBranchAddress("probe_trkSumPtHollowConeDR04", &probe_trkSumPtHollowConeDR04, &b_probe_trkSumPtHollowConeDR04);
   fChain->SetBranchAddress("probe_dR1jet00", &probe_dR1jet00, &b_probe_dR1jet00);
   fChain->SetBranchAddress("probe_dR2jet00", &probe_dR2jet00, &b_probe_dR2jet00);
   fChain->SetBranchAddress("probe_dR3jet00", &probe_dR3jet00, &b_probe_dR3jet00);
   fChain->SetBranchAddress("probe_dRjet03", &probe_dRjet03, &b_probe_dRjet03);
   fChain->SetBranchAddress("probe_dRjet05", &probe_dRjet05, &b_probe_dRjet05);
   fChain->SetBranchAddress("probe_dRjet07", &probe_dRjet07, &b_probe_dRjet07);
   fChain->SetBranchAddress("probe_dRjet09", &probe_dRjet09, &b_probe_dRjet09);
   fChain->SetBranchAddress("probe_nJets03", &probe_nJets03, &b_probe_nJets03);
   fChain->SetBranchAddress("probe_nJets05", &probe_nJets05, &b_probe_nJets05);
   fChain->SetBranchAddress("probe_nJets07", &probe_nJets07, &b_probe_nJets07);
   fChain->SetBranchAddress("probe_nJets09", &probe_nJets09, &b_probe_nJets09);
   fChain->SetBranchAddress("probe_passing", &probe_passing, &b_probe_passing);
   fChain->SetBranchAddress("weight", &weight, &b_weight);
   fChain->SetBranchAddress("PUWeight", &PUWeight, &b_PUWeight);
   fChain->SetBranchAddress("run", &run, &b_run);
   fChain->SetBranchAddress("lumi", &lumi, &b_lumi);
   fChain->SetBranchAddress("event", &event, &b_event);
   fChain->SetBranchAddress("event_nPV", &event_nPV, &b_mNPV);
   fChain->SetBranchAddress("event_met_calomet", &event_met_calomet, &b_mMET);
   fChain->SetBranchAddress("event_met_calosumet", &event_met_calosumet, &b_mSumET);
   fChain->SetBranchAddress("event_met_calometsignificance", &event_met_calometsignificance, &b_mMETSign);
   fChain->SetBranchAddress("event_met_tcmet", &event_met_tcmet, &b_mtcMET);
   fChain->SetBranchAddress("event_met_tcsumet", &event_met_tcsumet, &b_mtcSumET);
   fChain->SetBranchAddress("event_met_tcmetsignificance", &event_met_tcmetsignificance, &b_mtcMETSign);
   fChain->SetBranchAddress("event_met_pfmet", &event_met_pfmet, &b_mpfMET);
   fChain->SetBranchAddress("event_met_pfsumet", &event_met_pfsumet, &b_mpfSumET);
   fChain->SetBranchAddress("event_met_pfmetsignificance", &event_met_pfmetsignificance, &b_mpfMETSign);
   fChain->SetBranchAddress("event_PrimaryVertex_x", &event_PrimaryVertex_x, &b_mPVx);
   fChain->SetBranchAddress("event_PrimaryVertex_y", &event_PrimaryVertex_y, &b_mPVy);
   fChain->SetBranchAddress("event_PrimaryVertex_z", &event_PrimaryVertex_z, &b_mPVz);
   fChain->SetBranchAddress("event_BeamSpot_x", &event_BeamSpot_x, &b_mBSx);
   fChain->SetBranchAddress("event_BeamSpot_y", &event_BeamSpot_y, &b_mBSy);
   fChain->SetBranchAddress("event_BeamSpot_z", &event_BeamSpot_z, &b_mBSz);
   fChain->SetBranchAddress("xsec", &xsec, &b_mXsec);
   fChain->SetBranchAddress("nEvts", &nEvts, &b_mNEvts);
   fChain->SetBranchAddress("mass", &mass, &b_mass);
   fChain->SetBranchAddress("mcTrue", &mcTrue, &b_mcTrue);
   fChain->SetBranchAddress("tag_photon_HoverE", &tag_photon_HoverE, &b_tag_photon_HoverE);
   fChain->SetBranchAddress("tag_photon_HoverE_Depth1", &tag_photon_HoverE_Depth1, &b_tag_photon_HoverE_Depth1);
   fChain->SetBranchAddress("tag_photon_HoverE_Depth2", &tag_photon_HoverE_Depth2, &b_tag_photon_HoverE_Depth2);
   fChain->SetBranchAddress("tag_photon_e1x5", &tag_photon_e1x5, &b_tag_photon_e1x5);
   fChain->SetBranchAddress("tag_photon_e2x5", &tag_photon_e2x5, &b_tag_photon_e2x5);
   fChain->SetBranchAddress("tag_photon_e5x5", &tag_photon_e5x5, &b_tag_photon_e5x5);
   fChain->SetBranchAddress("tag_photon_ecaliso_dr03", &tag_photon_ecaliso_dr03, &b_tag_photon_ecaliso_dr03);
   fChain->SetBranchAddress("tag_photon_ecaliso_dr04", &tag_photon_ecaliso_dr04, &b_tag_photon_ecaliso_dr04);
   fChain->SetBranchAddress("tag_photon_eta", &tag_photon_eta, &b_tag_photon_eta);
   fChain->SetBranchAddress("tag_photon_hasPixelSeed", &tag_photon_hasPixelSeed, &b_tag_photon_hasPixelSeed);
   fChain->SetBranchAddress("tag_photon_hcaliso_dr03", &tag_photon_hcaliso_dr03, &b_tag_photon_hcaliso_dr03);
   fChain->SetBranchAddress("tag_photon_hcaliso_dr04", &tag_photon_hcaliso_dr04, &b_tag_photon_hcaliso_dr04);
   fChain->SetBranchAddress("tag_photon_isEB", &tag_photon_isEB, &b_tag_photon_isEB);
   fChain->SetBranchAddress("tag_photon_isEBEEGap", &tag_photon_isEBEEGap, &b_tag_photon_isEBEEGap);
   fChain->SetBranchAddress("tag_photon_isEBEtaGap", &tag_photon_isEBEtaGap, &b_tag_photon_isEBEtaGap);
   fChain->SetBranchAddress("tag_photon_isEBPhiGap", &tag_photon_isEBPhiGap, &b_tag_photon_isEBPhiGap);
   fChain->SetBranchAddress("tag_photon_isEE", &tag_photon_isEE, &b_tag_photon_isEE);
   fChain->SetBranchAddress("tag_photon_isEEDeeGap", &tag_photon_isEEDeeGap, &b_tag_photon_isEEDeeGap);
   fChain->SetBranchAddress("tag_photon_isEERingGap", &tag_photon_isEERingGap, &b_tag_photon_isEERingGap);
   fChain->SetBranchAddress("tag_photon_phi", &tag_photon_phi, &b_tag_photon_phi);
   fChain->SetBranchAddress("tag_photon_pt", &tag_photon_pt, &b_tag_photon_pt);
   fChain->SetBranchAddress("tag_photon_px", &tag_photon_px, &b_tag_photon_px);
   fChain->SetBranchAddress("tag_photon_py", &tag_photon_py, &b_tag_photon_py);
   fChain->SetBranchAddress("tag_photon_pz", &tag_photon_pz, &b_tag_photon_pz);
   fChain->SetBranchAddress("tag_photon_sigmaEtaEta", &tag_photon_sigmaEtaEta, &b_tag_photon_sigmaEtaEta);
   fChain->SetBranchAddress("tag_photon_sigmaIetaIeta", &tag_photon_sigmaIetaIeta, &b_tag_photon_sigmaIetaIeta);
   fChain->SetBranchAddress("tag_photon_trackiso_dr03", &tag_photon_trackiso_dr03, &b_tag_photon_trackiso_dr03);
   fChain->SetBranchAddress("tag_photon_trackiso_dr04", &tag_photon_trackiso_dr04, &b_tag_photon_trackiso_dr04);
   fChain->SetBranchAddress("tag_sc_energy", &tag_sc_energy, &b_tag_sc_energy);
   fChain->SetBranchAddress("tag_sc_et", &tag_sc_et, &b_tag_sc_et);
   fChain->SetBranchAddress("tag_sc_eta", &tag_sc_eta, &b_tag_sc_eta);
   fChain->SetBranchAddress("tag_sc_etaWidth", &tag_sc_etaWidth, &b_tag_sc_etaWidth);
   fChain->SetBranchAddress("tag_sc_phi", &tag_sc_phi, &b_tag_sc_phi);
   fChain->SetBranchAddress("tag_sc_phiWidth", &tag_sc_phiWidth, &b_tag_sc_phiWidth);
   fChain->SetBranchAddress("tag_sc_preshowerEnergy", &tag_sc_preshowerEnergy, &b_tag_sc_preshowerEnergy);
   fChain->SetBranchAddress("tag_sc_rawEnergy", &tag_sc_rawEnergy, &b_tag_sc_rawEnergy);
   fChain->SetBranchAddress("tag_sc_size", &tag_sc_size, &b_tag_sc_size);
   fChain->SetBranchAddress("tag_sc_x", &tag_sc_x, &b_tag_sc_x);
   fChain->SetBranchAddress("tag_sc_y", &tag_sc_y, &b_tag_sc_y);
   fChain->SetBranchAddress("tag_sc_z", &tag_sc_z, &b_tag_sc_z);
   fChain->SetBranchAddress("tag_flag", &tag_flag, &b_tag_flag);
   fChain->SetBranchAddress("mc_probe_charge", &mc_probe_charge, &b_mc_probe_charge);
   fChain->SetBranchAddress("mc_probe_e", &mc_probe_e, &b_mc_probe_e);
   fChain->SetBranchAddress("mc_probe_et", &mc_probe_et, &b_mc_probe_et);
   fChain->SetBranchAddress("mc_probe_eta", &mc_probe_eta, &b_mc_probe_eta);
   fChain->SetBranchAddress("mc_probe_mass", &mc_probe_mass, &b_mc_probe_mass);
   fChain->SetBranchAddress("mc_probe_mt", &mc_probe_mt, &b_mc_probe_mt);
   fChain->SetBranchAddress("mc_probe_p", &mc_probe_p, &b_mc_probe_p);
   fChain->SetBranchAddress("mc_probe_phi", &mc_probe_phi, &b_mc_probe_phi);
   fChain->SetBranchAddress("mc_probe_pt", &mc_probe_pt, &b_mc_probe_pt);
   fChain->SetBranchAddress("mc_probe_px", &mc_probe_px, &b_mc_probe_px);
   fChain->SetBranchAddress("mc_probe_py", &mc_probe_py, &b_mc_probe_py);
   fChain->SetBranchAddress("mc_probe_pz", &mc_probe_pz, &b_mc_probe_pz);
   fChain->SetBranchAddress("mc_probe_rapidity", &mc_probe_rapidity, &b_mc_probe_rapidity);
   fChain->SetBranchAddress("mc_probe_theta", &mc_probe_theta, &b_mc_probe_theta);
   fChain->SetBranchAddress("mc_probe_vx", &mc_probe_vx, &b_mc_probe_vx);
   fChain->SetBranchAddress("mc_probe_vy", &mc_probe_vy, &b_mc_probe_vy);
   fChain->SetBranchAddress("mc_probe_vz", &mc_probe_vz, &b_mc_probe_vz);
   fChain->SetBranchAddress("mc_probe_flag", &mc_probe_flag, &b_mc_probe_flag);
   fChain->SetBranchAddress("pair_e", &pair_e, &b_pair_e);
   fChain->SetBranchAddress("pair_et", &pair_et, &b_pair_et);
   fChain->SetBranchAddress("pair_eta", &pair_eta, &b_pair_eta);
   fChain->SetBranchAddress("pair_mass", &pair_mass, &b_pair_mass);
   fChain->SetBranchAddress("pair_mt", &pair_mt, &b_pair_mt);
   fChain->SetBranchAddress("pair_p", &pair_p, &b_pair_p);
   fChain->SetBranchAddress("pair_phi", &pair_phi, &b_pair_phi);
   fChain->SetBranchAddress("pair_pt", &pair_pt, &b_pair_pt);
   fChain->SetBranchAddress("pair_px", &pair_px, &b_pair_px);
   fChain->SetBranchAddress("pair_py", &pair_py, &b_pair_py);
   fChain->SetBranchAddress("pair_pz", &pair_pz, &b_pair_pz);
   fChain->SetBranchAddress("pair_rapidity", &pair_rapidity, &b_pair_rapidity);
   fChain->SetBranchAddress("pair_theta", &pair_theta, &b_pair_theta);
   fChain->SetBranchAddress("pair_vx", &pair_vx, &b_pair_vx);
   fChain->SetBranchAddress("pair_vy", &pair_vy, &b_pair_vy);
   fChain->SetBranchAddress("pair_vz", &pair_vz, &b_pair_vz);
   fChain->SetBranchAddress("pair_mass60to120", &pair_mass60to120, &b_pair_mass60to120);
   Notify();
}

Bool_t FitterTree::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void FitterTree::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t FitterTree::Cut(/*Long64_t entry*/)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef FitterTree_cxx
