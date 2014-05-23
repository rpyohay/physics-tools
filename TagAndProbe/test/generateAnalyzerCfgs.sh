#!/bin/bash

#variables
#input_dirs="PhotonToIDEB PhotonToECALIso PhotonToHCALIso PhotonToHOverE PhotonToTrackIso PhotonToSigmaIetaIetaEB"
input_dirs="PhotonToIDEB"
#input_dirs_PUCorrected="PhotonToECALIsoPUCorrected PhotonToHCALIsoPUCorrected PhotonToIDPUCorrectedEB"
#input_dirs_PUCorrected="PhotonToIDPUCorrectedEB"
input_dirs_PUCorrected=""
dir_name_1="analysis_CMSSWv425_golden_JSON_24052011_defaultPU_Photon-Run2011A-DoublePhoton-May10ReReco-v1"
dir_name_2="analysis_newCfg_EgammaTightID_golden_JSON_05082011_defaultPU_Photon-Run2011A-DoublePhoton-PromptSkim-v4"
label="allData"
pass="probe_passing"
passRho="probe_passing_rho"
passNPV="probe_passing_nPV"

#generate an analysis cfg file for a given dataset/efficiency
for input_dir in $input_dirs
  do
  sed -e "s%INPUT_DIRECTORY_NAME%$input_dir%g" -e "s%DIR_NAME_1%$dir_name_1%" -e "s%DIR_NAME_2%$dir_name_2%" -e "s%LABEL%$label%" -e "s%PASS%$pass%g" photon_TagProbeFitTreeAnalyzer_data_template_cfg.py > photon_TagProbeFitTreeAnalyzer_data_${input_dir}_${label}_cfg.py
done
for input_dir in $input_dirs_PUCorrected
  do
  sed -e "s%INPUT_DIRECTORY_NAME%$input_dir%g" -e "s%DIR_NAME_1%$dir_name_1%" -e "s%DIR_NAME_2%$dir_name_2%" -e "s%LABEL%$label%" -e "s%PASS_RHO%$passRho%g" -e "s%PASS_NPV%$passNPV%g" photon_TagProbeFitTreeAnalyzer_data_PUCorrected_template_cfg.py > photon_TagProbeFitTreeAnalyzer_data_${input_dir}_${label}_cfg.py
done

exit 0
