#include "PhysicsTools/TagAndProbe/interface/IDedJetProducer.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "DataFormats/JetReco/interface/JPTJet.h"
#include "DataFormats/EgammaCandidates/interface/PhotonFwd.h"
#include "DataFormats/EgammaCandidates/interface/Photon.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "PhysicsTools/TagAndProbe/interface/Typedefs.h"

IDedJetProducer::IDedJetProducer(const edm::ParameterSet &params)
{
  if ((params.existsAs<edm::InputTag>("caloJetSrc")) && 
      (params.existsAs<edm::InputTag>("jetIDSrc")) && 
      (params.existsAs<edm::InputTag>("JPTJetSrc"))) {
    caloJetSrc_ = 
      params.getParameter<edm::InputTag>("caloJetSrc");
    jetIDSrc_ =
      params.getParameter<edm::InputTag>("jetIDSrc");
    JPTJetSrc_ =
      params.getParameter<edm::InputTag>("JPTJetSrc");
    produces< std::vector<reco::JPTJet> >();
  }
  else if (params.existsAs<edm::InputTag>("PFJetSrc")) {
    PFJetSrc_ = params.getParameter<edm::InputTag>("PFJetSrc");
    produces< std::vector<reco::PFJet> >();
  }
  else {
    STRINGSTREAM err;
    err << "Specify either caloJetSrc, jetIDSrc, and JPTJetSrc or PFJetSrc.\n";
    throw cms::Exception("InvalidCfg") << err.str();
  }
  photonSrc_ = 
    params.getParameter<edm::InputTag>("photonSrc");
  cleaningDR_ = 
    params.getParameter<double>("cleaningDR");
  maxAbsEta_ = 
    params.getParameter<double>("maxAbsEta");
}

IDedJetProducer::~IDedJetProducer() {}

//
// member functions
//


// ------------ method called to produce the data  ------------

