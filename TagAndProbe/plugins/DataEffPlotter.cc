#include <memory>
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "PhysicsTools/TagAndProbe/interface/Typedefs.h"
#include "TFile.h"
#include "TCanvas.h"
#include "RooHist.h"
#include "TMultiGraph.h"
#include "TAxis.h"
#include "TLegend.h"
#include "TPaveStats.h"
#include "TH1F.h"

class DataEffPlotter : public edm::EDAnalyzer {
public:
  DataEffPlotter(const edm::ParameterSet& pset);
  virtual ~DataEffPlotter();
  virtual void analyze(const edm::Event& event, const edm::EventSetup& eventSetup) {};
  virtual void endRun(const edm::Run &run, const edm::EventSetup &setup) {};

  /*************all functions related to comparing the same data and MC efficiency*************/

  /*plot data and MC efficiencies (for both tag and probe and MC truth methods) on the same axes, 
    and make scale factor plots*/
  void overlayDataEffPlots();

  //create a name by concatenating the 2 given strings
  STRING name(const STRING&, const STRING&);

  //set ROOT fit graphics options
  void setFitOptions(TF1*, const unsigned int);

  //set ROOT TGraphAsymmErrors graphics options
  void setGraphOptions(TGraphAsymmErrors*, const unsigned int);

  //set ROOT TMultiGraph graphics options
  void setMultiGraphOptions(TMultiGraph*, const STRING&);

  //set ROOT TLegend graphics options
  void setLegendOptions(TLegend*);

  //set ROOT TCanvas graphics options
  void setCanvasOptions(TCanvas*);

  /********************************************************************************************/

  /***************all functions related to comparing different data efficiencies***************/

  /*plot different efficiencies vs. the same variable each on its own canvas for a given binning 
    variable*/
  void plotEffsVsVarMultipleCanvases(const STRING&, const STRING&, const float, const float, 
				     const STRING&, const STRING&);

  /*plot different efficiencies vs. the same variable all on the same canvas for a given binning 
    variable*/
  void plotEffsVsVarSingleCanvas(const STRING&, const STRING&, const float, const float, 
				 const STRING&, const unsigned int, const STRING&);

  /*plot different efficiencies vs. the same variable on the same axes, and plot individual 
    efficiencies on their own axes, for all binning variables supplied in cfg file*/
  void plotTagAndProbeEffs();

  /*for each efficiency variable, plot efficiency vs. that variable, comparing >=2 different 
    selections or methods on the same axes*/  
  void compareSelectionsOrMethods();

  /*get name of tag and probe efficiency canvas from efficiency directory name, efficiency binning 
    variable, name of the leaf corresponding to that binning variable, and any additional cuts*/
  STRING efficiencyCanvasName(const STRING&, const STRING&, const STRING&, const STRING&) const;

  //get a pointer to the tag and probe efficiency plot cast to a TGraphAsymmErrors
  TGraphAsymmErrors* getTagAndProbeEfficiencyPlot(const STRING&, TFile*);

  /*set ROOT TGraphAsymmErrors graphics options; if TMultiGraph is supplied, add the 
    TGraphAsymmErrors to it*/
  void setGraphOptions(TGraphAsymmErrors*, TLegend&, const unsigned int, 
		       TMultiGraph* effMultiGraph = NULL) const;

  //set ROOT TLegend graphics options
  void setLegendOptions(TLegend&) const;

  //set ROOT TCanvas graphics options
  void setCanvasOptions(TCanvas&, const STRING&, const float, const float) const;

  //update canvas and write file, optionally save canvas separately as PDF
  void updateAndWrite(TFile*, TCanvas&, const STRING& fileName = "");

  /********************************************************************************************/

  /********************************all functions related to I/O********************************/

  //open input files
  void openInputFiles();

  //open output file
  void openOutputFile();

  //close input files and free memory
  void closeInputFiles();

  //close output files and free memory
  void closeOutputFile();

  //check that inputs are consistent (no vector size mismatches that would cause segfaults, etc.)
  bool checkInputs() const;

  /********************************************************************************************/

private:

  //input parameters
  VSTRING inputFiles_;
  STRING outputFile_;
  VSTRING legendEntries_;
  VUINT plotColors_;
  VSTRING effVars_;
  VSTRING canvasFileNames_;
  VSTRING plotNames_;
  VSTRING units_;
  std::vector<double> fitLowerLim_;
  std::vector<double> fitUpperLim_;
  bool MCTruth_;
  bool doEffFits_;
  unsigned int opt_;
  VSTRING effDirs_;
  VSTRING cuts_;
  VSTRING effVarLeaves_;
  VDOUBLE xAxisLowerLim_;
  VDOUBLE xAxisUpperLim_;

