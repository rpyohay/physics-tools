#!/bin/bash

#variables
input_file_names_bkg="\"\/data2\/yohay\/eff_MC\/analysis_defaultPU_G_Pt-15to30_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_G_Pt-30to50_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_G_Pt-50to80_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_G_Pt-80to120_TuneZ2_7TeV_pythia6-Summer11-PU_S4_START42_V11-v1\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_G_Pt-120to170_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_G_Pt-170to300_TuneZ2_7TeV_pythia6-Summer11-PU_S4_START42_V11-v1\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_G_Pt-300to470_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_G_Pt-470to800_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_G_Pt-1800_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_QCD_Pt-15to30_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_QCD_Pt-30to50_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_QCD_Pt-50to80_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_QCD_Pt-80to120_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_QCD_Pt-120to170_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_QCD_Pt-170to300_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_QCD_Pt-300to470_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_QCD_Pt-470to600_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_QCD_Pt-600to800_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_QCD_Pt-800to1000_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_QCD_Pt-1000to1400_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_QCD_Pt-1400to1800_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_QCD_Pt-1800_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_TT_TuneZ2_7TeV-pythia6-tauola-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_WToENu_TuneZ2_7TeV-pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_WToTauNu_TuneZ2_7TeV-pythia6-tauola-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_DYToTauTau_M-20_TuneZ2_7TeV-pythia6-tauola-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\""
input_file_names="\"\/data2\/yohay\/eff_MC\/analysis_defaultPU_ZJetToEE_Pt-15to20_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_ZJetToEE_Pt-20to30_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_ZJetToEE_Pt-30to50_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_ZJetToEE_Pt-50to80_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_ZJetToEE_Pt-80to120_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_ZJetToEE_Pt-120to170_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_ZJetToEE_Pt-170to230_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_ZJetToEE_Pt-230to300_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\",\n    \"\/data2\/yohay\/eff_MC\/analysis_defaultPU_ZJetToEE_Pt-300_TuneZ2_7TeV_pythia6-Summer11-PU_S3_START42_V11-v2\/tagProbeTree_MC_photonToID_finalv2\.root\""
#missing:
#G_Pt-800to1400
#G_Pt-1400to1800

input_dirs="PhotonToIDEB"
#input_dirs_PUCorrected=""
dir_name="analysis_golden_JSON_24052011_defaultPU_01072011_Photon-Run2011A-DoublePhoton-May10ReReco-v1"
label="v2"

#open shape systematics file and grab stuff
num_lines=`cat model_variations_1Sigma.txt | wc -l`
arg_to_tail=`expr $num_lines - 1`
alphaPass=( $(cat model_variations_1Sigma.txt | tail -n $arg_to_tail | awk '{ print $1 }') )
nPass=( $(cat model_variations_1Sigma.txt | tail -n $arg_to_tail | awk '{ print $2 }') )
alphaFail=( $(cat model_variations_1Sigma.txt | tail -n $arg_to_tail | awk '{ print $3 }') )
nFail=( $(cat model_variations_1Sigma.txt | tail -n $arg_to_tail | awk '{ print $4 }') )
bkgShape=( $(cat model_variations_1Sigma.txt | tail -n $arg_to_tail | awk '{ print $5 }') )
num_cfgs=`expr ${#alphaPass[*]} - 1`

