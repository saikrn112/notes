Train
```
python Train.py \
--ExperimentFileName="multiscale_warp" \
--NetworkName=Network.MultiScaleResWarpNet \
--MiniBatchSize=16 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--LossFuncName=MultiscaleSL1-1 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--NumEpochs=1 \
--SaveTestModel
```


TFLiteConversion 
```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResWarpNet \
--tflite_path=../models/multiscale_warp/converted/ \
--tflite_edge_path=../models/multiscale_warp/converted/ \
--tf_model_path=../models/multiscale_warp/0a0model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--InitNeurons=32 
```


Test
```
python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResWarpNet \
--CheckPointFolder=../models/multiscale_warp/ \
--CheckPointNum=0a0 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnGPU \
--OnEdge \
--Display
```