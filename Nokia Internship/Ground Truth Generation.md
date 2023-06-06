
## High level Overview

```
T_markers_to_map = T_wv_to_map @ marker_coords_in_wv
T_harness_to_map = F_markers_to_harness(markers_in_map)
T_map_to_harness = T_harness_to_map.inv
T_map_to_optical = T_harness_to_optical @ T_map_to_harness
```

`marker_coords_in_wv` : 
	marker coordinates in world viz
`T_wv_to_map` : 
	Transformation matrix from World Viz frame to Map frame [[Ground Truth Generation#^2efb60|calibration]] 
	- Following are transformed with it 
		- world viz markers
		- fiducial markers

`F_markers_to_harness` :
	3 markers pose --> Fit a plane -->  harness frame pose -- #TODO check this code

`T_harness_to_optical` : 
	Transformation matrix from Harness to camera optical frame  [[Ground Truth Generation#^2715fa|calibration]]
	- #TODO need to compute


## Calibrating markers and camera frame

^2715fa
```
-- 1
T_fiducial_to_map = T_wv_to_map @ (T_wv_to_fiducials).inv

-- 2
T_cam_to_fiducial = F_fiducial_pose(fiducials_image).inv
T_cam_to_map = T_fiducial_to_map @ T_cam_to_fiducial
T_map_to_cam = T_cam_to_map.inv

-- 3
T_markers_to_map = T_wv_to_map @ marker_coords_in_wv
T_harness_to_map = F_markers_to_harness(T_markers_to_map)

-- 4
T_harness_to_optical = T_map_to_cam @ T_harness_to_map
```

`T_wv_to_fiducials`  : 
	we already have this transformation
	
`F_fiducial_pose` :
	this is some opencv function --  #TODO check the rosbag for pose from fiducials



## Calibrating Map and World Viz frame

^2efb60
```
measure fiducials_in_wv 
measure fiducials_in_map using scanning or lasers
using ICP get the required transformation
```


----
Things that need to be checked with Howard 
in `f_getVoxlCamGtFromWv.m`
1. where do we get `startTimwWv` - is it just first timestamp
2. what is the wv1File format
