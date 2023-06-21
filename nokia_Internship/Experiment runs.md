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



## Main Dataset 2023.06.19

link to be generated

### Subdatasets
---
##### 2023-06-21-20-48-05

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
##### 2023-06-21-20-43-10

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
#### 2023-06-21-20-40-13

To Run analysis 
```
python run_analysis.py \
--dataset_path=/home/sai-pinnama/Project/depth_from_stereo/src/bag_replay/manual_dataset/2023-06-21-20-40-13/ \
--bag_file_name=2023-06-21-20-40-13.bag \
--remote_copy_location=/home/camloc/sai_analysis/manual_dataset/2023-06-21-20-40-13/ \
--drone=SKR1 \
--left_image_topic=/SKR1/stereo/left \
--right_image_topic=/SKR1/stereo/right \
--no_rotate \
--only_images \
--dry_run

```