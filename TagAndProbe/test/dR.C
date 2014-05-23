{
  TFile* data1 = new TFile("/data/yohay/tagProbeTree_data/38EGReReco_photonToID/tagProbeTree_data_photonToID_nPVGreater0.root");
  TFile* data2 = new TFile("/data/yohay/tagProbeTree_data/38PhotonPromptReco_photonToID/tagProbeTree_data_photonToID_nPVGreater0.root");
  TFile* MC = new TFile("/data/yohay/tagProbeTree_MC_MCANCuts/tagProbeTree_MC_photonToID_nPVGreater0.root");
  TTree* dataTree1;
  TTree* dataTree2;
  TTree* MCTree;
  data1->GetObject("PhotonToID/fitter_tree", dataTree1);
  data2->GetObject("PhotonToID/fitter_tree", dataTree2);
  MC->GetObject("PhotonToID/fitter_tree", MCTree);
  dataTree1->Draw("probe_dRjet03 >> dataDR1(50, 0.0, 5.0)");
  dataTree2->Draw("probe_dRjet03 >> dataDR2(50, 0.0, 5.0)");
  MCTree->Draw("probe_dRjet03 >> MCDR(50, 0.0, 5.0)");
  TH1F* dataDR1 = (TH1F*)gDirectory->Get("dataDR1");
  TH1F* dataDR2 = (TH1F*)gDirectory->Get("dataDR2");
  TH1F* MCDR = (TH1F*)gDirectory->Get("MCDR");
  dataDR1->Add(dataDR2);
  MCDR->Scale(dataDR1->Integral(1, 50)/MCDR->Integral(1, 50));
  dataDR1->SetLineColor(kRed);
  dataDR1->SetLineWidth(2);
  MCDR->SetLineWidth(2);
  TCanvas* canvas = new TCanvas("canvas", "", 600, 600);
  canvas->cd();
  dataDR1->Draw();
  MCDR->Draw("SAME");
}
