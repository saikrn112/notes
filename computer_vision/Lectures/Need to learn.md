what are some frequency domain faster process than imge domain in IP?

classical ground plane detection
background subtraction

recap 
- [x] HoG
- [x] SIFT 
- [x] canny edge
- [x] Hough Transform
	


how does DoG work in practice and how does pyramid of scales and DoG related? 

what is FAST, orientation assignment in ORB, how is orb scale invariant? what is Brief? how is ORB fast? what is feature descriptor size? 

CMU slides and quizzes 
all lecture slides

ask gpt for different inverse warping ideas 

how does ICP get 3d-3d correspondences using nearest neighbours?
how does GICP find global minima? 
what are some popular ICP methods? - expected latency in stitiching scenes?

aperture problem - [[Optical flow intricate details]]
horn and schuk -- [[Optical flow intricate details]]
lucas and kanade -- [[Optical flow intricate details]]
farneback method 

upsampling and downsampling 
- optical flow images in flownet for example 

how is optical flow interpolated? [[Optical flow intricate details#^8b4152|link]]  
inverse warping using optical flow [[Optical flow intricate details#^8eb323|link]] -  
	https://ctim.ulpgc.es/research_works/computing_inverse_optical_flow/
	https://stackoverflow.com/questions/17459584/opencv-warping-image-based-on-calcopticalflowfarneback

what happens when we apply laplacian, gaussian, sobel to the image? 
standard ways to compare corner features
standard ways to get descriptor

what are some of the cameras used on drones? 
- and how does camera model change according to them

phase correlation - feature matching if low resolution

why correlation for pattern matching instead of subtraction

rotation and translation from homography
inverse warp based on fundamental matrix $F$ -- no inverse

disparity if 2 different focal lengths? 
- if two cameras have different resolution?

what happens when we apply laplacian, gaussian, sobel to the image? 

what are some of the cameras used on drones? 
- and how does camera model change according to them

Biliear interpolation
- what if the indices are falling out of bounds

homography inverse error -- by Radha
- related to reprojection error
some drone company - Radha

HSV equations -- [[HSV]]

frequency and convolutions

what are some ways for matching features? 
what did they do after super point? 


background subtraction methods 
ground plane detection for lanes 

problem with RANSAC
it relies heavily on the underlying mathematical model

what is SIFT? 
what is HoG? 
need to go through all the lectures for covering different concepts he taught
bag of visual words 


#### Deep Learning

convolution math
- implementing convolutions efficiently
- implementing convolution transpose efficiently
- implementing dialated convolutions

what about biases in conv operator - [[Biases]]

batch normalization

how is non linear function applied in convolutions? 
- it is applied per pixel output of the feature map

spatial transformer network 
how did we make differentiable DLT layer? 

checkout different losses similar to sigmoid


#### Math
what is PCA and how is it related to SVD? 
why PCA doesnt work in computer vision problems 

NeRF
- inverse transform sampling 

post rotation multiplication
affine transformation vs 
rigid transformation vs 

how is convolution fundamentally different from cross-correlation?

#### Parallel 
convolution impl cuda - [convolutionSeparable (nvidia.com)](https://developer.download.nvidia.com/compute/cuda/1.1-Beta/x86_64_website/projects/convolutionSeparable/doc/convolutionSeparable.pdf)
convolution impl python 