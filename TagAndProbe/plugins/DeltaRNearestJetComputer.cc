#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/Common/interface/View.h"

#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/Candidate.h"

#include "CommonTools/Utils/interface/StringCutObjectSelector.h"
#include "DataFormats/JetReco/interface/JPTJet.h"

class DeltaRNearestJetDRSortComputer : public edm::EDProducer {
    public:
        explicit DeltaRNearestJetDRSortComputer(const edm::ParameterSet & iConfig);
        virtual ~DeltaRNearestJetDRSortComputer() ;

        virtual void produce(edm::Event & iEvent, const edm::EventSetup & iSetup);
        void sortByMinDR2(double, std::vector<double>&) const;

    private:
        edm::InputTag probes_;            
        edm::InputTag objects_; 
  //edm::InputTag caloJets_;
        StringCutObjectSelector<reco::Candidate,true> objCut_; // lazy parsing, to allow cutting on variables not in reco::Candidate class
        double minDR_;
        unsigned int pos_;
};

DeltaRNearestJetDRSortComputer::DeltaRNearestJetDRSortComputer(const edm::ParameterSet & iConfig) :
    probes_(iConfig.getParameter<edm::InputTag>("probes")),
    objects_(iConfig.getParameter<edm::InputTag>("objects")),
    //caloJets_(iConfig.getParameter<edm::InputTag>("caloJets")),
    objCut_(iConfig.existsAs<std::string>("objectSelection") ? iConfig.getParameter<std::string>("objectSelection") : "", true),
    minDR_(iConfig.getParameter<double>("minDR")),
    pos_(iConfig.getUntrackedParameter<unsigned int>("pos", 0))
{
    produces<edm::ValueMap<float> >();
}


DeltaRNearestJetDRSortComputer::~DeltaRNearestJetDRSortComputer()
{
}

void 
DeltaRNearestJetDRSortComputer::produce(edm::Event & iEvent, const edm::EventSetup & iSetup) {
    using namespace edm;

    // read input
    Handle<View<reco::Candidate> > probes;
    Handle<View<reco::Jet> > objects;
    //Handle<View<reco::CaloJet> > caloJets;
    iEvent.getByLabel(probes_,  probes);
    iEvent.getByLabel(objects_, objects);
    //iEvent.getByLabel(caloJets_, caloJets);

    // prepare vector for output    
    std::vector<float> values;
    
    // fill
    unsigned int iProbe = 0;
    View<reco::Candidate>::const_iterator probe, endprobes = probes->end();
    View<reco::Jet>::const_iterator object, endobjects = objects->end();
    for (probe = probes->begin(); probe != endprobes; ++probe) {
	std::vector<double> dr2min;
	for (object = objects->begin(); object != endobjects; ++object) {
	  dr2min.push_back(10000);
	}
        for (object = objects->begin(); object != endobjects; ++object) {
            if (!objCut_(*object)) continue;

            double dr2 = deltaR2(*probe, /**(object->getCaloJetRef())*/*object);
	    if (dr2 > minDR_*minDR_) sortByMinDR2(dr2, dr2min);
            //if ((dr2 < dr2min1) && (dr2 > minDR_*minDR_)) { dr2min1 = dr2; }
        }
        //values.push_back(sqrt(dr2min));
	if (dr2min.size() == 0) values.push_back(100.0);
	else if (pos_ >= dr2min.size()) values.push_back(sqrt(dr2min[dr2min.size() - 1]));
	else values.push_back(sqrt(dr2min[pos_]));
	++iProbe;
    }

    // convert into ValueMap and store
    std::auto_ptr<ValueMap<float> > valMap(new ValueMap<float>());
    ValueMap<float>::Filler filler(*valMap);
    filler.insert(probes, values.begin(), values.end());
    filler.fill();
    iEvent.put(valMap);
}

void DeltaRNearestJetDRSortComputer::sortByMinDR2(double dr2, std::vector<double>& minDR2Vec) const
{
  bool foundSpot = false;
  unsigned int i = 0;
  while ((i < minDR2Vec.size()) && (!foundSpot)) {
    if (dr2 < minDR2Vec[i]) {
      for (unsigned int j = minDR2Vec.size() - 1; j >= (i + 1); --j) {
	minDR2Vec[j] = minDR2Vec[j - 1];
      }
      minDR2Vec[i] = dr2;
      foundSpot = true;
    }
    ++i;
  }
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(DeltaRNearestJetDRSortComputer);
