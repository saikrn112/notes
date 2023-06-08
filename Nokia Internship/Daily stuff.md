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

need to identify why l