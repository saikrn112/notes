category : 
parent link : [[dso.pdf]]

## Overview

Visual odometry based on 
- sparse 
- direct structure and motion formulation
combines 
- ==fully direct probalisitc model== 
- joint optimization of all model parameters including ==geometry represented as inverse depth==
integrates  ^7b2124
- full photometric calibration
- exposure time
- lens vignetting
- non linear response functions

>[!summary] what is?
>- direct structure and motion formulation
>	- direct could mean photometric
>	- why motion?
>- fully direct
>	- are there indirect methods?
>- probablistic model
>	- how does this combine photometric error?
>- geometry represented as inverse depth
>- integrating above [[Paper#^7b2124|points]]


### This Paper

^99cf36

optimizes ==likelihood==
- model parameters
- camera poses 
- camera intrinsics 
- camera extrinsics
- geometry parameters (inverse depth values)
-- optimizing the above is equivlent to windowed sparse BA

## Introduction

### Indirect
pre computation and keypoint extraction
optimizes geometric error 
- point positions
- flow vectors

>[!ERROR]
>establishing correspondences using dence regularized optical flow


>[!info]-
> for depth cameras optimizes point positions is direct approach not indirect

>[!summary]
>**Direct**: optimises photometric error
>**Sparse**: optimises geometric error without geometric prior
>**Dense**: uses geometric prior
>
>**Sparse + Indirect**: ORBSLAM2
>**Dense + Indirect**: need to check this 
>**Dense + Direct**: LSDSLAM, DTAM
>	- employs photometric error (direct)  with geometric prior (dense)
>**Direct + Sparse (==This Paper==)**
>	- opitmises photometric error + geometric prior
>	- using non linear optimisation framework unlike EKF


### History
### Interesting References
## Details 

### Direct Sparse Model
odometry is optimization of 
- photometric error for window of recent frames
- constraints: photometrically calibrated model for image formation and mentioned [[Paper#^99cf36| in this paper section]]

#### Calibration
geometric camera model: 
$$
\begin{bmatrix}
u \\ v \\1
\end{bmatrix}
\leftarrow
K 
\begin{bmatrix}
R | T
\end{bmatrix}
\begin{bmatrix}
X \\Y \\Z \\1
\end {bmatrix}
$$
photometric camera model:
$$
F: Intensity \rightarrow pixel \hspace{1mm} value
$$

>[!thoughts]
>usually these pixel intensity value are converted to feature descriptors which are robust to illumnation changes

##### Geometric Camera Calibration

$$
\Pi_{c} : \mathbb{R}^{3} \rightarrow \Omega
$$
> what is the above equation?

##### Photometric Camera Calibration
non linear response function
> [!thoughts]
	I think it is a mapping from real world energy to pixel values 

$$
G : \mathbb{R} \rightarrow [0,255]
$$

lens attenuation (vignetting) - [[Lens Attenuation (Vignetting)]]
$$
	V : \Omega \rightarrow [0,1]
$$

Auto exposure
>how is auto exposure accounted for?
below [[Paper#^5ff1c1|explanation]]

**model**
$$
I_{i}(x) = G(t_{i}V(x)B_{i}(x))
$$
$x$ - pixel or point
$i$ - frame i
$B_{i}$ - irradiance
$I_{i}$ - observed pixel intensity (0 to 255)

>[!info] Equation explanation
>- we have measured irradiance of the scene $B$ at frame $i$
>- because of vignetting the irradiance drops so we multiply that with $V$
>- since we want to understand how much light intensity we captured we multiply that with exposure time $t_{i}$
>- Finally, we want to convert irradiance to pixel intensities using $G$

^5ff1c1

**correction**
need to create inverse map using the calibration values 
![[inverse_photometric_correction.png|300]]
>[!todo] After correction
>we are dealing with photometric intensities not pixels anymore 
>



>[!tldr]- Factors considered vs not considered
>factors considered  
>- non linear response 
>- lens attenuating
>- exposure time
>
>Things not considered 
>- gamma correction
>- white balancing
>- strong geometric distortions
>  
>what other factors could be considered? 
>is there an exhaustive list of things to be considered?
>



#### Formulation

>[!attention]- Robustness to motion blur
>8 pixels arranges in spread pattern
>	this is because motions could be fast between snaps
>	but it is robust because motion couldve occupied only 1 more pixel apart from main pixel


Keywords 
- Irradiance derivative constancy term
- Irradiance constancy
![[error_formulation.png]]

we are trying to calculate photometric loss which is difference in irradiance
>[!important] Assumptions and Understanding
>assumptions:
>- scene is not changing drastically between two frames
>- i.e photometric intensity of pixel is almost same across two frames
>this assumption allows us to compute error assuming illumination is not changing a lot
>
>Understanding:
>- weighing each pixel considered in the patch
>- $t_{i}$ and $t_{j}$ are used because we want to compute actual irradiance instead of photometric value
>  
>  Missing understanding:
>  - what are parameters $b_{i}$, $b_{j}$, $a_{i}$, $a_{j}$
> 	 - ==affine brightness transfer function==
>  - why are $b$ subtracted?
>  - why are exponential terms multiplied?
	why are we using affine brightness transfer function here?
	how does it avoid lack of exposure times?
	why exponential term?
	
	






 







