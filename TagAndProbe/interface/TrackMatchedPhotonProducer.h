#ifndef PhysicsTools_TagAndProbe_TrackMatchedPhotonProducer_h
#define PhysicsTools_TagAndProbe_TrackMatchedPhotonProducer_h

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"


// forward declarations

class TrackMatchedPhotonProducer : public edm::EDProducer 
{
 public:
  explicit TrackMatchedPhotonProducer(const edm::ParameterSet&);
  ~TrackMatchedPhotonProducer();

 private:
  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
      
  // ----------member data ---------------------------

  edm::InputTag trackCollection_;
  edm::InputTag photonCollection_;
  double delRMatchingCut_;
  double trackPTMin_;
  double trackEtaMax_;
};

#endif
