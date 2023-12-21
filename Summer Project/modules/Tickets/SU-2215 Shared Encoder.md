Lit Review : https://torc.atlassian.net/wiki/spaces/VD/pages/537167380/SU-2344+-+Lit+review

env: 
dataset:
model:
loss: focalLoss, smooth loss + regl1Kploss
time to train: 
framework:


- [ ] there are different set of datasets


need to understand dataset for 

- [ ] understand different configs 
	- [ ] train
	- [ ] test 
	- [ ] onnx

aws_train_exp2-1-5_multi-head_trl_wk-linear_no-trl_lr-test.py

aws_train_exp_1-1_training_config_sample.py


```
1. Reivse the ground truth '_re' JSON file (~100 images)  
1.1. select batch: _night_3k:  
1.2. visualize the ds  
1.3. contact deepika ask for the GT for ds  
1.4. compare  
1.5. create toy json files with ds GT inside.2. Dataloader adjustment.  
2.1 Update the land-center dataloader  
(1) eos-road_lane/mmdet/datasets/pipelines/lane_formating_median_new_fitting.py  
> @PIPELINES.register_module  
class CollectLanePoints_Median_New_Fitting(Collect):  
(2) another file for init: eos-road_lane/mmdet/datasets/pipelines/__init__.py  
(3) config --> train_pipline ---> type = "CollectLanePoints_Median_New_Fitting"  
2.2 verify it.
```

- [ ] get the visualization code for atleast one annotation json 
- [ ] merging is little involved need to understand poly2d


- [x] merge data files
- [x] make a copy of it in shared_encoder 
- [x] create a new set in the shared_encoder 
- [ ] so that gong is not blocked
- [ ] create a new amend

- [ ] make the same changes as yesterday in new branch
- [ ] make sure they are working with new sample? 



- [ ] need to visualization for overfit 
	- [ ] amend the infer file to dump outputs on overfit 
	- [ ] run the eval on that 
- [ ] need to get vizualation for full training
	- [ ] amend the infer file to dump outputs on eval 
	- [ ] run eval on that 

infer wrapper script
```
/home/ubuntu/torc/git/ML/eos-road_lane2/scripts/laneSegNet_scripts/script_inference/infer_LaneSegNet_Drivable_surface_only.py
```
infer python script 
```
/home/ubuntu/torc/git/ML/eos-road_lane2/tools/ganet/tusimple/laneSegNet_infer_ds_only.py
```

eval python script
```
python ds_only_acc_comp.py --config /home/ubuntu/torc/git/ML/eos-road_lane2/configs/laneSegNet_configs/others/aws_laneSegNet_train_exp4-1_single_branch_ds_seg_infer.py --results_folder /home/ubuntu/torc/git/ML/eos-road_lane2/exp_stuff/20231102_LaneSegNet_Drivable_Surface_Only --csv_file /home/ubuntu/ramana_test/shared_encoder/report.csv
```


python script overfit 
```
python ds_only_acc_comp.py --config /home/ubuntu/torc/git/ML/eos-road_lane2/configs/laneSegNet_configs/others/aws_laneSegNet_train_exp4-1_single_branch_ds_seg_infer.py --results_folder /home/ubuntu/torc/git/ML/eos-road_lane2/exp_stuff/20231106_LaneSegNet_Drivable_Surface_Only_OverFit --csv_file /home/ubuntu/ramana_test/shared_encoder/ds_overfit_train_report.csv --concat_fold /home/ubuntu/ramana_test/shared_encoder/overfit/
```

```
counter:2144
Average IOU: 0.5593393906072938
Median IOU: 0.6063591016668728
Number of images with IOU < 0.4: 386
Number of images with IOU >= 0.4: 1758
```


python script full
```
python ds_only_acc_comp.py --config /home/ubuntu/torc/git/ML/eos-road_lane2/configs/laneSegNet_configs/others/aws_laneSegNet_train_exp4-1_single_branch_ds_seg_infer.py --results_folder /home/ubuntu/torc/git/ML/eos-road_lane2/exp_stuff/20231106_LaneSegNet_Drivable_Surface_Only_Full --csv_file /home/ubuntu/ramana_test/shared_encoder/ds_full_train_report.csv --concat_fold /home/ubuntu/ramana_test/shared_encoder/full/
```

