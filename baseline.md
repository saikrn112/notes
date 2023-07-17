

#### Best multiscale model 400 epochs
```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_xy_multiscale_loss_with_scales_3/converted/lite.tflite \
--tflite_edge_path=../models/multiscale_xy_multiscale_loss_with_scales_3/converted/ \
--tf_model_path=../models/multiscale_xy_multiscale_loss_with_scales_3/99a0model.ckpt \
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
--OnGPU \
--OnEdge \
--ShiftedFlow \
--Display

full for a counter of 640
full GPU time avg:0.008801507949829101
full GPU fps :113.61689447993022
full EPE:4.350075721740723
full final loss:2.7470510301413014
edge_quant for a counter of 640
edge_quant GPU time avg:0.07060475908219814
edge_quant GPU fps :14.163351210302961
edge_quant EPE:5.318717956542969
edge_quant final loss:3.404239693842828
```

#### Sintel Multiscale with uncertainity without chunking

default resolution 352x480

**clean**
```
python TFLiteConverter.py --NetworkName=Network.ResNet \
--tflite_path=../models/baseline_xy/converted_sintel/ \
--tflite_edge_path=../models/baseline_xy/converted_sintel/ \
--tf_model_path=../models/baseline_xy/99model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--NumOut=2

python Test_new_sintel.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNet \
--CheckPointFolder=../models/baseline_xy/ \
--TFLiteFolder=converted_sintel \
--CheckPointNum=99 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnGPU \
--OnEdge \
--DataList=./Misc/MPI_Sintel_train_clean.txt \
--ShiftedFlow \
--Display

full for a counter of 1041
full GPU time avg:0.009250757673631827
full GPU fps :108.09925362658453
full EPE:6.001053810119629
full final loss:3.784932344006759
edge_quant for a counter of 1041
edge_quant GPU time avg:0.046604824340996207
edge_quant GPU fps :21.457006096262532
edge_quant EPE:6.070018768310547
edge_quant final loss:3.8667309808255843

```

**Final**

```
python Test_new_sintel.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNet \
--CheckPointFolder=../models/baseline_xy/ \
--TFLiteFolder=converted_sintel \
--CheckPointNum=99 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnGPU \
--OnEdge \
--DataList=./Misc/MPI_Sintel_Final_train_list.txt \
--ShiftedFlow \
--Display

full for a counter of 1041
full GPU time avg:0.007931757385517747
full GPU fps :126.0754649185131
full EPE:7.343352794647217
full final loss:4.629847124118741
edge_quant for a counter of 1041
edge_quant GPU time avg:0.07068271778960507
edge_quant GPU fps :14.147729901623345
edge_quant EPE:8.126578330993652
```

---
---



# Chunking

#### FC2

```
python TFLiteConverter.py --NetworkName=Network.ResNet \
--tflite_path=../models/baseline_xy/converted_chunking/ \
--tflite_edge_path=../models/baseline_xy/converted_chunking/ \
--tf_model_path=../models/baseline_xy/99model.ckpt \
--ResizeCropStack \
--NumSubBlocks=2 \
--InitNeurons=32 \
--NumOut=2

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNet \
--CheckPointFolder=../models/baseline_xy/ \
--TFLiteFolder=converted_chunking \
--ResizeCropStack \
--CheckPointNum=99 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnGPU \
--OnEdge \
--ShiftedFlow \
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

full for a counter of 640
full GPU time avg:0.008948181942105293
full GPU fps :111.75454483044675
full EPE:4.763381481170654
full final loss:3.0091141235549004
edge_quant for a counter of 640
edge_quant GPU time avg:0.00967158041894436
edge_quant GPU fps :103.39571783337854
edge_quant EPE:5.571102142333984
edge_quant final loss:3.549365595076233
```


#### Sintel multiscale Clean

```
python TFLiteConverter.py --NetworkName=Network.ResNet \
--tflite_path=../models/baseline_xy/converted_sintel_chunking/ \
--tflite_edge_path=../models/baseline_xy/converted_sintel_chunking/ \
--tf_model_path=../models/baseline_xy/99model.ckpt \
--ResizeCropStack \
--NumSubBlocks=2 \
--InitNeurons=32 \
--NumOut=2

python Test_new_sintel.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.ResNet \
--CheckPointFolder=../models/baseline_xy/ \
--TFLiteFolder=converted_sintel_chunking \
--ResizeCropStack \
--CheckPointNum=99 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--OnGPU \
--OnEdge \
--DataList=./Misc/MPI_Sintel_train_clean.txt \
--ShiftedFlow \
--ResizeCropStack \
--Display

full for a counter of 1041
full GPU time avg:0.008186367128355703
full GPU fps :122.15430658322528
full EPE:7.009836196899414
full final loss:4.419779314517288
edge_quant for a counter of 1041
edge_quant GPU time avg:0.009521292907245793
edge_quant GPU fps :105.02775303120762
edge_quant EPE:7.819609642028809
edge_quant final loss:5.0121052899003375
```


#### Sintel multiscale Final

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
