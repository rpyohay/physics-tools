// -*- C++ -*-
//
// Package:    PhysicsTools/TagAndProbe
// Class:      ProbeMaker
// 
/**\class ProbeMaker ProbeMaker.cc PhysicsTools/TagAndProbe/plugins/ProbeMaker.cc

 Description: produce a collection of probes passing user-defined cuts from an input collection of 
 tag-probe pairs

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Rachel Yohay,512 1-010,+41227670495,
//         Created:  Mon May 30 15:33:36 CEST 2011
// $Id: ProbeMaker.cc,v 1.4 2012/04/13 14:05:26 yohay Exp $
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "PhysicsTools/TagAndProbe/interface/TagProbePairMaker.h"
#include "DataFormats/EgammaCandidates/interface/PhotonFwd.h"
#include "DataFormats/EgammaCandidates/interface/Photon.h"


//
// class declaration
//

class ProbeMaker : public edm::EDProducer {
   public:
      explicit ProbeMaker(const edm::ParameterSet&);
      ~ProbeMaker();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginJob() ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      virtual void beginRun(edm::Run&, edm::EventSetup const&);
      virtual void endRun(edm::Run&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);

      // ----------member data ---------------------------

      /// The object that produces pairs of tags and probes, making any arbitration needed
      tnp::TagProbePairMaker tagProbePairMaker_;
};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
ProbeMaker::ProbeMaker(const edm::ParameterSet& iConfig) :
  tagProbePairMaker_(iConfig)
{
   //register your products
  produces<reco::PhotonCollection>();

   //now do what ever other initialization is needed
  
}


ProbeMaker::~ProbeMaker()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
ProbeMaker::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   // get the list of (tag+probe) pairs, performing arbitration 
   tnp::TagProbePairs pairs = tagProbePairMaker_.run(iEvent);

   //fill CandidateBaseRefVector of probes and tags
   std::auto_ptr<reco::PhotonCollection> probesAndTags(new reco::PhotonCollection());
   for (tnp::TagProbePairs::const_iterator it = pairs.begin(), ed = pairs.end(); it != ed; ++it) {
     probesAndTags->push_back(*((it->probe).castTo<reco::PhotonRef>()));
     probesAndTags->push_back(*((it->tag).castTo<reco::PhotonRef>()));
   }

   //write CandidateBaseRefVector of probes and tags to event
   iEvent.put(probesAndTags);
}

// ------------ method called once each job just before starting event loop  ------------
void 
ProbeMaker::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
ProbeMaker::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
ProbeMaker::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
ProbeMaker::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
ProbeMaker::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
ProbeMaker::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
ProbeMaker::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(ProbeMaker);
