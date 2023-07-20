---

kanban-plugin: basic

---

## Backlog

- [ ] check if SAM gives good estimates for vertical estimates
- [ ] hires underneath to current yolov8
- [ ] FoV calculation with known box<br>- depends on hires calibration
- [ ] homography based yaw estimation
- [ ] explore FastSAM integration
- [ ] checkout Karter's Thesis
- [ ] save plots for ToF depth and yaw estimation
- [ ] documentation of ToF work
- [ ] Robustly estimate depth and yaw from ToF


## In Progress

- [ ] [[ToF Integration next steps]]
- [ ] [[compute cpu load metrics]]


## Pause

- [ ] color images from graybar<br>- [x] Mathew gave a script to download from MongoDB<br>- [x] share the dataset with Yoni<br>- [x] calibration for hires<br>- [x] segmentation for the images using previous Yolo<br>- [ ] segmentation using GroundingDino+SAM


## Done

- [ ] [[Camera Calibration]]<br>- [x]  SKR1 Hires <br>- [x]  SKR1 tracking<br>- [x]  SKR3 Hires<br>- [x]  SKR3 tracking<br>- [x]  check with team for drones
- [ ] hires preview stream with rectangular aspect ratio
- [ ] camera to harness transformation<br>- [x] code <br>- [x] euler angles -- not required<br>- [x] translation to left camera from 2nd marker
- [ ] [[Time of Flight]] ^0z3yh4
- [ ] [[showcase presentation]]
- [ ] integrating segmentation with ToF PC<br>- use sequence ID for segmentation
- [ ] camera wrapper
- [ ] transform and publish tof pc
- [ ] [[hires calibration on SKR1]]
- [ ] [[hires calibration on STR1]]
- [ ] verify the distance from ToF<br>[distance charaterization](https://docs.google.com/spreadsheets/d/1Z4md_isMuGlsjRxvag8epsKHRNfii5nQlp1vZVF5CNQ/edit#gid=0)
- [ ] consolidate conversation with Michael - 2023.07.05 starling dataset
- [ ] enter timecard
- [ ] [[hires segmentation with current yolo]]


## archive

- [ ] add videos to sharepoint
- [ ] savloc with hires vga<br>- [x] watch Pratyush's recording<br>- [x] extract the 10th july dataset<br>- [ ] create json topics from `extrac_rosbag.py`
- [ ] vp_yaw estimation wrt ground truth bags<br>- [ ]  collect yaw + distance ground truth<br>- [ ]  run segmentation and the other pipeline
- [ ] rosbag remapping
- [ ] graybar edges<br>- [x] bag files for graybar - Yoni<br>- [x] undistort and segment<br>- [ ] vp_yaw estimation
- [ ] how does drone compresss 4k to vga
- [ ] empty space detection using SAM+GroundingDino
- [ ] check optical flow between stereo pair
- [ ] gray bar hires images - run vp_yaw estimation




%% kanban:settings
```
{"kanban-plugin":"basic"}
```
%%