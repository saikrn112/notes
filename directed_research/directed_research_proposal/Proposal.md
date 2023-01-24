


Problems in getting "Robust" Visual odometry
Robustness of visual odometry can be categorized into following classes 
- robust towards faulty or partial sensor measurements 
- tracking across different environment and motion conditions (high speed)
- feature tracking across occlusions
- close to real time as possible
- identify dynamic obstacles to prevent error corrections
- less or no drift over a long run
- cheap to compute on smaller robots and devices

In this project, I want to primarily focus on points 2,4,5 and later improve on other items

focus on traditional works:
- mention about ORB-SLAM on how it is uses geometric losses
- mention about DSO on how it is photometric losses

focus on DNN works
- mention PoseNet - one of the first ones to use DCCN for camera pose estimation
- salientDSO - how it is trying to be salient by adding salience to the photometric 

Related work
WriteUp strategy:
what is the strategy in write up? 
in related work section, I covered classical approaches in visual odometry 
I need to cover how deep networks are being used? 
- it is used for extracting semantic informations - salientDSO 
- it is also used for end to end position estimation - DeepVO
- unsupervised end to end position estimation - UnDeepVO
- it is used only for dynamic feature extraction - RGBD
- 

I can also cover how inertial sensors are used along with the deep learning -- rather I would mention in potential problems? 


Potential Problems and approaches:
Based on the above approaches, some the problems of interest are to expand this entire approach fully neural net wherein we utilize end to end network for odometry. 