  //vectors to hold the ROOT objects needed to make the efficiency plots
  std::vector<TMultiGraph*> multigraphs_;
  std::vector<TLegend*> legends_;
  std::vector<TH1F*> hists_;
  std::vector<TCanvas*> effCanvases_;
  std::vector<TCanvas*> scaleFactorCanvases_;
  std::vector<TMultiGraph*> scaleFactorMultigraphs_;

  //I/O
  VTFILE input_;
  TFile* output_;
};

DataEffPlotter::DataEffPlotter(const edm::ParameterSet& pset) :
  inputFiles_(pset.getParameter<VSTRING>("inputFiles")),
  outputFile_(pset.getParameter<STRING>("outputFile")),
  legendEntries_(pset.getParameter<VSTRING>("legendEntries")),
  plotColors_(pset.getParameter<VUINT>("plotColors")),
  effVars_(pset.getParameter<VSTRING>("effVars")),
  canvasFileNames_(pset.getParameter<VSTRING>("canvasFileNames")),
  plotNames_(pset.getParameter<VSTRING>("plotNames")),
  units_(pset.getParameter<VSTRING>("units")),
  fitLowerLim_(pset.getParameter<std::vector<double> >("fitLowerLim")),
  fitUpperLim_(pset.getParameter<std::vector<double> >("fitUpperLim")),
  MCTruth_(pset.getParameter<bool>("MCTruth")),
  doEffFits_(pset.getParameter<bool>("doEffFits")),
  opt_(pset.getParameter<unsigned int>("opt")),
  effDirs_(pset.getParameter<VSTRING>("effDirs")),
  cuts_(pset.getParameter<VSTRING>("cuts")),
  effVarLeaves_(pset.getParameter<VSTRING>("effVarLeaves")),
  xAxisLowerLim_(pset.getParameter<VDOUBLE>("xAxisLowerLim")),
  xAxisUpperLim_(pset.getParameter<VDOUBLE>("xAxisUpperLim"))
{
  //I/O
  openInputFiles();
  openOutputFile();

  //sanity check
  if (!checkInputs()) cerr << "Error: vector size mismatch.\n";
  else {

    //decide which task to perform
    if (opt_ == 1) overlayDataEffPlots();
    else if (opt_ == 2) plotTagAndProbeEffs();
    else if ((opt_ == 3) || (opt_ == 4)) compareSelectionsOrMethods();
    else cerr << "Error: " << opt_ << " is not a recognizable option.\n";
  }

  //close files
  closeInputFiles();
  closeOutputFile();
}

DataEffPlotter::~DataEffPlotter()
{
  for (std::vector<TMultiGraph*>::iterator i = multigraphs_.begin(); i != multigraphs_.end(); 
       ++i) { delete *i; }
  for (std::vector<TLegend*>::iterator i = legends_.begin(); i != legends_.end(); 
       ++i) { delete *i; }
  for (std::vector<TCanvas*>::iterator i = effCanvases_.begin(); i != effCanvases_.end(); 
       ++i) { delete *i; }
  for (std::vector<TCanvas*>::iterator i = scaleFactorCanvases_.begin(); 
       i != scaleFactorCanvases_.end(); ++i) { delete *i; }
  for (std::vector<TMultiGraph*>::iterator i = scaleFactorMultigraphs_.begin(); 
       i != scaleFactorMultigraphs_.end(); ++i) { delete *i; }
}