void IDedJetProducer::produce(edm::Event &event, 
			      const edm::EventSetup &eventSetup)
{
  //get photons
  edm::Handle<reco::PhotonCollection> pPhotons;
  event.getByLabel(photonSrc_, pPhotons);

   // Create the output collection
  /*std::auto_ptr< edm::RefToBaseVector<reco::Photon> > 
    outColRef( new edm::RefToBaseVector<reco::Photon> );
  std::auto_ptr< edm::PtrVector<reco::Photon> > 
  outColPtr( new edm::PtrVector<reco::Photon> );*/
  if (JPTJetSrc_.label() != "") {
    std::auto_ptr< std::vector<reco::JPTJet> > outColRef( new std::vector<reco::JPTJet> );

    //Read candidates
    edm::Handle<edm::View<reco::CaloJet> > recoCandColl; 
    event.getByLabel( caloJetSrc_ , recoCandColl); 

    // Read jet ID
    edm::Handle<reco::JetIDValueMap> pJetID;
    event.getByLabel(jetIDSrc_, pJetID);
   
    //get JPT jets
    edm::Handle<std::vector<reco::JPTJet> > pJPTJets;
    event.getByLabel(JPTJetSrc_, pJPTJets);

    /*const edm::PtrVector<reco::Photon>& ptrVect = recoCandColl->ptrVector();
      const edm::RefToBaseVector<reco::Photon>& refs = recoCandColl->refVector();*/
    unsigned int counter=0;

    // jet ID selection
    JetIDSelectionFunctor jetIDFunctor( JetIDSelectionFunctor::PURE09, 
					JetIDSelectionFunctor::LOOSE );
    pat::strbitset ret = jetIDFunctor.getBitTemplate();

    // Loop over candidates
    unsigned int idx;
    for(edm::View<reco::CaloJet>::const_iterator jetIt = recoCandColl->begin();
	jetIt != recoCandColl->end(); ++jetIt, ++counter){

      idx = jetIt - recoCandColl->begin();
      edm::RefToBase<reco::CaloJet> jetRef = recoCandColl->refAt(idx);
      reco::JetID const & jetId = (*pJetID)[ jetRef ];
      ret.set(false);
      bool passed = jetIDFunctor( *jetIt, jetId, ret );

      //does this calo jet overlap with a photon?
      bool overlapsWithPhoton = false;
      reco::PhotonCollection::const_iterator iPhoton = pPhotons->begin();
      while ((iPhoton != pPhotons->end()) && (!overlapsWithPhoton)) {
	if (deltaR(*jetIt, *iPhoton) < cleaningDR_) {
	  overlapsWithPhoton = true;
	  /*std::cout << "jet " << idx << " of " << recoCandColl->size();
	    std::cout << " overlaps with photon " << iPhoton - pPhotons->begin() << std::endl;*/
	}
	++iPhoton;
      }
       
      if(passed && !overlapsWithPhoton && (fabs(jetIt->eta()) < maxAbsEta_)) {
	//outCol->push_back( *scIt );
	/*outColRef->push_back( refs[counter] );
	  outColPtr->push_back( ptrVect[counter]  );*/

	//get the JPT jet corresponding to the calo jet
	for (std::vector<reco::JPTJet>::const_iterator iJPTJet = pJPTJets->begin(); 
	     iJPTJet != pJPTJets->end(); ++iJPTJet) {
	  const edm::RefToBase<reco::Jet>& ref = iJPTJet->getCaloJetRef();
	  edm::RefToBase<reco::Jet> caloJetRef(jetRef);
	  if (caloJetRef == ref) {
	    /*std::cout << "Found matching JPT jet to passing calo jet " << idx << std::endl;
	      std::cout << "JPT jet ET: " << iJPTJet->et() << std::endl;
	      std::cout << "JPT jet eta: " << iJPTJet->eta() << std::endl;*/
	    outColRef->push_back(*iJPTJet);
	  }
	}
      } // end if loop
    } // end candidate loop

    event.put(outColRef);
    //event.put(outColPtr);
  }
  else if (PFJetSrc_.label() != "") {
    std::auto_ptr< std::vector<reco::PFJet> > outColRef( new std::vector<reco::PFJet> );

    //get PF jets
    edm::Handle<std::vector<reco::PFJet> > pPFJets;
    event.getByLabel(PFJetSrc_, pPFJets);

    // Loop over PF jets
    for(reco::PFJetCollection::const_iterator jetIt = pPFJets->begin();
	jetIt != pPFJets->end(); ++jetIt){

      //does the jet pass PF jet ID?
      bool passed = false;
      if ((jetIt->neutralHadronEnergyFraction() < 0.99) && 
	  (jetIt->neutralEmEnergyFraction() < 0.99) && (jetIt->getPFConstituents().size() > 1)) {
	if (fabs(jetIt->eta()) < 2.4) {
	  if ((jetIt->chargedHadronEnergyFraction() > 0) && 
	      (jetIt->chargedMultiplicity() > 0) && (jetIt->chargedEmEnergyFraction() < 0.99)) {
	    passed = true;
	  }
	}
	else passed = true;
      }

      //does this PF jet overlap with a photon?
      bool overlapsWithPhoton = false;
      reco::PhotonCollection::const_iterator iPhoton = pPhotons->begin();
      while ((iPhoton != pPhotons->end()) && (!overlapsWithPhoton)) {
	if (deltaR(*jetIt, *iPhoton) < cleaningDR_) {
	  overlapsWithPhoton = true;
	  /*std::cout << "jet " << idx << " of " << recoCandColl->size();
	    std::cout << " overlaps with photon " << iPhoton - pPhotons->begin() << std::endl;*/
	}
	++iPhoton;
      }
       
      if(passed && !overlapsWithPhoton && (fabs(jetIt->eta()) < maxAbsEta_)) {
	//outCol->push_back( *scIt );
	/*outColRef->push_back( refs[counter] );
	  outColPtr->push_back( ptrVect[counter]  );*/
	outColRef->push_back(*jetIt);
      }
    } // end candidate loop

    event.put(outColRef);
    //event.put(outColPtr);
  }
}




// ------ method called once each job just before starting event loop  ---



void IDedJetProducer::beginJob() {}



void IDedJetProducer::endJob() {}



//define this as a plug-in
DEFINE_FWK_MODULE( IDedJetProducer );
