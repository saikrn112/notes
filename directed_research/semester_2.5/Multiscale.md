
#### Best multiscale model 400 epochs
```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_xy_multiscale_loss_with_scales_3/converted/lite.tflite \
--tflite_edge_path=../models/multiscale_xy_multiscale_loss_with_scales_3/converted/ \
--tf_model_path=../models/multiscale_xy_multiscale_loss_with_scales_3/99a0model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--NumOut=2

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_xy_multiscale_loss_with_scales_3/ \
--CheckPointNum=99 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnGPU \
--OnEdge \
--Display

full for a counter of 1
full GPU time avg:1.6891412734985352
full GPU fps :0.5920167932009668
full EPE:2.8475914001464844
full final loss:1.7985994815826416
edge_quant for a counter of 1
edge_quant GPU time avg:0.04955124855041504
edge_quant GPU fps :20.1811261926643
edge_quant EPE:3.1930830478668213
edge_quant final loss:2.015470266342163

full for a counter of 640
full GPU time avg:0.01001957207918167
full GPU fps :99.80466152619096
full EPE:3.214668035507202
full final loss:2.029592012340436
edge_quant for a counter of 640
edge_quant GPU time avg:0.046877546980977056
edge_quant GPU fps :21.332174236971078
edge_quant EPE:3.5231850147247314
edge_quant final loss:2.2334298313129692
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
--CheckPointFolder=../models/multiscale_xy_multiscale_loss_with_scales_3/ \
--TFLiteFolder=converted_sintel \
--CheckPointNum=99 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnGPU \
--OnEdge \
--DataList=./Misc/MPI_Sintel_train_clean.txt \
--Display

full for a counter of 1041
full GPU time avg:0.009214357729718504
full GPU fps :108.52628358184545
full EPE:6.001053810119629
full final loss:3.784932344006759
edge_quant for a counter of 1041
edge_quant GPU time avg:0.0439348912491006
edge_quant GPU fps :22.760953118791917
edge_quant EPE:6.070018768310547
edge_quant final loss:3.8667309808255843

```

**Final**

```
python Test_new_sintel.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_xy_multiscale_loss_with_scales_3/ \
--TFLiteFolder=converted_sintel \
--CheckPointNum=99 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnGPU \
--OnEdge \
--DataList=./Misc/MPI_Sintel_Final_train_list.txt \
--Display

full for a counter of 1041
full GPU time avg:0.009244752548613535
full GPU fps :108.16947178861734
full EPE:6.7305498123168945
full final loss:4.242774353848411
edge_quant for a counter of 1041
edge_quant GPU time avg:0.043933020545014044
edge_quant GPU fps :22.761922298863876
edge_quant EPE:6.836266040802002
edge_quant final loss:4.350857518513139
```

----
---



# Chunking

#### FC2

```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_xy_multiscale_loss_with_scales_3/converted_chunking/ \
--tflite_edge_path=../models/multiscale_xy_multiscale_loss_with_scales_3/converted_chunking/ \
--tf_model_path=../models/multiscale_xy_multiscale_loss_with_scales_3/99model.ckpt \
--ResizeCropStack \
--NumSubBlocks=2 \
--InitNeurons=32 \
--NumOut=2


python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_xy_multiscale_loss_with_scales_3/ \
--TFLiteFolder=converted_chunking \
--ResizeCropStack \
--CheckPointNum=99 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnGPU \
--OnEdge \
--Display

full for a counter of 640
full GPU time avg:0.010172642767429352
full GPU fps :98.30287201294321
full EPE:3.5650992393493652
full final loss:2.251359105715528
edge_quant for a counter of 640
edge_quant GPU time avg:0.01138593815267086
edge_quant GPU fps :87.82763322541187
edge_quant EPE:3.752166986465454
edge_quant final loss:2.3799417934496887
```


#### Sintel multiscale Clean

```

python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_xy_multiscale_loss_with_scales_3/converted_sintel_chunking/ \
--tflite_edge_path=../models/multiscale_xy_multiscale_loss_with_scales_3/converted_sintel_chunking/ \
--tf_model_path=../models/multiscale_xy_multiscale_loss_with_scales_3/99model.ckpt \
--ResizeCropStack \
--NumSubBlocks=2 \
--InitNeurons=32 \
--NumOut=2

python Test_new_sintel.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_xy_multiscale_loss_with_scales_3/ \
--TFLiteFolder=converted_sintel_chunking \
--ResizeCropStack \
--CheckPointNum=99 \
--NumSubBlocks=2 \
--InitNeurons=32 \
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
