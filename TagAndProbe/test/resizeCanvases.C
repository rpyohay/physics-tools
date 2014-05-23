{
  #include <vector>

  //load code to be compiled
  gROOT->Reset();
  gROOT->LoadMacro("/afs/cern.ch/user/y/yohay/scratch0/CMSSW_4_2_3/src/PhysicsTools/TagAndProbe/test/PrettyHistMaker.C++");

  //configurables
  const std::string tag = "effWithR9";
  const bool MCTruth = false;
  const unsigned int numInputFiles = 2;
  const unsigned int blue = 857;
  const unsigned int green = 834;
  const unsigned int purple = 619;
  std::vector<unsigned int> colors;
  colors.push_back(blue);
  colors.push_back(green);
  colors.push_back(purple);

  //no PU correction, ET only
  makeScaleFactorHist(dRTagProbeScaleFactorCanvas, "dRTagProbe", tag);
  makeEffHist(dRTagProbeOutputCanvas, "dRTagProbe", tag);

  /*pTOutputCanvas->Draw();
  pTOutputCanvas->SetCanvasSize(600,600);
  pTOutputCanvas->SetWindowSize(610,630);
  TMultiGraph* pTMultiGraph = (TMultiGraph*)pTOutputCanvas->GetPrimitive("pTMultiGraph");
  TList* pTGraphs = pTMultiGraph->GetListOfGraphs();
  for (unsigned int iGraph = 0; iGraph < numInputFiles; ++iGraph) {
    std::stringstream graphName;
    graphName << "graph" << iGraph;
    TGraph* graph = (TGraph*)pTGraphs->FindObject(graphName.str().c_str());
    if (graph != 0) {
      TPaveStats* pStats = (TPaveStats*)graph->GetListOfFunctions()->FindObject("stats");
      double y1 = pStats->GetY1NDC();
      double y2 = pStats->GetY2NDC();
      double x1 = pStats->GetX1NDC();
      double x2 = pStats->GetX2NDC();
      pStats->SetY1NDC(y1 - 0.25 - iGraph*(y2 - y1));
      pStats->SetY2NDC(y1 - 0.25 - (iGraph + 1)*(y2 - y1));
      pStats->SetX1NDC(x1 - 0.1);
      pStats->SetX2NDC(x2 - 0.1);
      pStats->SetTextSize(0.02);
      pStats->SetTextColor(colors[iGraph]);
      pStats->SetLineColor(0);
    }
    else std::cerr << "Error: object named graph" << iGraph << " could not be found.\n";
  }
  if (MCTruth) {
    effVsPT_->Fit("pol0", "RE", "SAMES", 35.0, 120.0);
    effVsPT_->GetFunction("pol0")->SetLineStyle(2);
    effVsPT_->GetFunction("pol0")->SetLineColor(1);
    effVsPT_->GetFunction("pol0")->SetLineWidth(2);
    effVsPT_->Draw("PSAMES");
    gPad->Update();
    TPaveStats* pTStats = (TPaveStats*)effVsPT_->FindObject("stats");
    double y1 = pTStats->GetY1NDC();
    double y2 = pTStats->GetY2NDC();
    double x1 = pTStats->GetX1NDC();
    double x2 = pTStats->GetX2NDC();
    pTStats->SetY1NDC(y1 - 0.25 - numInputFiles*(y2 - y1));
    pTStats->SetY2NDC(y1 - 0.25 - (numInputFiles + 1)*(y2 - y1));
    pTStats->SetX1NDC(x1 - 0.1);
    pTStats->SetX2NDC(x2 - 0.1);
    pTStats->SetTextSize(0.02);
    pTStats->SetLineColor(0);
  }
  std::stringstream pTFile;
  pTFile << "/data/yohay/comparison_" << tag << "_pT.pdf";
  pTOutputCanvas->SaveAs(pTFile.str().c_str());
  etaOutputCanvas->Draw();
  etaOutputCanvas->SetCanvasSize(600,600);
  etaOutputCanvas->SetWindowSize(610,630);
  TMultiGraph* etaMultiGraph = (TMultiGraph*)etaOutputCanvas->GetPrimitive("etaMultiGraph");
  TList* etaGraphs = etaMultiGraph->GetListOfGraphs();
  for (unsigned int iGraph = 0; iGraph < numInputFiles; ++iGraph) {
    std::stringstream graphName;
    graphName << "graph" << iGraph;
    TGraph* graph = (TGraph*)etaGraphs->FindObject(graphName.str().c_str());
    if (graph != 0) {
      TPaveStats* pStats = (TPaveStats*)graph->GetListOfFunctions()->FindObject("stats");
      double y1 = pStats->GetY1NDC();
      double y2 = pStats->GetY2NDC();
      double x1 = pStats->GetX1NDC();
      double x2 = pStats->GetX2NDC();
      pStats->SetY1NDC(y1 - 0.25 - iGraph*(y2 - y1));
      pStats->SetY2NDC(y1 - 0.25 - (iGraph + 1)*(y2 - y1));
      pStats->SetX1NDC(x1 - 0.1);
      pStats->SetX2NDC(x2 - 0.1);
      pStats->SetTextSize(0.02);
      pStats->SetTextColor(colors[iGraph]);
      pStats->SetLineColor(0);
    }
    else std::cerr << "Error: object named graph" << iGraph << " could not be found.\n";
  }
  if (MCTruth) {
    effVsEta_->Fit("pol0", "RE", "SAMES", -1.6, 1.6);
    effVsEta_->GetFunction("pol0")->SetLineStyle(2);
    effVsEta_->GetFunction("pol0")->SetLineColor(1);
    effVsEta_->GetFunction("pol0")->SetLineWidth(2);
    effVsEta_->Draw("PSAMES");
    gPad->Update();
    TPaveStats* etaStats = (TPaveStats*)effVsEta_->FindObject("stats");
    double y1 = etaStats->GetY1NDC();
    double y2 = etaStats->GetY2NDC();
    double x1 = etaStats->GetX1NDC();
    double x2 = etaStats->GetX2NDC();
    etaStats->SetY1NDC(y1 - 0.25 - numInputFiles*(y2 - y1));
    etaStats->SetY2NDC(y1 - 0.25 - (numInputFiles + 1)*(y2 - y1));
    etaStats->SetX1NDC(x1 - 0.1);
    etaStats->SetX2NDC(x2 - 0.1);
    etaStats->SetTextSize(0.02);
    etaStats->SetLineColor(0);
  }
  std::stringstream etaFile;
  etaFile << "/data/yohay/comparison_" << tag << "_eta.pdf";
  etaOutputCanvas->SaveAs(etaFile.str().c_str());
  //dRJets05OutputCanvas->Draw();
  //dRJets05OutputCanvas->SetCanvasSize(600,600);
  //dRJets05OutputCanvas->SetWindowSize(610,630);
  //if (MCTruth) effVsDRPhotonJet_->Draw("PSAME");
  //std::stringstream dRJets05File;
  //dRJets05File << "/data/yohay/comparison_" << tag << "_dRJets05.pdf";
  dRJets09OutputCanvas->Draw();
  dRJets09OutputCanvas->SetCanvasSize(600,600);
  dRJets09OutputCanvas->SetWindowSize(610,630);
  if (MCTruth) effVsDRPhotonJet_->Draw("PSAME");
  std::stringstream dRJets09File;
  dRJets09File << "/data/yohay/comparison_" << tag << "_dRJets09.pdf";
  dRJets09OutputCanvas->SaveAs(dRJets09File.str().c_str());
  //nJets05OutputCanvas->Draw();
  //nJets05OutputCanvas->SetCanvasSize(600,600);
  //nJets05OutputCanvas->SetWindowSize(610,630);
  //if (MCTruth) effVsNJets_->Draw("PSAME");
  //std::stringstream nJets05File;
  //nJets05File << "/data/yohay/comparison_" << tag << "_nJets05.pdf";
  //nJets05OutputCanvas->SaveAs(nJets05File.str().c_str());
  nJets09OutputCanvas->Draw();
  nJets09OutputCanvas->SetCanvasSize(600,600);
  nJets09OutputCanvas->SetWindowSize(610,630);
  if (MCTruth) effVsNJets_->Draw("PSAME");
  std::stringstream nJets09File;
  nJets09File << "/data/yohay/comparison_" << tag << "_nJets09.pdf";
  nJets09OutputCanvas->SaveAs(nJets09File.str().c_str());
  nPVOutputCanvas->Draw();
  nPVOutputCanvas->SetCanvasSize(600,600);
  nPVOutputCanvas->SetWindowSize(610,630);
  TMultiGraph* nPVMultiGraph = (TMultiGraph*)nPVOutputCanvas->GetPrimitive("nPVMultiGraph");
  TList* nPVGraphs = nPVMultiGraph->GetListOfGraphs();
  for (unsigned int iGraph = 0; iGraph < numInputFiles; ++iGraph) {
    std::stringstream graphName;
    graphName << "graph" << iGraph;
    TGraph* graph = (TGraph*)nPVGraphs->FindObject(graphName.str().c_str());
    if (graph != 0) {
      TPaveStats* pStats = (TPaveStats*)graph->GetListOfFunctions()->FindObject("stats");
      double y1 = pStats->GetY1NDC();
      double y2 = pStats->GetY2NDC();
      double x1 = pStats->GetX1NDC();
      double x2 = pStats->GetX2NDC();
      pStats->SetY1NDC(y1 - 0.25 - iGraph*(y2 - y1));
      pStats->SetY2NDC(y1 - 0.25 - (iGraph + 1)*(y2 - y1));
      pStats->SetX1NDC(x1 - 0.1);
      pStats->SetX2NDC(x2 - 0.1);
      pStats->SetTextSize(0.02);
      pStats->SetTextColor(colors[iGraph]);
      pStats->SetLineColor(0);
    }
    else std::cerr << "Error: object named graph" << iGraph << " could not be found.\n";
  }
  std::stringstream nPVFile;
  nPVFile << "/data/yohay/comparison_" << tag << "_nPV.pdf";
  nPVOutputCanvas->SaveAs(nPVFile.str().c_str());*/
}