#generate an analysis cfg file for a given dataset/efficiency
for input_dir in $input_dirs
  do

  #this step won't be necessary with the latest ntuples
  if [ $input_dir = "PhotonToIDEB" ] || [ $input_dir = "PhotonToSigmaIetaIetaEB" ]
      then
      pass="probe_passing_sigmaIetaIeta_EB"
  else
      pass="probe_passing"
  fi

  #get stuff that has to be substituted into the generated file
  for i in `seq 0 $num_cfgs`
    do
    #echo "i = $i"
    alpha_pass=${alphaPass[$i]}
    #echo "alpha_pass = $alpha_pass"
    n_pass=${nPass[$i]}
    #echo "n_pass = $n_pass"
    alpha_fail=${alphaFail[$i]}
    #echo "alpha_fail = $alpha_fail"
    n_fail=${nFail[$i]}
    #echo "n_fail = $n_fail"
    bkg_shape=${bkgShape[$i]}
    #echo "bkg_shape = $bkg_shape"
    if [ $bkg_shape = "RooCMSShape" ]
	then
	bkg_shape_pass="RooCMSShape::backgroundPass(mass, aPass[79.8], bPass[0.081], gPass[0.02], peakPass[91.2])"
	bkg_shape_fail="RooCMSShape::backgroundFail(mass, aFail[79.8], bFail[0.081], gFail[0.02], peakFail[91.2])"
    elif [ $bkg_shape = "polynomial" ]
	then
	bkg_shape_pass="RooPolynomial::backgroundPass(mass, a1Pass[1.924, 1.0, 3.0], a2Pass[-0.01, -0.02, -0.005])"
	bkg_shape_fail="RooPolynomial::backgroundFail(mass, a1Fail[1.924, 1.0, 3.0], a2Fail[-0.01, -0.02, -0.005])"
    elif [ $bkg_shape = "exponential" ]
	then
	bkg_shape_pass="RooExponential::backgroundPass(mass, cPass[-0.02, -5.0, 0.0])"
	bkg_shape_fail="RooExponential::backgroundFail(mass, cFail[-0.02, -5.0, 0.0])"
    elif [ $bkg_shape = "powerLaw" ]
	then
	#echo "power law background shape"
	bkg_shape_pass="RooPowLaw::backgroundPass(mass, aPass[-10.0, 0.0])"
	bkg_shape_fail="RooPowLaw::backgroundFail(mass, aFail[-10.0, 0.0])"
    fi
    #echo "bkg_shape_pass = $bkg_shape_pass"
    #echo "bkg_shape_fail = $bkg_shape_fail"

    #futz with the above variables to put them into the file name
    alpha_pass_in_file_name=`echo $alpha_pass | sed "s%\.%%"`
    #echo "alpha_pass_in_file_name = $alpha_pass_in_file_name"
    n_pass_in_file_name=`echo $n_pass | sed "s%\.%%"`
    #echo "n_pass_in_file_name = $n_pass_in_file_name"
    alpha_fail_in_file_name=`echo $alpha_fail | sed "s%\.%%"`
    #echo "alpha_fail_in_file_name = $alpha_fail_in_file_name"
    n_fail_in_file_name=`echo $n_fail | sed "s%\.%%"`
    #echo "n_fail_in_file_name = $n_fail_in_file_name"
    bkg_shape_in_file_name=$bkg_shape
    #echo "bkg_shape_in_file_name = $bkg_shape_in_file_name"

    #do the substitution into the template cfg file
    sed -e "s%INPUT_DIRECTORY_NAME%$input_dir%g" -e "s%INPUT_FILE_NAMES%$input_file_names%" -e "s%INPUT_BKG_FILE_NAMES%$input_file_names_bkg%" -e "s%LABEL%$label%" -e "s%ALPHAPASSINFILENAME%$alpha_pass_in_file_name%g" -e "s%NPASSINFILENAME%$n_pass_in_file_name%g" -e "s%ALPHAFAILINFILENAME%$alpha_fail_in_file_name%g" -e "s%NFAILINFILENAME%$n_fail_in_file_name%g" -e "s%ALPHAPASS%$alpha_pass%g" -e "s%NPASS%$n_pass%g" -e "s%ALPHAFAIL%$alpha_fail%g" -e "s%NFAIL%$n_fail%g" -e "s%BKGPASS%$bkg_shape_pass%g" -e "s%BKGFAIL%$bkg_shape_fail%g" -e "s%BKG_SHAPE%$bkg_shape%" -e "s%PASS%$pass%g" MC_shapeModelingSystematic.py > /data2/yohay/eff_MC/shape_model_systematic/MC_shapeModelingSystematic_${input_dir}_alphaPass${alpha_pass_in_file_name}_nPass${n_pass_in_file_name}_alphaFail${alpha_fail_in_file_name}_nFail${n_fail_in_file_name}_bkg${bkg_shape_in_file_name}_${label}.py
    sed -e "s%INPUT_DIRECTORY_NAME%$input_dir%g" -e "s%DIR_NAME%$dir_name%" -e "s%LABEL%$label%" -e "s%ALPHAPASSINFILENAME%$alpha_pass_in_file_name%g" -e "s%NPASSINFILENAME%$n_pass_in_file_name%g" -e "s%ALPHAFAILINFILENAME%$alpha_fail_in_file_name%g" -e "s%NFAILINFILENAME%$n_fail_in_file_name%g" -e "s%ALPHAPASS%$alpha_pass%g" -e "s%NPASS%$n_pass%g" -e "s%ALPHAFAIL%$alpha_fail%g" -e "s%NFAIL%$n_fail%g" -e "s%BKGPASS%$bkg_shape_pass%g" -e "s%BKGFAIL%$bkg_shape_fail%g" -e "s%BKG_SHAPE%$bkg_shape%" -e "s%PASS%$pass%g" data_shapeModelingSystematic.py > /data2/yohay/$dir_name/shape_model_systematic/data_shapeModelingSystematic_${input_dir}_alphaPass${alpha_pass_in_file_name}_nPass${n_pass_in_file_name}_alphaFail${alpha_fail_in_file_name}_nFail${n_fail_in_file_name}_bkg${bkg_shape_in_file_name}_${label}.py
  done
done


#for input_dir in $input_dirs_PUCorrected
#  do
#  if [ $input_dir = "PhotonToIDPUCorrectedEB" ]
#      then
#      passRho="probe_passing_rho_sigmaIetaIeta_EB"
#      passNPV="probe_passing_nPV_sigmaIetaIeta_EB"
#  else
#      passRho="probe_passing_rho"
#      passNPV="probe_passing_nPV"
#  fi
  #sed -e "s%INPUT_DIRECTORY_NAME%$input_dir%g" -e "s%INPUT_FILE_NAMES%$input_file_names%" -e "s%INPUT_BKG_FILE_NAMES%$input_file_names_bkg%" -e "s%LABEL%$label%" -e "s%PASS_RHO%$passRho%g" -e "s%PASS_NPV%$passNPV%g" photon_TagProbeFitTreeAnalyzer_MC_PUCorrected_template_cfg.py > photon_TagProbeFitTreeAnalyzer_MC_${input_dir}_${label}_cfg.py
#sed -e "s%INPUT_DIRECTORY_NAME%$input_dir%g" -e "s%INPUT_FILE_NAMES%$input_file_names%" -e "s%INPUT_BKG_FILE_NAMES%$input_file_names_bkg%" -e "s%LABEL%$label%" -e "s%PASS_RHO%$passRho%g" -e "s%PASS_NPV%$passNPV%g" test_PUCorrected.py > test_${input_dir}_${label}_cfg.py
#done

exit 0
