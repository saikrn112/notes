

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
inverse warp based on fundamental matrix $F$

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