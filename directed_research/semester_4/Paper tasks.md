
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
```