 all the experiments can be found [here]()


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
--tflite_path=../models/baseline_xy/converted/ \
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
--OnEdge \
--Display


edge_quant for a counter of 640
edge_quant GPU time avg:0.07226385213434697
edge_quant GPU fps :13.838177324686246
edge_quant total L1 EPE:3.404239693842828
edge_quant total L2 EPE:10.508742298185826
edge_quant total L1 Photo:55.72987744263929

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
--LossFuncName=MultiscaleSL1-1 \
--NumSubBlocks=2 \
--NumEpochs=100

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
--CheckPointNum=99a0 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Display=True \
--Old="" \
--OnEdge=True

full for a counter of 640
full GPU time avg:0.014752897247672082
full GPU fps :67.7832959324511
full total L1 EPE:2.0943503261660226
full total L2 EPE:10.337391330051469
full total L1 Photo:50.30368340386286
quant for a counter of 640
quant GPU time avg:0.22361994683742523
quant GPU fps :4.4718729887142565
quant total L1 EPE:2.2365094435808714
quant total L2 EPE:10.276673146185932
quant total L1 Photo:43.72874550559308
edge_quant for a counter of 640
edge_quant GPU time avg:0.0462317768484354
edge_quant GPU fps :21.63014420316061
edge_quant total L1 EPE:2.2334298313129692
edge_quant total L2 EPE:10.253777088504284
edge_quant total L1 Photo:44.21823246811375
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

even smaller model

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

python TFLiteConverter.py --NetworkName=Network.ResNet \
--tflite_path=../models/160x120is3ic16in1.2ef/converted/ \
--tflite_edge_path=../models/160x120is3ic16in1.2ef/converted/ \
--tf_model_path=../models/160x120is3ic16in1.2ef/499model.ckpt \
--NumSubBlocks=1 \
--InitNeurons=32 \
--ExpansionFactor=1.2 \
--NumOut=2

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNet \
--CheckPointFolder=../models/160x120is3ic16in1.2ef/ \
--CheckPointNum=499 \
--NumSubBlocks=1 \
--InitNeurons=32 \
--ExpansionFactor=1.2 \
--Display \
--OnEdge

full for a counter of 640
full GPU time avg:0.009403812885284423
full GPU fps:106.33984450763074
full total L1 EPE:4.152434249967337
full total L2 EPE:10.465345383924433
full total L1 Photo:60.662987686311304
quant for a counter of 640
quant GPU time avg:0.15268371030688285
quant GPU fps:6.549487158715718
quant total L1 EPE:4.307384582119994
quant total L2 EPE:10.470071649271995
quant total L1 Photo:58.21334168096987
edge_quant for a counter of 640
edge_quant GPU time avg:0.041000325605273245
edge_quant GPU fps:24.390050206610685
edge_quant total L1 EPE:6.297618824616075
edge_quant total L2 EPE:12.61554172448814
edge_quant total L1 Photo:66.8179124712704
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
--OnEdge \
--Display

full GPU time avg:0.009135565534234048
full GPU fps:109.4622983385826
full total L1 EPE:3.0091141235549004
full total L2 EPE:10.437915360787883
full total L1 Photo:57.948302855828686
quant for a counter of 640
quant GPU time avg:0.05034426599740982
quant GPU fps:19.863235269960025
quant total L1 EPE:3.2446567573584617
quant total L2 EPE:10.226088681910188
quant total L1 Photo:51.84578637941915
edge_quant for a counter of 640
edge_quant GPU time avg:0.009443392977118492
edge_quant GPU fps:105.89414233030624
edge_quant total L1 EPE:3.675860301218927
edge_quant total L2 EPE:10.609538197517395
edge_quant total L1 Photo:56.69999125779276


