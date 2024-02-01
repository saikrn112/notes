
---
---
- [x] EPE in new resolution
	- [ ] nanoflownet run
	- [x] RAFT
	- [x] SPyNet
	- [x] PwCNet
	- [x] EdgeFlowNet full
	- [x] EdgeFlowNet chunking
- [ ] nano numbers
	- [x] girish access
	- [x] sintel dataset download
	- [x] RAFT - uday access
	- [x] SPyNet
	- [x] PwCNet
	- [ ] EdgeflowNet full
	- [ ] EdgeFlowNet chunking
- [ ] ablation study for different resolutions
	- [ ] need to figure out for images
- [ ] ablation study of the network
	- [x] actual network
	- [x] l1+50 network
	- [x] small network
	- [x] MS l1 network
	- [x] MS wo uncertainity
- [x] experiment quants 
	- [x] static
	- [x] dynamic
	- [x] gap

images
- [ ] network
- [ ] comparison pic 
- [ ] drone with equipment
- [ ] experiment sets
	- [ ] drone view optical flow insets
- [ ] blender


---


Optical flow comparison pic 
- [x] RAFT
- [x] SpyNet
- [x] PWCNet
- [x] FlowNet2
- [x] NanoFlowNet
- [x] EdgeFlowNet full res
- [x] EdgeFlowNet chunking

FlowNet2 inference 
```
cp OpticalFlowOnTPU/Datasets/Sintel//training/clean/alley_2/frame_0017.png flownet2-docker/data/sintel1.png
cp OpticalFlowOnTPU/Datasets/Sintel//training/clean/alley_2/frame_0018.png flownet2-docker/data/sintel2.png

./run-network.sh -n FlowNet2 -v ./data/sintel1.png ./data/sintel2.png ./outputs/sintel1.flo

#/home/ramu/Personal/flownet2-docker/outputs/sintel1.flo
```

---

SPyNet
```
cp OpticalFlowOnTPU/Datasets/Sintel//training/clean/alley_2/frame_0017.png pytorch-spynet/images/sintel1.png
cp OpticalFlowOnTPU/Datasets/Sintel//training/clean/alley_2/frame_0018.png pytorch-spynet/images/sintel2.png
cd pytorch-spynet

python3 slight_cropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/Datasets/Sintel//training/clean/alley_2/frame_0017.png --output_path /home/ramu/Personal/pytorch-spynet/images/sintel1.png 
python3 slight_cropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/Datasets/Sintel//training/clean/alley_2/frame_0018.png --output_path /home/ramu/Personal/pytorch-spynet/images/sintel2.png 

python run.py --one images/sintel1.png --two images/sintel2.png --out outputs/sintel1.flo

clean
full for a counter of 1041
full GPU time avg:0.12560586283461161
full GPU fps :7.961411811777648
full EPE:4.617524147033691
full final loss:2.9152872379543573


final 
full for a counter of 1041
full GPU time avg:0.12547489133279674
full GPU fps :7.969721984836811
full EPE:5.037983417510986
full final loss:3.1774951988593187


gpu
clean - 80W
full for a counter of 1041
full GPU time avg:0.033354137633192664
full GPU fps :29.981287808947613
full EPE:4.61790657043457
full final loss:2.915518681737921

final - 78W
full for a counter of 1041
full GPU time avg:0.03295783167499172
full GPU fps :30.341801908005866
full EPE:5.0384931564331055
full final loss:3.177810865136778

```

---

