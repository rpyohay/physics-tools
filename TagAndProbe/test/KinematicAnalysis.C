#include <string>
#include <iostream>
#include "DataTree.h"
#include "MCTree.h"
#include "TH3F.h"
#include "TH2F.h"
#include "TCanvas.h"
#include "TLegend.h"

void makeMCTreeClass()
{
  TChain MCTree("PhotonToIDEB/fitter_tree");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_G_Pt-15to30_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_G_Pt-30to50_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_G_Pt-50to80_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_G_Pt-80to120_TuneZ2_7TeV_pythia6-Summer11-PU_S4_START42_V11-v1/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_G_Pt-120to170_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_G_Pt-170to300_TuneZ2_7TeV_pythia6-Summer11-PU_S4_START42_V11-v1/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_G_Pt-300to470_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_G_Pt-470to800_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_G_Pt-800to1400_TuneZ2_7TeV_pythia6-Summer11-PU_S4_START42_V11-v1/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_G_Pt-1400to1800_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_G_Pt-1800_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_ZJetToEE_Pt-15to20_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_ZJetToEE_Pt-20to30_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_ZJetToEE_Pt-30to50_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_ZJetToEE_Pt-50to80_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_ZJetToEE_Pt-80to120_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_ZJetToEE_Pt-120to170_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_ZJetToEE_Pt-170to230_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_ZJetToEE_Pt-230to300_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_ZJetToEE_Pt-300_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_QCD_Pt-15to30_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_QCD_Pt-30to50_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_QCD_Pt-50to80_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_QCD_Pt-80to120_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_QCD_Pt-120to170_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_QCD_Pt-170to300_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_QCD_Pt-300to470_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_QCD_Pt-470to600_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_QCD_Pt-600to800_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_QCD_Pt-800to1000_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_QCD_Pt-1000to1400_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_QCD_Pt-1400to1800_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_QCD_Pt-1800_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_TT_TuneZ2_7TeV-pythia6-tauola-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_WToENu_TuneZ2_7TeV-pythia6-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_DYToTauTau_M-20_TuneZ2_7TeV-pythia6-tauola-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.Add("/data2/yohay/eff_MC/analysis_CMSSWv425_defaultPU_WToTauNu_TuneZ2_7TeV-pythia6-tauola-Summer11-PU_S3_START42_V11-v2/tagProbeTree_MC_photonToID_final.root");
  MCTree.MakeClass("MCTree");
}

template<typename T>
unsigned int loop(T& tree, TH3F* hist3D, TH2F* hist2D)
{
  unsigned int nEvtsRead = 0;
  unsigned int nEB = 0;
  Long64_t N = tree.fChain->GetEntriesFast();
  for (Long64_t iEvt = 0; iEvt < N; ++iEvt) {
    Long64_t localEntry = tree.LoadTree(iEvt);
    if (localEntry < 0) break;
    ++nEvtsRead;
    tree.fChain->GetEntry(iEvt);
    TObject* object = tree.fChain->GetListOfBranches()->FindObject("totalWeight");
    TBranch* branch = NULL;
    Float_t totalWeight = 1.0;
    if (object != 0) {
      branch = (TBranch*)object;
      totalWeight = *(Float_t*)branch->GetAddress();
    }
    if (fabs(tree.probe_SC_eta) < 1.4442) {
      ++nEB;
      hist3D->Fill(tree.dRTagProbe, tree.probe_nJets05, tree.event_nPV, totalWeight);
      hist2D->Fill(tree.dRTagProbe, tree.probe_passing, totalWeight);
    }
  }
  cout << "No. of probes in EB: " << nEB << endl;
  return nEvtsRead;
}

void setCanvasOptions(TCanvas& canvas)
{
  canvas.SetWindowSize(610,630);
  canvas.SetFillStyle(0);
  canvas.SetFillColor(0);
  canvas.SetGrid();
  canvas.SetBorderMode(0);
  canvas.SetFrameBorderMode(0);
  canvas.SetFrameBorderSize(1);
  canvas.SetFrameFillColor(0);
  canvas.SetFrameFillStyle(0);
  canvas.SetFrameLineColor(1);
  canvas.SetFrameLineStyle(1);
  canvas.SetFrameLineWidth(1);
  canvas.SetTopMargin(0.05);
  canvas.SetBottomMargin(0.13);
  canvas.SetLeftMargin(0.13);
  canvas.SetRightMargin(0.05);
  canvas.SetTickx(1);
  canvas.SetTicky(1);
  TH1F* frame = canvas.DrawFrame(0.0, 0.0, 5.0, 1.0);
  frame->GetXaxis()->SetTitle("#DeltaR_{tag-probe}");
  frame->GetYaxis()->SetTitle("Unit-normalized events per 0.1");
  frame->GetXaxis()->SetTitleColor(1);
  frame->GetYaxis()->SetTitleColor(1);
  frame->GetXaxis()->SetTitleFont(42);
  frame->GetYaxis()->SetTitleFont(42);
  frame->GetXaxis()->SetTitleSize(0.06);
  frame->GetYaxis()->SetTitleSize(0.06);
  frame->GetXaxis()->SetTitleOffset(0.9);
  frame->GetYaxis()->SetTitleOffset(1.05);
  frame->GetXaxis()->SetLabelColor(1);
  frame->GetYaxis()->SetLabelColor(1);
  frame->GetXaxis()->SetLabelFont(42);
  frame->GetYaxis()->SetLabelFont(42);
  frame->GetXaxis()->SetLabelSize(0.05);
  frame->GetXaxis()->SetLabelOffset(0.007);
  frame->GetYaxis()->SetLabelOffset(0.007);
  frame->GetXaxis()->SetAxisColor(1);
  frame->GetYaxis()->SetAxisColor(1);
  frame->GetXaxis()->SetDecimals(kTRUE);
  frame->GetYaxis()->SetDecimals(kTRUE);
  frame->GetXaxis()->SetTickLength(0.03);
  frame->GetYaxis()->SetTickLength(0.03);
  frame->GetXaxis()->SetNdivisions(510);
  frame->GetYaxis()->SetNdivisions(510);
}

