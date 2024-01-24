 ..
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
--TFLiteFolder=converted \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--Display


full for a counter of 640
full GPU time avg:0.0101580198854208
full GPU fps :98.44438298799162
full EPE:2.7591497898101807
full final loss:1.7277436164440587
edge_quant for a counter of 640
edge_quant GPU time avg:0.04386902153491974
edge_quant GPU fps :22.79512888620048
edge_quant EPE:3.60551381111145
edge_quant final loss:2.295692537468858
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


---
---

### Dev Board Mini Coral TPU


```
python3 test.py \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=/home/mendel/optical_flow/models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_half \
--BasePath=/home/mendel/optical_flow/val/ \
--ResizeToHalf \
--Uncertainity
```


```
python3 test_rt.py \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=/home/mendel/optical_flow/models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_half \
--BasePath=/home/mendel/optical_flow/val/ \
--OutputPath=/home/mendel/optical_flow/experiments/ \
--ResizeToHalf \
--Uncertainity
```


on desktop with usb accelerator
```
python3 test.py \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=/home/ramu/Personal/optical_flow/models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_half \
--BasePath=/home/ramu/Personal/optical_flow/val/ \
--ResizeToHalf \
--Uncertainity
```


on desktop with usb accelerator with real time feed
```
python3 test_rt.py \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=/home/ramu/Personal/optical_flow/models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_half \
--BasePath=/home/ramu/Personal/optical_flow/val/ \
--OutputPath=/home/ramu/Personal/optical_flow/experiments/ \
--ResizeToHalf \
--Uncertainity
```



```
python3 test_rt.py \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=/home/mendel/optical_flow/models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_half \
--BasePath=/home/mendel/optical_flow/val/ \
--OutputPath=/home/mendel/optical_flow/experiments/ \
--ResizeCropStack \
--Uncertainity
```




## ResizeCropStack
```
python3 test_rt.py \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=/home/mendel/optical_flow/models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_half \
--BasePath=/home/mendel/optical_flow/val/ \
--OutputPath=/home/mendel/optical_flow/experiments/ \
--ResizeCropStack \
--Uncertainity \
--RunMAVlink
```

## ResizeToHalf
```
python3 test_rt.py \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=/home/mendel/optical_flow/models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_half \
--BasePath=/home/mendel/optical_flow/val/ \
--OutputPath=/home/mendel/optical_flow/experiments/ \
--ResizeToHalf \
--Uncertainity \
--RunMAVlink
```


## ClosestResizeAndCrop
```
python3 test_rt.py \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=/home/mendel/optical_flow/models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_half \
--BasePath=/home/mendel/optical_flow/val/ \
--OutputPath=/home/mendel/optical_flow/experiments/ \
--ClosestResizeAndCrop \
--Uncertainity \
--RunMAVlink
```

```STATIC
python3 test_rt_static.py \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=/home/mendel/optical_flow/models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_half \
--BasePath=/home/mendel/optical_flow/val/ \
--OutputPath=/home/mendel/optical_flow/experiments/ \
--ClosestResizeAndCrop \
--Uncertainity \
--RunMAVlink
```

# SIM Desktop
```
python3 test_sim.py \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=/home/ramu/Personal/optical_flow/models/multiscale_uncertainity_1/  \
--TFLiteFolder=converted_half \
--ClosestResizeAndCrop \
--Uncertainity \
--exp_dir=/home/ramu/Personal/OpticalFlowOnTPU/Datasets/experiments/2023.10.04_static3/ \
--OutputPath=/home/ramu/Personal/OpticalFlowOnTPU/experiment_results/2023.10.04_static3/ \
--RunMAVlink
```

```
python3 test_sim.py \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=/home/ramu/Personal/optical_flow/models/multiscale_uncertainity_1/  \
--TFLiteFolder=converted_half \
--ClosestResizeAndCrop \
--Uncertainity \
--exp_dir=/home/ramu/Personal/OpticalFlowOnTPU/Datasets/experiments/2023.10.04_static2/ \
--OutputPath=/home/ramu/Personal/OpticalFlowOnTPU/experiment_results/2023.10.04_static2/ \
--RunMAVlink
```

```
python3 test_sim.py \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=/home/ramu/Personal/optical_flow/models/multiscale_uncertainity_1/  \
--TFLiteFolder=converted_half \
--ClosestResizeAndCrop \
--Uncertainity \
--exp_dir=/home/ramu/Personal/OpticalFlowOnTPU/Datasets/experiments/2023.10.08_dynamic1/ \
--OutputPath=/home/ramu/Personal/OpticalFlowOnTPU/experiment_results/2023.10.08_dynamic1/ \
--RunMAVlink
```

```
python3 test_sim.py \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=/home/ramu/Personal/optical_flow/models/multiscale_uncertainity_1/  \
--TFLiteFolder=converted_half \
--ClosestResizeAndCrop \
--Uncertainity \
--exp_dir=/home/ramu/Personal/OpticalFlowOnTPU/Datasets/experiments/2023.10.08_dynamic2/ \
--OutputPath=/home/ramu/Personal/OpticalFlowOnTPU/experiment_results/2023.10.08_dynamic2/ \
--RunMAVlink
```