```
![[test_pred_edge_quant.png]]

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

## 2023.04.05

resize, crop, stack and blur  chunking
```
python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNet \
--CheckPointFolder=../models/baseline_xy/ \
--TFLiteFolder=converted_half_crop_stack \
--ResizeCropStackBlur \
--CheckPointNum=99 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnEdge \
--Display
```

## 2023.04.06

resize, crop with overlap, stack and de overlap
```
python TFLiteConverter.py --NetworkName=Network.ResNet \
--tflite_path=../models/baseline_xy/overlap_crop_stack/ \
--tflite_edge_path=../models/baseline_xy/overlap_crop_stack/ \
--tf_model_path=../models/baseline_xy/99model.ckpt \
--OverlapCropStack \
--NumSubBlocks=2 \
--InitNeurons=32 \
--NumOut=2

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNet \
--CheckPointFolder=../models/baseline_xy/ \
--TFLiteFolder=overlap_crop_stack \
--OverlapCropStack \
--CheckPointNum=99 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnEdge \
--Display

full for a counter of 640
full GPU time avg:0.010770534351468086
full GPU fps:92.84590414622225
full total L1 EPE:3.632450472097844
full total L2 EPE:10.671652891486882
full total L1 Photo:60.57451371934684
quant for a counter of 640
quant GPU time avg:0.06560215540230274
quant GPU fps:15.243401590504728
quant total L1 EPE:3.822661381494254
quant total L2 EPE:10.495760880038143
quant total L1 Photo:56.24321880918565
edge_quant for a counter of 640
edge_quant GPU time avg:0.01274808682501316
edge_quant GPU fps:78.44314317328691
edge_quant total L1 EPE:4.792586874216795
edge_quant total L2 EPE:11.387322021275759
edge_quant total L1 Photo:63.15908787582862
```
![[overlap_pred_quant.png]]

same code with overlap 0
```
python TFLiteConverter.py --NetworkName=Network.ResNet \
--tflite_path=../models/baseline_xy/overlap_crop_stack/ \
--tflite_edge_path=../models/baseline_xy/overlap_crop_stack/ \
--tf_model_path=../models/baseline_xy/99model.ckpt \
--OverlapCropStack \
--NumSubBlocks=2 \
--InitNeurons=32 \
--PatchDelta=0 \
--NumOut=2

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNet \
--CheckPointFolder=../models/baseline_xy/ \
--TFLiteFolder=overlap_crop_stack \
--OverlapCropStack \
--CheckPointNum=99 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnEdge \
--PatchDelta=0

full GPU time avg:0.009201080724596977
full GPU fps:108.68288518833768
full total L1 EPE:3.0091141235549004
full total L2 EPE:10.437915360787883
full total L1 Photo:57.948302855828686
quant for a counter of 640
quant GPU time avg:0.0503825381398201
quant GPU fps:19.84814653888278
quant total L1 EPE:3.254907905915752
quant total L2 EPE:10.23179777613841
quant total L1 Photo:52.512276827108984
edge_quant for a counter of 640
edge_quant GPU time avg:0.009435063600540161
edge_quant GPU fps:105.98762682879526
edge_quant total L1 EPE:3.670211013406515
edge_quant total L2 EPE:10.582362260110676
edge_quant total L1 Photo:56.97900226323294
```
![[overlap_pred_full_0.png]]
we cant use the 20 pix because output shape is not same as input shape


using pix as 16
```
python TFLiteConverter.py --NetworkName=Network.ResNet \
--tflite_path=../models/baseline_xy/overlap_crop_stack/ \
--tflite_edge_path=../models/baseline_xy/overlap_crop_stack/ \
--tf_model_path=../models/baseline_xy/99model.ckpt \
--OverlapCropStack \
--NumSubBlocks=2 \
--InitNeurons=32 \
--PatchDelta=16 \
--NumOut=2

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNet \
--CheckPointFolder=../models/baseline_xy/ \
--TFLiteFolder=overlap_crop_stack \
--OverlapCropStack \
--CheckPointNum=99 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--PatchDelta=16 \
--OnEdge \
--Display

