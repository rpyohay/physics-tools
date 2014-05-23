#ifndef PhysicsTools_TagAndProbe_IDedJetProducer_h
#define PhysicsTools_TagAndProbe_IDedJetProducer_h

// system include files
#include <memory>

// user include files
#include "PhysicsTools/SelectorUtils/interface/JetIDSelectionFunctor.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

// forward declarations

class IDedJetProducer : public edm::EDProducer 
{
 public:
  explicit IDedJetProducer(const edm::ParameterSet&);
  ~IDedJetProducer();

 private:
  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
      
  // ----------member data ---------------------------

  edm::InputTag caloJetSrc_;
  edm::InputTag jetIDSrc_;
  edm::InputTag JPTJetSrc_;
  edm::InputTag PFJetSrc_;
  edm::InputTag photonSrc_;
  double cleaningDR_;
  double maxAbsEta_;
};

#endif
