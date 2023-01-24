## Abstract
Deep CNN to estimate _planar_ homographies
compared to traditional approaches
- faster inference speed
- comparable or better accuracy and robustness to illumination variation
==what about scale,rotation and zoom as mentioned in [[Panorama Stitching- Brown and Lowe 2007]] ?==
- better adaptability and performance compared to [[Supervised Homography Network]]

## Intro
#### Homography Uses
- Image mosaicing
- Monocular SLAM
- 3D camera pose reconstruction
- virtual touring ? 
#### Homography Estimation
##### Direct methods 
seminal Lucas-Kanade algorithm
- uses pixel to pixel matching by shifting or warping the image and comparing pixel intensity
- guess inital parameters, use SSD error criterion, search using gradient descent
- Robustness can be improved by
	- enhanced correlation coefficint (==ECC==) error criterion
	- integrating feature based methods with direct methods
	- or by representing images in fourier domain
- Speed can be increased by ==efficient compositional image alignment schemes==

##### Feature based methods
- extract keypoints using local invariant feature
- establish correspondence 
- RANSAC for best homography
- performant but maybe inaccurate when not sufficient keypoints
- significantly faster than direct methods

#### DCNN
estimating optical flow
dense matching
depth estimation
homography estimation

most of the ^ works treat estimation as supervised learning task

#### Current work
- unsupervised, end-to-end model to estimate homographies
- minimizes a ==pixel wise intensity== error metric
- faster inference times since it is ==parallel== 
- can handel large displacements ($\sim 65\%$) image overlap with large illumination varation 
	- any quatification for "large" here?
	- why is supervised network failing here? 
- hybrid approach
	- deep learning
	- traditional direct -- since error signal that drives the network is pixel wise error
	- traditional feature -- relies on features to compute homography estimates
- ==rather than online optimization==
- 
	- performs computation offline
	- caches the results through these learned features


## Models
Homography matrix ($H$) is a non-singular matrix

why $H_{4pt}$ is more useful to optimize that $H$ directly?
- rotation and shear components have smaller magnitude compared to translation
- although they have great effect overall $L_2$ loss sees smaller effect and thereby gradients related to that will be smaller
- moreover, this high variance in magnitude of elements makes it ==difficult to enforce $H$ to be non singular==?

Error signal in supervised model is **Euclidean $L_2$ norm**


Error signal in unsupervised model is $L_1$ pixel wise photometric loss
- $L_1$ because previous works observed that this is more suitable for image alignment problems
- empirically network is easier to train with $L_1$ error ==verify==
- because of this training is not easy or stable
- assumption that lighting and contrast between input images remains consistent
	- in traditional direct ECC this is addressed by modifying loss function
	- or preprocessing images
- in this model 
	- images are standardized by mean and variance of all pixels in our training dataset
	- perform data augmentation by injecting random illumination shifts
	- use standard $L_1$ 

SqueezeNet -- may yield better performance due to advantages in size and computation requirements


### Tensor Direct Linear Transform
objective: create a differentiable DLT applicable for tensors. (so that backpropagation is allowed during training)
input: $4pt$ corners of patch $C_A$ and and $C_B$ 
output: $3 \times 3$ Homography matrix

```ad-question
title: homography as cross product
-- why is homography matrix correspondences represented as cross product instead of subtraction?
-- technically makes sense since after homography both the vectors should be same and since parallel vectors cross product should be 0
```


final matrix to solve for H looks like $Ah = 0$ where $h$ contains elements of $H_{3\times3}$ 
solving for null space of $A$ is the solution
popular approach SVD 
- differentiable 
- but gradients in SVD has high complexity and practical implementations issues