```
counter:5768
Average IOU: 0.33316096271513274
Median IOU: 0.2757601392594432
Number of images with IOU < 0.4: 3397
Number of images with IOU >= 0.4: 2371
```



python train
```
python others_LaneSegNet_drivable_surface_only_train.py
```

https://stackoverflow.com/questions/72988735/replacing-thc-thc-h-module-to-aten-aten-h-module
https://github.com/pytorch/pytorch/pull/65472
https://github.com/pytorch/pytorch/issues/72807
https://discuss.pytorch.org/t/question-about-thc-thc-h/147145/8
https://github.com/microsoft/DeepSpeed/issues/1584


https://github.com/open-mmlab/mmcv/pull/2216
https://github.com/open-mmlab/mmengine/blob/main/mmengine/dist/utils.py#L55
https://unix.stackexchange.com/questions/366553/tmux-is-causing-anaconda-to-use-a-different-python-source
https://github.com/open-mmlab/mmdetection/issues/10720

https://github.com/jupyter/notebook/issues/5014

`pip install yapf==0.40.1`.

- [ ] copy the data 
- [ ] create a sample data for overfit (shared encoder )
- [ ] run the inference modules



overfit again 
```
/home/ubuntu/ramana/eos-road_lane/scripts/laneSegNet_scripts/script_others/others_LaneSegNet_loss_overfitting.py
```


if keypoints are projected to ground 
then extending might not make sense 
- camera lane lines are not projected to bev
how is keypoint projected down to ground? 
fit a "local" plane and project keypoints
- will work with sloppy model
if the plane is curved? 


- lidar based road segmentation is not done
	- segmentation on entire lidar intensity image 
	- vectormapnet gives polygon output?? 

world modelling vs localizatoin model??

what is lane position? 


adjacent lane line coefficients using line fit or curve fit? 


why cant lidar see full road? 
- lidar data is fused I thought? 
- so surrounding lidar 

casten knoeppel 

some monte carlo based approach using radar 

interfaces more closely 
cameo as well 

need to go through architecture so that I can ask questions

```
who manages fisheye thing
what was previous calibration? 
how were models trained ? 
should they be trained again? 
```



multi head lane loss equially distributed? 

why cant loss and metric be same? 



need to test out running individual lane center inference 
- [ ] lane center
- [x] segmentation
- [ ] shared encoder 

need corresponding 
- [ ] configs 
- [ ] scripts 

let's start with segmentation

- [x] copy the inference batch data

- [x] benchmarking
- [x] need to check Rilwan's scripts 

- [ ] run only the relevant metrics
- [ ] understand the tegrastats output
- [ ] figure out that GMACs thingy
- [ ] run the inferences on all the models 
	- [ ] compare the metrics 


- [ ] visualization for the lane center onnx

onnx conversion 
- [x] scripts which create onnx models 
- [ ] run the lane center pipelines 
- [ ] run the visualizations
- [ ] run the metrics 
- [ ] upload the onnx models to s3

infer_shared.py has only infer code 
eval_shared.py has entire eval pipeline 

infer_shared_onnx.py which runs infereneces for onnx 

eval_shared.py should be same as the previous ones

1 wrapper script 
- [x] runs onnx conversion
- [ ] calls infer on pytorch
- [ ] calls infer on onnx 
- [ ] runs evals on both 
- [ ] ==compare both==
	- [ ] should report overall pytorch acc 
	- [ ] should report overall onnx acc


1 wrapper script 
- runs onnx conversion
- calls infer on pytorch and onnx 
- runs eavls on onnx
- runs evals on pytorch
- ==compare both==
	- should report overall pytorch acc 
	- should report overall onnx acc



hm torch.Size([40, 100])
off1x torch.Size([40, 100])
off1y torch.Size([40, 100])
off2x torch.Size([40, 100])
off2y torch.Size([40, 100])


- config
- scripts 
- metrics 
	- pytorch
	- onnx
- visuals 
	- pytorch 
	- onnx


finalize the code
- pictures 
- performance metrics

orin deliverables
- onnx models 
	- upload to S3



