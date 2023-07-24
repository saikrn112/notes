```
- extract synchronized frames, poses
- undistort the frames based on intrinsics
- run the segmentation on the undistorted frames
- run the depth and yaw estimation based on the segmentation - save the poses in the json
- run the script to generate the ground truth from wv_to_map.py
- plot the ground truth
- run the plotter for ground truth and depth and yaw estimation
```