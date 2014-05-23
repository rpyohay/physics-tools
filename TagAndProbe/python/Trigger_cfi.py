import FWCore.ParameterSet.Config as cms

#implementation of trgMatchedPhotonProducer that accepts multiple HLT paths
probePhotonsPassingHLTEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingIdEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon32_CaloIdL_Photon26_CaloIdL_v2", "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag("hltEG32CaloIdLClusterShapeFilter")
    )
probePhotonsPassingHLTEE = probePhotonsPassingHLTEB.clone()
probePhotonsPassingHLTEE.InputProducer = cms.InputTag("probePhotonsPassingIdEE")

##################### 26 IsoVL / 18 leading #####################
#unprescaled runs 160404-161215

#photons passing IsoVL && R9Id that fire the leading leg of 26 IsoVL / 18
selectedIsoVLR9IdPhotonsPassingHLT26IsoVL18LeadingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLR9IdEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon26_IsoVL_Photon18_v2", "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag("hltPhoton26IsoVLTrackIsoFilter")
    )

#photons passing IsoVL that fire the leading leg of 26 IsoVL / 18
selectedIsoVLPhotonsPassingHLT26IsoVL18LeadingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon26_IsoVL_Photon18_v2", "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag("hltPhoton26IsoVLTrackIsoFilter")
    )

#photons passing R9Id that fire the leading leg of 26 IsoVL / 18
selectedR9IdPhotonsPassingHLT26IsoVL18LeadingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdR9IdEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon26_IsoVL_Photon18_v2", "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag("hltPhoton26IsoVLTrackIsoFilter")
    )

##################### 26 IsoVL / 18 trailing #####################
#unprescaled runs 160404-161215

#photons passing IsoVL && R9Id that fire the trailing leg of 26 IsoVL / 18
selectedIsoVLR9IdPhotonsPassingHLT26IsoVL18TrailingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLR9IdEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon26_IsoVL_Photon18_v2", "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag(
    "hltDoubleIsoEG18HELastFilter"
    )
    )

#photons passing IsoVL that fire the trailing leg of 26 IsoVL / 18
selectedIsoVLPhotonsPassingHLT26IsoVL18TrailingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon26_IsoVL_Photon18_v2", "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag(
    "hltDoubleIsoEG18HELastFilter"
    )
    )

#photons passing R9Id that fire the trailing leg of 26 IsoVL / 18
selectedR9IdPhotonsPassingHLT26IsoVL18TrailingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdR9IdEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon26_IsoVL_Photon18_v2", "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag(
    "hltDoubleIsoEG18HELastFilter"
    )
    )

##################### 36 CaloIdL / 22 CaloIdL leading #####################
#unprescaled runs 161216-166346

#photons passing IsoVL && R9Id that fire the leading leg of 36 CaloIdL / 22 CaloIdL
selectedIsoVLR9IdPhotonsPassingHLT36CaloIdL22CaloIdLLeadingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLR9IdEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon36_CaloIdL_Photon22_CaloIdL_v2", "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag("hltEG36CaloIdLClusterShapeFilter")
    )

#photons passing IsoVL that fire the leading leg of 36 CaloIdL / 22 CaloIdL
selectedIsoVLPhotonsPassingHLT36CaloIdL22CaloIdLLeadingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon36_CaloIdL_Photon22_CaloIdL_v2", "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag("hltEG36CaloIdLClusterShapeFilter")
    )

#photons passing R9Id that fire the leading leg of 36 CaloIdL / 22 CaloIdL
selectedR9IdPhotonsPassingHLT36CaloIdL22CaloIdLLeadingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdR9IdEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon36_CaloIdL_Photon22_CaloIdL_v2", "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag("hltEG36CaloIdLClusterShapeFilter")
    )

##################### 36 CaloIdL / 22 CaloIdL trailing #####################
#unprescaled runs 161216-166346

