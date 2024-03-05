
category : 
SLAM

parent link : 
[[dense_rgbd_slam.pdf]]

## Overview
better way to combine depth information along with RGB

### This Paper

- a fast frame-to-frame registration method that optimizes both intensity and depth errors,
- an entropy-based method to select keyframes, which significantly decreases the drift,
    
- a method to validate loop closures based on the same entropy metric, and
    
- the integration of all of the above techniques into a general graph SLAM solver that further reduces drift.

## Introduction

### History
### Interesting References
## Details 

Given RGB-D images at two consecutive timestamps we need rigid body motion g of the camera
- camera motion by maximizing the photo-consistency between the two images.
- the motion can be estimated by minimizing the difference between the predicted and the actual depth measurements.

depth error is equivalent to point-to-plane ICP with projective lookup


>[!info] Summary of the method
>To summarize, the method presented in this section allows us to align two RGB-D images by minimizing the photo- metric and geometric error. By using the t-distribution, our method is robust to small deviations from the model.



```
I did see it. We are really excited about it. One of the main problems we need your help with is related to pose estimation. We can talk more about it on your first day.


Here is a good starter paper to focus your efforts. Try to look at follow up work and recent stuff too. We need stuff that actually works so be wary of too heavy ML work unless it is crazy good like duster.

  
[https://jsturm.de/publications/data/kerl13iros.pdf]

Haha yes very similar! Mainly just the core part of how they are doing pose estimation with RGBD, and then we will also need a form of either pose graph optimization or bundle adjustment for refining.


But again, try to focus on the core math and code parts, because there are some unique things going on for us that will make our implementation different than the paper.


```
