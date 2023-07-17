story time 


depth and yaw estimation
- stereo - not so robust results due to lack of feature matches
- use ToF 
- first step was to verify if can even get depth and yaw estimations from point cloud 
	- show the wall thingy
- show without segmentation
	- the results 
- needed hires segmentation
	- why did I use Hires? 
		- 2 reasons
			- better image quality 
			- better FoV than stereo (show the comparison) --> motivation for us to use with current savloc as well
			- starling has only hires camera
	- instead of annotating I created a pipeline for annotation using SAM + GroundingDino
		- show some results (maybe comparsion between stereo yolov8)
		- 0.8 secs in nikola
- finally show the entire pipeline

somehow need to incorporate gt annotation with segmentation from SAM and 