void DataEffPlotter::overlayDataEffPlots()
{
  //grab all efficiency graphs from input files and put them in TMultiGraph objects
  //create canvas legends for all efficiency graphs
  for (VSTRING_IT iEffVar = effVars_.begin(); iEffVar != effVars_.end(); ++iEffVar) {
    multigraphs_.push_back(new TMultiGraph(name(*iEffVar, "Multigraph").c_str(), ""));
    if (*iEffVar == "pT") legends_.push_back(new TLegend(0.4, 0.2, 0.8, 0.4));
    else legends_.push_back(new TLegend(0.2, 0.2, 0.6, 0.4));
    hists_.push_back(NULL);
    effCanvases_.push_back(new TCanvas(name(*iEffVar, "OutputCanvas").c_str(), "", 600, 600));
    scaleFactorCanvases_.push_back(new TCanvas(name(*iEffVar, "ScaleFactorCanvas").c_str(), "", 
					       600, 600));
    scaleFactorMultigraphs_.push_back(new TMultiGraph(name(*iEffVar, 
							   "ScaleFactorMultigraph").c_str(), ""));
  }

  //loop over the input files
  for (std::vector<TFile*>::const_iterator iInput = input_.begin(); iInput != input_.end(); 
       ++iInput) {
    const STRING fileName = inputFiles_[iInput - input_.begin()];

    //check that the file is valid
    if (*iInput != NULL) {
      const unsigned int fileIndex = iInput - input_.begin();
      const STRING legendEntry = legendEntries_[fileIndex];

      //loop over efficiency variables
      for (VSTRING_IT iEffVar = effVars_.begin(); iEffVar != effVars_.end(); ++iEffVar) {
	const unsigned int effVarIndex = iEffVar - effVars_.begin();

	//is this a tag and probe efficiency file?
	if (!MCTruth_) {
	  TCanvas* inputCanvas = NULL;
	  (*iInput)->GetObject(plotNames_[effVarIndex].c_str(), inputCanvas);
	  if (inputCanvas != NULL) {

	    //get the efficiency graph, set plotting options, and add it to the multigraph
	    TGraphAsymmErrors* graph = dynamic_cast<TGraphAsymmErrors*>
	      ((RooHist*)(inputCanvas->GetPrimitive("hxy_fit_eff")));
	    if (doEffFits_) {
	      graph->Fit("pol0", "RE", "", fitLowerLim_[effVarIndex], fitUpperLim_[effVarIndex]);
	      setFitOptions(graph->GetFunction("pol0"), fileIndex);
	    }
	    setGraphOptions(graph, fileIndex);
	    multigraphs_[effVarIndex]->Add(graph);
	    legends_[effVarIndex]->AddEntry(graph, legendEntry.c_str(), "lep");
	  }//if (inputCanvas != NULL)
	  else {
	    std::cerr << "Error getting canvas " << plotNames_[effVarIndex] << " from file ";
	    std::cerr << fileName << ".\n";
	  }
	}//if (!MCTruth)

	//is this a MC truth efficiency file?
	else {
	  (*iInput)->GetObject(plotNames_[effVarIndex].c_str(), hists_[effVarIndex]);
	  if (hists_[effVarIndex] != NULL) {
	    hists_[effVarIndex]->SetMarkerStyle(20);
	    legends_[effVarIndex]->AddEntry(hists_[effVarIndex], legendEntry.c_str(), "lep");
	  }
	  else {
	    std::cerr << "Error getting histogram " << plotNames_[effVarIndex] << " from file ";
	    std::cerr << fileName << ".\n";
	  }
	}//else (i.e. MCTruth == true)

      }//for (VSTRING_IT iEffVar = effVars_.begin(); iEffVar != effVars_.end(); ++iEffVar)

    }//if (*iInput != NULL)
    else std::cerr << "Error opening file " << fileName << ".\n";

  }/*for (std::vector<TFile*>::const_iterator iInput = input_.begin(); iInput != input_.end(); 
     ++iInput)*/

  //loop over efficiency variables
  for (VSTRING_IT iEffVar = effVars_.begin(); iEffVar != effVars_.end(); ++iEffVar) {
    const unsigned int index = iEffVar - effVars_.begin();

    //draw real efficiency comparison plot
    setCanvasOptions(effCanvases_[index]);
    effCanvases_[index]->cd();
    multigraphs_[index]->Draw("APZ");
    legends_[index]->Draw();
    setLegendOptions(legends_[index]);
    setMultiGraphOptions(multigraphs_[index], units_[index]);
    effCanvases_[index]->Update();

    //are there exactly two inputs to divide?
    vector<double> effVar;
    vector<double> effVarErrLower;
    vector<double> effVarErrUpper;
    vector<double> effVarScale;
    vector<double> effVarScaleErr;
    if /*(*/(inputFiles_.size() == 2)/* && (effVars_[index] != "nPV"))*/ { //MC should only have 0-1 PV
      setCanvasOptions(scaleFactorCanvases_[index]);
      scaleFactorCanvases_[index]->cd();

      //get the efficiency graphs to be divided
      TList* graphs = multigraphs_[index]->GetListOfGraphs();
      TGraphAsymmErrors* graph1 = (TGraphAsymmErrors*)graphs->FindObject("graph0");
      TGraphAsymmErrors* graph2 = (TGraphAsymmErrors*)graphs->FindObject("graph1");

      //is this a calculation of eff(tag and probe) - eff(MC truth)?
      if (MCTruth_) {
	if (graph1 != NULL) {
	  if (graph1->GetN() == hists_[index]->GetNbinsX()) {

	    //calculate the values needed to fill the difference graph
	    for (int i = 0; i <= graph1->GetN(); ++i) {
	      double x1, y1, x2, y2, y1Err, y2Err;
	      graph1->GetPoint(i, x1, y1);
	      y1Err = graph1->GetErrorYlow(i); //symmetric error assumption
	      x2 = hists_[index]->GetBinLowEdge(i + 1) + ((hists_[index]->GetBinWidth(i + 1))/2);
	      y2 = hists_[index]->GetBinContent(i + 1);
	      y2Err = hists_[index]->GetBinError(i + 1);
	      effVar.push_back(x2);
	      effVarScale.push_back(y1 - y2);
	      effVarErrLower.push_back(0.0);
	      effVarErrUpper.push_back(0.0);
	      effVarScaleErr.push_back(sqrt((y1Err*y1Err) + (y2Err*y2Err)));
	    }//for (int i = 0; i <= graph1->GetN(); ++i)

	  }//if (graph1->GetN() == hists_[index]->GetNbinsX())
	  else {
	    std::cerr << "Error: graph1->GetN() = " << graph1->GetN();
	    std::cerr << ", hists_[index]->GetNbinsX() = " << hists_[index]->GetNbinsX() << ".\n";
	  }

	}//if (graph1 != NULL)
	else {
	  std::cerr << "Error getting graph graph0 from multigraph ";
	  std::cerr << multigraphs_[index]->GetName() << ".\n";
	}

      }//if (MCTruth_)

      //is this a calculation of data/MC scale factor?
      else {
	if ((graph1 != NULL) && (graph2 != NULL)) {
	  if (graph1->GetN() == graph2->GetN()) {

	    //calculate the values needed to fill the scale factor graph
	    for (int i = 0; i <= graph1->GetN(); ++i) {
	      double x1, y1, x2, y2, y1Err, y2Err;
	      graph1->GetPoint(i, x1, y1);
	      y1Err = graph1->GetErrorYlow(i);
	      graph2->GetPoint(i, x2, y2);
	      y2Err = graph2->GetErrorYlow(i);
	      effVar.push_back(x2);
	      effVarScale.push_back(y1/y2);
	      std::cout << "scale: " << y1/y2 << std::endl;
	      effVarErrLower.push_back(0.0);
	      effVarErrUpper.push_back(0.0);
	      effVarScaleErr.push_back((y1/y2)*
				       sqrt(((y1Err*y1Err)/(y1*y1)) + ((y2Err*y2Err)/(y2*y2))));
	      std::cout << "error: " << (y1/y2)*sqrt(((y1Err*y1Err)/(y1*y1)) + ((y2Err*y2Err)/(y2*y2))) << std::endl;
	    }//for (int i = 0; i <= graph1->GetN(); ++i)

	  }//if (graph1->GetN() == graph2->GetN())
	  else {
	    std::cerr << "Error: graph1->GetN() = " << graph1->GetN();
	    std::cerr << ", graph2->GetN() = " << graph2->GetN() << ".\n";
	  }

	}//if ((graph1 != NULL) && (graph2 != NULL))
	else {
	  std::cerr << "Error getting graphs graph0 and/or graph1 from multigraph ";
	  std::cerr << multigraphs_[index]->GetName() << ": graph1 = " << graph1 << ", graph2 = ";
	  std::cerr << graph2 << ".\n";
	}

      }//else (i.e. MCTruth = false)

      //draw the difference or scale factor plot
      TGraphAsymmErrors* scaleFactor = new TGraphAsymmErrors(graph1->GetN(), &effVar[0], 
							     &effVarScale[0], &effVarErrLower[0], 
							     &effVarErrUpper[0], 
							     &effVarScaleErr[0], 
							     &effVarScaleErr[0]);
      setGraphOptions(scaleFactor, 0);
      scaleFactor->Fit("pol0", "RE", "", fitLowerLim_[index], fitUpperLim_[index]);
      setFitOptions(scaleFactor->GetFunction("pol0"), 0);
      scaleFactorMultigraphs_[index]->Add(scaleFactor); //keep graphics simple
      scaleFactorMultigraphs_[index]->Draw("APZ");
      setMultiGraphOptions(scaleFactorMultigraphs_[index], units_[index]);
      scaleFactorCanvases_[index]->Update();

    }//((inputFiles_.size() == 2) && (effVars_[index] != "nPV"))
  }//for (VSTRING_IT iEffVar = effVars_.begin(); iEffVar != effVars_.end(); ++iEffVar)

  //write to output file
  if ((output_ != NULL) && (output_->IsOpen())) {
    output_->cd();
    for (std::vector<TCanvas*>::iterator iCanvas = effCanvases_.begin(); 
	 iCanvas != effCanvases_.end(); ++iCanvas) { (*iCanvas)->Write(); }
    for (std::vector<TH1F*>::iterator iHist = hists_.begin(); iHist != hists_.end(); 
	 ++iHist) { if (*iHist != NULL) (*iHist)->Write(); }
    for (std::vector<TCanvas*>::iterator iCanvas = scaleFactorCanvases_.begin(); 
	 iCanvas != scaleFactorCanvases_.end(); ++iCanvas) { (*iCanvas)->Write(); }
    output_->Write();
  }
}

