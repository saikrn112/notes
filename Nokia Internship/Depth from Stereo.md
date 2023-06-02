Howard Huang and Yonni 

10 weeks


plan for 10 weeks 
DfS

depth from voxel 2
- time of flight

compare 
something to do with yaw
camera intrinsics 
and extrinsics 

qvio
savloc
fidloc

----


	repeating texture can have a bad stereo matching results




- [ ] need to update the confluence for weekly report kinda thing
- [ ] need to check howard as to what else is there in savloc improvement


what is happening right now? 
so I am getting depth by assuming some initial estimate. 
I need a metric to actually compare the depth I am getting
thing is, I am getting for points 
how do I compare the depth for points? 
and I also need to check how tolerant this algorithm is. 
as in if the inital depth is off by a few cms 



I have algo 1 which is dense depth, 
I thought we could use validate disparity function but looks like that is not usable 
another way is to check if there are good features using SIFT metrics. I need someway to correlate the sift features and dense depth. 
sift features could just be a check 


but for both of them I need a code which reads in left, right images and also reads in yaml file corresponding to that image for bounding box 

I need code to read yaml files 


ideas: 
1. use semantic tags as place recognition modules 
2. can we use bars itself as semantic tags ? 