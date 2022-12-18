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
python Test.py --NetworkName=Network.ResNet \
--CheckPointFolder=../models/flow_hsv_rnetd2n32lr4/ \
--CheckPointNum=11 \
--NumSubBlocks=2 \
--InitNeurons=32

# tflite conversion
python TFLiteConverter.py --NetworkName=Network.ResNet \
--tflite_path=../models/flow_hsv_rnetd2n32lr4/converted/resnet.tflite \
--tflite_edge_path=../models/flow_hsv_rnetd2n32lr4/converted/ \
--tf_model_path=../models/flow_hsv_rnetd2n32lr4/11model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 

# tflite test
python TestTFLite.py --ModelPath=../models/flow_hsv_rnetd2n32lr4/converted/ \
--ModelName=resnet

# test image collect
python Test.py --NetworkName=Network.ResNet \
--CheckPointFolder=../models/flow_hsv_rnetd2n32lr4/ \
--CheckPointNum=11 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Display=True

```

```

# resnet row 7 in sheet in 3060ti
python Test.py --NetworkName=Network.ResNet \
--CheckPointFolder=../models/flow_hsv_rnet32nlr4d1/\
--CheckPointNum=317\
--NumSubBlocks=1\
--InitNeurons=64

# resnet row 10 in sheet in 3080 
python Test.py --NetworkName=Network.ResNet \
--CheckPointFolder=../models/flow_hsv_rnet32nlr4/
--CheckPointNum=33\
--NumSubBlocks=2\
--InitNeurons=32

# resnet row 12 in sheet in 3080 
python Test.py --NetworkName=Network.ResNet \
--CheckPointFolder=../models/flow_hsv_rnetlr4/
--CheckPointNum=30\ -- TODO
--NumSubBlocks=3\
--InitNeurons=32

# resnet row 13 in sheet model is in 3060ti
python Test.py --NetowrkName=Network.ResNet \
--CheckPointFolder=../models/flow_hsv_rnet64nlr4/
--CheckPointNum=120\
--NumSubBlocks=2\
--InitNeurons=64
```


```
# 
python Test.py --NetworkName=Network.ResNet \
--CheckPointPathFolder=../models/flow_hsv_rnetd1n32lr4/\
--CheckPointNum=7\
--NumSubBlocks=2\
--InitNeurons=32
```

```
# unet row 15 in model in turint 3

```


converted to tflite
```
# converted to tflite
# resnet row 4 in sheet in turing 2

```

tflite test
```
# resnet row 4 in sheet in turing 2

```