PwcNet
```
cp OpticalFlowOnTPU/Datasets/Sintel//training/clean/alley_2/frame_0017.png pytorch-pwc/images/sintel1.png
cp OpticalFlowOnTPU/Datasets/Sintel//training/clean/alley_2/frame_0018.png pytorch-pwc/images/sintel2.png
cd pytorch-pwc

python3 slight_cropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/Datasets/Sintel//training/clean/alley_2/frame_0017.png --output_path /home/ramu/Personal/pytorch-pwc/images/sintel1.png 
python3 slight_cropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/Datasets/Sintel//training/clean/alley_2/frame_0018.png --output_path /home/ramu/Personal/pytorch-pwc/images/sintel2.png 

python run.py --one images/sintel1.png --two images/sintel2.png --out outputs/sintel1.flo


python run3.py
full for a counter of 1041
full GPU time avg:0.09277570327810092
full GPU fps :10.778684123821062
full EPE:3.787311553955078
full final loss:2.370214404157156

full for a counter of 1041
full GPU time avg:0.09247692036697432
full GPU fps :10.81350888450567
full EPE:3.9290106296539307
full final loss:2.449189836408059


gpu 
final - 50
full for a counter of 1041
full GPU time avg:0.02155334003606058
full GPU fps :46.39652129678809
full EPE:3.92818284034729
full final loss:2.448568066719859
clean - 50
full for a counter of 1041
full GPU time avg:0.021417386250124886
full GPU fps :46.691038221069995
full EPE:3.786980390548706
full final loss:2.3700733068976176

```

---

ground truth and other crops 
```
python3 slight_cropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/1_img1_sintel1.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/1_img1_sintel1_crop.png
python3 slight_cropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/3_flownet2_sintel1.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/3_flownet2_sintel1_crop.png

python3 slight_cropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/5_pwc_sintel1.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/5_pwc_sintel1_crop.png

python3 slight_cropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/6_raft_sintel1.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/6_raft_sintel1_crop.png
```

---

RAFT

```
gpu 
clean
full for a counter of 1041
full GPU time avg:0.074943647146454
full GPU fps :13.34335915152103
full EPE:3.4547040462493896
full final loss:2.1320647328526614

final 
full for a counter of 1041
full GPU time avg:0.06501937668330388
full GPU fps :15.380030554134594
full EPE:4.232720375061035
full final loss:2.637825960806937

nano
clean
full for a counter of 1041
full GPU time avg:0.30853018339268873
full GPU fps :3.2411739720364006
full EPE:3.4609313011169434
full final loss:2.1349265053188367

final
full for a counter of 1041
full GPU time avg:0.3084065337002449
full GPU fps :3.2424734586587842
full EPE:4.197347164154053
full final loss:2.6173407556659094
```

----
---
---



- [ ] GPU clean full
- [ ] GPU final full
- [ ] TPU clean full
- [ ] TPU final full
- [ ] GPU clean chunk
- [ ] GPU final chunk
- [ ] TPU clean chunk
- [ ] TPU final chunk

GPU clean full
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
--DataList=./Misc/MPI_Sintel_train_clean.txt 

full for a counter of 1041
full GPU time avg:0.017679216080737963
full GPU fps :56.56359396441396
full EPE:5.464992046356201
full final loss:3.4176779372490564
```


GPU clean chunk
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
--DataList=./Misc/MPI_Sintel_train_clean.txt \
--ResizeCropStack
full for a counter of 1041
full GPU time avg:0.018869996872461266
full GPU fps :52.99417942455479
full EPE:5.663519859313965
full final loss:3.543716961165441
1024 x 436
```

GPU final full
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
--PatchSize0=416 \
--PatchSize1=1024 \
--DataList=./Misc/MPI_Sintel_Final_train_list.txt
full for a counter of 1041
full GPU time avg:0.018367929944158402
full GPU fps :54.44271635617994
full EPE:6.3117876052856445
full final loss:3.9505115545119494

```


GPU final chunk
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
--PatchSize0=416 \
--PatchSize1=1024 \
--DataList=./Misc/MPI_Sintel_Final_train_list.txt \
--ResizeCropStack

full for a counter of 1041
full GPU time avg:0.018350146345858614
full GPU fps :54.49547819141436
full EPE:6.533306121826172
full final loss:4.092133875639249
```

--- 352 x 480 ---

GPU clean full
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
--PatchSize0=352 \
--PatchSize1=480 \
--ResizeNearestCrop \
--DataList=./Misc/MPI_Sintel_train_clean.txt 

full for a counter of 1041
full GPU time avg:0.009294622569675061
full GPU fps :107.58909170369463
full EPE:5.660618782043457
full final loss:3.5436044794996695
```


GPU clean chunk
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
--PatchSize0=352 \
--PatchSize1=480 \
--ResizeNearestCropStack \
--DataList=./Misc/MPI_Sintel_train_clean.txt

full for a counter of 1041
full GPU time avg:0.009404067003761313
full GPU fps :106.33697097224353
full EPE:5.910791397094727
full final loss:3.7059149030277525
```

