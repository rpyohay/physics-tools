#ifndef PhysicsTools_TagAndProbe_PlotAux_h
#define PhysicsTools_TagAndProbe_PlotAux_h

#include <vector>
#include <sstream>
#include "TGraphAsymmErrors.h"
#include "TMultiGraph.h"
#include "TLegend.h"
#include "TCanvas.h"
#include "TAxis.h"

//space-saving typedefs
typedef std::string STRING;
typedef std::vector<STRING> VSTRING;
typedef VSTRING::const_iterator VSTRING_IT;
typedef std::vector<unsigned int> VUINT;
typedef std::vector<double> VDOUBLE;

class PlotAux {

 public:

  //constructors and assignment operator
  PlotAux();
  PlotAux(const VUINT&);
  PlotAux(const PlotAux&);
  ~PlotAux();
  PlotAux& operator=(const PlotAux&);

  //getters and setters
  VUINT getPlotColors() const;
  void setPlotColors(const VUINT&);

  //all kinds of graphical properties of plots
  STRING name(const STRING&, const STRING&) const;
  STRING name(const VSTRING&) const;
  void setFitOptions(TF1*, const unsigned int) const;
  void setGraphOptions(TGraphAsymmErrors*, const unsigned int) const;
  void setMultiGraphOptions(TMultiGraph*, const STRING&, const bool, const bool) const;
  void setLegendOptions(TLegend*) const;
  void setCanvasOptions(TCanvas*) const;

 private:
  VUINT plotColors_;

};

#endif
