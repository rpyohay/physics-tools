// -*- C++ -*-
//
// Package:    PUSubtractedPhotonSelector
// Class:      PUSubtractedPhotonSelector
// 
/**\class PUSubtractedPhotonSelector PUSubtractedPhotonSelector.cc PhysicsTools/TagAndProbe/plugins/PUSubtractedPhotonSelector.cc

 Description: filters photon collection based on PU-subtracted isolations

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Rachel Yohay,512 1-010,+41227670495,
//         Created:  Mon Jun  6 15:52:44 CEST 2011
// $Id: PUSubtractedPhotonSelector.cc,v 1.5 2012/04/13 14:05:26 yohay Exp $
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
#include "DataFormats/EgammaCandidates/interface/PhotonFwd.h"
#include "DataFormats/EgammaCandidates/interface/Photon.h"
#include "FWCore/Framework/interface/LuminosityBlock.h"
#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "PhysicsTools/TagAndProbe/interface/Typedefs.h"

//isolation types
#define ECAL 0
#define HCAL 1
#define TRACK 2
#define HOVERE 3
#define SIGMAIETAIETA 4
#define R9MIN 5
#define R9MAX 6

//cone sizes
#define DR03 0
#define DR04 1

//
// class declaration
//

class PUSubtractedPhotonSelector : public edm::EDProducer {
   public:
      explicit PUSubtractedPhotonSelector(const edm::ParameterSet&);
      ~PUSubtractedPhotonSelector();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginJob() ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      virtual void beginRun(edm::Run&, edm::EventSetup const&);
      virtual void endRun(edm::Run&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);

  void putProductIntoEvent(const edm::Handle<edm::View<reco::Photon> >&, const VFLOAT&, 
			   edm::Event&, const STRING&) const;

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

  //input collections
  edm::InputTag photonSrc_;
  edm::InputTag rhoSrc_;
  edm::InputTag PVSrc_;

  //isolation cuts
  VDOUBLE ETMultiplier_;
  VDOUBLE constant_;
  VDOUBLE rhoEffectiveArea_;
  VDOUBLE nPVEffectiveArea_;
  double combinedIsoMax_;

  //isolation type
  VUINT type_;

  //cone size
  VUINT coneSize_;
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
PUSubtractedPhotonSelector::PUSubtractedPhotonSelector(const edm::ParameterSet& iConfig) :

  //input collections
  photonSrc_(iConfig.getParameter<edm::InputTag>("photonSrc")),
  rhoSrc_(iConfig.getParameter<edm::InputTag>("rhoSrc")),
  PVSrc_(iConfig.getParameter<edm::InputTag>("PVSrc")),

  //isolation cuts
  ETMultiplier_(iConfig.getParameter<VDOUBLE>("ETMultiplier")),
  constant_(iConfig.getParameter<VDOUBLE>("constant")),
  rhoEffectiveArea_(iConfig.getParameter<VDOUBLE>("rhoEffectiveArea")),
  nPVEffectiveArea_(iConfig.getParameter<VDOUBLE>("nPVEffectiveArea")),
  combinedIsoMax_(iConfig.getParameter<double>("combinedIsoMax")),

  //isolation type
  type_(iConfig.getParameter<VUINT>("type")),

  //cone size
  coneSize_(iConfig.getParameter<VUINT>("coneSize"))
{
   //now do what ever other initialization is needed
  if ((ETMultiplier_.size() != constant_.size()) || 
      (constant_.size() != rhoEffectiveArea_.size()) || 
      (rhoEffectiveArea_.size() != nPVEffectiveArea_.size()) || 
      (nPVEffectiveArea_.size() != coneSize_.size())) {
    throw cms::Exception("VectorSizeMismatch");
  }

   //register your products
  produces<reco::PhotonCollection>("rhoCorrected");
  produces<reco::PhotonCollection>("nPVCorrected");
  produces<reco::PhotonRefVector>("rhoCorrected");
  produces<reco::PhotonRefVector>("nPVCorrected");
  if (ETMultiplier_.size() == 1) {
    produces<edm::ValueMap<float> >("rhoCorrected");
    produces<edm::ValueMap<float> >("nPVCorrected");
  }
}


PUSubtractedPhotonSelector::~PUSubtractedPhotonSelector()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
PUSubtractedPhotonSelector::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

//    std::cerr << "Types:\n";
//    for (VUINT_IT i = type_.begin(); i != type_.end(); ++i) { std::cerr << *i << " "; }
//    std::cerr << std::endl;

   //pointers to the photon collections to be produced
   std::auto_ptr<reco::PhotonCollection> 
     photonsPassingRhoCorrectedIsoCollection(new reco::PhotonCollection());
   std::auto_ptr<reco::PhotonCollection> 
     photonsPassingNPVCorrectedIsoCollection(new reco::PhotonCollection());
   std::auto_ptr<reco::PhotonRefVector> 
     photonsPassingRhoCorrectedIsoRefVector(new reco::PhotonRefVector());
   std::auto_ptr<reco::PhotonRefVector> 
     photonsPassingNPVCorrectedIsoRefVector(new reco::PhotonRefVector());

   //vector of PU-subtracted isolation values
   VFLOAT PURhoSubtractedIsoVec;
   VFLOAT PUNPVSubtractedIsoVec;

   //get event rho
   Handle<double> pRho;
   double rho = 0.0;
   if (getCollection_(pRho, rhoSrc_, iEvent)) rho = *pRho;

   //get event nPV
   Handle<reco::VertexCollection> pVertices;
   unsigned int nPV = 0;
   if (getCollection_(pVertices, PVSrc_, iEvent)) {
     for (reco::VertexCollection::const_iterator iPV = pVertices->begin(); 
	  iPV != pVertices->end(); ++iPV) {
       if (!iPV->isFake() && (iPV->ndof() > 4) && (fabs(iPV->z()) <= 24.0/*cm*/) && 
	   (iPV->position().Rho() <= 2.0/*cm*/)) ++nPV;
     }
   }

   //loop over photon collection
   Handle<edm::View<reco::Photon> > pPhotons;
   if (getCollection_(pPhotons, photonSrc_, iEvent)) {
//      std::cerr << "Size of photon collection: " << pPhotons->size() << std::endl;
     for (edm::View<reco::Photon>::const_iterator iPhoton = pPhotons->begin(); 
	  iPhoton != pPhotons->end(); ++iPhoton) {
//        std::cerr << "Photon " << (iPhoton - pPhotons->begin()) << std::endl;

       //photon ref
       edm::RefToBase<reco::Photon> ref(pPhotons->refAt(iPhoton - pPhotons->begin()));

       //loop over isolation/PU-subtraction criteria to get the decision
       bool rhoDecision = true;
       bool nPVDecision = true;
       double combinedIso = 0.0;
       for (VDOUBLE_IT iIso = ETMultiplier_.begin(); iIso != ETMultiplier_.end(); ++iIso) {
	 const unsigned int i = iIso - ETMultiplier_.begin();

	 //get the uncorrected cut variables
	 float uncorrVar = 0.0;
	 switch (type_[i]) {
	 case ECAL:
	   switch (coneSize_[i]) {
	   case DR03:
// 	     std::cerr << "Cone size 0.3\n";
	     uncorrVar = iPhoton->ecalRecHitSumEtConeDR03();
	     break;
	   case DR04:
	     uncorrVar = iPhoton->ecalRecHitSumEtConeDR04();
// 	     std::cerr << "Cone size 0.4\n";
	     break;
	   default:
	     STRINGSTREAM info;
	     info << "Cone size " << coneSize_[i] << " at position " << i;
	     info << " is invalid.  Assuming value 999.0.\n";
	     edm::LogInfo("InvalidType") << info.str();
	     uncorrVar = 999.0;
	     break;
	   }
	   break;
	 case HCAL:
	   switch (coneSize_[i]) {
	   case DR03:
// 	     std::cerr << "Cone size 0.3\n";
	     uncorrVar = iPhoton->hcalTowerSumEtConeDR03();
	     break;
	   case DR04:
	     uncorrVar = iPhoton->hcalTowerSumEtConeDR04();
// 	     std::cerr << "Cone size 0.4\n";
	     break;
	   default:
	     STRINGSTREAM info;
	     info << "Cone size " << coneSize_[i] << " at position " << i;
	     info << " is invalid.  Assuming value 999.0.\n";
	     edm::LogInfo("InvalidType") << info.str();
	     uncorrVar = 999.0;
	     break;
	   }
	   break;
	 case TRACK:
	   switch (coneSize_[i]) {
	   case DR03:
// 	     std::cerr << "Cone size 0.3\n";
	     uncorrVar = iPhoton->trkSumPtHollowConeDR03();
	     break;
	   case DR04:
// 	     std::cerr << "Cone size 0.4\n";
	     uncorrVar = iPhoton->trkSumPtHollowConeDR04();
	     break;
	   default:
	     STRINGSTREAM info;
	     info << "Cone size " << coneSize_[i] << " at position " << i;
	     info << " is invalid.  Assuming value 999.0.\n";
	     edm::LogInfo("InvalidType") << info.str();
	     uncorrVar = 999.0;
	     break;
	   }
	   break;
	 case HOVERE:
	   uncorrVar = iPhoton->hadronicOverEm();
	   break;
	 case SIGMAIETAIETA:
	   uncorrVar = iPhoton->sigmaIetaIeta();
	   break;
	 case R9MIN:
	   uncorrVar = iPhoton->r9();
	   break;
	 case R9MAX:
	   uncorrVar = iPhoton->r9();
	   break;
	 default:
	   STRINGSTREAM info;
	   info << "Type " << type_[i] << " at position " << i;
	   info << " is invalid and will be ignored.\n";
	   edm::LogInfo("InvalidType") << info.str();
	 }

	 /*fill the vectors of PU-subtracted isolations if only 1 kind of subtraction is to be 
	   performed*/
	 if ((ETMultiplier_.size() == 1) && ((type_[i] == ECAL) || (type_[i] == HCAL))) {
	   PURhoSubtractedIsoVec.push_back(uncorrVar - (float)(rhoEffectiveArea_[i]*rho));
	   PUNPVSubtractedIsoVec.push_back(uncorrVar - (float)(nPVEffectiveArea_[i]*nPV));
	 }

	 //compute the cut value
	 float cut = (float)((*iIso)*iPhoton->et() + constant_[i]);

	 //compute the pass flag
	 bool passPUNPVSubtractedCut = (type_[i] == R9MIN) ? ((uncorrVar - nPVEffectiveArea_[i]*nPV) > cut) : ((uncorrVar - nPVEffectiveArea_[i]*nPV) < cut);
	 bool passPURhoSubtractedCutNonCombinedIso = (type_[i] == R9MIN) ? ((uncorrVar - rhoEffectiveArea_[i]*rho) > cut) : ((uncorrVar - rhoEffectiveArea_[i]*rho) < cut);
	 bool passPURhoSubtractedCut = true;

	 /*if not doing a combined isolation cut, then this photon passes if it passes the cut 
	   above*/
	 /*if doing the combined isolation cut, set the pass flag to true and check whether the 
	   sum passes later*/
	 //applies to rho only	 
	 if ((combinedIsoMax_ == -1.0) || 
	     ((type_[i] != ECAL) && (type_[i] != HCAL) && (type_[i] != TRACK))) {
	   passPURhoSubtractedCut = passPURhoSubtractedCutNonCombinedIso;
// 	   std::cerr << "Not a combined iso thing\n";
	 }
	 else {
	   combinedIso+=(uncorrVar - rhoEffectiveArea_[i]*rho);
// 	   std::cerr << "combinedIso = " << combinedIso << std::endl;
	 }

	 //decision
	 rhoDecision = rhoDecision && passPURhoSubtractedCut;
	 nPVDecision = nPVDecision && passPUNPVSubtractedCut;
// 	 std::cerr << "Rho-subtracted value: " << (uncorrVar - rhoEffectiveArea_[i]*rho);
// 	 std::cerr << std::endl;
// 	 std::cerr << "NPV-subtracted value: " << (uncorrVar - nPVEffectiveArea_[i]*nPV);
// 	 std::cerr << std::endl;
// 	 std::cerr << "rhoDecision = " << rhoDecision << std::endl;
// 	 std::cerr << "nPVDecision = " << nPVDecision << std::endl;
       }

       //make the combined isolation decision
       rhoDecision = rhoDecision && ((combinedIsoMax_ == -1.0) || (combinedIso < combinedIsoMax_));
//        std::cerr << "final rhoDecision = " << rhoDecision << std::endl;

       /*put the photon in the rho-corrected collection if it passes the rho-corrected 
	 isolation cut*/
       if (rhoDecision) {
	 photonsPassingRhoCorrectedIsoCollection->push_back(*iPhoton);
	 photonsPassingRhoCorrectedIsoRefVector->push_back(ref.castTo<reco::PhotonRef>());
       }

       /*put the photon in the nPV-corrected collection if it passes the nPV-corrected 
	 isolation cut*/
       if (nPVDecision) {
	 photonsPassingNPVCorrectedIsoCollection->push_back(*iPhoton);
	 photonsPassingNPVCorrectedIsoRefVector->push_back(ref.castTo<reco::PhotonRef>());
       }
     }
   }

   //write the filtered photon collections to the event
