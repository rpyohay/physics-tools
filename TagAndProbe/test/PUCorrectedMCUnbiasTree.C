#define PUCorrectedMCUnbiasTree_cxx
#include "PUCorrectedMCUnbiasTree.h"
#include "../../../DataFormats/Math/interface/deltaR.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>

void PUCorrectedMCUnbiasTree::Loop(TTree* tree, Float_t& totalWeight, Float_t& SCEta, 
				   Int_t& probePassingRhoSigmaIetaIetaEB, 
				   Int_t& probePassingNPVSigmaIetaIetaEB, float realWeight)
{
//   In a ROOT session, you can do:
//      Root > .L PUCorrectedMCUnbiasTree.C
//      Root > PUCorrectedMCUnbiasTree t
//      Root > t.GetEntry(12); // Fill t data members with entry number 12
//      Root > t.Show();       // Show values of entry 12
//      Root > t.Show(16);     // Read and show values of entry 16
//      Root > t.Loop();       // Loop on all entries
//

//     This is the loop skeleton where:
//    jentry is the global entry number in the chain
//    ientry is the entry number in the current Tree
//  Note that the argument to GetEntry must be:
//    jentry for TChain::GetEntry
//    ientry for TTree::GetEntry and TBranch::GetEntry
//
//       To read only selected branches, Insert statements like:
// METHOD1:
//    fChain->SetBranchStatus("*",0);  // disable all branches
//    fChain->SetBranchStatus("branchname",1);  // activate branchname
// METHOD2: replace line
//    fChain->GetEntry(jentry);       //read all branches
//by  b_branchname->GetEntry(ientry); //read only this branch
   if (fChain == 0) return;

   Long64_t nentries = fChain->GetEntriesFast();

   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      // if (Cut(ientry) < 0) continue;
      if (realWeight != -1.0) weight = realWeight;
      totalWeight = (Float_t)(PUWeight)*weight;
      SCEta = 0.0;
      probePassingRhoSigmaIetaIetaEB = 
	((probe_passing_rho == 1) && (probe_sigmaIetaIeta < 0.011)) ? 1 : 0;
      probePassingNPVSigmaIetaIetaEB = 
	((probe_passing_nPV == 1) && (probe_sigmaIetaIeta < 0.011)) ? 1 : 0;
      tree->Fill();
   }
}
