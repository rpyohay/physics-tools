#ifndef PUCorrectedMCUnbiasTree_h
#define PUCorrectedMCUnbiasTree_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

class PUCorrectedMCUnbiasTree {
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
   Float_t         probe_PUNPVSubtractedECALIso04;
   Float_t         probe_PUNPVSubtractedHCALIso04;
   Float_t         probe_PURhoSubtractedECALIso04;
   Float_t         probe_PURhoSubtractedHCALIso04;
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
   Int_t           probe_passing_nPV;
   Int_t           probe_passing_rho;
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
   TBranch        *b_probe_PUNPVSubtractedECALIso04;   //!
   TBranch        *b_probe_PUNPVSubtractedHCALIso04;   //!
   TBranch        *b_probe_PURhoSubtractedECALIso04;   //!
   TBranch        *b_probe_PURhoSubtractedHCALIso04;   //!
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
   TBranch        *b_probe_passing_nPV;   //!
   TBranch        *b_probe_passing_rho;   //!
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

   PUCorrectedMCUnbiasTree(const std::string&, const std::string&, TTree *tree=0);
   virtual ~PUCorrectedMCUnbiasTree();
   virtual Int_t    Cut(/*Long64_t entry*/);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop(TTree*, Float_t&, Float_t&, Int_t&, Int_t&, float realWeight = -1.0);
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef PUCorrectedMCUnbiasTree_cxx
PUCorrectedMCUnbiasTree::PUCorrectedMCUnbiasTree(const std::string& file, const std::string& dir, 
						 TTree *tree)
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject(file.c_str());
      if (!f) {
         f = new TFile(file.c_str());
      }
      f->cd(dir.c_str());
      tree = (TTree*)gDirectory->Get("mcUnbias_tree");

   }
   Init(tree);
}

PUCorrectedMCUnbiasTree::~PUCorrectedMCUnbiasTree()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t PUCorrectedMCUnbiasTree::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t PUCorrectedMCUnbiasTree::LoadTree(Long64_t entry)
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

void PUCorrectedMCUnbiasTree::Init(TTree *tree)
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
   fChain->SetBranchAddress("probe_PUNPVSubtractedECALIso04", &probe_PUNPVSubtractedECALIso04, &b_probe_PUNPVSubtractedECALIso04);
   fChain->SetBranchAddress("probe_PUNPVSubtractedHCALIso04", &probe_PUNPVSubtractedHCALIso04, &b_probe_PUNPVSubtractedHCALIso04);
   fChain->SetBranchAddress("probe_PURhoSubtractedECALIso04", &probe_PURhoSubtractedECALIso04, &b_probe_PURhoSubtractedECALIso04);
   fChain->SetBranchAddress("probe_PURhoSubtractedHCALIso04", &probe_PURhoSubtractedHCALIso04, &b_probe_PURhoSubtractedHCALIso04);
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
   fChain->SetBranchAddress("probe_passing_nPV", &probe_passing_nPV, &b_probe_passing_nPV);
   fChain->SetBranchAddress("probe_passing_rho", &probe_passing_rho, &b_probe_passing_rho);
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
   Notify();
}

Bool_t PUCorrectedMCUnbiasTree::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void PUCorrectedMCUnbiasTree::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t PUCorrectedMCUnbiasTree::Cut(/*Long64_t entry*/)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef PUCorrectedMCUnbiasTree_cxx
