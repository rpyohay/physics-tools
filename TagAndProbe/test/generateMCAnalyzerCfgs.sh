#!/bin/bash

#parameters
type="data"
label="_dRJet05" #should begin with an _
#input_dirs="SCToECALIso SCToHCALIso SCToTrackIso SCToIsoVLOnly SCToCombinedIso SCToHOverE SCToR9 SCToSigmaIetaIeta SCToIsoVLR9Id SCToIsoVL SCToR9Id" #ignore trigger efficiencies for now
input_dirs="SCToIsoVL"

#variables
input_file_names_data="\"\/data2\/yohay\/RA3\/data_tagProbeTrees\/Prompt_17-8_runs165088-166346\/tagProbeTree\.root\",\n    \"\/data2\/yohay\/RA3\/data_tagProbeTrees\/Prompt_17-8_runs166347-167913\/tagProbeTree\.root\",\n    \"\/data2\/yohay\/RA3\/data_tagProbeTrees\/Aug05ReReco_17-8\/tagProbeTree\.root\",\n    \"\/data2\/yohay\/RA3\/data_tagProbeTrees\/Prompt_17-8_runs172620-173692\/tagProbeTree\.root\",\n    \"\/data2\/yohay\/RA3\/data_tagProbeTrees\/Prompt_17-8_runs175860-180252\/tagProbeTree\.root\""
input_file_names_signal_MC="\"\/data2\/yohay\/RA3\/MC_tagProbeTrees\/DYJetsToLL_17-8\/tagProbeTree_final\.root\""
input_file_names_background_MC="\"\/data2\/yohay\/RA3\/MC_tagProbeTrees\/QCD_Pt-20to30_BCtoE_17-8\/tagProbeTree_final\.root\",\n    \"\/data2\/yohay\/RA3\/MC_tagProbeTrees\/QCD_Pt-30to80_BCtoE_17-8\/tagProbeTree_final\.root\",\n    \"\/data2\/yohay\/RA3\/MC_tagProbeTrees\/QCD_Pt-80to170_BCtoE_17-8\/tagProbeTree_final\.root\",\n    \"\/data2\/yohay\/RA3\/MC_tagProbeTrees\/GJet_Pt-20_doubleEMEnriched_17-8\/tagProbeTree_final\.root\",\n    \"\/data2\/yohay\/RA3\/MC_tagProbeTrees\/WJetsToLNu_17-8\/tagProbeTree_final\.root\",\n    \"\/data2\/yohay\/RA3\/MC_tagProbeTrees\/TTJets_17-8\/tagProbeTree_final\.root\",\n    "
#input_file_names_signal_MC="\"\/data2\/yohay\/RA3\/MC_tagProbeTrees\/DYJetsToLL_17-8\/tagProbeTree_SCToIsoVLOnly\.root\""
#input_file_names_background_MC="\"\/data2\/yohay\/RA3\/MC_tagProbeTrees\/QCD_Pt-20to30_BCtoE_17-8\/tagProbeTree_SCToIsoVLOnly\.root\",\n    \"\/data2\/yohay\/RA3\/MC_tagProbeTrees\/QCD_Pt-30to80_BCtoE_17-8\/tagProbeTree_SCToIsoVLOnly\.root\",\n    \"\/data2\/yohay\/RA3\/MC_tagProbeTrees\/QCD_Pt-80to170_BCtoE_17-8\/tagProbeTree_SCToIsoVLOnly\.root\",\n    \"\/data2\/yohay\/RA3\/MC_tagProbeTrees\/GJet_Pt-20_doubleEMEnriched_17-8\/tagProbeTree_SCToIsoVLOnly\.root\",\n    \"\/data2\/yohay\/RA3\/MC_tagProbeTrees\/WJetsToLNu_17-8\/tagProbeTree_SCToIsoVLOnly\.root\",\n    \"\/data2\/yohay\/RA3\/MC_tagProbeTrees\/TTJets_17-8\/tagProbeTree_SCToIsoVLOnly\.root\",\n    "
output_file_name_data="\"\/data2\/yohay\/RA3\/data_tagProbeTrees\/eff_EFFICIENCY${label}\.root\""
output_file_name_MC="\"\/data2\/yohay\/RA3\/MC_tagProbeTrees\/eff_EFFICIENCY${label}\.root\""
weight_line_data=""
weight_line_MC="WeightVariable = cms\.string(\"totalWeight\"),"
unbinned_vars_data="\"mass\""
unbinned_vars_MC="\"mass\", \"totalWeight\""

#set the variables depending on data or MC
if [ $type = "data" ]
    then
    input_file_names=$input_file_names_data
    input_file_names_bkg=$input_file_names_data
    output_file_name=$output_file_name_data
    weight_line=$weight_line_data
    unbinned_vars=$unbinned_vars_data
elif [ $type = "MC" ]
    then
    input_file_names=$input_file_names_signal_MC
    input_file_names_bkg=$input_file_names_background_MC
    output_file_name=$output_file_name_MC
    weight_line=$weight_line_MC
    unbinned_vars=$unbinned_vars_MC
else
    echo "type must be data or MC, not $type"
    exit 1
fi

#generate an analysis cfg file for a given dataset/efficiency
for input_dir in $input_dirs
  do
  output_final=`echo $output_file_name | sed -e "s%EFFICIENCY%$input_dir%"`
  sed -e "s%INPUT_DIRECTORY_NAME%$input_dir%g" -e "s%INPUT_FILE_NAMES%$input_file_names%g" -e "s%INPUT_BKG_FILE_NAMES%$input_file_names_bkg%g" -e "s%OUTPUT_FILE_NAME%$output_final%g" -e "s%WEIGHT_LINE%$weight_line%g" -e "s%UNBINNED_VARS%$unbinned_vars%g" photon_TagProbeFitTreeAnalyzer_cfg.py > photon_TagProbeFitTreeAnalyzer_${type}_${input_dir}${label}_cfg.py
done

exit 0
