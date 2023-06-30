## Steps to analyse 
```
1. Take a frame which has good segmentation on both left and right
2. manually calculate what the depth should be or a different script which just takes in left/right stereo pair and bounding box and gives initial depth
3. get ground truth inital depth for that frame of interest 
4. note down values here https://docs.google.com/spreadsheets/d/1ySSU5L8hPuwg2qroAT9QrLC0ga53-PejeBYJzPP56To/edit?usp=sharing
5. 
```


## Main dataset MH 2023.06.13
https://teams.microsoft.com/_#/apps/d7958adf-f419-46fa-941b-1b946497ef84/sections/MyNotebook


### Subdatasets
----
##### WV_test1

To Run analysis 
```
python run_analysis.py \
--dataset_path=/home/sai-pinnama/Project/depth_from_stereo/src/bag_replay/dataset6/AIMS013/WV_test1/ \
--bag_file_name=2023-06-14-15-28-21.bag \
--remote_copy_location=/home/camloc/sai_analysis/dataset6/AIMS013/WV_test1/ \
--drone=SKR3 \
--left_image_topic=/SKR3/stereo/left \
--right_image_topic=/SKR3/stereo/right \
--dry_run

```

##### Problems 
- left stereo is smudged 
- need to calibrate again 

Frame of interest - frame 201
![[frame201.png]]

---
---

## Main Dataset 2023.06.17

