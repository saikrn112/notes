aall the experiments can be found [here]()


with normal conv layers
```
python Train.py \
--ExperimentFileName="rnetn32lr4d2" \
--NetworkName=Network.ResNet \
--MiniBatchSize=32 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=32 \
--NumSubBlocks=2 \
--NumEpochs=500
```
Num Params: `2724195`
Num FLOPs: `1311954139312`
Estimated Model Size (MB): `31.185832977294922`


with depthwise conv layers (only conv not transpose)
```
python Train.py \
--ExperimentFileName="separable_rnetn32lr4d2" \
--NetworkName=Network.SeparableResNet \
--MiniBatchSize=32 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=32 \
--NumSubBlocks=2 \
--NumEpochs=500
```

Num Params: `2342697`
Num FLOPs: `874306807420`
Estimated Model Size (MB): `26.819934844970703`



unet with separable conv layers
```
python Train.py \
--ExperimentFileName="separable_unetn32lr4d2" \
--NetworkName=Network.SeparableUNet \  
--MiniBatchSize=32 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=32 \
--NumSubBlocks=2 \
--NumEpochs=500
```

Num Params: `1854249`
Num FLOPs: `3973400376568`
Estimated Model Size (MB): `21.230091094970703`


unet with seperable conv layers
```
python Train.py \
--ExperimentFileName="separable_unetn32lr4d1" \
--NetworkName=Network.SeparableUNet \
--MiniBatchSize=128 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=32 \
--NumSubBlocks=1 \
--NumEpochs=500

```


Num Params: `441129`
Num FLOPs: `4459030557171`
Estimated Model Size (MB): `5.052356719970703`




---

```
python TFLiteConverter.py --NetworkName=Network.SeparableResNet \
--tflite_path=../models/separable_rnetn32lr4d3/converted/lite.tflite \
--tflite_edge_path=../models/separable_rnetn32lr4d3/converted/ \
--tf_model_path=../models/separable_rnetn32lr4d3/499model.ckpt \
--NumSubBlocks=3 \
--InitNeurons=32 
```



```
python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.SeparableResNet \
--CheckPointFolder=../models/separable_rnetn32lr4d3/ \
--CheckPointNum=499 \
--NumSubBlocks=3 \
--InitNeurons=32 \
--Display="" \
--OnEdge=""
```


hardware compatible models

end goal 
- dynamic obstacle - color clustering based on optical flow



----
Seperable ResNet with polar
```
python Train.py \
--ExperimentFileName="separable_rnetn32lr4d3_polar" \
--NetworkName=Network.SeparableResNet \
--MiniBatchSize=128 \
--LoadCheckPoint=1 \
--LR=1e-4 \
--InitNeurons=32 \
--NumSubBlocks=3 \
--NumEpochs=500
```


```
python TFLiteConverter.py --NetworkName=Network.SeparableResNet \
--tflite_path=../models/separable_rnetn32lr4d3_polar/converted/lite.tflite \
--tflite_edge_path=../models/separable_rnetn32lr4d3_polar/converted/ \
--tf_model_path=../models/separable_rnetn32lr4d3_polar/47a0model.ckpt \
--NumSubBlocks=3 \
--InitNeurons=32 
```

```
python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.SeparableResNet \
--CheckPointFolder=../models/separable_rnetn32lr4d3_polar/ \
--CheckPointNum=47a0 \
--NumSubBlocks=3 \
--InitNeurons=32 \
--Display="" \
--OnEdge=""
```
---
Separable ResNet with polar Depth 1

```
python Train.py \
--ExperimentFileName="separable_rnetn32lr4d1_polar" \
--NetworkName=Network.SeparableResNet \
--MiniBatchSize=128 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=32 \
--NumSubBlocks=1 \
--NumEpochs=500
```

---
Normal ResNet with depth 2

```
python Train.py \
--ExperimentFileName="rnetn32lr4d2" \
--NetworkName=Network.ResNet \
--MiniBatchSize=32 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=32 \
--NumSubBlocks=2 \
--NumEpochs=500
```
---

Separable_resnet with polar
```
python Train.py \
--ExperimentFileName="separable_rnetn32lr4d2_polar" \
--NetworkName=Network.SeparableResNet \
--MiniBatchSize=32 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=32 \
--NumSubBlocks=2 \
--NumEpochs=500
```
---
Separable resnet with byte rep
```
python Train.py \
--ExperimentFileName="separable_rnetn32lr4d2_byte" \
--NetworkName=Network.SeparableResNet \
--MiniBatchSize=32 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=32 \
--NumSubBlocks=2 \
--NumEpochs=500
```
----
# 2023.02.22
Seperable ResNet with polar new
```
python Train.py \
--ExperimentFileName="separable_rnetn32lr4d2_polar_new_5" \
--NetworkName=Network.SeparableResNet \
--MiniBatchSize=128 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=32 \
--NumSubBlocks=2 \
--NumEpochs=100
```


