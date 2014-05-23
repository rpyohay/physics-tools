{
  gROOT->Reset();
  gROOT->LoadMacro("/afs/cern.ch/user/y/yohay/CMSSW_4_2_5/src/PhysicsTools/TagAndProbe/test/computeVariedScaleFactors.C++");

  computeVariedScaleFactors("data_efficiency_variations_1Sigma.txt", 
			    "MC_efficiency_variations_1Sigma.txt", 
			    "scale_factor_variations_1Sigma.txt", 4, 0.953);
}