GPU final full
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
--PatchSize0=352 \
--PatchSize1=480 \
--ResizeNearestCrop \
--DataList=./Misc/MPI_Sintel_Final_train_list.txt

full for a counter of 1041
full GPU time avg:0.009368693565200087
full GPU fps :106.7384681802903
full EPE:7.347682952880859
full final loss:4.604579629296013

```


GPU final chunk
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
--PatchSize0=480 \
--PatchSize1=352 \
--ResizeNearestCropStack \
--DataList=./Misc/MPI_Sintel_Final_train_list.txt

full for a counter of 1041
full GPU time avg:0.009498946604879857
full GPU fps :105.27483115720156
full EPE:7.68755578994751
full final loss:4.8234380759105555


```


TPU clean full
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
--OnEdge \
--PatchSize0=352 \
--PatchSize1=480 \
--ResizeNearestCrop \
--DataList=./Misc/MPI_Sintel_train_clean.txt 



edge_quant for a counter of 1041
edge_quant GPU time avg:0.04462274533985442
edge_quant GPU fps :22.410095846497786
edge_quant EPE:6.1780900955200195
edge_quant final loss:3.9352900368965784
```

TPU clean chunk
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
--OnEdge \
--PatchSize0=352 \
--PatchSize1=480 \
--ResizeNearestCropStack \
--DataList=./Misc/MPI_Sintel_train_clean.txt

edge_quant for a counter of 1041
edge_quant GPU time avg:0.010846139374658765
edge_quant GPU fps :92.19870457652692
edge_quant EPE:6.346118927001953
edge_quant final loss:4.044365763048732

```


TPU final full
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
--OnEdge \
--PatchSize0=352 \
--PatchSize1=480 \
--ResizeNearestCrop \
--DataList=./Misc/MPI_Sintel_Final_train_list.txt

edge_quant for a counter of 1041
edge_quant GPU time avg:0.0446074748703428
edge_quant GPU fps :22.417767490910997
edge_quant EPE:6.907169818878174
edge_quant final loss:4.3998320054881965


```

TPU final chunk
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
--OnEdge \
--PatchSize0=352 \
--PatchSize1=480 \
--ResizeNearestCropStack \
--DataList=./Misc/MPI_Sintel_Final_train_list.txt

edge_quant for a counter of 1041
edge_quant GPU time avg:0.010843743050361803
edge_quant GPU fps :92.21907927508803
edge_quant EPE:7.090342998504639
edge_quant final loss:4.519403679999563

```




---
---
---
inference speeds ablation study
- [x] 1024 x 416 -  
- [x] 640 x 480 -- not possible
- [x] 480 x 352  - 1
- [x] 176 x 240 - 2
- [x] 88 x 120 -- 96 x 128 - 3
- [ ] 44 x 60 -- 48 x 64 - 4
- [ ] 22 x 30 -- 32 x 32 - 5
- [ ] 11 x 15 -- 16 x 16 - 6

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
--PatchSize0=416 \
--PatchSize1=1024 \
--DataList=./Misc/MPI_Sintel_Final_train_list.txt

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
--PatchSize0=416 \
--PatchSize1=1024 \
--DataList=./Misc/MPI_Sintel_train_clean.txt
```


```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted_sintel_1024_416/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted_sintel_1024_416/ \
--tf_model_path=../models/multiscale_uncertainity_1/399model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--NumOut=4 \
--PatchSize0=416 \
--PatchSize1=1024

python Test_new_sintel.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_sintel_1024_416 \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--PatchSize0=416 \
--PatchSize1=1024 \
--DataList=./Misc/MPI_Sintel_Final_train_list.txt
full for a counter of 10
full GPU time avg:0.2049251079559326
full GPU fps :4.879831514911494
full EPE:6.866844177246094
full final loss:4.271678671240807
edge_quant for a counter of 1041
edge_quant GPU time avg:0.26065118970147244
edge_quant GPU fps :3.8365449286662163
edge_quant EPE:6.472112655639648
edge_quant final loss:4.123972919986983
```



```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted_sintel_480_352/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted_sintel_480_352/ \
--tf_model_path=../models/multiscale_uncertainity_1/399model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--NumOut=4 \
--PatchSize0=352 \
--PatchSize1=480

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_sintel_480_352 \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--PatchSize0=352 \
--PatchSize1=480 

