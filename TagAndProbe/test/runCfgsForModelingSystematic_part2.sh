#!/bin/bash

#dir="analysis_golden_JSON_24052011_defaultPU_01072011_Photon-Run2011A-DoublePhoton-May10ReReco-v1"
dir="eff_MC"
type="MC"

#set LANG variable to match that on uvapc01
export LANG C

#set up CMSSW environment
cd ~/CMSSW_4_2_5/src
eval `scramv1 runtime -sh`
cd PhysicsTools/TagAndProbe/test

#run cfg files sequentially
for cfg in `ls -alh /data/yohay/$dir/shape_model_systematic | grep py | awk '{ print $9 }' | tail -n 85`
  do
  identifier=`echo $cfg | sed -e "s%"$type"_shapeModelingSystematic_\(.*\)\.py%\1%"`
  if [ ! -e "/data/yohay/$dir/shape_model_systematic/efficiency_${identifier}.root" ]
      then
      cp /data/yohay/$dir/shape_model_systematic/$cfg .
      sed -e "s%data2%data%g" $cfg > uvapc00_$cfg
      echo "cmsRun uvapc00_$cfg > /data/yohay/$dir/shape_model_systematic/efficiency_${identifier}.txt"
      cmsRun uvapc00_$cfg > /data/yohay/$dir/shape_model_systematic/efficiency_${identifier}.txt
      rm $cfg*
      rm uvapc00_$cfg*
  fi
done

exit 0
