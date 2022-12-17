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
# resnet row 4 in sheet
python Test.py --NetworkName=Network.ResNet \
--CheckPointPathFolder=../models/flow_hsv_rnetd1n32lr4/\
--CheckPointNum=7\
--NumSubBlocks=2\
--InitNeurons=32

# resnet row 7 in sheet
python Test.py --NetworkName=Network.ResNet \
--CheckPointPathFolder=../models/flow_hsv_rnetd1n64lr4/\
--CheckPointNum=7\
--NumSubBlocks=2\
--InitNeurons=32

```