```
python TFLiteConverter.py --NetworkName=Network.SeparableResNet \
--tflite_path=../models/separable_rnetn32lr4d2_polar_new_5/converted/lite.tflite \
--tflite_edge_path=../models/separable_rnetn32lr4d2_polar_new_5/converted/ \
--tf_model_path=../models/separable_rnetn32lr4d2_polar_new_5/206a0model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--NumOut=2
```

```
python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.SeparableResNet \
--CheckPointFolder=../models/separable_rnetn32lr4d2_polar_new_5/ \
--CheckPointNum=206a0 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Display="" \
--OnEdge=""
```
----
adhoc AB byte rep
```
python Train.py \
--ExperimentFileName="adhoc_ab" \
--NetworkName=Network.SeparableResNet \
--MiniBatchSize=128 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=32 \
--NumSubBlocks=2 \
--NumEpochs=100
```
---

# 2023.02.24
first I am checking baseline model 
in this model I am first checking shift this is running in 3080
```
python Train.py \
--ExperimentFileName="baseline_xy" \
--NetworkName=Network.ResNet \
--MiniBatchSize=32 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=32 \
--NumSubBlocks=2 \
--NumEpochs=100

python TFLiteConverter.py --NetworkName=Network.ResNet \
--tflite_path=../models/baseline_xy/converted/lite.tflite \
--tflite_edge_path=../models/baseline_xy/converted/ \
--tf_model_path=../models/baseline_xy/99model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--NumOut=2

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNet \
--CheckPointFolder=../models/baseline_xy/ \
--CheckPointNum=99 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Display="" \
--Old="" \
--OnEdge=True
```

---
# 2023.02.26
today I will cehck the multiscaling outputs
see if accuracy is better or not

```
multiscalepreds but single scale loss
python Train.py \
--ExperimentFileName="multiscale_xy_final_loss" \
--NetworkName=Network.MultiScaleResNet \
--MiniBatchSize=32 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=32 \
--NumSubBlocks=2 \
--NumEpochs=100

python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_xy_final_loss/converted/lite.tflite \
--tflite_edge_path=../models/multiscale_xy_final_loss/converted/ \
--tf_model_path=../models/multiscale_xy_final_loss/95a0model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--NumOut=2


python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_xy_final_loss/ \
--CheckPointNum=51a0 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Display="" \
--Old="" \
--OnEdge=True
```


# 2023.02.27

adding more scales M/8, M/4, M/2, M
```
python Train.py \
--ExperimentFileName="multiscale_xy_multiscale_loss_with_scales_3" \
--NetworkName=Network.MultiScaleResNet \
--MiniBatchSize=32 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=32 \
--NumSubBlocks=2 \
--NumEpochs=100

python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_xy_multiscale_loss_with_scales_3/converted/lite.tflite \
--tflite_edge_path=../models/multiscale_xy_multiscale_loss_with_scales_3/converted/ \
--tf_model_path=../models/multiscale_xy_multiscale_loss_with_scales_3/60a0model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--NumOut=2

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_xy_multiscale_loss_with_scales_3/ \
--CheckPointNum=60a0 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Display="" \
--Old="" \
--OnEdge=True
```

ran multiscale single loss again 


trying another network where I am not accumulating the losses 
```
python Train.py \
--ExperimentFileName="multiscale_xy_independent_loss" \
--NetworkName=Network.MultiScaleResNet \
--MiniBatchSize=32 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=32 \
--NumSubBlocks=2 \
--NumEpochs=100

python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_xy_independent_loss/converted/lite.tflite \
--tflite_edge_path=../models/multiscale_xy_independent_loss/converted/ \
--tf_model_path=../models/multiscale_xy_independent_loss/48a0model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--NumOut=2

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_xy_independent_loss/ \
--CheckPointNum=48a0 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Display="" \
--Old="" \
--OnEdge=True
```
---
# 2023.03.16

```
python Train.py \
--ExperimentFileName="rnetn32lr4d2" \
--NetworkName=Network.ResNet \
--MiniBatchSize=32 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=32 \
--NumSubBlocks=2 \
--NumEpochs=500
```

```
python Inference.py \
--NetworkName=Network.ResNet \
--InitNeurons=16 \
--NumOut=2
```

# Speed Tests

