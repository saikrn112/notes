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