full for a counter of 640
full GPU time avg:0.009779304265975952
full GPU fps:102.25676314001079
full total L1 EPE:2.869394014636055
full total L2 EPE:10.40343977995217
full total L1 Photo:57.69966947305083
quant for a counter of 640
quant GPU time avg:0.05839962214231491
quant GPU fps:17.123398462460685
quant total L1 EPE:3.1142013667151334
quant total L2 EPE:10.1428628845606
quant total L1 Photo:50.9603722990402
edge_quant for a counter of 640
edge_quant GPU time avg:0.010574305802583695
edge_quant GPU fps:94.5688557404556
edge_quant total L1 EPE:3.4600023234263064
edge_quant total L2 EPE:10.44239654932171
edge_quant total L1 Photo:55.779751485188775
```
![[overlap_pred_full_16.png]]

## 2023.04.09

checking if edge tpu can support the crop
```
python Train.py \
--ExperimentFileName="edge_new_arch" \
--NetworkName=Network.ResNetEdge \
--MiniBatchSize=32 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=32 \
--NumSubBlocks=2 \
--SaveTestModel \
--EdgeNewArch \
--NumEpochs=100

python TFLiteConverter.py --NetworkName=Network.ResNetEdge \
--tflite_path=../models/edge_new_arch/converted/ \
--tflite_edge_path=../models/edge_new_arch/converted/ \
--tf_model_path=../models/edge_new_arch/0a0model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--NumOut=2
```

trying out chunking+smaller model
```
python TFLiteConverter.py --NetworkName=Network.ResNet \
--tflite_path=../models/160x120is3ic16in1.2ef/converted_half_crop_stack/ \
--tflite_edge_path=../models/160x120is3ic16in1.2ef/converted_half_crop_stack/ \
--tf_model_path=../models/160x120is3ic16in1.2ef/499model.ckpt \
--ResizeCropStack \
--NumSubBlocks=1 \
--InitNeurons=32 \
--ExpansionFactor=1.2 \
--NumOut=2

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNet \
--CheckPointFolder=../models/160x120is3ic16in1.2ef/ \
--TFLiteFolder=converted_half_crop_stack \
--ResizeCropStack \
--CheckPointNum=499 \
--NumSubBlocks=1 \
--InitNeurons=32 \
--ExpansionFactor=1.2 \
--OnEdge \
--Display

-----SUMMARY-------
full for a counter of 640
full GPU time avg:0.009580765292048455
full GPU fps:104.37579561936967
full total L1 EPE:4.292015033611096
full total L2 EPE:10.446411436633207
full total L1 Photo:61.439810411857785
quant for a counter of 640
quant GPU time avg:0.037748049944639206
quant GPU fps:26.49143469574155
quant total L1 EPE:4.495259568886832
quant total L2 EPE:10.393467425601557
quant total L1 Photo:59.35025435630716
edge_quant for a counter of 640
edge_quant GPU time avg:0.00962969809770584
edge_quant GPU fps:103.84541549004926
edge_quant total L1 EPE:5.91215978320688
edge_quant total L2 EPE:11.915670185908676
edge_quant total L1 Photo:65.50682769158877
```


trying out chunking with resize, overlap
```
python TFLiteConverter.py --NetworkName=Network.ResNet \
--tflite_path=../models/160x120is3ic16in1.2ef/overlap_crop_stack/ \
--tflite_edge_path=../models/160x120is3ic16in1.2ef/overlap_crop_stack/ \
--tf_model_path=../models/160x120is3ic16in1.2ef/499model.ckpt \
--OverlapCropStack \
--NumSubBlocks=1 \
--InitNeurons=32 \
--PatchDelta=16 \
--ExpansionFactor=1.2 \
--NumOut=2

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNet \
--CheckPointFolder=../models/160x120is3ic16in1.2ef/ \
--TFLiteFolder=overlap_crop_stack \
--ResizeCropStack \
--CheckPointNum=499 \
--NumSubBlocks=1 \
--InitNeurons=32 \
--ExpansionFactor=1.2 \
--OnEdge \
--Display
```

## 2023.04.10
testing out cost volume model 
```
python Train.py \
--ExperimentFileName="cost_volume_test" \
--NetworkName=Network.ResNetCostVolume \
--MiniBatchSize=32 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=32 \
--NumSubBlocks=2 \
--SaveTestModel \
--NumEpochs=100

