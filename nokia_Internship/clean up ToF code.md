- [ ] should I use depth_image_proc tools ?
	- [ ] see why camera_info computed is 0 ? 
		- [ ] check if depth image point cloud is good or not 
- [ ] if I can send the image instead of `tof_pc`
- [ ] compute cpu load
	- [ ] if I am sending point_cloud computed by voxl
	- [ ] if I am sending tof_depth image instead + tof_camera_info
- [ ] compute network load 
	- [ ] if I am sending point_cloud computed by voxl
	- [ ] if I am sending tof_depth image instead + tof_camera_info


what will be beneficial from resume point of view? 
Research on depth from stereo in textureless and repetitive scenes using classical computer vision
improved segmentation pipeline for yolov8 
Integrated tof + hires estimation and improved localization pipeline
improved their VPS by 100% 
streamlined their ground truth estimation using worldviz



if I can get some numbers showing improvement, that will be good 
what numbers? 
currently we have a bag file 


let's create a metric for VPS 
number of possible corrections vs number of actual corrections 
out of actual corrections what should have been the actual value in each axis vs what is the actual correction 

need something to compare pose estimations, how about EPE ? 

