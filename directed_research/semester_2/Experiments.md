
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



all the experiments can be found [here]()