how should I go about it? 
- what is the goal? 
	- get a shared encoder between drivable surface segmentation and lane line keypoint detection, rather perform a multi task learning between them. this is so that all the camera features are extracted once and and used for further downstream processing for different objectives like lane line, drivable surface etc
	- merge the networks lane keypoint detection and some segementation
	- why segmentation? for post processing tasks like where all can the truck drive, 
		- `how does world modelling use this information?`
	- why lane keypoint detection? - check ganet paper
- what are the inputs?
	- cropped image with size 320x800
- what are the outputs and their formats? 
	- 5 head outputs
		- ego
		- left ego
		- right ego
		- left split ego
		- right split ego
	- 1 mask - 320 x 800
	- additional post processing for the outputs
- what are investigation results?
	- I was able to demonstrate shared encoder performance
- what did I do? 
	- I found out some models that corroborate how the multitask learning is generally done
		- YOLOPv2
		- Multinet
	- integrated the dataset
		- challenges, integrated json
		- mmcv integration
		- visualiser
	- fixed bugs in mmcv cuda 12 compatibility
	- tried two different models (baseline + shared FPN)
		- model1 - baseline
			- architecture
			- loss function
			- metrics 
				- seg IoU
				- Tusimple lane center accuracy
		- model2 - shared FPN
			- architecture
			- loss function
			- metrics
				- seg IoU
				- Tusimple lane center accuracy
	- showed the differences between them
	- converted them to onnx
	- benchmarked those models for performance
		- profiled with nsight nvidia 
		- ![[profiled_individual_components.png]]
		- ![[benchmarking_timers.png]]
	- tried with multiloss weighing but only did lit survey due to lack of time
		- using homoscedastic uncertainity - https://arxiv.org/pdf/1705.07115.pdf
		- ![[multi_loss.png]]
		- ![[multi_task_loss_torch.png]]

| Segmentation Type       | Training                 | Popular Architectures           | Loss Functions                             | Datasets                                     | Output Representations                     | Unsupervised Version                                                                              |  |  |  |
|-------------------------|--------------------------|---------------------------------|--------------------------------------------|----------------------------------------------|--------------------------------------------|---------------------------------------------------------------------------------------------------|--|--|--|
| Semantic Segmentation   | Supervised               | U-Net, FCN, DeepLab, PSPNet     | [[Loss Functions#^e669b4\|Cross-Entropy]] [[Loss Functions#^0ac185\|Dice Loss]] [[Loss Functions#^0ecb79\|Focal Loss]]                   | Cityscapes, PASCAL VOC, COCO                 | Pixel-wise class labels                    | Yes (e.g., DeepCluster, SEED, GANs)                                                               |  |  |  |
| Instance Segmentation   | Supervised               | Mask R-CNN, FCIS, PANet, YOLACT | Combined classification and mask loss      | COCO, Pascal VOC, ADE20K                     | Masks with instance-specific labels        | Yes (e.g., MaskJoint, D2-Net)                                                                     |  |  |  |
| Panoptic Segmentation   | Supervised               | PANet, UPSNet, Panoptic FPN     | Semantic segmentation loss + Instance loss | COCO, Cityscapes                             | Unified segmentation with stuff and things | Yes (e.g., UPSNet, Panoptic-DeepLab, ViP-DeepLab)                                                 |  |  |  |
| Superpixel Segmentation | Unsupervised (generally) | SLIC, QuickShift, EGBIS         | Compactness-based, Color similarity        | Berkeley Segmentation Dataset, MSRC, BSDS500 | Pixel clusters with similar attributes     | Yes (e.g., SLICO, SLIC0, Simple Linear Iterative Clustering)                                      |  |  |  |
| Depth Segmentation      | Supervised               | Monodepth, DeepDepth, MegaDepth | L1 or L2 loss on depth values              | NYU Depth, KITTI, Make3D                     | Depth maps                                 | Yes (e.g., Unsupervised Monocular Depth Estimation, Digging Into Self-Supervised Monocular Depth) |



# CPT 

22nd 

loop in Dave/

what about FTE? 
when can I get an estimate for that ? 
what are the chances of getting an approval



![[performance.png]]