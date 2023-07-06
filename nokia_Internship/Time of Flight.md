need to integrate time of flight to the SAVLoc enhancement 

configuration [link](https://docs.modalai.com/voxl2-camera-configs/#c6---hires--tof--tracking)
[tof sensor dataset](https://docs.modalai.com/M0040/)
[tof sensor guide](https://docs.modalai.com/voxl-tof-sensor-user-guide/#viewing-the-data-with-ros)
[hires camera guid](https://docs.modalai.com/voxl-hi-res-sensor-user-guide/)
[hires imx214 datasheet](https://docs.modalai.com/M0025/)
[hires imx412 datasheet](https://www.modalai.com/products/mdk-m0061-1?variant=45119396413744)

![[sensor_configuration.png]]

- [ ] update the powerpoint with initial results, in plots maybe
	- [x] manually get the masks from GroundingDino + SAM (not many images)
- [ ] understand how ToF works with IR
	- [ ] undistortion for ToF
- [ ] integrate rgb + depth = rgb pointcloud
	- [ ] should I do more research on this integration? 
		- [ ] this starts from calibration related papers
	- [ ] calculate hires to tof extrinsics 
	- [ ] assume some focal length to the hires 
	- [ ] get focal length of the ToF 
	- [ ] make sure to match resolution
	- [ ] compute the math and get the RGB point cloud for verification
- [ ] integrate that with rgb segmentation