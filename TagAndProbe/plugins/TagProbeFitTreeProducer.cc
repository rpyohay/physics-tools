// -*- C++ -*-
//
// Package:    TagProbeFitTreeProducer
// Class:      TagProbeFitTreeProducer
// 
/**\class TagProbeFitTreeProducer TagProbeFitTreeProducer.cc 

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Sep 15 09:45
//         Created:  Mon Sep 15 09:49:08 CEST 2008
// $Id: TagProbeFitTreeProducer.cc,v 1.7 2012/04/13 14:05:26 yohay Exp $
//
//


// system include files
#include <memory>
#include <ctype.h>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/Candidate.h"

#include "DataFormats/Common/interface/Association.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "PhysicsTools/TagAndProbe/interface/TPTreeFiller.h"
#include "PhysicsTools/TagAndProbe/interface/TagProbePairMaker.h"

#include <set>

#include "FWCore/ParameterSet/interface/Registry.h"

//
// class decleration
//

class TagProbeFitTreeProducer : public edm::EDAnalyzer {
   public:
      explicit TagProbeFitTreeProducer(const edm::ParameterSet&);
      ~TagProbeFitTreeProducer();


   private:
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      //---- MC truth information
      /// Is this sample MC?
      bool isMC_; 
      /// InputTag to an edm::Association<reco::GenParticle> from tags & probes to MC truth
      edm::InputTag tagMatches_, probeMatches_;
      /// Possible pdgids for the mother. If empty, any truth-matched mu will be considered good
      std::set<int32_t> motherPdgId_;
      /// Return true if ref is not null and has an ancestor with pdgId inside 'motherPdgId_'
      bool checkMother(const reco::GenParticleRef &ref) const ;

      //---- Unbiased MC truth information
      /// Do we have to compute this
      bool makeMCUnbiasTree_;
      /// Check mother pdgId in unbiased inefficiency measurement
      bool checkMotherInUnbiasEff_;
      /// InputTag to the collection of all probes
      edm::InputTag allProbes_;

      //---- Jet information
//       edm::InputTag jetSrc_;

      /// The object that produces pairs of tags and probes, making any arbitration needed
      tnp::TagProbePairMaker tagProbePairMaker_;
      /// The object that actually computes variables and fills the tree for T&P
      std::auto_ptr<tnp::TPTreeFiller> treeFiller_; 
      /// The object that actually computes variables and fills the tree for unbiased MC
      std::auto_ptr<tnp::BaseTreeFiller> mcUnbiasFiller_;
      std::auto_ptr<tnp::BaseTreeFiller> oldTagFiller_;
      std::auto_ptr<tnp::BaseTreeFiller> tagFiller_;
      std::auto_ptr<tnp::BaseTreeFiller> pairFiller_;
//       std::auto_ptr<tnp::BaseTreeFiller> jetFiller_;
      std::auto_ptr<tnp::BaseTreeFiller> mcFiller_;
};

//
// constructors and destructor
//
TagProbeFitTreeProducer::TagProbeFitTreeProducer(const edm::ParameterSet& iConfig) :
    isMC_(iConfig.getParameter<bool>("isMC")),
    makeMCUnbiasTree_(isMC_ ? iConfig.getParameter<bool>("makeMCUnbiasTree") : false),
    checkMotherInUnbiasEff_(makeMCUnbiasTree_ ? iConfig.getParameter<bool>("checkMotherInUnbiasEff") : false),
    tagProbePairMaker_(iConfig),
    treeFiller_(new tnp::TPTreeFiller(iConfig)),
    oldTagFiller_((iConfig.existsAs<bool>("fillTagTree") && iConfig.getParameter<bool>("fillTagTree")) ? new tnp::BaseTreeFiller("tag_tree",iConfig) : 0)// ,
//     jetSrc_(iConfig.getParameter<edm::InputTag>("jets"))
{
    if (isMC_) { 
        // For mc efficiency we need the MC matches for tags & probes
        tagMatches_ = iConfig.getParameter<edm::InputTag>("tagMatches");
        probeMatches_ = iConfig.getParameter<edm::InputTag>("probeMatches");
        //.. and the pdgids of the possible mothers
        if (iConfig.existsAs<int32_t>("motherPdgId")) {
            motherPdgId_.insert(iConfig.getParameter<int32_t>("motherPdgId"));
        } else {
            std::vector<int32_t> motherIds = iConfig.getParameter<std::vector<int32_t> >("motherPdgId");
            motherPdgId_.insert(motherIds.begin(), motherIds.end());
        }

        // For unbiased efficiency we also need the collection of all probes
        if (makeMCUnbiasTree_) {
            allProbes_ = iConfig.getParameter<edm::InputTag>("allProbes");
            mcUnbiasFiller_.reset(new tnp::BaseTreeFiller("mcUnbias_tree",iConfig));
        }
    }

    edm::ParameterSet tagPSet;
    if (iConfig.existsAs<edm::ParameterSet>("tagVariables")) tagPSet.addParameter<edm::ParameterSet>("variables", iConfig.getParameter<edm::ParameterSet>("tagVariables"));
    if (iConfig.existsAs<edm::ParameterSet>("tagFlags"    )) tagPSet.addParameter<edm::ParameterSet>("flags",     iConfig.getParameter<edm::ParameterSet>("tagFlags"));
    if (!tagPSet.empty()) { tagFiller_.reset(new tnp::BaseTreeFiller(*treeFiller_, tagPSet, "tag_")); }
    edm::ParameterSet mcPSet;
    if (iConfig.existsAs<edm::ParameterSet>("mcVariables")) mcPSet.addParameter<edm::ParameterSet>("variables", iConfig.getParameter<edm::ParameterSet>("mcVariables"));
    if (iConfig.existsAs<edm::ParameterSet>("mcFlags"    )) mcPSet.addParameter<edm::ParameterSet>("flags",     iConfig.getParameter<edm::ParameterSet>("mcFlags"));
    if (!mcPSet.empty()) { mcFiller_.reset(new tnp::BaseTreeFiller(*treeFiller_, mcPSet, "mc_")); }
    edm::ParameterSet pairPSet;
    if (iConfig.existsAs<edm::ParameterSet>("pairVariables")) pairPSet.addParameter<edm::ParameterSet>("variables", iConfig.getParameter<edm::ParameterSet>("pairVariables"));
    if (iConfig.existsAs<edm::ParameterSet>("pairFlags"    )) pairPSet.addParameter<edm::ParameterSet>("flags",     iConfig.getParameter<edm::ParameterSet>("pairFlags"));
    if (!pairPSet.empty()) { pairFiller_.reset(new tnp::BaseTreeFiller(*treeFiller_, pairPSet, "pair_")); }

//     edm::ParameterSet jetPSet;
//     if (iConfig.existsAs<edm::ParameterSet>("jetVariables")) jetPSet.addParameter<edm::ParameterSet>("variables", iConfig.getParameter<edm::ParameterSet>("jetVariables"));
//     if (iConfig.existsAs<edm::ParameterSet>("jetFlags"    )) jetPSet.addParameter<edm::ParameterSet>("flags",     iConfig.getParameter<edm::ParameterSet>("jetFlags"));
//     if (!jetPSet.empty()) { jetFiller_.reset(new tnp::BaseTreeFiller(*treeFiller_, jetPSet, "jet_")); }
}


TagProbeFitTreeProducer::~TagProbeFitTreeProducer()
{
}


//
// member functions
//

// ------------ method called to for each event  ------------
void
TagProbeFitTreeProducer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    using namespace edm; using namespace std; 
    Handle<reco::CandidateView> src, allProbes;
    Handle<Association<vector<reco::GenParticle> > > tagMatches, probeMatches;

    treeFiller_->init(iEvent); // read out info from the event if needed (external vars, list of passing probes, ...)
    if (oldTagFiller_.get()) oldTagFiller_->init(iEvent);
    if (tagFiller_.get())    tagFiller_->init(iEvent);
    if (pairFiller_.get())   pairFiller_->init(iEvent);
//     if (jetFiller_.get())    jetFiller_->init(iEvent);
    if (mcFiller_.get())     mcFiller_->init(iEvent);

    // on mc we want to load also the MC match info
    if (isMC_) {
        iEvent.getByLabel(tagMatches_, tagMatches);
        iEvent.getByLabel(probeMatches_, probeMatches);
    }

    // get the list of (tag+probe) pairs, performing arbitration 
    tnp::TagProbePairs pairs = tagProbePairMaker_.run(iEvent);
    // loop on them to fill the tree
    for (tnp::TagProbePairs::const_iterator it = pairs.begin(), ed = pairs.end(); it != ed; ++it) {
        // on mc, fill mc info (on non-mc, let it to 'true', the treeFiller will ignore it anyway
        bool mcTrue = false;
        if (isMC_ && makeMCUnbiasTree_) {
            reco::GenParticleRef mtag = (*tagMatches)[it->tag], mprobe = (*probeMatches)[it->probe];
            mcTrue = checkMother(mtag) && checkMother(mprobe);
            if (mcTrue && mcFiller_.get()) mcFiller_->fill(reco::CandidateBaseRef(mprobe));
        }
        // fill in the variables for this t+p pair
	if (tagFiller_.get())    tagFiller_->fill(it->tag);
	if (oldTagFiller_.get()) oldTagFiller_->fill(it->tag);
	if (pairFiller_.get())   pairFiller_->fill(it->pair);
// 	std::cout << "Probe #" << it - pairs.begin() << " ET: " << it->probe->et();
// 	std::cout << " GeV---------------\n";
	treeFiller_->fill(it->probe, it->mass, mcTrue);
// 	std::cout << "--------------------\n";
    }

    // loop over jets
//     edm::Handle<reco::CandidateView> pJets;
//     iEvent.getByLabel(jetSrc_, pJets);
//     for (reco::CandidateView::const_iterator iJet = pJets->begin(); iJet != pJets->end(); ++iJet) {
//       if (jetFiller_.get()) jetFiller_->fill(pJets->refAt(iJet - pJets->begin());
//     }

    if (isMC_ && makeMCUnbiasTree_) {
        // read full collection of probes
        iEvent.getByLabel(allProbes_, allProbes);
        // init the tree filler
        mcUnbiasFiller_->init(iEvent);
        // loop on probes
        for (size_t i = 0, n = allProbes->size(); i < n; ++i) {
            const reco::CandidateBaseRef & probe = allProbes->refAt(i);
            // check mc match, and possibly mother match
            reco::GenParticleRef probeMatch = (*probeMatches)[probe];
            bool probeOk = checkMotherInUnbiasEff_ ? checkMother(probeMatch) : probeMatch.isNonnull();
            // fill the tree only for good ones
            if (probeOk) {
	      mcUnbiasFiller_->fill(probe);
	    }
        }
    }
   
}

bool
TagProbeFitTreeProducer::checkMother(const reco::GenParticleRef &ref) const {
    if (ref.isNull()) return false;
    if (motherPdgId_.empty()) return true;
    if (motherPdgId_.find(abs(ref->pdgId())) != motherPdgId_.end()) return true;
    reco::GenParticle::mothers m = ref->motherRefVector();
    for (reco::GenParticle::mothers::const_iterator it = m.begin(), e = m.end(); it != e; ++it) {
        if (checkMother(*it)) return true;
    }
    return false;
}


// ------------ method called once each job just after ending the event loop  ------------
void 
TagProbeFitTreeProducer::endJob() {
    // ask to write the current PSet info into the TTree header
    treeFiller_->writeProvenance(edm::getProcessParameterSet());
}

//define this as a plug-in
DEFINE_FWK_MODULE(TagProbeFitTreeProducer);
