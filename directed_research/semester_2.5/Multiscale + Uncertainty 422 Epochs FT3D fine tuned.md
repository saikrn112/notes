
#### Best multiscale model 422 epochs
```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted/ \
--tf_model_path=../models/multiscale_uncertainity_1/422model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--NumOut=4

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--CheckPointNum=422 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--Display

full for a counter of 640
full GPU time avg:0.010481477156281472
full GPU fps :95.40639979363094
full EPE:9.9285249710083
full final loss:6.426803948299494
edge_quant for a counter of 640
edge_quant GPU time avg:0.0472762256860733
edge_quant GPU fps :21.152280781470704
edge_quant EPE:10.064444541931152
edge_quant final loss:6.513150138925994
```

#### Sintel Multiscale with uncertainity without chunking

default resolution 352x480

**clean**
```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted_sintel/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted_sintel/ \
--tf_model_path=../models/multiscale_uncertainity_1/449model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--NumOut=4

python Test_new_sintel.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_sintel \
--CheckPointNum=449 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--DataList=./Misc/MPI_Sintel_train_clean.txt \
--Display

full for a counter of 1041
full GPU time avg:0.00948160182502153
full GPU fps :105.46741135670179
full EPE:5.914168357849121
full final loss:3.696589076152567
edge_quant for a counter of 1041
edge_quant GPU time avg:0.04660170291274013
edge_quant GPU fps :21.458443307800597
edge_quant EPE:6.149776458740234
edge_quant final loss:3.9246251183659497

```

**Final**

```
python Test_new_sintel.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_sintel \
--CheckPointNum=449 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--DataList=./Misc/MPI_Sintel_Final_train_list.txt \
--Display


full for a counter of 1041
full GPU time avg:0.009290723360924624
full GPU fps :107.6342455966183
full total L1 EPE:4.320951257276776
full total L2 EPE:12.772706958104738
full total L1 Photo:90.78476560225833
edge_quant for a counter of 1041
edge_quant GPU time avg:0.04625691071252887
edge_quant GPU fps :21.6183913840391
edge_quant total L1 EPE:4.444677126195772
edge_quant total L2 EPE:12.043474947455751
edge_quant total L1 Photo:92.46464510013683


full for a counter of 1041
full GPU time avg:0.009770119682627155
full GPU fps :102.35289151863317
full EPE:6.899102687835693
full final loss:4.320899210204652
edge_quant for a counter of 1041
edge_quant GPU time avg:0.046565335032804786
edge_quant GPU fps :21.475202514821607
edge_quant EPE:6.957962989807129
edge_quant final loss:4.444677126195772
```

---
---
# Chunking

#### FC2

```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted_chunking/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted_chunking/ \
--tf_model_path=../models/multiscale_uncertainity_1/449model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--ResizeCropStack \
--NumOut=4

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_chunking \
--CheckPointNum=449 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--ResizeCropStack \
--OnGPU \
--OnEdge \
--Display

full for a counter of 640
full GPU time avg:0.01013028472661972
full GPU fps :98.71390854121438
full EPE:3.1019206047058105
full final loss:1.9459755161136854
edge_quant for a counter of 640
edge_quant GPU time avg:0.011302993819117545
edge_quant GPU fps :88.47213543624433
edge_quant EPE:3.675316333770752
edge_quant final loss:2.335738085041521
```


#### Sintel multiscale Clean

```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted_sintel_chunking/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted_sintel_chunking/ \
--tf_model_path=../models/multiscale_uncertainity_1/449model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--ResizeCropStack \
--Uncertainity \
--NumOut=4




python Test_new_sintel.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_chunking \
--CheckPointNum=449 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--ResizeCropStack \
--OnEdge \
--DataList=./Misc/MPI_Sintel_train_clean.txt \
--Display

python Test_new_sintel.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_sintel_chunking \
--CheckPointNum=422 \
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
--CheckPointNum=449 \
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



----
---
---

# FT3D

```
python Train.py \
--Dataset=FT3D \
--BasePath=../../Datasets/FlyingThings3D \
--LabelBasePath=../../Datasets/flyingthings3d_optical_flow/ \
--ExperimentFileName="multiscale_uncertainity_1" \
--NetworkName=Network.MultiScaleResNet \
--MiniBatchSize=16 \
--LoadCheckPoint=1 \
--LR=1e-4 \
--InitNeurons=32 \
--LossFuncName=MultiscaleSL1-1 \
--UncType=LinearSoftplus \
--NumSubBlocks=2 \
--NumEpochs=450
```

monitoring status
```
[TensorBoard](http://localhost:6007/?pinnedCards=%5B%7B%22plugin%22%3A%22images%22%2C%22tag%22%3A%22I1Patch%2Fimage%22%2C%22runId%22%3A%22defaultExperimentId%2F.%22%2C%22sample%22%3A0%7D%2C%7B%22plugin%22%3A%22images%22%2C%22tag%22%3A%22Label1_1%2Fimage%22%2C%22runId%22%3A%22defaultExperimentId%2F.%22%2C%22sample%22%3A0%7D%2C%7B%22plugin%22%3A%22images%22%2C%22tag%22%3A%22prVal_final%2Fimage%22%2C%22runId%22%3A%22defaultExperimentId%2F.%22%2C%22sample%22%3A0%7D%2C%7B%22plugin%22%3A%22scalars%22%2C%22tag%22%3A%22LossEveryIter%22%7D%5D&darkMode=true#timeseries)
```



```
python Test_new_FT3D.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--CheckPointNum=449 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--Display
```



