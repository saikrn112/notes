double derivative  $\nabla^{2}$ has zero crossing
- easier to implement than max or min
- radially symmetric - so no directionality 



Hessian - optimization math 
Laplacian - image processing math

Laplacian edge detector
- take zero crossing
- end up with double borders since falling and rising edge


reality
- smooth since noise

LoG - David Marr 1989 ICCV
DoG - David Marr -- biological beings do this 

###### Detecting Blobs
characteristic scale -- scale at which we get maximum response
```
Nyquist criterion requires that the sampling frequency be at least twice the highest frequency contained in the signal
```
NLoG - Normalized Laplacian of Gaussian

###### Scale Space


Root filter -- didnt understand 

blob's interest point -- not exactly circle  
- location is centroid of it
- scale - size
- orientation -- gradient orientation
- description

derivatives - orientation
DoG - scales
how did we get interest points in DoG  for scales ? 

##### SIFT
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
8. descriptors are matched using SSD or cross correlation