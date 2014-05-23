import FWCore.ParameterSet.Config as cms

#make the PU weights for May10ReReco data
PUWeightProducerMay10ReReco = cms.EDProducer('PUWeightProducer',
                                             PU = cms.string("S6"),
                                             dataRecoEra = cms.string("May10ReReco"),
                                             PUSummaryInfoTag = cms.InputTag("addPileupInfo")
                                             )

#make the PU weights for PromptRecov4
PUWeightProducerPromptRecov4 = PUWeightProducerMay10ReReco.clone()
PUWeightProducerPromptRecov4.dataRecoEra = cms.string("PromptRecov4")

#make the PU weights for PromptRecov4 + Aug5ReReco + PromptRecov6 + Run2011BPromptRecov1
PUWeightProducerPostMay10ReReco = PUWeightProducerMay10ReReco.clone()
PUWeightProducerPostMay10ReReco.dataRecoEra = cms.string("postMay10ReReco")

#PU weight sequence
PU_weight_sequence = cms.Sequence(PUWeightProducerPostMay10ReReco)