#photons passing IsoVL && R9Id that fire the trailing leg of 36 CaloIdL / 22 CaloIdL
selectedIsoVLR9IdPhotonsPassingHLT36CaloIdL22CaloIdLTrailingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLR9IdEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon36_CaloIdL_Photon22_CaloIdL_v2", "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag(
    "hltPhoton36CaloIdLPhoton22CaloIdLEgammaClusterShapeDoubleFilter"
    )
    )

#photons passing IsoVL that fire the trailing leg of 36 CaloIdL / 22 CaloIdL
selectedIsoVLPhotonsPassingHLT36CaloIdL22CaloIdLTrailingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon36_CaloIdL_Photon22_CaloIdL_v2", "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag(
    "hltPhoton36CaloIdLPhoton22CaloIdLEgammaClusterShapeDoubleFilter"
    )
    )

#photons passing R9Id that fire the trailing leg of 36 CaloIdL / 22 CaloIdL
selectedR9IdPhotonsPassingHLT36CaloIdL22CaloIdLTrailingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdR9IdEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon36_CaloIdL_Photon22_CaloIdL_v2", "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag(
    "hltPhoton36CaloIdLPhoton22CaloIdLEgammaClusterShapeDoubleFilter"
    )
    )

##################### 36 CaloIdL IsoVL / 22 CaloIdL IsoVL leading #####################
#unprescaled runs 165970-180252

#photons passing IsoVL && R9Id that fire the leading leg of 36 CaloIdL IsoVL / 22 CaloIdL IsoVL
selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLLeadingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLR9IdEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v2",
                                         "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag("hltEG36CaloIdLIsoVLHcalIsoLastFilter")
    )

#photons passing IsoVL that fire the leading leg of 36 CaloIdL IsoVL / 22 CaloIdL IsoVL
selectedIsoVLPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLLeadingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v2",
                                         "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag("hltEG36CaloIdLIsoVLHcalIsoLastFilter")
    )

##################### 36 CaloIdL IsoVL / 22 CaloIdL IsoVL trailing #####################
#unprescaled runs 165970-180252

#photons passing IsoVL && R9Id that fire the trailing leg of 36 CaloIdL IsoVL / 22 CaloIdL IsoVL
selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLTrailingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLR9IdEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v2",
                                         "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag(
    "hltDoubleIsoEG22TrackIsolDoubleLastFilterUnseeded"
    )
    )

#photons passing IsoVL that fire the trailing leg of 36 CaloIdL IsoVL / 22 CaloIdL IsoVL
selectedIsoVLPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLTrailingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_CaloIdL_IsoVL_v2",
                                         "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag(
    "hltDoubleIsoEG22TrackIsolDoubleLastFilterUnseeded"
    )
    )

##################### 36 CaloIdL IsoVL / 22 R9Id leading #####################
#unprescaled runs 165970-180252

#photons passing IsoVL && R9Id that fire the leading leg of 36 CaloIdL IsoVL / 22 R9Id
selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22R9IdLeadingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLR9IdEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v2",
                                         "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag("hltEG36CaloIdLIsoVLTrackIsoLastFilter")
    )

#photons passing IsoVL that fire the leading leg of 36 CaloIdL IsoVL / 22 R9Id
selectedIsoVLPhotonsPassingHLT36CaloIdLIsoVL22R9IdLeadingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v2",
                                         "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag("hltEG36CaloIdLIsoVLTrackIsoLastFilter")
    )

##################### 36 CaloIdL IsoVL / 22 R9Id trailing #####################
#unprescaled runs 165970-180252

#photons passing IsoVL && R9Id that fire the trailing leg of 36 CaloIdL IsoVL / 22 R9Id
selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22R9IdTrailingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLR9IdEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v2",
                                         "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag(
    "hltDoubleIsoEG22TrackIsolLastFilterUnseeded"
    )
    )

#photons passing R9Id that fire the trailing leg of 36 CaloIdL IsoVL / 22 R9Id
selectedR9IdPhotonsPassingHLT36CaloIdLIsoVL22R9IdTrailingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdR9IdEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon36_CaloIdL_IsoVL_Photon22_R9Id_v2",
                                         "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag(
    "hltDoubleIsoEG22TrackIsolLastFilterUnseeded"
    )
    )

