
1. DoG (an Normalized LoG approximater)  on entire image with different scales (scale space) (image pyramid)
2. subtract two scale space DoG feature maps 
![[scale_space.png|500]]
4. Find characteristic scale at each point -  scale it which each point resonates well. 
	1. So at each scale we identify interest points at sub pixel accuracy
	2. threshold the intensities that we got for each scale space response
	3. find the local maxima in a patch on the scale space response
	4. from here we get interest point candidates in each scale
![[scale_space_response.png|500]]
![[finding_keypoints_exp_better.png|400]]

5. remove weak extrema
6. bin the orientations 
7. create a descriptor
9. descriptors are matched using SSD or cross correlation
[Introduction to SIFT( Scale Invariant Feature Transform) | by Deepanshu Tyagi | Data Breach | Medium](https://medium.com/data-breach/introduction-to-sift-scale-invariant-feature-transform-65d7f3a72d40)
[image processing - What steps come after finding the gradients of the SIFT key points? - Signal Processing Stack Exchange](https://dsp.stackexchange.com/questions/14433/what-steps-come-after-finding-the-gradients-of-the-sift-key-points#:~:text=SIFT%20computes%20this%20descriptor%20by,vector%2C%20which%20is%20the%20descriptor.)