- input size: 352x480, 176x240,,88x120
- NumInputChannels: 2, 4, 6
- NetworkStyle: 10MB, 0.5MB
- FPS on EdgeTPU

Train 0.5MB Model of highest speed (if speed is almost same for num. channels, then use 6)

**Monday 20th 12PM**





```
python Train.py \
--ExperimentFileName="160x120is3ic16in" \
--NetworkName=Network.ResNet \
--MiniBatchSize=64 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=16 \
--NumSubBlocks=1 \
--NumEpochs=500


```


../models/160x120is3ic16in/ -- didnt work

```
python Train.py \
--ExperimentFileName="160x120is3ic16in1.2ef" \
--NetworkName=Network.ResNet \
--MiniBatchSize=64 \
--ExpansionFactor=1.2 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=32 \
--NumSubBlocks=1 \
--NumEpochs=500
```


## 2023.03.23
running inferences for H/2xW/2 resize and resize them back to HxW and then compute accuracies

```
python TFLiteConverter.py --NetworkName=Network.ResNet \
--tflite_path=../models/baseline_xy/converted_half/ \
--tflite_edge_path=../models/baseline_xy/converted_half/ \
--tf_model_path=../models/baseline_xy/99model.ckpt \
--ResizeToHalf \
--NumSubBlocks=2 \
--InitNeurons=32 \
--NumOut=2

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNet \
--CheckPointFolder=../models/baseline_xy/ \
--TFLiteFolder=converted_half \
--ResizeToHalf \
--CheckPointNum=99 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Display \
--OnEdge

full for a counter of 640
full GPU time avg:0.006659317389130592
full GPU fps:150.16554123583455
full total L1 EPE:4.41510023274459
full total L2 EPE:9.211464794655331
full total L1 Photo:67.36561982742464
quant for a counter of 640
quant GPU time avg:0.05301336087286472
quant GPU fps:18.8631692753488
quant total L1 EPE:4.4726688537281
quant total L2 EPE:9.214873417746276
quant total L1 Photo:63.283651872114646
edge_quant for a counter of 640
edge_quant GPU time avg:0.009334630519151687
edge_quant GPU fps:107.12796804847484
edge_quant total L1 EPE:4.8024076671339575
edge_quant total L2 EPE:9.576508963480592
edge_quant total L1 Photo:66.80991632326676

```

resize them, crop them and stack them along batch dim
```
python TFLiteConverter.py --NetworkName=Network.ResNet \
--tflite_path=../models/baseline_xy/converted_half_crop_stack/ \
--tflite_edge_path=../models/baseline_xy/converted_half_crop_stack/ \
--tf_model_path=../models/baseline_xy/99model.ckpt \
--ResizeCropStack \
--NumSubBlocks=2 \
--InitNeurons=32 \
--NumOut=2

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNet \
--CheckPointFolder=../models/baseline_xy/ \
--TFLiteFolder=converted_half_crop_stack \
--ResizeCropStack \
--CheckPointNum=99 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnEdge

full for a counter of 640
full GPU time avg:0.03638054430484772
full GPU fps:27.487219312074718
full total L1 EPE:4.794524928694591
full total L2 EPE:11.409134369203821
full total L1 Photo:65.15361456668735
quant for a counter of 640
quant GPU time avg:0.053315301239490506
quant GPU fps:18.756341552081537
quant total L1 EPE:4.822937816148624
quant total L2 EPE:11.10059376237914
quant total L1 Photo:61.40598839962128
edge_quant for a counter of 640
edge_quant GPU time avg:0.009429481625556946
edge_quant GPU fps:106.05036837758678
edge_quant total L1 EPE:5.1748013714328405
edge_quant total L2 EPE:11.450105336681009
edge_quant total L1 Photo:64.18703907976236

```

## 2023.03.25
training for h/2 x w/2 x 4(2)

```
python Train.py \
--ExperimentFileName="176x240is24ic32in2nsb" \
--NetworkName=Network.ResNet \
--MiniBatchSize=64 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=32 \
--NumSubBlocks=2 \
--NumEpochs=500 \
--ResizeCropStack

python TFLiteConverter.py --NetworkName=Network.ResNet \
--tflite_path=../models/baseline_xy/converted_half/ \
--tflite_edge_path=../models/baseline_xy/converted_half/ \
--tf_model_path=../models/baseline_xy/99model.ckpt \
--ResizeToHalf \
--NumSubBlocks=2 \
--InitNeurons=32 \
--NumOut=2

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNet \
--CheckPointFolder=../models/baseline_xy/ \
--TFLiteFolder=converted_half \
--ResizeToHalf \
--CheckPointNum=99 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Display \
--OnEdge
```

![[h_w_24.png]]
