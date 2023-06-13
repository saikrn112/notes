### 2023.06.05
only meetings
Discussed briefly with Yoni on how we can use points to get full pose
using something like PnP
I will check out ground truth generation now 


### 2023.06.06

- script which extracts frames and corresponding timestamps in sequence
- when I do rosbag replay I will pump it through synchronizer, subscribe and save -- easiest to do 
	- saver will create a csv with following fields
	- `frame_id, mk1_pose, mk2_pose, mk3_pose, cam_pose`
	- otherwise I need to something like Howard did 
		- save the images, sequences and their timestamps in csv
		- find time correspondences between images based on the lowest set of images
		- find time correspondences between ref image and wv data
		- save that as the above csv format

- get world viz information with only one marker
- hopefully one of the axis is aligning with the depth and get difference 
	- if not I need some transformation that makes it a difference (`T_map_to_align`)
- plot depth vs time for both ground truth and estimated

- get 6DoF pose from world viz markers 
- plot yaw vs time for both ground truth and estimated


## 2023.06.07

need the output of the savloc code


in the metrics, 
number of vertical bars seen and number of horizontal bars seen 
fiducial loc 

logical layer in savloc should be abstracted out from the batch,dev,rest modes

- need to create another folder / branch with evaluation metrics 

## 2023.06.08

need to identify why sometimes the plane that was fit is bad
could be related to dispersing the points more and more 

## 2023.06.09

- got scripts from Mouhaymen on the ground truth testing 
- need to add Howard's logic for yaw estimation into 


omnigraph 
- very small detail - if we can control the stereo extrinsics with respect to each other to simulate different voxel configurations

- standardized and pushed the code to gitlab
- looking at autodistill for few mins

## 2023.06.12
- need to mail people for virtual meet up 
| Group 1 | Sai Pinnama Raju | sai.pinnama_raju@nokia.com | Luke McDermott | luke.mcdermott@nokia.com | Jiangqi Hu | jiangqi.hu@nokia.com | Muhammad Karam | muhammad.shehzad@nokia.com | Haseeb | muhammad.haseeb@nokia.com |
|---------|------------------|----------------------------|----------------|--------------------------|------------|----------------------|----------------|----------------------------|--------|---------------------------|



---
- install matlab and run gt script
- ~~catch up with Yoni on yaw estimation~~

need to update on what I have done so far in presentation 
- block matching
- semi global block matching
- fundamental matrix based approach for feature correspondences (without heuristic)

line/plane fit criterion 


call with Yoni
- see if we can get rid of projection from initial depth for matching correspondences
- start with undistorted images
- see how the dispartiy range changes based on the z assumption
- simpler assumption : take out the projection based filter by assuming that roll is 0
- slide show: to explain the algorithm; ,clear and concise;
- ask Jim /Daniel for Friday stereo pair based autonomous flights

call with Prasanth
- ~~Yaw estimates~~
- slow it is 
- ~~check with Jim about running matlab code~~
- updates from Yoni on algorithm
- ~~week extension for internship?~~
- It's not part of internship but discussed about some software upgrades with Michael to streamline deployment - responsibilities like Pratyush
- ~~autodistill for annotation (privacy concerns)~~ -- 5 or 10 images should work! 


last Monday 2023.06.05
![[IMG_20230605_134534.jpg]]

## 2023.06.13

- onboarding 
- think about final summary report/presentation
- schedule a virtual meet
- run matlab scripts of Jim 



call with Yoni
- see if we can get rid of projection from initial depth for matching correspondences
- start with undistorted images
- see how the dispartiy range changes based on the z assumption
- simpler assumption : take out the projection based filter by assuming that roll is 0
- slide show: to explain the algorithm; ,clear and concise;
- ask Jim /Daniel for Friday stereo pair based autonomous flights
- remove the shows 
- decrease number of points 
- minimal mask and distance between points ( decrease the width of shelf)
- segmentation is the priority

---

segmentation 
- camera tilt 

pre flight checks -- ask publicly 
- check if stereo is good 
- imu is good 
- sensor suit tests 


stereo right image training 
data augmentation 
- cropping 
- resizing 
- rotating 
- random patches 
- noise 

something about boundary detection 



--- 
annotation 
acto  for labelling 
- need code to convert acto format to yolo trainable format 
---


presentation 
- problem at hand - what are we trying to solve 
	- take it from howard's slides from minutes of meeting etc 
- approach 1 
	- opencv variant 
- approach 2 
	- sparse depth variant
- approach 3 
	- more hybrid approach 
- current algo 
	- what all elements from flow chart 
- next steps 
	- more robust 
- evaluation
	- run it on MH flights 
	- get the ground truth data 
	- run howard's code 
tell that feature matching was highly sensitive to the calibration 



totally 3 presentations 
- 11th July 
- 28th July