python TFLiteConverter.py --NetworkName=Network.ResNetCostVolume \
--tflite_path=../models/cost_volume_test/converted/ \
--tflite_edge_path=../models/cost_volume_test/converted/ \
--tf_model_path=../models/cost_volume_test/0a0model.ckpt \
--NumSubBlocks=2 \
--PatchSize0=8 \
--PatchSize1=8 \
--InitNeurons=32 \
--NumOut=2

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNetCostVolume \
--CheckPointFolder=../models/cost_volume_test/ \
--TFLiteFolder=converted \
--CheckPointNum=0a0 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--PatchSize0=8 \
--PatchSize1=8 \
--OnEdge \
--Display
```


## 2023.04.12

adding more scales M/8, M/4, M/2, M
```
python Train.py \
--ExperimentFileName="multiscale_xy_multiscale_loss_with_scales_4" \
--NetworkName=Network.MultiScaleResNet \
--MiniBatchSize=32 \
--LoadCheckPoint=0 \
--LR=1e-3 \
--InitNeurons=32 \
--NumSubBlocks=2 \
--NumEpochs=200

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
--CheckPointNum=99a0 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Display="" \
--Old="" \
--OnEdge=True
```

## 2023.04.12

```
5e-4 and 1e-3 didnt train
```

we are trying 1e-3 with minibatch 8
and 2e-4 with minibatch 32


## 2023.04.14

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
--tflite_path=../models/multiscale_xy_multiscale_loss_with_scales_1e_4/converted/lite.tflite \
--tflite_edge_path=../models/multiscale_xy_multiscale_loss_with_scales_1e_4/converted/ \
--tf_model_path=../models/multiscale_xy_multiscale_loss_with_scales_1e_4/2a0model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--NumOut=2

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_xy_multiscale_loss_with_scales_1e_4/ \
--CheckPointNum=2a0 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Display="" \
--Old="" \
--OnEdge=True
```


testing optical flow with multiscale with learning rate 2e-4
```
python Train.py \
--ExperimentFileName="multiscale_xy_multiscale_loss_with_scales_2e_4_1" \
--NetworkName=Network.MultiScaleResNet \
--MiniBatchSize=32 \
--LoadCheckPoint=0 \
--LR=2e-4 \
--InitNeurons=32 \
--NumSubBlocks=2 \
--NumEpochs=100

python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_xy_multiscale_loss_with_scales_2e_4_1/converted/lite.tflite \
--tflite_edge_path=../models/multiscale_xy_multiscale_loss_with_scales_2e_4_1/converted/ \
--tf_model_path=../models/multiscale_xy_multiscale_loss_with_scales_2e_4_1/90a0model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--NumOut=2

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_xy_multiscale_loss_with_scales_2e_4_1/ \
--CheckPointNum=90a0 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Display=True \
--Old="" \
--OnEdge=True

full for a counter of 640
full GPU time avg:0.2359493300318718
full GPU fps :4.238198090517659
full total L1 EPE:1.9696512518101372
full total L2 EPE:10.370981792471138
full total L1 Photo:56.795700563372996
quant for a counter of 640
quant GPU time avg:0.22441018149256706
quant GPU fps :4.456125802086756
quant total L1 EPE:2.060245623975061
quant total L2 EPE:10.277372009417741
quant total L1 Photo:50.2506475244387
edge_quant for a counter of 640
edge_quant GPU time avg:0.04564637690782547
edge_quant GPU fps :21.90754376890235
edge_quant total L1 EPE:2.060728432610631
edge_quant total L2 EPE:10.29362592123798
edge_quant total L1 Photo:51.12454019565776

```


