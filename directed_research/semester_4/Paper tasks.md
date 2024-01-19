
Optical flow comparison pic 
- [ ] RAFT
- [ ] SpyNet
- [ ] PWCNet
- [ ] FlowNet2
- [ ] NanoFlowNet
- [ ] EdgeFlowNet full res
- [ ] EdgeFlowNet chunking


---
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
```

---

ground truth and other crops 
```
python3 slight_cropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/1_img1_sintel1.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/1_img1_sintel1_crop.png
python3 slight_cropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/3_flownet2_sintel1.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/3_flownet2_sintel1_crop.png

python3 slight_cropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/5_pwc_sintel1.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/5_pwc_sintel1_crop.png

python3 slight_cropper.py --input_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/6_raft_sintel1.png --output_path /home/ramu/Personal/OpticalFlowOnTPU/paper_results/6_raft_sintel1_crop.png
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
--DataList=./Misc/MPI_Sintel_train_clean.txt 
edge_quant for a counter of 1041
edge_quant GPU time avg:0.04400682907397649
edge_quant GPU fps :22.72374586042037
edge_quant EPE:6.149776458740234
edge_quant final loss:3.9246251183659497
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
--DataList=./Misc/MPI_Sintel_train_clean.txt \
--ResizeCropStack
edge_quant for a counter of 1041
edge_quant GPU time avg:0.01068276012321714
edge_quant GPU fps :93.60876669192189
edge_quant EPE:6.368882656097412
edge_quant final loss:4.064157241001711
352x480
```


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
--DataList=./Misc/MPI_Sintel_train_clean.txt \
--ResizeCropStack \
--Display


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
--ResizeToHalf
```