STRING DataEffPlotter::name(const STRING& part1, const STRING& part2)
{
  std::stringstream nameStream;
  nameStream << part1 << part2;
  return nameStream.str();
}

void DataEffPlotter::setFitOptions(TF1* fit, const unsigned int fileIndex)
{
  fit->SetLineColor(plotColors_[fileIndex]);
  fit->SetLineStyle(2); //dotted
}

void DataEffPlotter::setGraphOptions(TGraphAsymmErrors* graph, const unsigned int fileIndex)
{
  std::stringstream graphName;
  graphName << "graph" << fileIndex;
  graph->SetName(graphName.str().c_str());
  graph->SetMarkerStyle(20 + fileIndex);
  unsigned int color = plotColors_[fileIndex];
  graph->SetMarkerColor(color);
  graph->SetLineColor(color);
}

void DataEffPlotter::setMultiGraphOptions(TMultiGraph* graph, const std::string& title)
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
  if (string(graph->GetName()).find("ScaleFactor") != string::npos) {
    if (!MCTruth_) {
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

void DataEffPlotter::setLegendOptions(TLegend* legend)
{
  legend->SetTextFont(42);
  legend->SetTextSize(0.02);
  legend->SetShadowColor(0);
  legend->SetLineColor(0);
  legend->SetFillColor(0);
}

void DataEffPlotter::setCanvasOptions(TCanvas* canvas)
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

void DataEffPlotter::plotEffsVsVarMultipleCanvases(const STRING& effVar, const STRING& unit, 
						   const float xAxisLowerLim, 
						   const float xAxisUpperLim, 
						   const STRING& effVarLeaf, const STRING& cut)
{
  //loop over all efficiencies
  for (VSTRING_IT iEffDir = effDirs_.begin(); iEffDir != effDirs_.end(); ++iEffDir) {
    const unsigned int index = iEffDir - effDirs_.begin();

    //create canvas for individual efficiency graph
    STRINGSTREAM indEffCanvasName;
    indEffCanvasName << "effCanvas" << *iEffDir << "_" << effVar;
    TCanvas indEffCanvas(indEffCanvasName.str().c_str(), "", 600, 600);
    setCanvasOptions(indEffCanvas, unit.c_str(), xAxisLowerLim, xAxisUpperLim);

    //create legend
    TLegend indLegend(0.15, 0.33, 0.65, 0.63);
    setLegendOptions(indLegend);

    //get the efficiency plots
    TGraphAsymmErrors* effVsVar = 
      getTagAndProbeEfficiencyPlot(efficiencyCanvasName(*iEffDir, effVar, effVarLeaf, cut), 
				   input_[index]);

    //set graphics options for the individual efficiency graph
    output_->cd();
    indEffCanvas.cd();
    setGraphOptions(effVsVar, indLegend, index);

    //draw the individual efficiency plots and legend on the canvas
    if (effVsVar != NULL) effVsVar->Draw("P");
    indLegend.Draw();
    indEffCanvas.Draw();

    //update and write individual efficiency canvas
    updateAndWrite(output_, indEffCanvas);
  }
}

void DataEffPlotter::plotEffsVsVarSingleCanvas(const STRING& effVar, const STRING& unit, 
					       const float xAxisLowerLim, 
					       const float xAxisUpperLim, 
					       const STRING& effVarLeaf, const unsigned int i, 
					       const STRING& cut)
{
  //create canvas
  STRINGSTREAM effCanvasName;
  effCanvasName << "effCanvasAll" << "_" << effVar;
  TCanvas effCanvas(effCanvasName.str().c_str(), "", 600, 600);
  setCanvasOptions(effCanvas, unit.c_str(), xAxisLowerLim, xAxisUpperLim);

  //create legend
  TLegend legend(0.15, 0.33, 0.65, 0.63);
  setLegendOptions(legend);

  //loop over all efficiencies
  TMultiGraph effMultiGraph;
  for (VSTRING_IT iEffDir = effDirs_.begin(); iEffDir != effDirs_.end(); ++iEffDir) {
    const unsigned int index = iEffDir - effDirs_.begin();

    /*for the case where the efficiency variable name is different in the different files because 
      it's a PU-subtracted efficiency*/
    STRING theEffVar;
    if (opt_ == 4) {
      if (legendEntries_[index].find("#rho") != string::npos) theEffVar = effVar + "Rho";
      else if (legendEntries_[index].find("n_{PV}") != string::npos) theEffVar = effVar + "NPV";
      else theEffVar = effVar;
    }
    else theEffVar = effVar;

    //get the efficiency plots
    TGraphAsymmErrors* effVsVar = 
      getTagAndProbeEfficiencyPlot(efficiencyCanvasName(*iEffDir, theEffVar, effVarLeaf, cut), 
				   input_[index]);

    //set graphics options for the efficiency graph and add to the multigraph
    output_->cd();
    effCanvas.cd();
    setGraphOptions(effVsVar, legend, index, &effMultiGraph);
  }

  //draw the efficiency plots and legend on the same canvas
  output_->cd();
  effCanvas.cd();
  effMultiGraph.Draw("P");
  legend.Draw();

  //update and write efficiency canvas and save canvas as a PDF
  if (opt_ == 4) updateAndWrite(output_, effCanvas, canvasFileNames_[i]);
  else updateAndWrite(output_, effCanvas);
}

void DataEffPlotter::plotTagAndProbeEffs()
{
  //loop over efficiency variables
  for (VSTRING_IT iEffVar = effVars_.begin(); iEffVar != effVars_.end(); ++iEffVar) {

    /*for each efficiency variable, make a single plot of all efficiencies vs. that variable AND 
      individual plots of each efficiency vs. that variable*/
    const unsigned int i = iEffVar - effVars_.begin();
    plotEffsVsVarSingleCanvas(*iEffVar, units_[i], (float)xAxisLowerLim_[i], 
			      (float)xAxisUpperLim_[i], effVarLeaves_[i], i, cuts_[i]);
    plotEffsVsVarMultipleCanvases(*iEffVar, units_[i], (float)xAxisLowerLim_[i], 
				  (float)xAxisUpperLim_[i], effVarLeaves_[i], cuts_[i]);
  }
}

void DataEffPlotter::compareSelectionsOrMethods()
{
  //loop over efficiency variables
  for (VSTRING_IT iEffVar = effVars_.begin(); iEffVar != effVars_.end(); ++iEffVar) {

    /*for each efficiency variable, plot efficiency vs. that variable, comparing >=2 different 
      selections or methods on the same axes*/
    const unsigned int i = iEffVar - effVars_.begin();
    plotEffsVsVarSingleCanvas(*iEffVar, units_[i], (float)xAxisLowerLim_[i], 
			      (float)xAxisUpperLim_[i], effVarLeaves_[i], i, cuts_[i]);
  }
}

STRING DataEffPlotter::efficiencyCanvasName(const STRING& inputDir, const STRING& effVar, 
					    const STRING& varName, const STRING& cut) const
{
  STRINGSTREAM name;
  name << inputDir << "/" << effVar << "/fit_eff_plots/" << varName << "_PLOT" << cut;
  return name.str();
}

TGraphAsymmErrors* DataEffPlotter::getTagAndProbeEfficiencyPlot(const STRING& effCanvasName, 
								TFile* file)
{
  TGraphAsymmErrors* effGraph = NULL;
  TCanvas* effCanvas = NULL;
  if (file != NULL) {
    file->GetObject(effCanvasName.c_str(), effCanvas);
    if (effCanvas == NULL) {
      cerr << "Error getting TCanvas object " << effCanvasName;
      cerr << " from file " << file->GetName() << ".\n";
    }
    else {
      effGraph = 
	dynamic_cast<TGraphAsymmErrors*>((RooHist*)(effCanvas->GetPrimitive("hxy_fit_eff")));
      if (effGraph == NULL) {
	cerr << "Error getting RooHist object hxy_fit_eff ";
	cerr << "from file " << file->GetName() << ".\n";
      }
    }
  }
  return effGraph;
}

void DataEffPlotter::setGraphOptions(TGraphAsymmErrors* effGraph, TLegend& legend, 
				     const unsigned int iMarker, TMultiGraph* effMultiGraph) const
{
  if (effGraph != NULL) {
    effGraph->SetMarkerStyle(20 + iMarker);
    effGraph->SetMarkerColor(iMarker + 1);
    effGraph->SetLineColor(iMarker + 1);
    if (effMultiGraph != NULL) effMultiGraph->Add(effGraph);
    legend.AddEntry(effGraph, (legendEntries_[iMarker]).c_str(), "P");
  }
  else cerr << "Error: TGraphAsymmErrors is null.\n";
}

void DataEffPlotter::setLegendOptions(TLegend& legend) const
{
  legend.SetFillColor(0);
  legend.SetFillStyle(0);
  legend.SetTextFont(42);
  legend.SetShadowColor(0);
  legend.SetLineColor(0);
}

void DataEffPlotter::setCanvasOptions(TCanvas& canvas, const STRING& xAxisLabel, 
				      const float xAxisLowerLim, const float xAxisUpperLim) const
{
  canvas.SetFillStyle(0);
  canvas.SetFillColor(0);
  canvas.SetGrid();
  TH1F* frame = canvas.DrawFrame(xAxisLowerLim, 0.3, xAxisUpperLim, 1.1);
  frame->GetXaxis()->SetTitle(xAxisLabel.c_str());
  frame->GetYaxis()->SetTitle("Efficiency");
}

void DataEffPlotter::updateAndWrite(TFile* file, TCanvas& canvas, const STRING& fileName)
{
  canvas.Update();
  canvas.Write();
  file->Write();
  if (fileName != "") canvas.SaveAs(fileName.c_str());
}

void DataEffPlotter::openInputFiles()
{
  for (VSTRING_IT iInputFile = inputFiles_.begin(); iInputFile != inputFiles_.end(); 
       ++iInputFile) {
    TFile* pFile = NULL;
    try { pFile = new TFile((*iInputFile).c_str()); }
    catch (cms::Exception& ex) { cerr << ex.what(); }
    input_.push_back(pFile);
  }
}

void DataEffPlotter::openOutputFile()
{
  output_ = NULL;
  try { output_ = new TFile(outputFile_.c_str(), "RECREATE"); }
  catch (cms::Exception& ex) { cerr << ex.what(); }
}

void DataEffPlotter::closeInputFiles()
{
  for (VTFILE_IT iInput = input_.begin(); iInput != input_.end(); ++iInput) {
    (*iInput)->Close();
    delete *iInput;
  }
}

void DataEffPlotter::closeOutputFile()
{
  output_->Close();
  delete output_;
}

bool DataEffPlotter::checkInputs() const
{
  bool ok = false;
  if (legendEntries_.size() == inputFiles_.size()) {
    if ((opt_ == 1) && (inputFiles_.size() == plotColors_.size()) && 
	(effVars_.size() == plotNames_.size()) && (plotNames_.size() == units_.size())) {
      if (doEffFits_ == true) {
	if ((units_.size() == fitLowerLim_.size()) && 
	    (fitLowerLim_.size() == fitUpperLim_.size())) ok = true;
      }
      else ok = true;
    }
    else if (((opt_ == 2) || (opt_ == 3) || (opt_ == 4)) && 
	     (inputFiles_.size() == effDirs_.size()) && (effVars_.size() == units_.size()) && 
	     (units_.size() == effVarLeaves_.size()) && 
	     (effVarLeaves_.size() == xAxisLowerLim_.size()) && 
	     (xAxisLowerLim_.size() == xAxisUpperLim_.size())) {
      ok = true;
    }
  }
  return ok;
}

//define this as a plug-in
DEFINE_FWK_MODULE(DataEffPlotter);