void writeToCanvas(TCanvas& canvas, TH1D* hist1, TH1D* hist2, TLegend& legend)
{
  setCanvasOptions(canvas);
  hist1->Scale(1.0/hist1->Integral());
  hist2->Scale(1.0/hist2->Integral());
  hist1->SetLineColor(8);
  hist2->SetLineColor(9);
  hist1->SetLineWidth(2);
  hist2->SetLineWidth(2);
  hist1->SetFillStyle(0);
  hist2->SetFillStyle(0);
  string title(canvas.GetTitle());
  size_t slashPos = title.find('/');
  legend.AddEntry(hist1, title.substr(0, slashPos).c_str(), "L");
  legend.AddEntry(hist2, title.substr(slashPos + 1, string::npos).c_str(), "L");
  legend.SetTextFont(42);
  legend.SetTextSize(0.02);
  legend.SetShadowColor(0);
  legend.SetLineColor(0);
  legend.SetFillStyle(0);
  canvas.cd();
  hist1->Draw();
  hist2->Draw("SAME");
  legend.Draw();
}

void write(TFile& file, TH3F* hist, const string& label)
{
  //cd to file
  file.cd();
  hist->Write();

  //make projections
  TH1D* dRTagProbe = hist->ProjectionX(("dRTagProbe" + label).c_str(), 0, -1, 0, -1);
  TH1D* dRTagProbe0j = hist->ProjectionX(("dRTagProbe0j" + label).c_str(), 1, 1, 0, -1);
  TH1D* dRTagProbe1j = hist->ProjectionX(("dRTagProbe1j" + label).c_str(), 2, 2, 0, -1);
  TH1D* dRTagProbe1To4PV = 
    hist->ProjectionX(("dRTagProbe1To4PV" + label).c_str(), 0, -1, 1, 4);
  TH1D* dRTagProbeGreaterEqual5PV = 
    hist->ProjectionX(("dRTagProbeGreaterEqual5PV" + label).c_str(), 0, -1, 5, -1);
  TH1D* dRTagProbe0j1To4PV = 
    hist->ProjectionX(("dRTagProbe0j1To4PV" + label).c_str(), 1, 1, 1, 4);
  TH1D* dRTagProbe0jGreaterEqual5PV = 
    hist->ProjectionX(("dRTagProbe0jGreaterEqual5PV" + label).c_str(), 1, 1, 5, -1);
  TH1D* dRTagProbe1j1To4PV = 
    hist->ProjectionX(("dRTagProbe1j1To4PV" + label).c_str(), 2, 2, 1, 4);
  TH1D* dRTagProbe1jGreaterEqual5PV = 
    hist->ProjectionX(("dRTagProbe1jGreaterEqual5PV" + label).c_str(), 2, 2, 5, -1);

  //draw pairs of unit-normalized histograms on the same axes
  TCanvas dRTagProbe0And1Jet(("dRTagProbe0And1Jet" + label).c_str(), "0 jets/1 jet", 600, 600);
  TLegend legend0And1Jet(0.7, 0.8, 0.9, 0.9);
  writeToCanvas(dRTagProbe0And1Jet, dRTagProbe0j, dRTagProbe1j, legend0And1Jet);
  TCanvas dRTagProbe1To4AndGreaterEqual5PV(("dRTagProbe1To4AndGreaterEqual5PV" + label).c_str(), 
					   "1-4 PVs/#geq5 PVs", 600, 600);
  TLegend legend1To4AndGreaterEqual5PV(0.7, 0.8, 0.9, 0.9);
  writeToCanvas(dRTagProbe1To4AndGreaterEqual5PV, dRTagProbe1To4PV, dRTagProbeGreaterEqual5PV, 
		legend1To4AndGreaterEqual5PV);
  TCanvas dRTagProbe0j1To4AndGreaterEqual5PV(("dRTagProbe0j1To4AndGreaterEqual5PV" + 
					      label).c_str(), 
					     "0 jets, 1-4 PVs/0 jets, #geq5 PVs", 600, 600);
  TLegend legend0j1To4AndGreaterEqual5PV(0.7, 0.8, 0.9, 0.9);
  writeToCanvas(dRTagProbe0j1To4AndGreaterEqual5PV, dRTagProbe0j1To4PV, 
		dRTagProbe0jGreaterEqual5PV, legend0j1To4AndGreaterEqual5PV);
  TCanvas dRTagProbe1j1To4AndGreaterEqual5PV(("dRTagProbe1j1To4AndGreaterEqual5PV" + 
					      label).c_str(), 
					     "1 jet, 1-4 PVs/1 jet, #geq5 PVs", 600, 600);
  TLegend legend1j1To4AndGreaterEqual5PV(0.7, 0.8, 0.9, 0.9);
  writeToCanvas(dRTagProbe1j1To4AndGreaterEqual5PV, dRTagProbe1j1To4PV, 
		dRTagProbe1jGreaterEqual5PV, legend1j1To4AndGreaterEqual5PV);
  TCanvas dRTagProbe0And1Jet1To4PV(("dRTagProbe0And1Jet1To4PV" + label).c_str(), 
				   "0 jets, 1-4 PVs/1 jet, 1-4 PVs", 600, 600);
  TLegend legend0And1j1To4PV(0.7, 0.8, 0.9, 0.9);
  writeToCanvas(dRTagProbe0And1Jet1To4PV, dRTagProbe0j1To4PV, dRTagProbe1j1To4PV, 
		legend0And1j1To4PV);
  TCanvas dRTagProbe0And1JetGreaterEqual5PV(("dRTagProbe0And1JetGreaterEqual5PV" + 
					     label).c_str(), 
					    "0 jets, #geq5 PVs/1 jet, #geq5 PVs", 600, 600);
  TLegend legend0And1jGreaterEqual5PV(0.7, 0.8, 0.9, 0.9);
  writeToCanvas(dRTagProbe0And1JetGreaterEqual5PV, dRTagProbe0jGreaterEqual5PV, 
		dRTagProbe1jGreaterEqual5PV, legend0And1jGreaterEqual5PV);

  //write canvases
  dRTagProbe0And1Jet.Write();
  dRTagProbe1To4AndGreaterEqual5PV.Write();
  dRTagProbe0j1To4AndGreaterEqual5PV.Write();
  dRTagProbe1j1To4AndGreaterEqual5PV.Write();
  dRTagProbe0And1Jet1To4PV.Write();
  dRTagProbe0And1JetGreaterEqual5PV.Write();

  //write histograms
  dRTagProbe->Write();
}

