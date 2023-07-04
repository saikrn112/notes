
#### Best multiscale model 400 epochs
```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted/ \
--tf_model_path=../models/multiscale_uncertainity_1/399model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--NumOut=4

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--Display

full for a counter of 640
full GPU time avg:0.010512028262019158
full GPU fps :95.12912019206456
full total L1 EPE:1.7277436164440587
full total L2 EPE:10.314434289670317
full total L1 Photo:61.838499241067815
edge_quant for a counter of 640
edge_quant GPU time avg:0.04676539152860641
edge_quant GPU fps :21.38333428446332
edge_quant total L1 EPE:2.2848535845056177
edge_quant total L2 EPE:9.61459982196684
edge_quant total L1 Photo:52.225522029375746
```

#### Chunking
```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted_chunking/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted_chunking/ \
--tf_model_path=../models/multiscale_uncertainity_1/399model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--ResizeCropStack \
--NumOut=4

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_chunking \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--ResizeCropStack \
--OnGPU \
--OnEdge \
--Display

full for a counter of 640
full GPU time avg:0.010406124964356422
full GPU fps :96.09725074657952
full total L1 EPE:1.9459755161136854
full total L2 EPE:10.334374720428604
full total L1 Photo:59.38486818564055
edge_quant for a counter of 640
edge_quant GPU time avg:0.011344940215349198
edge_quant GPU fps :88.14502157067734
edge_quant total L1 EPE:2.335738085041521
edge_quant total L2 EPE:9.793180834682426
edge_quant total L1 Photo:48.17355235706676
```

#### Sintel Multiscale with uncertainity without chunking

default resolution 352x480

**clean**
```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted_sintel/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted_sintel/ \
--tf_model_path=../models/multiscale_uncertainity_1/399model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--NumOut=4

python Test_new_sintel.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_sintel \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--DataList=./Misc/MPI_Sintel_train_clean.txt \
--Display


full for a counter of 1041
full GPU time avg:0.009318163255220646
full GPU fps :107.31728695993112
full total L1 EPE:3.696589076152567
full total L2 EPE:12.379776165762506
full total L1 Photo:93.79953202814947
edge_quant for a counter of 1041
edge_quant GPU time avg:0.0462067253193411
edge_quant GPU fps :21.64187124469135
edge_quant total L1 EPE:3.9246251183659497
edge_quant total L2 EPE:11.75666346281452
edge_quant total L1 Photo:95.75280982290786

```

**Final**

```
python Test_new_sintel.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_sintel \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--DataList=./Misc/MPI_Sintel_Final_train_list.tx \
--Display


full for a counter of 1041
full GPU time avg:0.009290723360924624
full GPU fps :107.6342455966183
full total L1 EPE:4.320951257276776
full total L2 EPE:12.772706958104738
full total L1 Photo:90.78476560225833
edge_quant for a counter of 1041
edge_quant GPU time avg:0.04625691071252887
edge_quant GPU fps :21.6183913840391
edge_quant total L1 EPE:4.444677126195772
edge_quant total L2 EPE:12.043474947455751
edge_quant total L1 Photo:92.46464510013683
```

## Sintel multiscale  chunking

#### clean

```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted_sintel_chunking/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted_sintel_chunking/ \
--tf_model_path=../models/multiscale_uncertainity_1/399model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--ResizeCropStack \
--Uncertainity \
--NumOut=4

python Test_new_sintel.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_sintel_chunking \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--DataList=./Misc/MPI_Sintel_train_clean.txt \
--ResizeCropStack \
--Display


full for a counter of 1041
full GPU time avg:0.009591420949593286
full GPU fps :104.25983858443873
full total L1 EPE:3.8841858846810893
full total L2 EPE:12.459870779305325
full total L1 Photo:93.83764791284607
edge_quant for a counter of 1041
edge_quant GPU time avg:0.011260012270279738
edge_quant GPU fps :88.80984993590567
edge_quant total L1 EPE:4.064157241001711
edge_quant total L2 EPE:11.870938483736586
edge_quant total L1 Photo:93.5930516458564
```


#### Final

```
python Test_new_sintel.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_sintel_chunking \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--DataList=./Misc/MPI_Sintel_Final_train_list.txt \
--ResizeCropStack \
--Display

full for a counter of 1041
full GPU time avg:0.009500829905529187
full GPU fps :105.25396306885057
full total L1 EPE:4.530900527468161
full total L2 EPE:12.883063874344318
full total L1 Photo:90.17325320212495
edge_quant for a counter of 1041
edge_quant GPU time avg:0.011299086349956355
edge_quant GPU fps :88.50273101982822
edge_quant total L1 EPE:4.600230609692139
edge_quant total L2 EPE:12.199189553285997
edge_quant total L1 Photo:90.44254458080448

```
