#include "PhysicsTools/TagAndProbe/interface/PlotAux.h"

PlotAux::PlotAux()
{
  plotColors_.push_back(1);
  plotColors_.push_back(2);
  plotColors_.push_back(3);
}

PlotAux::PlotAux(const VUINT& plotColors) { plotColors_ = plotColors; }

PlotAux::PlotAux(const PlotAux& otherPlotAux) :
  plotColors_(otherPlotAux.getPlotColors()) {}

PlotAux::~PlotAux() {}

PlotAux& PlotAux::operator=(const PlotAux& otherPlotAux)
{
  if (this != &otherPlotAux) plotColors_ = otherPlotAux.getPlotColors();
  return *this;
}

VUINT PlotAux::getPlotColors() const { return plotColors_; }

void PlotAux::setPlotColors(const VUINT& plotColors) { plotColors_ = plotColors; }

STRING PlotAux::name(const STRING& part1, const STRING& part2) const
{
  VSTRING vec;
  vec.push_back(part1);
  vec.push_back(part2);
  return name(vec);
}

STRING PlotAux::name(const VSTRING& parts) const
{
  std::stringstream nameStream;
  for (VSTRING_IT iPart = parts.begin(); iPart != parts.end(); ++iPart) { nameStream << *iPart; }
  return nameStream.str();
}

void PlotAux::setFitOptions(TF1* fit, const unsigned int fileIndex) const
{
  fit->SetLineColor(plotColors_[fileIndex]);
  fit->SetLineStyle(2); //dotted
}

void PlotAux::setGraphOptions(TGraphAsymmErrors* graph, const unsigned int fileIndex) const
{
  std::stringstream graphName;
  graphName << "graph" << fileIndex;
  graph->SetName(graphName.str().c_str());
  graph->SetMarkerStyle(20 + fileIndex);
  unsigned int color = plotColors_[fileIndex];
  graph->SetMarkerColor(color);
  graph->SetLineColor(color);
}

void PlotAux::setMultiGraphOptions(TMultiGraph* graph, const std::string& title, 
				   const bool MCTruth, const bool parPlot) const
{
  graph->GetXaxis()->SetTitleColor(1);
  graph->GetYaxis()->SetTitleColor(1);
  graph->GetXaxis()->SetTitleFont(42);
  graph->GetYaxis()->SetTitleFont(42);
  graph->GetXaxis()->SetTitleSize(0.06);
  graph->GetYaxis()->SetTitleSize(0.06);
  graph->GetXaxis()->SetTitleOffset(0.9);
  graph->GetYaxis()->SetTitleOffset(1.05);
  graph->GetXaxis()->SetLabelColor(1);
  graph->GetYaxis()->SetLabelColor(1);
  graph->GetXaxis()->SetLabelFont(42);
  graph->GetYaxis()->SetLabelFont(42);
  graph->GetXaxis()->SetLabelSize(0.05);
  graph->GetXaxis()->SetLabelOffset(0.007);
  graph->GetYaxis()->SetLabelOffset(0.007);
  graph->GetXaxis()->SetAxisColor(1);
  graph->GetYaxis()->SetAxisColor(1);
  graph->GetXaxis()->SetDecimals(kTRUE);
  graph->GetYaxis()->SetDecimals(kTRUE);
  graph->GetXaxis()->SetTickLength(0.03);
  graph->GetYaxis()->SetTickLength(0.03);
  graph->GetXaxis()->SetNdivisions(510);
  graph->GetYaxis()->SetNdivisions(510);
  graph->GetXaxis()->SetTitle(title.c_str());
  std::string theString(graph->GetName());
  if (!parPlot) {
    if (theString.find("ScaleFactor") != std::string::npos) {
      if (!MCTruth) {
	graph->GetYaxis()->SetTitle("#epsilon_{data}/#epsilon_{MC}");
	graph->GetYaxis()->SetRangeUser(0.0, 1.5);
	graph->GetYaxis()->SetLabelSize(0.05);
      }
      else {
	graph->GetYaxis()->SetTitle("#epsilon_{tag and probe} - #epsilon_{MC truth matching}");
	graph->GetYaxis()->SetRangeUser(-0.05, 0.05);
	graph->GetYaxis()->SetLabelSize(0.03);
      }
    }
    else {
      graph->GetYaxis()->SetTitle("Efficiency");
      graph->GetYaxis()->SetRangeUser(0.0, 1.1);
    }
  }
  else graph->GetYaxis()->SetTitle("parameter value");
}

void PlotAux::setLegendOptions(TLegend* legend) const
{
  legend->SetTextFont(42);
  legend->SetTextSize(0.02);
  legend->SetShadowColor(0);
  legend->SetLineColor(0);
  legend->SetFillColor(0);
}

void PlotAux::setCanvasOptions(TCanvas* canvas) const
{
  canvas->SetCanvasSize(600, 600);
  canvas->SetBorderMode(0);
  canvas->SetFillColor(kWhite);
  canvas->SetGridx(false);
  canvas->SetGridy(false);
  canvas->SetFrameBorderMode(0);
  canvas->SetFrameBorderSize(1);
  canvas->SetFrameFillColor(0);
  canvas->SetFrameFillStyle(0);
  canvas->SetFrameLineColor(1);
  canvas->SetFrameLineStyle(1);
  canvas->SetFrameLineWidth(1);
  canvas->SetTopMargin(0.05);
  canvas->SetBottomMargin(0.13);
  canvas->SetLeftMargin(0.13);
  canvas->SetRightMargin(0.05);
  canvas->SetTickx(1);
  canvas->SetTicky(1);
}
