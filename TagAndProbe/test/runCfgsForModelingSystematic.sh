#!/bin/bash

#dir="analysis_golden_JSON_24052011_defaultPU_01072011_Photon-Run2011A-DoublePhoton-May10ReReco-v1"
dir="eff_MC"
type="MC"

#set up CMSSW environment
cd ~/CMSSW_4_2_5/src
eval `scramv1 runtime -sh`
cd PhysicsTools/TagAndProbe/test

#run cfg files sequentially
for cfg in `ls -alh /data2/yohay/$dir/shape_model_systematic | grep py | awk '{ print $9 }'`
  do
  identifier=`echo $cfg | sed -e "s%"$type"_shapeModelingSystematic_\(.*\)\.py%\1%"`
  if [ ! -e "/data2/yohay/$dir/shape_model_systematic/efficiency_${identifier}.root" ]
      then
      cp /data2/yohay/$dir/shape_model_systematic/$cfg .
      echo "cmsRun $cfg > /data2/yohay/$dir/shape_model_systematic/efficiency_${identifier}.txt"
      cmsRun $cfg > /data2/yohay/$dir/shape_model_systematic/efficiency_${identifier}.txt
      rm $cfg*
  fi
done

exit 0