full for a counter of 640
full GPU time avg:0.010173048079013824
full GPU fps :98.29895545887759
full EPE:2.7591497898101807
full final loss:1.7277436164440587
edge_quant for a counter of 640
edge_quant GPU time avg:0.04382377080619335
edge_quant GPU fps :22.818666253582084
edge_quant EPE:3.475637912750244
edge_quant final loss:2.213274074695073

```


```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted_sintel_240_176/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted_sintel_240_176/ \
--tf_model_path=../models/multiscale_uncertainity_1/399model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--NumOut=4 \
--PatchSize0=352 \
--PatchSize1=480 \
--NumberOfHalves=1

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_sintel_240_176 \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--PatchSize0=352 \
--PatchSize1=480 \
--NumberOfHalves=1




python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_sintel_240_176 \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--PatchSize0=352 \
--PatchSize1=480 \
--ResizeCropStack

full for a counter of 640
full GPU time avg:0.010183043777942657
full GPU fps :98.20246498066574
full EPE:3.1019206047058105
full final loss:1.9459755161136854
edge_quant for a counter of 640
edge_quant GPU time avg:0.01070760264992714
edge_quant GPU fps :93.39158658514513
edge_quant EPE:3.71882700920105
edge_quant final loss:2.3647628543083554
```


```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted_sintel_128_96/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted_sintel_128_96/ \
--tf_model_path=../models/multiscale_uncertainity_1/399model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--NumOut=4 \
--PatchSize0=96 \
--PatchSize1=128 

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_sintel_128_96 \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--PatchSize0=96 \
--PatchSize1=128 \
--ResizeNearestCrop


full for a counter of 640
full GPU time avg:0.0050098937004804615
full GPU fps :199.60503351679847
full EPE:4.52716064453125
full final loss:2.862200757025312
edge_quant for a counter of 640
edge_quant GPU time avg:0.0035309799015522
edge_quant GPU fps :283.2075026992947
edge_quant EPE:4.961106777191162
edge_quant final loss:3.169987844162871

```

```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted_sintel_64_48/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted_sintel_64_48/ \
--tf_model_path=../models/multiscale_uncertainity_1/399model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--NumOut=4 \
--PatchSize0=48 \
--PatchSize1=64 

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_sintel_64_48 \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--PatchSize0=48 \
--PatchSize1=64 \
--ResizeNearestCrop

full for a counter of 640
full GPU time avg:0.0046003714203834535
full GPU fps :217.37375281682088
full EPE:6.582145690917969
full final loss:4.233218090164155
edge_quant for a counter of 640
edge_quant GPU time avg:0.0014661997556686401
edge_quant GPU fps :682.035306672087
edge_quant EPE:6.6732587814331055
edge_quant final loss:4.327118266394147
```

```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted_sintel_32_32/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted_sintel_32_32/ \
--tf_model_path=../models/multiscale_uncertainity_1/399model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--NumOut=4 \
--PatchSize0=32 \
--PatchSize1=32 

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_sintel_32_32 \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--PatchSize0=32 \
--PatchSize1=32 \
--ResizeNearestCrop

full for a counter of 640
full GPU time avg:0.004488033428788185
full GPU fps :222.81473965536173
full EPE:9.40993881225586
full final loss:6.0832035601211825
edge_quant for a counter of 640
edge_quant GPU time avg:0.0009825576096773147
edge_quant GPU fps :1017.7520281262832
edge_quant EPE:12.633868217468262
edge_quant final loss:8.166470732539892
```


```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted_sintel_16_16/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted_sintel_16_16/ \
--tf_model_path=../models/multiscale_uncertainity_1/399model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--NumOut=4 \
--PatchSize0=16 \
--PatchSize1=16 

python3 Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_sintel_16_16 \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--PatchSize0=16 \
--PatchSize1=16 \
--ResizeNearestCrop

