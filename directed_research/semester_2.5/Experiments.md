
## Sintel multiscale 


default resolution 352x480

**Final**
```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_xy_multiscale_loss_with_scales_3/converted_sintel/ \
--tflite_edge_path=../models/multiscale_xy_multiscale_loss_with_scales_3/converted_sintel/ \
--tf_model_path=../models/multiscale_xy_multiscale_loss_with_scales_3/99a0model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--ResizeCropStack \
--NumOut=2


python Test_new_sintel.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_xy_multiscale_loss_with_scales_3/ \
--TFLiteFolder=converted_sintel \
--CheckPointNum=99a0 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnGPU \
--OnEdge \
--DataList=./Misc/MPI_Sintel_train_clean.txt \
--Display


full for a counter of 1041
full GPU time avg:0.029321534489348575
full GPU fps :34.10462710821846
full total L1 EPE:4.001940751496584
full total L2 EPE:11.921487198582529
full total L1 Photo:99.42744551588764
edge_quant for a counter of 1041
edge_quant GPU time avg:0.04619856778528688
edge_quant GPU fps :21.645692668387778
edge_quant total L1 EPE:4.096076461727177
edge_quant total L2 EPE:11.85449020329802
edge_quant total L1 Photo:91.30718597970883

```

**Final**

```
python Test_new_sintel.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_xy_multiscale_loss_with_scales_3/ \
--TFLiteFolder=converted_sintel \
--CheckPointNum=99a0 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnGPU \
--OnEdge \
--DataList=./Misc/MPI_Sintel_Final_train_list.txt \
--Display


full for a counter of 1041
full GPU time avg:0.008919163922869622
full GPU fps :112.11813222043163
full total L1 EPE:4.302633700736662
full total L2 EPE:12.11473921926175
full total L1 Photo:97.70352662635918
edge_quant for a counter of 1041
edge_quant GPU time avg:0.046244513404472415
edge_quant GPU fps :21.62418687928691
edge_quant total L1 EPE:4.393862498711211
edge_quant total L2 EPE:12.052160252826816
edge_quant total L1 Photo:90.2440098177985
```

## Sintel multiscale  chunking

#### clean

```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_xy_multiscale_loss_with_scales_3/converted_sintel_chunking/ \
--tflite_edge_path=../models/multiscale_xy_multiscale_loss_with_scales_3/converted_sintel_chunking/ \
--tf_model_path=../models/multiscale_xy_multiscale_loss_with_scales_3/99a0model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--ResizeCropStack \
--NumOut=2

python Test_new_sintel.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_xy_multiscale_loss_with_scales_3/ \
--TFLiteFolder=converted_sintel_chunking \
--CheckPointNum=99a0 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnGPU \
--OnEdge \
--DataList=./Misc/MPI_Sintel_train_clean.txt \
--ResizeCropStack \
--Display


full for a counter of 1041
full GPU time avg:0.009563799206736452
full GPU fps :104.56095724967021
full total L1 EPE:3.9439029489124087
full total L2 EPE:12.175757836596995
full total L1 Photo:104.0784421253088
edge_quant for a counter of 1041
edge_quant GPU time avg:0.011341755030592626
edge_quant GPU fps :88.16977595642429
edge_quant total L1 EPE:4.057102328075112
edge_quant total L2 EPE:12.05957962178932
edge_quant total L1 Photo:101.77319359579539
```


#### Final

```
python Test_new_sintel.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_xy_multiscale_loss_with_scales_3/ \
--TFLiteFolder=converted_sintel_chunking \
--CheckPointNum=99a0 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnGPU \
--OnEdge \
--DataList=./Misc/MPI_Sintel_Final_train_list.txt \
--ResizeCropStack \
--Display


full for a counter of 1041
full GPU time avg:0.00911331978357262
full GPU fps :109.72949745520486
full total L1 EPE:4.454485693851649
full total L2 EPE:12.524431202356684
full total L1 Photo:98.47459952968387
edge_quant for a counter of 1041
edge_quant GPU time avg:0.011330528286760753
edge_quant GPU fps :88.25713812201131
edge_quant total L1 EPE:4.53375384329633
edge_quant total L2 EPE:12.382184382073588
edge_quant total L1 Photo:96.13008828301632
```


## 2023.07.03

```
python Train.py \
--ExperimentFileName="multiscale_uncertainity_mb_1" \
--NetworkName=Network.MultiScaleMBResNet \
--MiniBatchSize=32 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=32 \
--LossFuncName=MultiscaleSL1-1 \
--UncType=LinearSoftplus \
--NumSubBlocks=2 \
--NumEpochs=100
```

## 2023.07.04


[[Multiscale + Uncertainity 400 Epochs (Best Model)]]

