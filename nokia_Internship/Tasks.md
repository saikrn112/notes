---

kanban-plugin: basic

---

## Backlog

- [ ] enter timecard
- [ ] hires calibration on STR1
- [ ] FoV calculation with known box<br>- depends on hires calibration
- [ ] integrating segmentation with ToF PC<br>- use sequence ID for segmentation
- [ ] homography based yaw estimation
- [ ] rosbag remapping


## Progress

- [ ] transform and publish tof pc


## Pause

- [ ] [[Time of Flight]] ^0z3yh4
- [ ] vp_yaw estimation wrt ground truth bags<br>- [ ]  collect yaw + distance ground truth<br>- [ ]  run segmentation and the other pipeline


## Done

- [ ] verify the distance from ToF<br>[distance charaterization](https://docs.google.com/spreadsheets/d/1Z4md_isMuGlsjRxvag8epsKHRNfii5nQlp1vZVF5CNQ/edit#gid=0)
- [ ] consolidate conversation with Michael - 2023.07.05 starling dataset
- [ ] color images from graybar<br>- Mathew gave a script to download from MongoDB
- [ ] [[hires segmentation with current yolo]]


## archive

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