full for a counter of 640
full GPU time avg:0.004154730215668678
full GPU fps :240.68951486397685
full EPE:11.307138442993164
full final loss:7.412464184040436
edge_quant for a counter of 640
edge_quant GPU time avg:0.0006826259195804596
edge_quant GPU fps :1464.931188980632
edge_quant EPE:11.610689163208008
edge_quant final loss:7.607230754010379
```



```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted_sintel_128_96_halve/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted_sintel_128_96_halve/ \
--tf_model_path=../models/multiscale_uncertainity_1/399model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--NumOut=4 \
--PatchSize0=384 \
--PatchSize1=512 \
--NumberOfHalves=2

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_sintel_128_96_halve \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--PatchSize0=384 \
--PatchSize1=512 \
--NumberOfHalves=2

full for a counter of 640
full GPU time avg:0.010807115957140923
full GPU fps :92.53162490028052
full EPE:6.987936973571777
full final loss:4.509842362458585
edge_quant for a counter of 640
edge_quant GPU time avg:0.003437686339020729
edge_quant GPU fps :290.8933222467479
edge_quant EPE:6.903756141662598
edge_quant final loss:4.457191512506688
```


```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted_sintel_64_48_halve/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted_sintel_64_48_halve/ \
--tf_model_path=../models/multiscale_uncertainity_1/399model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--NumOut=4 \
--PatchSize0=384 \
--PatchSize1=512 \
--NumberOfHalves=3

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_sintel_64_48_halve \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--PatchSize0=384 \
--PatchSize1=512 \
--NumberOfHalves=3
```


```
python TFLiteConverter.py --NetworkName=Network.MultiScaleResNet \
--tflite_path=../models/multiscale_uncertainity_1/converted_sintel_16_16_halve/ \
--tflite_edge_path=../models/multiscale_uncertainity_1/converted_sintel_16_16_halve/ \
--tf_model_path=../models/multiscale_uncertainity_1/399model.ckpt \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--NumOut=4 \
--PatchSize0=256 \
--PatchSize1=256 \
--NumberOfHalves=4

python Test_new.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_sintel_16_16_halve \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--OnEdge \
--PatchSize0=256 \
--PatchSize1=256 \
--NumberOfHalves=4
```


---
---
---
```
docker run -v /home/ramu/Personal/OpticalFlowOnTPU/Datasets/FlyingChairs2:/workspace/FlyingChairs2  -v /home/ramu/Personal/nanoflownet-cnns:/workspace/nanoflownet --gpus all -it tensorflow/tensorflow:2.8.0-gpu

pip install opencv-python-headless==4.5.5.64

pip install tensorflow_model_optimization==0.7.2
pip install tqdm==4.64.0
pip install tensorflow_addons==0.16.1
pip install wandb==0.12.14
pip install --extra-index-url https://developer.download.nvidia.com/compute/redist --upgrade nvidia-dali-tf-plugin-cuda110==1.12.0

docker run -p 8883:8883 -v /home/ramu/Personal/OpticalFlowOnTPU/Datasets/FlyingChairs2:/workspace/FlyingChairs2 -v /home/ramu/Personal/OpticalFlowOnTPU/Datasets/Sintel/:/workspace/flowData/MPI-Sintel -v /home/ramu/Personal/nanoflownet-cnns:/workspace/nanoflownet --gpus all -it nanoflownet3


python main.py --pretrained /workspace/nanoflownet/pretrained_models/nanoflownet/model-best.h5 
```



---
---
---


- [ ] real
	- [ ] gap
	- [ ] dodging
	- [ ] static
- [ ] sim
	- [ ] gap
	- [ ] dodging
	- [ ] static


rgb image, depth, flow, raft, nanoflownet, edgeflownet

sim
- [ ] gap_flyt
	- [x] rgb
	- [x] depth
	- [x] flow_gt
	- [x] raft
	- [ ] edgeflownet
	- [ ] nanoflownet
- [ ] dyn
	- [x] rgb
	- [x] depth
	- [x] flow_gt
	- [x] raft
	- [ ] edgeflownet
	- [ ] nanoflownet
- [ ] static
	- [x] rgb
	- [x] depth
	- [x] flow_gt
	- [x] raft
	- [ ] edgeflownet
	- [ ] nanoflownet



---
---
---

```
python ClosestResizeCropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/gapflyt_real/frame0024.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/gapflyt_real/frame0024_re.png

python ClosestResizeCropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/gapflyt_real/frame0098.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/gapflyt_real/frame0098_re.png

python ClosestResizeCropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/static_real1/frame0489.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/static_real1/frame0489_re.png

python run.py --one /home/ramu/Personal/OpticalFlowOnTPU/paper_results/gapflyt_real/frame0024_re.png --two /home/ramu/Personal/OpticalFlowOnTPU/paper_results/gapflyt_real/frame0098_re.png --out outputs/gapflyt_real.flo


python run.py --one /home/ramu/Personal/OpticalFlowOnTPU/paper_results/gapflyt_real/frame0024_re.png --two /home/ramu/Personal/OpticalFlowOnTPU/paper_results/gapflyt_real/frame0098_re.png --out outputs/gapflyt_real.flo


python ClosestResizeCropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/dyn_real1/frame0369.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/dyn_real1/frame0369_re.png


python ClosestResizeCropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/dyn_real1/frame0370.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/dyn_real1/frame0370_re.png


python ClosestResizeCropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/dyn_aero_inset2/frame0183.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/dyn_aero_inset2/frame0183_re.png

python ClosestResizeCropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/dyn_aero_inset2/frame0184.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/dyn_aero_inset2/frame0184_re.png

python ClosestResizeCropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/dyn_aero_inset2/frame0185.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/dyn_aero_inset2/frame0185_re.png

python ClosestResizeCropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/dyn_ball_inset1/frame0678.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/dyn_ball_inset1/frame0678_re.png

python ClosestResizeCropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/dyn_ball_inset1/frame0679.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/dyn_ball_inset1/frame0679_re.png

python ClosestResizeCropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/dyn_ball_inset1/frame0677.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/dyn_ball_inset1/frame0677_re.png


python ClosestResizeCropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/static1_inset1/frame0494.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/static1_inset1/frame0494_re.png

python ClosestResizeCropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/insets/static1_inset2/frame0300.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/insets/static1_inset2/frame0300_re.png

python ClosestResizeCropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/insets/static2_inset1/frame0191.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/insets/static2_inset1/frame0191_re.png

python ClosestResizeCropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/insets/static2_inset2/frame0515.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/insets/static2_inset2/frame0515_re.png


python ClosestResizeCropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/insets/gap1_inset3/frame0236.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/insets/gap1_inset3/frame0236_re.png


python ClosestResizeCropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/banner/frame_0195.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/banner/frame_0195_re.png

python ClosestResizeCropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/banner/dyn2/frame0675.png --output_path  /home/ramu/Personal/OpticalFlowOnTPU/paper_results/banner/dyn2/frame0675_re.png

python ClosestResizeCropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/banner/dyn2/frame0676.png --output_path  /home/ramu/Personal/OpticalFlowOnTPU/paper_results/banner/dyn2/frame0676_re.png

python ClosestResizeCropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/banner/static1/frame_0027.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/banner/static1/frame_0027_re.png

```



```
python Test_new_single.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_sintel_chunking \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU \
--ResizeCropStack

python Test_new_single.py \
--BasePath=../Datasets/FlyingChairs2/ \
--NetworkName=Network.MultiScaleResNet \
--CheckPointFolder=../models/multiscale_uncertainity_1/ \
--TFLiteFolder=converted_sintel_chunking \
--CheckPointNum=399 \
--NumSubBlocks=2 \
--InitNeurons=32 \
--Uncertainity \
--OnGPU 


```



- [x] gapflyt_real
- [x] static_real
- [x] dynamic_real
- [x] gapflyt_sim
- [ ] static_sim
	- [x] image brightness
- [x] dynamic_sim

134 - 0:23-0:25

- [ ] banner
	- [ ] dynamic flow
	- [ ] gap flow
	- [ ] static flow
- [ ] network
- [ ] nano numbers
- [ ] tensorflow numbers


0:48, 1:12, 1:15,1:17

Figure 3
- nanoflownet
	- [x] dyn sim
	- [x] static sim
	- [x] gap sim
	- [x] dyn real
	- [x] static real
	- [ ] gap real
- order