// -*- C++ -*-
//
// Package:    PUWeightProducer
// Class:      PUWeightProducer
// 
/**\class PUWeightProducer PUWeightProducer.cc PhysicsTools/TagAndProbe/plugins/PUWeightProducer.cc

 Description: make a product to hold the PU weight for each event

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Rachel Yohay,512 1-010,+41227670495,
//         Created:  Tue Jun  7 15:13:15 CEST 2011
// $Id: PUWeightProducer.cc,v 1.6 2012/04/13 14:05:26 yohay Exp $
//
//


// system include files
#include <memory>
#include <iomanip>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/LuminosityBlock.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "PhysicsTools/TagAndProbe/interface/Typedefs.h"

//
// class declaration
//

class PUWeightProducer : public edm::EDProducer {
   public:
      explicit PUWeightProducer(const edm::ParameterSet&);
      ~PUWeightProducer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginJob() ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      virtual void beginRun(edm::Run&, edm::EventSetup const&);
      virtual void endRun(edm::Run&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);

  //retrieve collection from the event
  template<typename T>
  const bool getCollection_(T& pCollection, const edm::InputTag& tag, const edm::Event& iEvent)
  {
    bool collectionFound = false;
    try { collectionFound = iEvent.getByLabel(tag, pCollection); }
    catch (cms::Exception& ex) {}
    if (!collectionFound) {
      std::cerr << "No collection of type " << tag << " found in run " << iEvent.run();
      std::cerr << ", event " << iEvent.id().event() << ", lumi section ";
      std::cerr << iEvent.getLuminosityBlock().luminosityBlock() << ".\n";
    }
    return collectionFound;
  }

      // ----------member data ---------------------------

  //sample PU generation scenario
  STRING PU_;

  //data reconstruction era
  STRING dataRecoEra_;

  //PileupSummaryInfo InputTag
  edm::InputTag PUSummaryInfoTag_;

  //LumiReWeighting object
  edm::LumiReWeighting* pS3S4Weights_;
  edm::LumiReWeighting* pS6Weights_;
};

//
// constants, enums and typedefs
//

//S3/S4 in time dist.: PoissonOneXDist, "spike + smeared"
Double_t S3S4InTimeDist[55] = {1.45346E-01, 6.42802E-02, 6.95255E-02, 6.96747E-02, 6.92955E-02,
			       6.84997E-02, 6.69528E-02, 6.45515E-02, 6.09865E-02, 5.63323E-02,
			       5.07322E-02, 4.44681E-02, 3.79205E-02, 3.15131E-02, 2.54220E-02,
			       2.00184E-02, 1.53776E-02, 1.15387E-02, 8.47608E-03, 6.08715E-03, 
			       4.28255E-03, 2.97185E-03, 2.01918E-03, 1.34490E-03, 8.81587E-04, 
			       5.69954E-04, 3.61493E-04, 2.28692E-04, 1.40791E-04, 8.44606E-05, 
			       5.10204E-05, 3.07802E-05, 1.81401E-05, 1.00201E-05, 5.80004E-06, 
			       0.0,         0.0,         0.0,         0.0,         0.0, 
			       0.0,         0.0,         0.0,         0.0,         0.0, 
			       0.0,         0.0,         0.0,         0.0,         0.0, 
			       0.0,         0.0,         0.0,         0.0,         0.0};

//S6 dist.: Fall2011
Double_t S6Dist[55] = {0.003388501, 0.010357558, 0.024724258, 0.042348605, 0.058279812,
		       0.068851751, 0.072914824, 0.071579609, 0.066811668, 0.060672356, 
		       0.054528356, 0.04919354,  0.044886042, 0.041341896, 0.0384679, 
		       0.035871463, 0.03341952,  0.030915649, 0.028395374, 0.025798107, 
		       0.023237445, 0.020602754, 0.0180688,   0.015559693, 0.013211063, 
		       0.010964293, 0.008920993, 0.007080504, 0.005499239, 0.004187022, 
		       0.003096474, 0.002237361, 0.001566428, 0.001074149, 0.000721755, 
		       0.000470838, 0.00030268,  0.000184665, 0.000112883, 6.74043E-05, 
		       3.82178E-05, 2.22847E-05, 1.20933E-05, 6.96173E-06, 3.4689E-06, 
		       1.96172E-06, 8.49283E-07, 5.02393E-07, 2.15311E-07, 9.56938E-08, 
		       0.0,         0.0,         0.0,         0.0,         0.0};

//S6 in time dist.: Fall2011_InTime
Double_t S6IntTimeDist[55] = {0.014583699, 0.025682975, 0.038460562, 0.049414536, 0.056931087, 
			      0.061182816, 0.062534625, 0.061476918, 0.058677499, 0.055449877, 
			      0.051549051, 0.047621024, 0.043923799, 0.040569076, 0.037414654, 
			      0.034227033, 0.031437714, 0.028825596, 0.026218978, 0.023727061, 
			      0.021365645, 0.01918743,  0.016972815, 0.014920601, 0.013038989, 
			      0.011293777, 0.009612465, 0.008193556, 0.006888047, 0.005715239, 
			      0.004711232, 0.003869926, 0.003154521, 0.002547417, 0.002024714, 
			      0.001574411, 0.001245808, 0.000955206, 0.000735305, 0.000557304, 
			      0.000412503, 0.000305502, 0.000231002, 0.000165701, 0.000121201, 
			      9.30006E-05, 6.40004E-05, 4.22003E-05, 2.85002E-05, 1.96001E-05, 
			      1.59001E-05, 1.01001E-05, 8.50006E-06, 6.60004E-06, 2.70002E-06};

//May10ReReco S3/S4 dist.
Double_t May10ReRecoS3S4Dist[55] = {1.41192e+06, 6.09123e+06, 1.42242e+07, 2.3449e+07, 
				    3.03709e+07, 3.2781e+07,  3.06149e+07, 2.53907e+07, 
				    1.90579e+07, 1.31326e+07, 8.40198e+06, 5.03605e+06, 
				    2.84935e+06, 1.53159e+06, 786560,      387886, 
				    184514,      85013.3,     38077.1,     16632.2, 
				    7104.18,     2973.79,     1221.97,     493.491, 
				    196.009,     76.5954,     29.4498,     11.139, 
				    4.14345,     1.5152,      0.544498,    0.192205, 
				    0.0666233,   0.0226692,   0.0112094,   0.006, 
				    0.0,         0.0,         0.0,         0.0, 
				    0.0,         0.0,         0.0,         0.0, 
				    0.0,         0.0,         0.0,         0.0, 
				    0.0,         0.0,         0.0,         0.0, 
				    0.0,         0.0,         0.0};

//PromptRecov4 S3/S4 dist.
Double_t PromptRecov4S3S4Dist[55] = {6.70456e+06, 2.92307e+07, 6.74612e+07, 1.08937e+08, 
				     1.37719e+08, 1.44854e+08, 1.31674e+08, 1.06159e+08, 
				     7.73452e+07, 5.16504e+07, 3.19653e+07, 1.84976e+07, 
				     1.00824e+07, 5.20822e+06, 2.56301e+06, 1.20692e+06, 
				     545916,      237963,      100239,      40901.9, 
				     16199.4,     6237.94,     2338.79,     854.812, 
				     304.872,     106.194,     36.1515,     12.0354, 
				     3.92033,     1.24997,     0.39025,     0.11934, 
				     0.03575,     0.0105,      0.00419,     0.002, 
				     0.0,         0.0,         0.0,         0.0, 
				     0.0,         0.0,         0.0,         0.0, 
				     0.0,         0.0,         0.0,         0.0, 
				     0.0,         0.0,         0.0,         0.0, 
				     0.0,         0.0,         0.0};

//postMay10ReReco S3/S4 dist.
Double_t postMay10ReRecoS3S4Dist[55] = {1.20346e+07, 5.29741e+07, 1.26678e+08, 2.17852e+08, 
					3.03374e+08, 3.6593e+08,  3.99492e+08, 4.06892e+08, 
					3.94762e+08, 3.69713e+08, 3.36762e+08, 2.99308e+08, 
					2.59706e+08, 2.19799e+08, 1.81196e+08, 1.45302e+08, 
					1.13229e+08, 8.56939e+07, 6.29743e+07, 4.4943e+07, 
					3.11619e+07, 2.10049e+07, 1.37747e+07, 8.79591e+06, 
					5.47422e+06, 3.3237e+06,  1.97061e+06, 1.14203e+06, 
					647534,      359546,      195673,      104460, 
					54745.1,     28185.5,     28005.5,     0.002, 
					0.0,         0.0,         0.0,         0.0, 
					0.0,         0.0,         0.0,         0.0, 
					0.0,         0.0,         0.0,         0.0, 
					0.0,         0.0,         0.0,         0.0, 
					0.0,         0.0,         0.0};

//May10ReReco S6 dist.
Double_t May10ReRecoS6Dist[55] = {0.0,         100379,      988726,     3.34865e+06, 2.83186e+07, 
				  6.25181e+07, 6.50772e+07, 3.9395e+07, 1.23125e+07, 2.85924e+06, 
				  758175,      146587,      26479.3,    4621.37,     0.0, 
				  0.0,         0.0,         0.0,        0.0,         0.0, 
				  0.0,         0.0,         0.0,        0.0,         0.0, 
				  0.0,         0.0,         0.0,        0.0,         0.0, 
				  0.0,         0.0,         0.0,        0.0,         0.0, 
				  0.0,         0.0,         0.0,        0.0,         0.0, 
				  0.0,         0.0,         0.0,        0.0,         0.0, 
				  0.0,         0.0,         0.0,        0.0,         0.0};

//PromptRecov4 S6 dist.
Double_t PromptRecov4S6Dist[55] = {0.0,         78842.9,     2.82582e+06, 2.24236e+07, 
				   1.44669e+08, 2.93716e+08, 2.88572e+08, 1.35679e+08, 
				   3.55512e+07, 7.75447e+06, 841246,      96727.5, 
				   0.0,         0.0,         0.0,         0.0, 
				   0.0,         0.0,         0.0,         0.0,
 				   0.0,         0.0,         0.0,         0.0, 
				   0.0,         0.0,         0.0,         0.0, 
				   0.0,         0.0,         0.0,         0.0, 
				   0.0,         0.0,         0.0,         0.0, 
				   0.0,         0.0,         0.0,         0.0, 
				   0.0,         0.0,         0.0,         0.0, 
				   0.0,         0.0,         0.0,         0.0, 
				   0.0,         0.0,         0.0,         0.0, 
				   0.0,         0.0,         0.0};

//postMay10ReReco S6 dist.
Double_t postMay10ReRecoS6Dist[55] = {0.0,         204382,      4.79259e+06, 4.73212e+07, 
				      2.40919e+08, 4.56336e+08, 5.11551e+08, 4.93648e+08, 
				      4.5379e+08,  4.23747e+08, 3.81667e+08, 3.5166e+08, 
				      3.30735e+08, 2.94181e+08, 2.29225e+08, 1.45499e+08, 
				      7.43711e+07, 3.08969e+07, 1.0913e+07,  3.68176e+06, 
				      1.13003e+06, 288668,      64020.4,     2350.83, 
				      0.0,         0.0,         0.0,         0.0, 
				      0.0,         0.0,         0.0,         0.0, 
				      0.0,         0.0,         0.0,         0.0, 
				      0.0,         0.0,         0.0,         0.0, 
				      0.0,         0.0,         0.0,         0.0, 
				      0.0,         0.0,         0.0,         0.0, 
				      0.0,         0.0,         0.0,         0.0, 
				      0.0,         0.0,         0.0};

//
//static data member definitions
//

//
// constructors and destructor
//
PUWeightProducer::PUWeightProducer(const edm::ParameterSet& iConfig) :
  PU_(iConfig.getParameter<STRING>("PU")),
  dataRecoEra_(iConfig.getParameter<STRING>("dataRecoEra")),
  PUSummaryInfoTag_(iConfig.getParameter<edm::InputTag>("PUSummaryInfoTag"))
{
  //sanity check
  if ((PU_ != "S3S4") && (PU_ != "S6")) {
    throw cms::Exception("BadInput") << "Error: \"" << PU_ << "\" is not a valid PU scenario.\n";
  }

   //register your products
  produces<double>();

   //now do what ever other initialization is needed
  VFLOAT S3S4Dist;
  VFLOAT S6Dist;
  VFLOAT dataDist;
  for (unsigned int i = 0; i < 55; ++i) { S3S4Dist.push_back((float)S3S4InTimeDist[i]); }
  for (unsigned int i = 0; i < 55; ++i) { S6Dist.push_back((float)S6IntTimeDist[i]); }
  for (unsigned int i = 0; i < 55; ++i) {
    if (dataRecoEra_ == "May10ReReco") {
      if (PU_ == "S3S4") dataDist.push_back((float)May10ReRecoS3S4Dist[i]);
      else dataDist.push_back((float)May10ReRecoS6Dist[i]);
    }
    else if (dataRecoEra_ == "PromptRecov4") {
      if (PU_ == "S3S4") dataDist.push_back((float)PromptRecov4S3S4Dist[i]);
      else dataDist.push_back((float)PromptRecov4S6Dist[i]);
    }
    else if (dataRecoEra_ == "postMay10ReReco") {
      if (PU_ == "S3S4") dataDist.push_back((float)postMay10ReRecoS3S4Dist[i]);
      else dataDist.push_back((float)postMay10ReRecoS6Dist[i]);
    }
    else {
      STRINGSTREAM err;
      err << "Error: \"" << dataRecoEra_ << "\" is not a valid data reconstruction era.\n";
      throw cms::Exception("BadInput") << err.str();
    }
  }
  pS3S4Weights_ = new edm::LumiReWeighting(S3S4Dist, dataDist);
  pS6Weights_ = new edm::LumiReWeighting(S6Dist, dataDist);
}


PUWeightProducer::~PUWeightProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)
  delete pS3S4Weights_;
  delete pS6Weights_;
  pS3S4Weights_ = NULL;
  pS6Weights_ = NULL;
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
PUWeightProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   //access the PU info
   Handle<std::vector<PileupSummaryInfo> > pPUInfo;
   int nInTimeInteractions = -1;
   int nTrueInTimeInteractions = -1;
   if (getCollection_(pPUInfo, PUSummaryInfoTag_, iEvent)) {
     for (std::vector<PileupSummaryInfo>::const_iterator iPU = pPUInfo->begin(); 
	  iPU != pPUInfo->end(); ++iPU) {
       int BX = iPU->getBunchCrossing();

       //get the number of in-time interactions in the event
       if (BX == 0) {
	 nInTimeInteractions = iPU->getPU_NumInteractions();
	 nTrueInTimeInteractions = iPU->getTrueNumInteractions();
       }
     }
   }

   //sanity check
   if ((nInTimeInteractions == -1) || (nTrueInTimeInteractions == -1)) {
     STRINGSTREAM err;
     err << "nInTimeInteractions = " << nInTimeInteractions << std::endl;
     err << "nTrueInTimeInteractions = " << nTrueInTimeInteractions << std::endl;
     throw cms::Exception("BadInput") << err.str();
   }

   //get the weight from the reweighting object and store it in the event
   std::auto_ptr<double> weightProd(new double());
   if (PU_ == "S3S4") *weightProd = pS3S4Weights_->weight(nInTimeInteractions);
   else if (PU_ == "S6") *weightProd = pS6Weights_->weight(nTrueInTimeInteractions);
   iEvent.put(weightProd);
}

// ------------ method called once each job just before starting event loop  ------------
void 
PUWeightProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
PUWeightProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
PUWeightProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
PUWeightProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
PUWeightProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
PUWeightProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PUWeightProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PUWeightProducer);
