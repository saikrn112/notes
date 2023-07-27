
## 2023.06.20

 [[Daily stuff^2023.06.20|daily stuff]]

yesterday I have collected some data. 
I need to update the calibration and run the pipeline
I think I have to add ground truth generation scripts as part of run_analysis so that I dont have to think too much all the time



for this dataset I need a different strategy to generate the ground truth
I need to extract the poses.json -- changes needed in the script 
transformation from this frame to baselink frame -- needed 
	need to identify which marker is the reference frame -- needed 
baselink frame to camera frame -- some other drone constants 
map frame transformation


To get
- reference marker 
- transformation from marker -> baselink -> optical frame 


if everything in map frame
- transformation between map frame and baselink
- or relative marker pose 


invert z coordinates to make the system right handed


  

1. need to get translation from marker to camera optical frame
	1. check initial coordinates 
2. need to get rotation from marker to camera optical frame

---
Local tower shelf fid0 coords in world viz frame:  
-3.125  
0.051  
0.596

[12:20 PM] Sai Pinnama Raju (Nokia)

config 123:  
marker 1 --- -3.125,0.242,0.183

[12:21 PM] Sai Pinnama Raju (Nokia)

config 132:  
marker 1 -- -3.128, 0.238, 0.182

[12:22 PM] Sai Pinnama Raju (Nokia)

config 213: marker 2 -- -3.096, 0.283,0.051

[12:23 PM] Sai Pinnama Raju (Nokia)

config 231: marker 2-- -3.095, 0.284, 0.051

[12:24 PM] Sai Pinnama Raju (Nokia)

config 312: marker 3- -3.123, 0.311, -0.006

[12:25 PM] Sai Pinnama Raju (Nokia)

config 321: marker 3

from first few estimates 

"x": -3.122958820408644,

"y": 0.23811468708938605,

"z": 0.1516606826838719

---

for tomorrow's presentation I need to tell about the standardized way to collect the ground truth 
- I can create a document maybe
- show some results of plots that I got 


for code I need to read the ground truth as well so that I can plot in the image

I can show some analysis that finer estimate is indeed improving the estimate


if we can 

plot the transformed Z vs X ? 


---


manual flight 
with protractor 

- fix a table 
- keep the drone
- measure the drone distance using measuring scale 
- measure the drone using protractor 
- maybe draw the lines 


video start
- take snapshots of videos 100 frames each 
- linspace (start=-20, end=20, step=4)

measuring tape 
protractor

figuring out rest of the internship week 


```
voxl-logger
```

once the data is copied I need to run the script and generate depth and yaw estimates 


## 2023.06.22

improve matching 

Custom matching algorithm 

## 2023.06.23

final day of the week 
I can present the results of bruteforce+heuristic vs heuristic matching


let's take another rosbag from SKR1 again 
this time no tilt 
pure distance measurement 


agenda for the meeting 
- present the results
- say that it's giving what we want 80-90times out of 100 
- but more concerned about outliers 
- custom matching algorithm gives more weightage to initial depth 
- previous algorithm gives

suggestions on where the savloc is going? is DfS gonna add any value? 
I want other opionions so that I can take more generalized call 


final comments 
- get better test 
- geometric test 
- debug the code with Yoni

## 2023.06.26
doing some [[Depth discrepancy analysis]] 
found that get optimal camera is the reason for offset
I can try generating the same plot again by removing the offset
- need to ask Yoni

generated the plots on friday 
![[staggered_masks_wo_optimal_mtx_distance_to_shelf.png]]

now the estimates are definitely closer to the expected values 

next step:
- select two feature correspondences 
- and manually triangulate 
[[Triangulation analysis]]


## 2023.06.28

- savloc should be ros
- capture savloc topic separately
- capture savloc filtered
- manual handling to evaluate the savloc
- metric for savloc evaluation
- plotting standard 
- evaluate savloc core algorithm standalone instead of full information

## 2023.06.29

ToF FoV and granularity



patch in the horizontal segment 




## 2023.06.30

![[pointer_left.png]]
>[!info] left_loc
loc : 327,178

![[laser_pointer_right.png]]
>[!info] right_loc
loc : 242, 178

disparity = 


## 2023.07.03
[[Daily stuff#^6b528d]]
too many discussions and brain is super confused on what the next steps are 



## 2023.07.05

no presentation today since I am working on something new 

I have two options, 
I can either use the current Yolov8 segmentation or play around with autodistill and other functionalities 

- in the meanwhile I can try playing around with graybar edge detection 


## 2023.07.06

- [ ] get starling1 
- [ ] understand how to operate it for calibration
- [ ] calibrate hires camera on starling1

what does Yoni want me to do ? 
we discussed 2 different ideas
- lookup table idea 
- homography based idea 

both of them need good segmentation

what does Nilesh want? 
- he wants me to run current Yolo network with grayscale to see how the segmentation is 


## 2023.07.10

- [ ] hires image configuration preview on drone 
- [x] rosbag topic pruning
- [ ] rosbag topic addition 1.0 
- [ ] rosbag topic addition savloc 

## 2023.07.12

image and tof info are synchronized 
now I need to integrate the segmentation mask with tof info 
first ensure they both are in same focal length

for presentation:
- give context about why stereo cannot be used due to lack of robust features 
- exploring two threads 
	- `vp` estimation - depends on the reliable edges -- depends on the 
	- ToF integration - show the tof pipeline 

Hey everyone, 

I am looking at the camera to harness transformation now. to make sure we are in same page I will outline how I am planning to compute this transformation. 

1. Align one of the markers on the drone to worldviz origin 
2. get other two measurements



## 2023.07.14

ok so I can publish the rgb_camera info 
i need to publish the depth_camera info 
depth image rectified 


## 2023.07.16

all I want is depth image registered in the rgb frame 
for this I am doing opposite, 
taking existing pointcloud in tof frame, convert it to depth_image 
and then pass this depth_image to the register frame so that will transform everything to rgb frame


then hopefully the pointcloudxyzrgb will work 