##################### 36 R9Id / 22 CaloIdL IsoVL leading #####################
#unprescaled runs 165970-180252

#photons passing IsoVL && R9Id that fire the leading leg of 36 R9Id / 22 CaloIdL IsoVL
selectedIsoVLR9IdPhotonsPassingHLT36R9Id22CaloIdLIsoVLLeadingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLR9IdEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v2",
                                         "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag("hltEG36R9IdLastFilter")
    )

#photons passing R9Id that fire the leading leg of 36 R9Id / 22 CaloIdL IsoVL
selectedR9IdPhotonsPassingHLT36R9Id22CaloIdLIsoVLLeadingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdR9IdEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v2",
                                         "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag("hltEG36R9IdLastFilter")
    )

##################### 36 R9Id / 22 CaloIdL IsoVL trailing #####################
#unprescaled runs 165970-180252

#photons passing IsoVL && R9Id that fire the trailing leg of 36 R9Id / 22 CaloIdL IsoVL
selectedIsoVLR9IdPhotonsPassingHLT36R9Id22CaloIdLIsoVLTrailingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLR9IdEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v2",
                                         "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag(
    "hltDoubleIsoEG22TrackIsolLastFilterUnseeded"
    )
    )

#photons passing IsoVL that fire the trailing leg of 36 R9Id / 22 CaloIdL IsoVL
selectedIsoVLPhotonsPassingHLT36R9Id22CaloIdLIsoVLTrailingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon36_R9Id_Photon22_CaloIdL_IsoVL_v2",
                                         "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag(
    "hltDoubleIsoEG22TrackIsolLastFilterUnseeded"
    )
    )

##################### 36 R9Id / 22 R9Id leading #####################
#unprescaled runs 165970-180252

#photons passing IsoVL && R9Id that fire the leading leg of 36 R9Id / 22 R9Id
selectedIsoVLR9IdPhotonsPassingHLT36R9Id22R9IdLeadingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLR9IdEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon36_R9Id_Photon22_R9Id_v2",
                                         "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag("hltEG36R9IdLastFilter")
    )

#photons passing R9Id that fire the leading leg of 36 R9Id / 22 R9Id
selectedR9IdPhotonsPassingHLT36R9Id22R9IdLeadingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdR9IdEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon36_R9Id_Photon22_R9Id_v2",
                                         "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag("hltEG36R9IdLastFilter")
    )

##################### 36 R9Id / 22 R9Id trailing #####################
#unprescaled runs 165970-180252

#photons passing IsoVL && R9Id that fire the trailing leg of 36 R9Id / 22 R9Id
selectedIsoVLR9IdPhotonsPassingHLT36R9Id22R9IdTrailingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdIsoVLR9IdEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon36_R9Id_Photon22_R9Id_v2",
                                         "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag("hltDoubleIsoEG22R9IdDoubleLastFilterUnseeded")
    )

#photons passing R9Id that fire the trailing leg of 36 R9Id / 22 R9Id
selectedR9IdPhotonsPassingHLT36R9Id22R9IdTrailingEB = cms.EDProducer(
    "trgMatchedPhotonProducer",                     
    InputProducer = cms.InputTag("probePhotonsPassingPUCorrectedCombinedIsoIdR9IdEB"),
    hltTags = cms.VInputTag(cms.InputTag("HLT_Photon36_R9Id_Photon22_R9Id_v2",
                                         "", "HLT")),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults", "", "HLT"),
    isTriggerFilter = cms.untracked.bool(True),
    HLTSubFilters = cms.untracked.VInputTag("hltDoubleIsoEG22R9IdDoubleLastFilterUnseeded")
    )

#trigger sequences
trigger_sequence_May10ReReco1 = cms.Sequence(
    selectedIsoVLR9IdPhotonsPassingHLT26IsoVL18LeadingEB + 
    selectedIsoVLPhotonsPassingHLT26IsoVL18LeadingEB + 
    selectedIsoVLR9IdPhotonsPassingHLT26IsoVL18TrailingEB + 
    selectedIsoVLPhotonsPassingHLT26IsoVL18TrailingEB
    )