```
python3 test_sim.py \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=/home/ramu/Personal/optical_flow/models/multiscale_uncertainity_1/  \
--TFLiteFolder=converted_half \
--ClosestResizeAndCrop \
--Uncertainity \
--exp_dir=/home/ramu/Personal/OpticalFlowOnTPU/Datasets/experiments/2023.10.11_bw_static2/ \
--OutputPath=/home/ramu/Personal/OpticalFlowOnTPU/experiment_results/2023.10.11_bw_static2/ \
--RunMAVlink
```

```
python3 test_sim.py \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=/home/ramu/Personal/optical_flow/models/multiscale_uncertainity_1/  \
--TFLiteFolder=converted_half \
--ClosestResizeAndCrop \
--Uncertainity \
--exp_dir=/home/ramu/Personal/OpticalFlowOnTPU/Datasets/experiments/2023.10.11_bw_static3/ \
--OutputPath=/home/ramu/Personal/OpticalFlowOnTPU/experiment_results/2023.10.11_bw_static3/ \
--RunMAVlink
```

```
python3 test_sim.py \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=/home/ramu/Personal/optical_flow/models/multiscale_uncertainity_1/  \
--TFLiteFolder=converted_half \
--ClosestResizeAndCrop \
--Uncertainity \
--exp_dir=/home/ramu/Personal/OpticalFlowOnTPU/Datasets/experiments/2023.10.11_color_static1/ \
--OutputPath=/home/ramu/Personal/OpticalFlowOnTPU/experiment_results/2023.10.11_color_static1/ \
--RunMAVlink
```


```
python3 test_raft_custom.py \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=/home/ramu/Personal/optical_flow/models/multiscale_uncertainity_1/  \
--TFLiteFolder=converted_half \
--ClosestResizeAndCrop \
--Uncertainity \
--exp_dir=/home/ramu/Personal/OpticalFlowOnTPU/Datasets/experiments/2023.10.24_static_gray_washburn_exp_ideal1/ \
--OutputPath=/home/ramu/Personal/OpticalFlowOnTPU/experiment_results/2023.10.24_static_gray_washburn_exp_ideal1/
```

```
python3 test_raft_custom.py \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=/home/ramu/Personal/optical_flow/models/multiscale_uncertainity_1/  \
--TFLiteFolder=converted_half \
--ResizeToHalf \
--Uncertainity \
--exp_dir=/home/ramu/Personal/OpticalFlowOnTPU/Datasets/experiments/2023.10.24_static_gray_washburn_exp_ideal1/ \
--OutputPath=/home/ramu/Personal/OpticalFlowOnTPU/experiment_results/2023.10.24_static_gray_washburn_exp_ideal1/
```


- [x] choppy flow 
	- [ ] run it on previous frames where there was good enogh flow
	- [ ] run it on phone video or color images 
	- [ ] root cause if possible 
	- [ ] run the network on desktop
	- [ ] 
- [x] change to the FT3d fine tuned version
- [ ] x only flow 
	- [ ] angle threshold
- [ ] left right split 
	- [ ] take a patch on left 
	- [ ] take a patch on right
- [ ] resize 
	- [ ] to half 
	- [ ] to quarter
	- [ ] to eights
- [ ] understand different videos and paths
- [ ] lower resolution,
	- [ ] 120p
- [ ] divide image into 8x8 patches and take median 
- [ ] lookup table 
- [ ] weighted sum of flows 
- [ ] arrow scaling is not good

```
python3 test_raft_custom.py \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=/home/ramu/Personal/optical_flow/models/multiscale_uncertainity_1/  \
--TFLiteFolder=converted_half \
--ClosestResizeAndCrop \
--Uncertainity \
--exp_dir=/home/ramu/Personal/OpticalFlowOnTPU/Datasets/experiments/2023.10.04_dynamic/ \
--OutputPath=/home/ramu/Personal/OpticalFlowOnTPU/experiment_results/2023.10.04_dynamic/

```

```
python3 test_raft_custom.py \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=/home/ramu/Personal/optical_flow/models/multiscale_uncertainity_1/  \
--TFLiteFolder=converted_half \
--ResizeToHalf \
--Uncertainity \
--exp_dir=/home/ramu/Personal/OpticalFlowOnTPU/Datasets/experiments/2023.10.24_static_gray_washburn_exp0/ \
--OutputPath=/home/ramu/Personal/OpticalFlowOnTPU/experiment_results/2023.10.24_static_gray_washburn_exp0/
```


----

- [ ] GPU clean full
- [ ] GPU final full
- [ ] TPU clean full
- [ ] TPU final full
- [ ] GPU clean chunk
- [ ] GPU final chunk
- [ ] TPU clean chunk
- [ ] TPU final chunk

```
GPU clean full
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
--DataList=./Misc/MPI_Sintel_train_clean.txt 

full for a counter of 1041
full GPU time avg:0.017679216080737963
full GPU fps :56.56359396441396
full EPE:5.464992046356201
full final loss:3.4176779372490564
```



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
--DataList=./Misc/MPI_Sintel_train_clean.txt \
--ResizeCropStack


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
--ResizeToHalf
```

----


```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted_fp16/ \
--tf_model_path=../models/multiscale_uncertainity_1/399model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--ResizeCropStack \
--NumOut=4
```