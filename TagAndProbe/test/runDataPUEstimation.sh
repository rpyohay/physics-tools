#!/bin/bash

cd ~/scratch0/CMSSW_4_2_3/src/PhysicsTools/TagAndProbe/test
export SCRAM_ARCH=slc5_amd64_gcc434
eval `scramv1 runtime -sh`

#echo "Estimating PU in 1st quarter of dataset..."
#./estimatePileupD.py -i May10ReRecoJSON1.txt --histName=nPVDist --maxPileupBin=30 dataPU1.root > dataPU1.txt &
echo "Estimating PU in 2nd quarter of dataset..."
./estimatePileupD.py -i May10ReRecoJSON2.txt --histName=nPVDist --maxPileupBin=30 dataPU2.root > dataPU2.txt &
#echo "Estimating PU in 3rd quarter of dataset..."
#./estimatePileupD.py -i May10ReRecoJSON3.txt --histName=nPVDist --maxPileupBin=30 dataPU3.root > dataPU3.txt &
#echo "Estimating PU in 4th quarter of dataset..."
#./estimatePileupD.py -i May10ReRecoJSON4.txt --histName=nPVDist --maxPileupBin=30 dataPU4.root > dataPU4.txt &

exit 0
