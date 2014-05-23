#include "PhysicsTools/TagAndProbe/interface/TrackMatchedPhotonProducer.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/EgammaCandidates/interface/Photon.h"

#include "DataFormats/Math/interface/deltaR.h" // reco::deltaR


TrackMatchedPhotonProducer::TrackMatchedPhotonProducer(const edm::ParameterSet &params)
{

  const edm::InputTag allTracks("generalTracks", "", "RECO");
  trackCollection_ = 
    params.getUntrackedParameter<edm::InputTag>("ReferenceTrackCollection", 
						allTracks);
  photonCollection_ = 
    params.getParameter<edm::InputTag>("src");

  delRMatchingCut_ = params.getUntrackedParameter<double>("deltaR",
							   0.30);

  trackPTMin_ = params.getParameter<double>("trackPTMin");

  trackEtaMax_ = params.getParameter<double>("trackEtaMax");
  
  /*produces< edm::PtrVector<reco::Photon> >();
    produces< edm::RefToBaseVector<reco::Photon> >();*/
  produces< std::vector<reco::Photon> >();
}




TrackMatchedPhotonProducer::~TrackMatchedPhotonProducer()
{

}


//
// member functions
//


// ------------ method called to produce the data  ------------

void TrackMatchedPhotonProducer::produce(edm::Event &event, 
			      const edm::EventSetup &eventSetup)
{
   // Create the output collection
  /*std::auto_ptr< edm::RefToBaseVector<reco::Photon> > 
    outColRef( new edm::RefToBaseVector<reco::Photon> );
  std::auto_ptr< edm::PtrVector<reco::Photon> > 
  outColPtr( new edm::PtrVector<reco::Photon> );*/
  std::auto_ptr< std::vector<reco::Photon> > outColRef( new std::vector<reco::Photon> );


  // Read tracks
  edm::Handle<edm::View<reco::Track> > tracks;
  event.getByLabel(trackCollection_, tracks);
   


  //Read candidates
  edm::Handle<edm::View<reco::Photon> > recoCandColl; 
  event.getByLabel( photonCollection_ , recoCandColl); 


  /*const edm::PtrVector<reco::Photon>& ptrVect = recoCandColl->ptrVector();
    const edm::RefToBaseVector<reco::Photon>& refs = recoCandColl->refVector();*/
  unsigned int counter=0;

  // Loop over candidates
  for(edm::View<reco::Photon>::const_iterator photonIt = recoCandColl->begin();
      photonIt != recoCandColl->end(); ++photonIt, ++counter){
    // Now loop over tracks
    for(edm::View<reco::Track>::const_iterator  iTrack = tracks->begin(); 
	iTrack != tracks->end();  ++iTrack) {

      double dRval = reco::deltaR((float)iTrack->eta(), (float)iTrack->phi(), 
				  photonIt->eta(), photonIt->phi());	
       
      if((iTrack->pt() > trackPTMin_) && (iTrack->eta() < trackEtaMax_) && ( dRval < delRMatchingCut_ )) {
	//outCol->push_back( *scIt );
	/*outColRef->push_back( refs[counter] );
	  outColPtr->push_back( ptrVect[counter]  );*/
	outColRef->push_back(*photonIt);
      } // end if loop
    } // end electron loop

  } // end candidate loop

  event.put(outColRef);
  //event.put(outColPtr);
}




// ------ method called once each job just before starting event loop  ---



void TrackMatchedPhotonProducer::beginJob() {}



void TrackMatchedPhotonProducer::endJob() {}



//define this as a plug-in
//DEFINE_FWK_MODULE( TrackMatchedPhotonProducer );

