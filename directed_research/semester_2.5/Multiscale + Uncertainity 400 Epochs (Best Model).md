
#### Best multiscale model 400 epochs
```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted/ \
--tf_model_path=../models/multiscale_uncertainity_1/399model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--NumOut=4

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--Display

full for a counter of 640
full GPU time avg:0.010254282131791114
full GPU fps :97.52023468319865
full EPE:2.7591497898101807
full final loss:1.7277436164440587
edge_quant for a counter of 640
edge_quant GPU time avg:0.0466144397854805
edge_quant GPU fps :21.452580028892264
edge_quant EPE:3.58379864692688
edge_quant final loss:2.2848535845056177
```

#### Sintel Multiscale with uncertainity without chunking

default resolution 352x480

**clean**
```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted_sintel/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted_sintel/ \
--tf_model_path=../models/multiscale_uncertainity_1/399model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--NumOut=4

python Test_new_sintel.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_sintel \
--CheckPointNum=399 \
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
--CheckPointNum=399 \
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
--tf_model_path=../models/multiscale_uncertainity_1/399model.ckpt \
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
--CheckPointNum=399 \
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
--TFLiteFolder=converted_chunking \
--CheckPointNum=399 \
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
--MiniBatchSize=32 \
--LoadCheckPoint=1 \
--LR=1e-4 \
--InitNeurons=32 \
--LossFuncName=MultiscaleSL1-1 \
--UncType=LinearSoftplus \
--NumSubBlocks=2 \
--NumEpochs=450
```
