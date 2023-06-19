
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
--left_image_topic=/SKR3/stereo/left \
--right_image_topic=/SKR3/stereo/right \
--dry_run

```

##### Problems 
- left stereo is smudged 
- need to calibrate again 

---

## Main Dataset 2023.06.17

[link](https://nokianam.sharepoint.com/sites/BellLabsAeroFarmsInternal/Shared%20Documents/Forms/AllItems.aspx?csf=1&web=1&e=CO3641&cid=69278ce7%2Da8c5%2D4905%2D8efb%2D187b82e31733&RootFolder=%2Fsites%2FBellLabsAeroFarmsInternal%2FShared%20Documents%2FCustomer%20Use%20Cases%2FWarehouse%20Monitoring%2FGraybar%2FGraybar%2DCranbury%2DNJ%2F2023616%5Fvisit&FolderCTID=0x01200014CFCFA45E696148B6EAC454AC4969A3)

#### Sub dataset test 2


```
python run_analysis.py \
--dataset_path=/home/sai-pinnama/Project/depth_from_stereo/src/bag_replay/GB_616_test2/ \
--bag_file_name=2023-06-16-10-06-30.bag.active \
--remote_copy_location=/home/camloc/sai_analysis/GB_616_test2/ \
--left_image_topic=/SKR3/stereo/left \
--right_image_topic=/SKR3/stereo/right \
--dry_run
```