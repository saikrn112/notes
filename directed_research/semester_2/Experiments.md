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
stdout='Running on EdgeTPU:  True\nfull for a counter of 1\nfull GPU time avg:1.0544953346252441\nfull GPU fps:0.9483209334021272\nfull total L1 EPE:42.21338653564453\nfull total L2 EPE:60.0238037109375\nfull total L1 Photo:50.071431107954545\nquant for a counter of 1\nquant GPU time avg:0.1404106616973877\nquant GPU fps:7.121966294519676\nquant total L1 EPE:42.206050872802734\nquant total L2 EPE:60.014549255371094\nquant total L1 Photo:50.135931581439394\nedge_quant for a counter of 1\nedge_quant GPU time avg:0.05222296714782715\nedge_quant GPU fps:19.148663023479838\nedge_quant total L1 EPE:42.20557403564453\nedge_quant total L2 EPE:60.01387405395508\nedge_quant total L1 Photo:49.956015230429294\n'

```
