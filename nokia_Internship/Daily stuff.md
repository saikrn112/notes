## 2023.06.05
only meetings
Discussed briefly with Yoni on how we can use points to get full pose
using something like PnP
I will check out ground truth generation now 


## 2023.06.06

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

---

stereo right image training 
data augmentation 
- cropping 
- resizing 
- rotating 
- random patches 
- noise 
---
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
---



totally 3 presentations 
- 11th July 
- 28th July

## 2023.06.14
- something wrong with right mask numbers
- Bharat about extrinsics 

call with Yoni
- see if we can get rid of projection from initial depth for matching correspondences
- start with undistorted images
- see how the dispartiy range changes based on the z assumption
- simpler assumption : take out the projection based filter by assuming that roll is 0
- ask Jim /Daniel for Friday stereo pair based autonomous flights
- remove the shows 
- decrease number of points 
- minimal mask and distance between points ( decrease the width of shelf)
- segmentation is the priority

Let's focus on the ground truth today
- only z axis, I had a AI chat to write the data to json 
- after that I need to apply the transformation from world viz to map frame -- need to run that IcpFady for that 


## 2023.06.15
- checked the markers and transformation given by Howard
- I want to streamline the process by removing the bottlenecks 
	- I will first run with Howards outputs on dataset4
I need segmentation outputs for AIMS dataset 

I need to check ground truth estimations for previous dataset using Howard's transformation
- generate

## 2023.06.18

- worked on implementing the pipeline
- stuck at camera extrinsics of SKR3 
- need to get initial pose from /SKR3/odom

## 2023.06.19

- check mails to analyse today's scope 
- pay yagmur
- follow up with Daniel about stereo extrinisics 
- some scripts from Yoni
I did speak with Howard very briefly 

--- 
I used the dataset2 to run some stuff 
that entire pipeline creates some jsons and images 
jsons 
- poses.json - ground truth directly from bag file
- transformed.json - after wv_to_map transformation
- left/right_out.json - segmentaiton bounding boxes 
- yaw_and_depth.json - estimated yaw and depth to shelf 

plots 
- depth_per_frame - ground truth using transformed.json
- depth_plot - ground truth using transformed.json 
- distance_to_shelf_per_frame.json - estimated distance to shelf
- trajectory_plot.png - ground truth using transformed.json
- yaw_per_frame.png - estimated yaw per frame

do I need to make any code changes? 
- not right now, I will just run the yaw with latest extrinsics and data 

1-1 with Prasanth: 
- ~~I will decide by 12PM not now~~
- ~~ask about presentation and what to do for next one~~
- note down pre flight checks (health)
- post flight checks (bag files, stereo images, distortion etc)

-> Mouhymen document ground truth collection and processing
-> SIM dataset for algorithm correctness


## 2023.06.20

- ~~schedule weekly sync meeting~~
- ~~check mails to analyse today's scope ~~
- ~~got the ground truth finally~~
- think about what to present for tomorrow's meeting
	- sync with Pratyush about depth
	- issues with depth and calculation
- pay yagmur
 
-> Mouhymen document ground truth collection and processing
-> SIM dataset for algorithm correctness


call with Yoni
- see if we can get rid of projection from initial depth for matching correspondences
- start with undistorted images
- see how the dispartiy range changes based on the z assumption
- simpler assumption : take out the projection based filter by assuming that roll is 0
- ask Jim /Daniel for Friday stereo pair based autonomous flights
- remove the shows 
- decrease number of points 
- minimal mask and distance between points ( decrease the width of shelf)
- segmentation is the priority

## 2023.06.21

presentation today 
- ground truth generation
- plots 
- evaluation framework

next steps


manually check distance compare with worldviz 

## 2023.06.22

- update the experiment runs with pictures I took in ipad
- use the segmentation masks 
- ~~add initial depth estimate in the plot (yellow)~~
- verify the math for perpendicular distance to plane
- ~~working on custom matching algorithm ~~

- are left tilt's correct in general? 
- pay yagmur
 
-> Mouhymen document ground truth collection and processing
-> SIM dataset for algorithm correctness


call with Yoni
- see if we can get rid of projection from initial depth for matching correspondences
- start with undistorted images
- see how the dispartiy range changes based on the z assumption
- simpler assumption : take out the projection based filter by assuming that roll is 0
- decrease number of points 
- minimal mask and distance between points ( decrease the width of shelf)

## 2023.06.26
today is the day where I fully debug the code and prove Yoni once and for all that feature matching is super crucial

- update the experiment runs with pictures I took in ipad
- use the segmentation masks 
- verify the math for perpendicular distance to plane

- are left tilt's correct in general? 
- pay yagmur

Yoni
- see if we can get rid of projection from initial depth for matching correspondences
- start with undistorted images
- see how the dispartiy range changes based on the z assumption
- simpler assumption : take out the projection based filter by assuming that roll is 0
- decrease number of points 
- minimal mask and distance between points ( decrease the width of shelf)


## 2023.06.28

meetings 
discussed with Nilesh and Pratyush about different things that happened 

## 2023.06.30

collected some datasets 
- laser pointer with stereo on SKR1 
- ToF with high res on STR1



## 2023.07.03

^6b528d

spoke with Yoni on next steps 
- ask Michael about hires being captured in rosbags for SKR 
- check graybar stereo pair images for edge detection
- work on ToF 

spoke with Michael about hires
- if we want VGA resolution for savloc we can try 

spoke with Nilesh 
- use the hires we captured from the starlink 
- run the segmentation pipeline 
- and run the savloc pipeline 

idea is somehow (quantitatively) say that color and 4k images are providing better information for savloc to work - doesnt matter if it is geometric_2d or vanishing point method 

send this information to Yoni (what I discussed with Michael)

## 2023.07.05
extracted hires images from rosbags


## 2023.07.06
hires segmentation with current Yolo

## 2023.07.07
graybar visit
depth characterization [link](https://docs.google.com/spreadsheets/d/1Z4md_isMuGlsjRxvag8epsKHRNfii5nQlp1vZVF5CNQ/edit#gid=0)
tof extrinsics transformation


## 2023.07.10
hires images for Yoni

## 2023.07.11
hires calibration SKR1
apply it on skr4 and get plots from pratyush's code 

SKR1 drone
```
Matrix
[333.4551103839864, 0, 314.6164849327728;
 0, 332.9890750027212, 235.5810911245538;
 0, 0, 1]
Distortion
[0.03400399196418848;
 -0.03000010086997222;
 -0.001106385385495436;
 0.0005396856541603922;
 0]
```

STR1 drone
```
Matrix
[665.8262901483788, 0, 323.3443829398281;
 0, 667.4129291671338, 342.4803441157025;
 0, 0, 1]
Distortion
[0.08076263723665855;
 -0.157181686463221;
 0.002255317079462612;
 0.0001581278385476036;
 0]

```