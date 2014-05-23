{
  gROOT->Reset();
  gROOT->LoadMacro("/afs/cern.ch/user/y/yohay/CMSSW_4_2_5/src/PhysicsTools/TagAndProbe/test/DataTree.C++");
  gROOT->LoadMacro("/afs/cern.ch/user/y/yohay/CMSSW_4_2_5/src/PhysicsTools/TagAndProbe/test/MCTree.C++");
  gROOT->LoadMacro("/afs/cern.ch/user/y/yohay/CMSSW_4_2_5/src/PhysicsTools/TagAndProbe/test/KinematicAnalysis.C++");
  analyzeDRTagProbe("/data2/yohay/kinematic_analysis.root");
}
