
## 2023.06.20

 [[Daily stuff^2023.06.20|daily stuff]]

yesterday I have collected some data. 
I need to update the calibration and run the pipeline
I think I have to add ground truth generation scripts as part of run_analysis so that I dont have to think too much all the time



for this dataset I need a different strategy to generate the ground truth
I need to extract the poses.json -- changes needed in the script 
transformation from this frame to baselink frame -- needed 
	need to identify which marker is the reference frame -- needed 
baselink frame to camera frame -- some other drone constants 
map frame transformation


To get
- reference marker 
- transformation from marker -> baselink -> optical frame 


if everything in map frame
- transformation between map frame and baselink
- or relative marker pose 