testing without deconvolution  -- 3MB model
```
python Train.py \
--ExperimentFileName="wo-deconvolve" \
--NetworkName=Network.ResNetWODeconv \
--MiniBatchSize=32 \
--LoadCheckPoint=0 \
--LR=2e-4 \
--InitNeurons=32 \
--NumSubBlocks=2 \
--NumEpochs=500

python TFLiteConverter.py --NetworkName=Network.ResNetWODeconv \
--tflite_path=../models/wo-deconvolve/converted/ \
--tflite_edge_path=../models/wo-deconvolve/converted/ \
--tf_model_path=../models/wo-deconvolve/0a0model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--NumOut=2


python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNetWODeconv \
--CheckPointFolder=../models/wo-deconvolve/ \
--CheckPointNum=0a0 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnEdge \
--Display


full for a counter of 640
full GPU time avg:0.005251797288656235
full GPU fps:190.4110050401179
full total L1 EPE:45.68989619016647
full total L2 EPE:65.31123426556587
full total L1 Photo:135.47720650412828
quant for a counter of 640
quant GPU time avg:0.07125775255262852
quant GPU fps:14.033560759040702
quant total L1 EPE:45.70259735584259
quant total L2 EPE:65.32376669049263
quant total L1 Photo:135.42281079841385
edge_quant for a counter of 640
edge_quant GPU time avg:0.016442444548010825
edge_quant GPU fps:60.8182072367687
edge_quant total L1 EPE:45.69705154001713
edge_quant total L2 EPE:65.3165008187294
edge_quant total L1 Photo:135.37964678831767

```


```
python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNetWODeconv \
--CheckPointFolder=../models/deconvolve/ \
--CheckPointNum=0a0 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnEdge \
--Display
```

## 2023.04.18

```
python Train.py \
--ExperimentFileName="baseline_scaled4" \
--NetworkName=Network.ResNet \
--MiniBatchSize=32 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=32 \
--NumSubBlocks=2 \
--NumEpochs=100


python TFLiteConverter.py --NetworkName=Network.ResNet \
--tflite_path=../models/baseline_scaled4/converted/ \
--tflite_edge_path=../models/baseline_scaled4/converted/ \
--tf_model_path=../models/baseline_scaled4/99model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--NumOut=2

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNet \
--CheckPointFolder=../models/baseline_scaled4/ \
--CheckPointNum=99 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnEdge \
--Display


full for a counter of 640
full GPU time avg:0.010285009071230889
full GPU fps:97.22888847975727
full total L1 EPE:4.745787614182336
full total L2 EPE:8.894557633477962
full total L1 Photo:54.66630416099472
quant for a counter of 640
quant GPU time avg:0.21255083121359347
quant GPU fps:4.704756948210165
quant total L1 EPE:4.763469806266949
quant total L2 EPE:8.92114234934561
quant total L1 Photo:43.26738527548433
edge_quant for a counter of 640
edge_quant GPU time avg:0.07104876413941383
edge_quant GPU fps:14.074840176498673
edge_quant total L1 EPE:4.7391038845526055
edge_quant total L2 EPE:8.92224491359666
edge_quant total L1 Photo:42.03177195847639

```
![[test_pred_full.png]]
![[test_pred_quant.png]]
![[test_pred_edge_quant 1.png]]


Aniket's multiscale network
-- didnt work because it was trained with standardization

```
python3 Train.py \
--NetworkName=Network.ResNet_mscale \
--UncType=LinearSoftplus \
--BasePath=/home/pear_group/ramana/OpticalFlowOnTPU/Datasets/FlyingChairs2 
--CheckPointPath= /home/pear_group/uncert_flow/PRGEyeOmni/CheckPoints/multiscale_added_incremental_preds_ep400_LinearSoftplus/ \ 
--LogsPath=/home/pear_group/uncert_flow/PRGEyeOmni/Logs/multiscale_added_incremental_preds_ep400_LinearSoftplus 
--NumEpochs=400 \
--LR 1e-3


python TFLiteConverter.py --NetworkName=Network.ResNetAniketMscale \
--tflite_path=../models/multiscale_added_incremental_preds_ep400_LinearSoftplus/converted/lite.tflite \
--tflite_edge_path=../models/multiscale_added_incremental_preds_ep400_LinearSoftplus/converted/ \
--tf_model_path=../models/multiscale_added_incremental_preds_ep400_LinearSoftplus/399model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--NumOut=2


python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNetAniketMscale \
--CheckPointFolder=../models/multiscale_added_incremental_preds_ep400_LinearSoftplus/ \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnGPU \
--OnEdge \
--Display
```




## 2023.04.21

training edge dilation

