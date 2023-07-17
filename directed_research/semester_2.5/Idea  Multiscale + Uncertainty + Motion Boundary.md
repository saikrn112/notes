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

---
---

# Chunking

#### FC2

```
python TFLiteConverter.py --NetworkName=Network.MultiScaleMBResNet \
--tflite_path=../models/multiscale_uncertainity_mb_2/converted/ \
--tflite_edge_path=../models/multiscale_uncertainity_mb_2/converted/ \
--tf_model_path=../models/multiscale_uncertainity_mb_2/399model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--ResizeCropStack \
--NumOut=5

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_chunking \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--ResizeCropStack \
--OnGPU \
--OnEdge \
--Display

full for a counter of 640
full GPU time avg:0.010406124964356422
full GPU fps :96.09725074657952
full total L1 EPE:1.9459755161136854
full total L2 EPE:10.334374720428604
full total L1 Photo:59.38486818564055
edge_quant for a counter of 640
edge_quant GPU time avg:0.011344940215349198
edge_quant GPU fps :88.14502157067734
edge_quant total L1 EPE:2.335738085041521
edge_quant total L2 EPE:9.793180834682426
edge_quant total L1 Photo:48.17355235706676
```


#### Sintel multiscale Clean

```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted_sintel_chunking/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted_sintel_chunking/ \
--tf_model_path=../models/multiscale_uncertainity_1/399model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--ResizeCropStack \
--Uncertainity \
--NumOut=4

python Test_new_sintel.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_sintel_chunking \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--DataList=./Misc/MPI_Sintel_train_clean.txt \
--ResizeCropStack \
--Display


full for a counter of 1041
full GPU time avg:0.009591420949593286
full GPU fps :104.25983858443873
full total L1 EPE:3.8841858846810893
full total L2 EPE:12.459870779305325
full total L1 Photo:93.83764791284607
edge_quant for a counter of 1041
edge_quant GPU time avg:0.011260012270279738
edge_quant GPU fps :88.80984993590567
edge_quant total L1 EPE:4.064157241001711
edge_quant total L2 EPE:11.870938483736586
edge_quant total L1 Photo:93.5930516458564
```


#### Sintel multiscale Final

```
python Test_new_sintel.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_sintel_chunking \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--DataList=./Misc/MPI_Sintel_Final_train_list.txt \
--ResizeCropStack \
--Display

full for a counter of 1041
full GPU time avg:0.009500829905529187
full GPU fps :105.25396306885057
full total L1 EPE:4.530900527468161
full total L2 EPE:12.883063874344318
full total L1 Photo:90.17325320212495
edge_quant for a counter of 1041
edge_quant GPU time avg:0.011299086349956355
edge_quant GPU fps :88.50273101982822
edge_quant total L1 EPE:4.600230609692139
edge_quant total L2 EPE:12.199189553285997
edge_quant total L1 Photo:90.44254458080448

```
