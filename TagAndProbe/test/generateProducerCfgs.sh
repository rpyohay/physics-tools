#!/bin/bash

#variables
datasets[0]="DYJetsToLL"
datasets[1]="QCD_Pt-20to30_BCtoE"
datasets[2]="QCD_Pt-30to80_BCtoE"
datasets[3]="QCD_Pt-80to170_BCtoE"
datasets[4]="GJet_Pt-20_doubleEMEnriched"
datasets[5]="WJetsToLNu"
datasets[6]="TTJets"
weights[0]=0.319992240404159
weights[1]=315.033614934434
weights[2]=331.900537183386
weights[3]=40.801366594901
weights[4]=0.347352542647261
weights[5]=1.59904199108736
weights[6]=0.00744549781946322
xsecs[0]=2475.0
xsecs[1]=139240 #xsec*filterEff
xsecs[2]=143748 #xsec*filterEff
xsecs[3]=9431.1 #xsec*filterEff
xsecs[4]=501.15 #xsec*filterEff
xsecs[5]=27770.0
xsecs[6]=94.76
nsEvts[0]=36228691
nsEvts[1]=2071133
nsEvts[2]=2030033
nsEvts[3]=1082691
nsEvts[4]=6757937
nsEvts[5]=81345381
nsEvts[6]=59613991
array_len=`expr ${#datasets[@]} - 1`
PU_only_flag="False"
if [ $PU_only_flag = "True" ]
    then
    PU_only="altPUOnly"
else
    PU_only="defaultPU"
fi
#data_reco_era="all2011"

#generate a producer cfg file for a given MC dataset with a particular weight
for i in `seq 0 $array_len`
  do
  event_weight=${weights[$i]}
  xsec=${xsecs[$i]}
  nEvts=${nsEvts[$i]}
  dataset=${datasets[$i]}
  #sample=`echo $dataset | sed -e "s%_%%g" -e "s%-%To%"`
  #echo $sample
  #sed -e "s%MY_EVENT_WEIGHT%$event_weight%g" -e "s%MY_XSEC%$xsec%g" -e "s%MY_NEVTS%$nEvts%g" -e "s%MY_SAMPLE%$dataset%g" -e "s%PU_ONLY_FLAG%$PU_only_flag%g" -e "s%MY_DATA_RECO_ERA%$data_reco_era%g" Photon_TagProbeTreeProducer_MC_template_cfg.py > Photon_TagProbeTreeProducer_MC_${dataset}_${PU_only}_cfg.py
  sed -e "s%MY_EVENT_WEIGHT%$event_weight%g" -e "s%MY_XSEC%$xsec%g" -e "s%MY_NEVTS%$nEvts%g" -e "s%MY_SAMPLE%$dataset%g" -e "s%PU_ONLY_FLAG%$PU_only_flag%g" Photon_TagProbeTreeProducer_17-8_MC_cfg.py > Photon_TagProbeTreeProducer_17-8_MC_${dataset}_${PU_only}_cfg.py
#  sed -e "s%MY_EVENT_WEIGHT%$event_weight%g" -e "s%MY_XSEC%$xsec%g" -e "s%MY_NEVTS%$nEvts%g" -e "s%MY_SAMPLE%$dataset%g" -e "s%PU_ONLY_FLAG%$PU_only_flag%g" Photon_TagProbeTreeProducer_32-17_MC_cfg.py > Photon_TagProbeTreeProducer_32-17_MC_${dataset}_${PU_only}_cfg.py
done

exit 0
