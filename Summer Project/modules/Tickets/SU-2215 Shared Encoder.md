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


- [ ] merge data files
- [ ] make a copy of it in shared_encoder 
- [ ] create a new set in the shared_encoder 
- [ ] so that gong is not blocked

- [ ] make the same changes as yesterday in new branch
- [ ] make sure they are working with new sample? 
- [ ] 