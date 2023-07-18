need to integrate time of flight to the SAVLoc enhancement 

configuration [link](https://docs.modalai.com/voxl2-camera-configs/#c6---hires--tof--tracking)
[tof sensor dataset](https://docs.modalai.com/M0040/)
[tof sensor guide](https://docs.modalai.com/voxl-tof-sensor-user-guide/#viewing-the-data-with-ros)
[hires camera guid](https://docs.modalai.com/voxl-hi-res-sensor-user-guide/)
[hires imx214 datasheet](https://docs.modalai.com/M0025/)
[hires imx412 datasheet](https://www.modalai.com/products/mdk-m0061-1?variant=45119396413744)

![[sensor_configuration.png]]

- [x] update the powerpoint with initial results, in plots maybe
	- [x] manually get the masks from GroundingDino + SAM (not many images)
- [x] understand how ToF works with IR
	- [x] undistortion for ToF
- [x] integrate rgb + depth = rgb pointcloud
	- [x] should I do more research on this integration? 
		- [ ] this starts from calibration related papers
	- [x] calculate hires to tof extrinsics 
	- [x] assume some focal length to the hires 
	- [x] get focal length of the ToF 
	- [x] make sure to match resolution
	- [x] compute the math and get the RGB point cloud for verification
- [x] integrate that with rgb segmentation

rotation extrinsics [[ex_roll.pdf]]



- depth characterization
	- stabilze at known depths 