void analyzeDRTagProbe(const string& outputFile)
{
  //read trees
  DataTree data;
  if (data.fChain == 0) {
    cerr << "Error: DataTree object has no associated tree.\n";
    return;
  }
  MCTree MC;
  if (MC.fChain == 0) {
    cerr << "Error: MCTree object has no associated tree.\n";
    return;
  }

  //histograms
  TH3F* dRTagProbeVsNjVsNPVData = new TH3F("dRTagProbeVsNjVsNPVData", "", 
					   50, 0.0, 5.0, 5, -0.5, 4.5, 20, 0.5, 20.5);
  TH3F* dRTagProbeVsNjVsNPVMC = new TH3F("dRTagProbeVsNjVsNPVMC", "", 
					 50, 0.0, 5.0, 5, -0.5, 4.5, 20, 0.5, 20.5);
  TH2F* dRTagProbeVsProbePassingData = new TH2F("dRTagProbeVsProbePassingData", "", 
						50, 0.0, 5.0, 2, -0.5, 1.5);
  TH2F* dRTagProbeVsProbePassingMC = new TH2F("dRTagProbeVsProbePassingMC", "", 
					      50, 0.0, 5.0, 2, -0.5, 1.5);

  //loop
  cout << "No. data events read: ";
  cout << loop(data, dRTagProbeVsNjVsNPVData, dRTagProbeVsProbePassingData) << endl;
  cout << "No. MC events read: ";
  cout << loop(MC, dRTagProbeVsNjVsNPVMC, dRTagProbeVsProbePassingMC) << endl;

  //write histograms to output file
  TFile out(outputFile.c_str(), "RECREATE");
  if (!out.IsOpen()) {
    cerr << "Error: cannot open file " << outputFile << ".\n";
    delete dRTagProbeVsNjVsNPVData;
    delete dRTagProbeVsNjVsNPVMC;
    return;
  }
  out.cd();
  write(out, dRTagProbeVsNjVsNPVData, "Data");
  write(out, dRTagProbeVsNjVsNPVMC, "MC");
  dRTagProbeVsProbePassingData->Write();
  dRTagProbeVsProbePassingMC->Write();
  out.Write();
  out.Close();
  delete dRTagProbeVsNjVsNPVData;
  delete dRTagProbeVsNjVsNPVMC;
}