[link](https://nokianam.sharepoint.com/sites/BellLabsAeroFarmsInternal/Shared%20Documents/Forms/AllItems.aspx?csf=1&web=1&e=CO3641&cid=69278ce7%2Da8c5%2D4905%2D8efb%2D187b82e31733&RootFolder=%2Fsites%2FBellLabsAeroFarmsInternal%2FShared%20Documents%2FCustomer%20Use%20Cases%2FWarehouse%20Monitoring%2FGraybar%2FGraybar%2DCranbury%2DNJ%2F2023616%5Fvisit&FolderCTID=0x01200014CFCFA45E696148B6EAC454AC4969A3)

---
---

## Main Dataset 2023.06.19

[link]([6_19](https://nokianam.sharepoint.com/:f:/s/BellLabsAeroFarmsInternal-MediumDrone/EpH2ZqMlawRIpM2s9JPwoQwBx2gpoCIDlJh-9F7brOUiVw?email=sai.pinnama_raju%40nokia.com&e=Ln5RYJ))

To Run analysis 
```
python run_analysis.py \
--dataset_path=/home/sai-pinnama/Project/depth_from_stereo/src/bag_replay/2023.06.19/ \
--bag_file_name=2023-06-19-16-56-30.bag \
--remote_copy_location=/home/camloc/sai_analysis/2023.06.19/ \
--drone=SKR1 \
--left_image_topic=/SKR1/stereo/left \
--right_image_topic=/SKR1/stereo/right \
--no_rotate \
--dry_run


```

---
---


## Main Dataset 2023.06.21

link to be generated

### Subdatasets
---
##### 2023-06-21-20-48

To Run analysis 
```
python run_analysis.py \
--dataset_path=/home/sai-pinnama/Project/depth_from_stereo/src/bag_replay/manual_dataset/2023-06-21-20-48-05/ \
--bag_file_name=2023-06-21-20-48-05.bag \
--remote_copy_location=/home/camloc/sai_analysis/manual_dataset/2023-06-21-20-48-05/ \
--drone=SKR1 \
--left_image_topic=/SKR1/stereo/left \
--right_image_topic=/SKR1/stereo/right \
--no_rotate \
--only_images \
--dry_run

```


----
##### 2023-06-21-20-43

To Run analysis 
```
python run_analysis.py \
--dataset_path=/home/sai-pinnama/Project/depth_from_stereo/src/bag_replay/manual_dataset/2023-06-21-20-43-10/ \
--bag_file_name=2023-06-21-20-43-10.bag \
--remote_copy_location=/home/camloc/sai_analysis/manual_dataset/2023-06-21-20-43-10/ \
--drone=SKR1 \
--left_image_topic=/SKR1/stereo/left \
--right_image_topic=/SKR1/stereo/right \
--no_rotate \
--only_images \
--dry_run

```


----
#### 2023-06-21-20-40

To Run analysis 
```
python run_analysis.py \
--dataset_path=/home/sai-pinnama/Project/depth_from_stereo/src/bag_replay/manual_dataset_2023.06.21/2023-06-21-20-40/ \
--bag_file_name=2023-06-21-20-40-13.bag \
--remote_copy_location=/home/camloc/sai_analysis/manual_dataset_2023.06.21/2023-06-21-20-40/ \
--drone=SKR1 \
--left_image_topic=/SKR1/stereo/left \
--right_image_topic=/SKR1/stereo/right \
--no_rotate \
--only_images \
--dry_run

```

for masks which are horizontal the yaw output is not stable

----
---
## Main Dataset 2023.06.23



### Subdatasets
---
##### Test1 --> 2023-06-23-16-07


this test 38 cm 
no yaw

To Run analysis 
```
python run_analysis.py \
--dataset_path=/home/sai-pinnama/Project/depth_from_stereo/src/bag_replay/manual_dataset_2023.06.23/2023-06-23-16-07/ \
--bag_file_name=2023-06-23-16-07-27.bag \
--remote_copy_location=/home/camloc/sai_analysis//manual_dataset_2023.06.23/2023-06-23-16-07/ \
--drone=SKR1 \
--left_image_topic=/SKR1/stereo/left \
--right_image_topic=/SKR1/stereo/right \
--prefix="brute_force" \
--no_rotate \
--only_images \
--dry_run
```

----
##### Test2 --> 2023-06-23-16-19


this test 50 cm 
no yaw

To Run analysis 
```
python run_analysis.py \
--dataset_path=/home/sai-pinnama/Project/depth_from_stereo/src/bag_replay/manual_dataset_2023.06.23/2023-06-23-16-19/ \
--bag_file_name=2023-06-23-16-19-07.bag \
--remote_copy_location=/home/camloc/sai_analysis//manual_dataset_2023.06.23/2023-06-23-16-19/ \
--drone=SKR1 \
--left_image_topic=/SKR1/stereo/left \
--right_image_topic=/SKR1/stereo/right \
--prefix="brute_force" \
--no_rotate \
--only_images \
--dry_run
```


----
##### Test3 --> 2023-06-23-16-25


this test 85 cm 
no yaw

To Run analysis 
```
python run_analysis.py \
--dataset_path=/home/sai-pinnama/Project/depth_from_stereo/src/bag_replay/manual_dataset_2023.06.23/2023-06-23-16-25/ \
--bag_file_name=2023-06-23-16-25-15.bag \
--remote_copy_location=/home/camloc/sai_analysis//manual_dataset_2023.06.23/2023-06-23-16-25/ \
--drone=SKR1 \
--left_image_topic=/SKR1/stereo/left \
--right_image_topic=/SKR1/stereo/right \
--prefix="staggered_masks" \
--no_rotate \
--only_images \
--dry_run
```

NO segmentation 

----
##### Test5 --> 2023-06-23-16-33


this test 51 cm 
no yaw

To Run analysis 
```
python run_analysis.py \
--dataset_path=/home/sai-pinnama/Project/depth_from_stereo/src/bag_replay/manual_dataset_2023.06.23/2023-06-23-16-33/ \
--bag_file_name=2023-06-23-16-33-53.bag \
--remote_copy_location=/home/camloc/sai_analysis//manual_dataset_2023.06.23/2023-06-23-16-33/ \
--drone=SKR1 \
--left_image_topic=/SKR1/stereo/left \
--right_image_topic=/SKR1/stereo/right \
--prefix="staggered_masks" \
--no_rotate \
--only_images \
--dry_run
```


----
---


## Main Dataset 2023.06.30


### Subdatasets
---
##### 2023-06-30-19-08

0.54

To Run analysis 
```
python run_analysis.py \
--dataset_path=/home/sai-pinnama/Project/depth_from_stereo/src/bag_replay/2023.06.30/stereo/2023-06-30-19-08/ \
--bag_file_name=2023-06-30-19-08-05.bag \
--remote_copy_location=/home/camloc/sai_analysis/2023.06.30/stereo/2023-06-30-19-08/ \
--drone=SKR1 \
--left_image_topic=/SKR1/stereo/left \
--right_image_topic=/SKR1/stereo/right \
--no_rotate \
--only_images \
--dry_run
```

frame 73-109,503-543,634-699


331,173

