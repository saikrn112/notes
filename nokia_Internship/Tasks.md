---

kanban-plugin: basic

---

## Backlog

- [ ] hires calibration on STR1
- [ ] FoV calculation with known box<br>- depends on hires calibration
- [ ] integrating segmentation with ToF PC<br>- use sequence ID for segmentation
- [ ] homography based yaw estimation
- [ ] rosbag remapping
- [ ] add videos to sharepoint
- [ ] explore FastSAM integration


## Progress

- [ ] savloc with hires vga<br>- [ ] watch Pratyush's recording
- [ ] color images from graybar<br>- [x] Mathew gave a script to download from MongoDB<br>- [x] share the dataset with Yoni<br>- [x] calibration for hires<br>- [x] segmentation for the images using previous Yolo<br>- [ ] segmentation using GroundingDino+SAM


## Pause

- [ ] [[Time of Flight]] ^0z3yh4
- [ ] transform and publish tof pc


## Done

- [ ] verify the distance from ToF<br>[distance charaterization](https://docs.google.com/spreadsheets/d/1Z4md_isMuGlsjRxvag8epsKHRNfii5nQlp1vZVF5CNQ/edit#gid=0)
- [ ] consolidate conversation with Michael - 2023.07.05 starling dataset
- [ ] enter timecard
- [ ] [[hires segmentation with current yolo]]


## archive

- [ ] vp_yaw estimation wrt ground truth bags<br>- [ ]  collect yaw + distance ground truth<br>- [ ]  run segmentation and the other pipeline
- [ ] graybar edges<br>- [ ] bag files for graybar - Yoni<br>- [ ] undistort and segment<br>- [ ] vp_yaw estimation
- [ ] how does drone compresss 4k to vga
- [ ] empty space detection using SAM+GroundingDino
- [ ] check optical flow between stereo pair
- [ ] gray bar hires images - run vp_yaw estimation




%% kanban:settings
```
{"kanban-plugin":"basic"}
```
%%