#!/bin/bash

#variables
type="data"
label="_dRJet05" #should begin with an _
#input_dirs="SCToECALIso SCToHCALIso SCToTrackIso SCToIsoVLOnly SCToCombinedIso SCToHOverE SCToR9 SCToSigmaIetaIeta SCToIsoVLR9Id SCToIsoVL SCToR9Id" #ignore trigger efficiencies for now
input_dirs="SCToIsoVL"

#CMSSW environment
export SCRAM_ARCH=slc5_amd64_gcc434
eval `scramv1 runtime -sh`

#run analysis cfg file for a given dataset/efficiency
for input_dir in $input_dirs
  do
  echo "Calculating $input_dir efficiency..."
  cmsRun photon_TagProbeFitTreeAnalyzer_${type}_${input_dir}${label}_cfg.py > /data2/yohay/RA3/${type}_tagProbeTrees/${input_dir}${label}_stdout.txt
done

exit 0
