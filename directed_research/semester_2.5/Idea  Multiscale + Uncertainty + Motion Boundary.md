```
python Train.py \
--ExperimentFileName="multiscale_uncertainity_mb_2" \
--NetworkName=Network.MultiScaleMBResNet \
--MiniBatchSize=32 \
--LoadCheckPoint=1 \
--LR=1e-4 \
--InitNeurons=32 \
--LossFuncName=MultiscaleSL1-1 \
--UncType=LinearSoftplus \
--NumSubBlocks=2 \
--NumEpochs=400

python TFLiteConverter.py --NetworkName=Network.MultiScaleMBResNet \
--tflite_path=../models/multiscale_uncertainity_mb_2/converted/ \
--tflite_edge_path=../models/multiscale_uncertainity_mb_2/converted/ \
--tf_model_path=../models/multiscale_uncertainity_mb_2/399model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--NumOut=5
```

### FC2
```
python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleMBResNet \
--CheckPointFolder=../models/multiscale_uncertainity_mb_2/ \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnGPU \
--OnEdge \
--Display

full for a counter of 640
full GPU time avg:0.010368925333023072
full GPU fps :96.44200993666996
full EPE:4.1001434326171875
full final loss:2.590655952238012
edge_quant for a counter of 640
edge_quant GPU time avg:0.0673658411949873
edge_quant GPU fps :14.844318459641087
edge_quant EPE:4.787198543548584
edge_quant final loss:3.042882319947239
```

## Sintel Clean
```
python Test_new_sintel.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleMBResNet \
--CheckPointFolder=../models/multiscale_uncertainity_mb_2/ \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnGPU \
--OnEdge \
--DataList=./Misc/MPI_Sintel_train_clean.txt \
--Display

full for a counter of 1041
full GPU time avg:0.00940379125355071
full GPU fps :106.34008912335408
full EPE:7.136682510375977
full final loss:4.482216550854968
edge_quant for a counter of 1041
edge_quant GPU time avg:0.0684331812386783
edge_quant GPU fps :14.612794289253383
edge_quant EPE:7.366853713989258
edge_quant final loss:4.640155553388321


```


## Sintel Final
```
python Test_new_sintel.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleMBResNet \
--CheckPointFolder=../models/multiscale_uncertainity_mb_2/ \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnGPU \
--OnEdge \
--DataList=./Misc/MPI_Sintel_Final_train_list.tx \
--Display

full for a counter of 1041
full GPU time avg:0.009855272446997914
full GPU fps :101.46852919369238
full EPE:7.726470947265625
full final loss:4.863680335260949
edge_quant for a counter of 1041
edge_quant GPU time avg:0.06742635492403615
edge_quant GPU fps :14.830995997434824
edge_quant EPE:7.977627754211426
edge_quant final loss:5.028615005436022
```
