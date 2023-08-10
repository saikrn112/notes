model - [[Multiscale + Uncertainty 422 Epochs FT3D fine tuned]]


Generate the model in a separate folder 
```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted_blender/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted_blender/ \
--tf_model_path=../models/multiscale_uncertainity_1/422model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--NumOut=4
```
to run on generated frames

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