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


## TODOs
inference speed 
movidus 

predict polar coordinates instead of full HSV -- today
- test it with ResNet 100mb
- vizualize it back 

speed test based on number of channels
combining 3 (or more) channels 

hardware compatible models

end goal 
- dynamic obstacle - color clustering based on optical flow


- train on the full dataset
- inference speeds
- visualize the outputs 
- 

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
