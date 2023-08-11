```
python Test_blender_new.py \
--BasePath=../blender_test/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_blender \
--CheckPointNum=422 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--Display
```


```
convert the flow to radial and magnitude
take mean of all the flows 
do imgradient equivalent 
and get edges
```