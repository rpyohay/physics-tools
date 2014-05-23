{
  gROOT->Reset();
  gROOT->LoadMacro("/afs/cern.ch/user/y/yohay/CMSSW_4_2_8/src/PhysicsTools/TagAndProbe/test/Data.C++");
  gROOT->LoadMacro("/afs/cern.ch/user/y/yohay/CMSSW_4_2_8/src/PhysicsTools/TagAndProbe/test/MC.C++");
  gROOT->LoadMacro("/afs/cern.ch/user/y/yohay/CMSSW_4_2_8/src/PhysicsTools/TagAndProbe/test/TreeEditing.C++");

  vector<string> input;
  input.push_back("/data2/yohay/RA3/MC_tagProbeTrees/DYJetsToLL_17-8/tagProbeTree.root");
  input.push_back("/data2/yohay/RA3/MC_tagProbeTrees/GJet_Pt-20_doubleEMEnriched_17-8/tagProbeTree.root");
  input.push_back("/data2/yohay/RA3/MC_tagProbeTrees/QCD_Pt-20to30_BCtoE_17-8/tagProbeTree.root");
  input.push_back("/data2/yohay/RA3/MC_tagProbeTrees/QCD_Pt-30to80_BCtoE_17-8/tagProbeTree.root");
  input.push_back("/data2/yohay/RA3/MC_tagProbeTrees/QCD_Pt-80to170_BCtoE_17-8/tagProbeTree.root");
  input.push_back("/data2/yohay/RA3/MC_tagProbeTrees/TTJets_17-8/tagProbeTree.root");
  input.push_back("/data2/yohay/RA3/MC_tagProbeTrees/WJetsToLNu_17-8/tagProbeTree.root");

  vector<string> dirs;
  dirs.push_back("SCToIsoVLOnly");

  addVariables(input, dirs, "SCToIsoVLOnly");
}