//    std::cerr << "Size of filtered photon collection: ";
//    std::cerr << photonsPassingRhoCorrectedIsoCollection->size() << std::endl;
   iEvent.put(photonsPassingRhoCorrectedIsoCollection, "rhoCorrected");
   iEvent.put(photonsPassingNPVCorrectedIsoCollection, "nPVCorrected");
   iEvent.put(photonsPassingRhoCorrectedIsoRefVector, "rhoCorrected");
   iEvent.put(photonsPassingNPVCorrectedIsoRefVector, "nPVCorrected");

   //write the value maps to the event if only 1 cut decision was requested
   if (ETMultiplier_.size() == 1) {
     putProductIntoEvent(pPhotons, PURhoSubtractedIsoVec, iEvent, "rhoCorrected");
     putProductIntoEvent(pPhotons, PUNPVSubtractedIsoVec, iEvent, "nPVCorrected");
   }
}

// ------------ method called once each job just before starting event loop  ------------
void 
PUSubtractedPhotonSelector::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
PUSubtractedPhotonSelector::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
PUSubtractedPhotonSelector::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
PUSubtractedPhotonSelector::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
PUSubtractedPhotonSelector::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
PUSubtractedPhotonSelector::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PUSubtractedPhotonSelector::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

void 
PUSubtractedPhotonSelector::putProductIntoEvent(const edm::Handle<edm::View<reco::Photon> >& 
						pPhotons, const VFLOAT& vals, edm::Event& iEvent, 
						const STRING& label) const
{
  std::auto_ptr<edm::ValueMap<float> > out(new edm::ValueMap<float>());
  edm::ValueMap<float>::Filler filler(*out);
  try { filler.insert(pPhotons, vals.begin(), vals.end()); }
  catch (cms::Exception& ex) {
    STRINGSTREAM err;
    err << "putProductIntoEvent/" << label << ": " << ex.what();
    throw cms::Exception("PUSubtractedPhotonSelector") << err.str();
  }
  filler.fill();
  iEvent.put(out, label);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PUSubtractedPhotonSelector);