```
python Train.py \
--ExperimentFileName="edge_dilation" \
--NetworkName=Network.ResNetDilateTest \
--MiniBatchSize=32 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=32 \
--NumSubBlocks=2 \
--SaveTestModel \
--NumEpochs=400

python TFLiteConverter.py --NetworkName=Network.ResNetDilateTest \
--tflite_path=../models/edge_dilation/converted/ \
--tflite_edge_path=../models/edge_dilation/converted/ \
--tf_model_path=../models/edge_dilation/0a0model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--NumOut=2

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNetDilateTest \
--CheckPointFolder=../models/edge_dilation/ \
--TFLiteFolder=converted \
--CheckPointNum=0a0 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnEdge \
--Display
```


baseline- scaled-down working doesnt make sense. let me try the baseline version itself

```
python Train.py \
--ExperimentFileName="baseline_wo_shift" \
--NetworkName=Network.ResNet \
--MiniBatchSize=32 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=32 \
--NumSubBlocks=2 \
--NumEpochs=100

python TFLiteConverter.py --NetworkName=Network.ResNet \
--tflite_path=../models/baseline_wo_shift/converted/ \
--tflite_edge_path=../models/baseline_wo_shift/converted/ \
--tf_model_path=../models/baseline_wo_shift/3model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--NumOut=2

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNet \
--CheckPointFolder=../models/baseline_wo_shift/ \
--CheckPointNum=3 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnGPU \
--OnGPUQuant \
--OnEdge \
--Display
```

## 2023.04.25

Training multiscale with uncertainity 
```
python Train.py \
--ExperimentFileName="multiscale_uncertainity_1" \
--NetworkName=Network.MultiScaleResNet \
--MiniBatchSize=32 \
--LoadCheckPoint=1 \
--LR=1e-4 \
--InitNeurons=32 \
--LossFuncName=MultiscaleSL1-1 \
--UncType=LinearSoftplus \
--NumSubBlocks=2 \
--NumEpochs=400

python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted/ \
--tf_model_path=../models/multiscale_uncertainity_1/141a0model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--NumOut=4

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--CheckPointNum=141a0 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--Display


full GPU time avg:0.010684720054268838
full GPU fps :93.59159574803017
full total L1 EPE:2.0316751237085553
full total L2 EPE:10.356702087476151
full total L1 Photo:57.55838465835107

edge_quant for a counter of 640
edge_quant GPU time avg:0.047227543592453
edge_quant GPU fps :21.174084526382202
edge_quant total L1 EPE:2.2423165198008066
edge_quant total L2 EPE:9.984831518476131
edge_quant total L1 Photo:48.096894873416744
```

testing with resize to half
```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted_half/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted_half/ \
--tf_model_path=../models/multiscale_uncertainity_1/141a0model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--ResizeToHalf \
--NumOut=4

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_half \
--CheckPointNum=141a0 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--ResizeToHalf \
--OnGPU \
--OnEdge \
--Display

edge_quant for a counter of 640
edge_quant GPU time avg:0.012731166556477547
edge_quant GPU fps :78.54739748819055
edge_quant total L1 EPE:4.280480678996537
edge_quant total L2 EPE:9.056758094165707
edge_quant total L1 Photo:57.8630079111427
```

testing with chunking resize crop stack

```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted_crop_stack/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted_crop_stack/ \
--tf_model_path=../models/multiscale_uncertainity_1/141a0model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--ResizeCropStack \
--NumOut=4


python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_crop_stack \
--CheckPointNum=141a0 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--ResizeCropStack \
--OnGPU \
--OnEdge \
--Display


full for a counter of 640
full GPU time avg:0.011194894462823868
full GPU fps :89.32643387758691
full total L1 EPE:2.251788202143507
full total L2 EPE:10.3740508556657
full total L1 Photo:55.936199032561966
edge_quant for a counter of 640
edge_quant GPU time avg:0.01168380193412304
edge_quant GPU fps :85.58857858412145
edge_quant total L1 EPE:2.4799906041182114
edge_quant total L2 EPE:9.944058768358081
edge_quant total L1 Photo:44.92328416304157
```
