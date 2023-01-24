paper: http://matthewalunbrown.com/papers/ijcv2007.pdf

### Overview
1. Invariant features for reliable matching
	1. rotation
	2. zoom
	3. illumination change 
2. Image stitching as multi image matching problem
	1. matching relationships
	2. recogniaze panorams in unordered datasets
3. High quality results using multi-band blending to render seamless output panoramas
	1. shows hot perform multi band blending for multiple overlapping images with any number of bands
4. extends their other work by introducing _gain compensation_ and _automatic straightening_ steps
5. Efficient bundle adjustment implementation

### 1. Feature Matching
- uses SIFT features
- features are extracted from `n` images
- each feature is matched to its k nearest neighbours in feature space `k = 4` 
- for this k-d tree gives `O(nlogn)`
	- axis aligned binary space partition
	- recursively partitionas feature space at mean in the dimension with highest variance
	- so basically KD tree is comparing distances along features, but how does it use features from `n` images for it's compute
	- <font style="color:DarkRed">Need to understand this part</font>

### 2. Image Matching
_Objective_ 
1. find all matching or overlapping images
2. connected sets will become panoramas
_Complexity_
1. since each image could match with one and another - `O(n^2)`
2. But it is only ncessary to match each image to a small number of overlapping images for good solution

_steps_
1. consider a constant number of `m` images that have **greatest** number of feature matches to the <font style="color:DarkRed"> current image</font> `m=6`
2. RANSAC to select a set of inliers that are compatible with a homography between the images
3. probablistic model to verify the match

```ad-question
title: RANSAC
How does RANSAC give high probability of estimating the correct homography?
```

### 3. Bundle Adjustment
- Idea is to solve for all the camera parameters jointly instead of pairwise homography 
- pairwise homography would accumulate errors an disregard multiple constraints between images

```ad-error
title: _Steps_
- Images are added to bundle adjuster one by one with the best matching image (maximum number of consistent matches) being added at each step
- new image is initialized with same rotation and focal length as the image to which it best matches
- Levenberg-Marquardt is used to update parameters

```

#### Related Math
lets say $u_{i}^{k} \space \leftrightarrow \space u_{j}^{l}$ are point to point correspondences 
where $u_{i}^{k}$ denotes position of $k_{th}$ feature in $i_{th}$ frame

Residual
	$r_{ij}^{k} = u_{i}^{k} \space - \space p_{ij}^{k}$
	$\tilde{p}_{ij}^{k} \space = \space K_{i}R_{i}R_{j}^{T}K_{j}^{-1}\tilde{u}_{j}^{l}$

where $p_{ij}^{k}$ is projection from frame $i$ to frame $j$ of the point corresponding to $u_{i}^{k}$

Error
	$e = \sum\limits_{i=1}^{n}\sum\limits_{j \in I(i)}\sum\limits_{k \in F(i,j)} h(r_{ij}^{k})$
	
	$h(x)$ is Huber robust error function


![[Pasted image 20220911141946.png]]