trigger_sequence_May10ReReco2 = cms.Sequence(
    selectedIsoVLR9IdPhotonsPassingHLT36CaloIdL22CaloIdLLeadingEB + 
    selectedIsoVLPhotonsPassingHLT36CaloIdL22CaloIdLLeadingEB + 
    selectedIsoVLR9IdPhotonsPassingHLT36CaloIdL22CaloIdLTrailingEB + 
    selectedIsoVLPhotonsPassingHLT36CaloIdL22CaloIdLTrailingEB
    )
trigger_sequence_postMay10ReReco = cms.Sequence(
    selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLLeadingEB + 
    selectedIsoVLPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLLeadingEB + 
    selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLTrailingEB + 
    selectedIsoVLPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLTrailingEB + 
    selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22R9IdLeadingEB + 
    selectedIsoVLPhotonsPassingHLT36CaloIdLIsoVL22R9IdLeadingEB + 
    selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22R9IdTrailingEB + 
    selectedIsoVLR9IdPhotonsPassingHLT36R9Id22CaloIdLIsoVLLeadingEB + 
    selectedIsoVLR9IdPhotonsPassingHLT36R9Id22CaloIdLIsoVLTrailingEB + 
    selectedIsoVLPhotonsPassingHLT36R9Id22CaloIdLIsoVLTrailingEB + 
    selectedIsoVLR9IdPhotonsPassingHLT36R9Id22R9IdLeadingEB + 
    selectedIsoVLR9IdPhotonsPassingHLT36R9Id22R9IdTrailingEB
    )
trigger_sequence_2011 = cms.Sequence(
    selectedIsoVLR9IdPhotonsPassingHLT26IsoVL18LeadingEB + 
    selectedIsoVLPhotonsPassingHLT26IsoVL18LeadingEB + 
    selectedIsoVLR9IdPhotonsPassingHLT26IsoVL18TrailingEB + 
    selectedIsoVLPhotonsPassingHLT26IsoVL18TrailingEB + 
    selectedIsoVLR9IdPhotonsPassingHLT36CaloIdL22CaloIdLLeadingEB + 
    selectedIsoVLPhotonsPassingHLT36CaloIdL22CaloIdLLeadingEB + 
    selectedIsoVLR9IdPhotonsPassingHLT36CaloIdL22CaloIdLTrailingEB + 
    selectedIsoVLPhotonsPassingHLT36CaloIdL22CaloIdLTrailingEB + 
    selectedIsoVLR9IdPhotonsPassingHLT36CaloIdL22CaloIdLLeadingEB + 
    selectedIsoVLPhotonsPassingHLT36CaloIdL22CaloIdLLeadingEB + 
    selectedIsoVLR9IdPhotonsPassingHLT36CaloIdL22CaloIdLTrailingEB + 
    selectedIsoVLPhotonsPassingHLT36CaloIdL22CaloIdLTrailingEB + 
    selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLLeadingEB + 
    selectedIsoVLPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLLeadingEB + 
    selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLTrailingEB + 
    selectedIsoVLPhotonsPassingHLT36CaloIdLIsoVL22CaloIdLIsoVLTrailingEB + 
    selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22R9IdLeadingEB + 
    selectedIsoVLPhotonsPassingHLT36CaloIdLIsoVL22R9IdLeadingEB + 
    selectedIsoVLR9IdPhotonsPassingHLT36CaloIdLIsoVL22R9IdTrailingEB + 
    selectedIsoVLR9IdPhotonsPassingHLT36R9Id22CaloIdLIsoVLLeadingEB + 
    selectedIsoVLR9IdPhotonsPassingHLT36R9Id22CaloIdLIsoVLTrailingEB + 
    selectedIsoVLPhotonsPassingHLT36R9Id22CaloIdLIsoVLTrailingEB + 
    selectedIsoVLR9IdPhotonsPassingHLT36R9Id22R9IdLeadingEB + 
    selectedIsoVLR9IdPhotonsPassingHLT36R9Id22R9IdTrailingEB
    )
