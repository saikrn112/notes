HSV based flow prediction
1000
unet 
results/hsv_unet_100mb.csv
logs/flow_hsv_unet_wo_standard/
github - https://github.com/saikrn112/OpticalFlowOnTPU/pull/3/files

![[Pasted image 20221213204046.png]]





resnet n 32 s 3 lr3 - 125mb
![[Pasted image 20221214011958.png]]


resnet n 64 s 2 lr 3 - 125mb
![[Pasted image 20221215180850.png]]

resnet n 64 s 2 lr 4 - 125mb

we need commands for creating a test result, test values for both full model and quantized model
let's write commands for test result for full model
and commands for converting to tflite
```
# the following are commands for testing full model
# resnet row 4 in sheet in turing 2
python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNet \
--CheckPointFolder=../models/flow_hsv_rnetd2n32lr4/ \
--CheckPointNum=11 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Display="" \
--OnEdge=True

# tflite conversion
python TFLiteConverter.py --NetworkName=Network.ResNet \
--tflite_path=../models/flow_hsv_rnetd2n32lr4/converted/lite.tflite \
--tflite_edge_path=../models/flow_hsv_rnetd2n32lr4/converted/ \
--tf_model_path=../models/flow_hsv_rnetd2n32lr4/11model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 

# test image collect
python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNet \
--CheckPointFolder=../models/flow_hsv_rnetd2n32lr4/ \
--CheckPointNum=11 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Display=True \
--OnEdge=True
```

```
# unet row 11 in 3060
python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.UNet \
--CheckPointFolder=../models/flow_hsv_unet_wo_standard/ \
--CheckPointNum=34a0 \
--NumSubBlocks=3 \
--InitNeurons=32 \
--Display="" \
--OnEdge=True

python TFLiteConverter.py \
--NetworkName=Network.UNet \
--tflite_path=../models/flow_hsv_unet_wo_standard/converted/lite.tflite \
--tflite_edge_path=../models/flow_hsv_unet_wo_standard/converted/ \
--tf_model_path=../models/flow_hsv_unet_wo_standard/34a0model.ckpt \
--NumSubBlocks=3 \
--InitNeurons=32 
```

```
# resnet row 7 in sheet in turing 2
python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNet \
--CheckPointFolder=../models/flow_hsv_rnetd2n64lr4/ \
--CheckPointNum=120 \
--NumSubBlocks=2 \
--InitNeurons=64 \
--Display="" \
--OnEdge=True

python TFLiteConverter.py \
--NetworkName=Network.ResNet \
--tflite_path=../models/flow_hsv_rnetd2n64lr4/converted/lite.tflite \
--tflite_edge_path=../models/flow_hsv_rnetd2n64lr4/converted/ \
--tf_model_path=../models/flow_hsv_rnetd2n64lr4/120model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=64
```


baseline model
```
python TFLiteConverter.py --NetworkName=Network.ResNet \
--tflite_path=../models/golden/converted/lite.tflite \
--tflite_edge_path=../models/golden/converted/ \
--tf_model_path=../models/golden/49model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Old=True

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNet \
--CheckPointFolder=../models/golden/ \
--CheckPointNum=49 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Display="" \
--Old=True \
--OnEdge=True

```