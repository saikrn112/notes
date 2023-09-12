

$L(r) = k_1 r^2 + k_2 r^4 + k_3 r^6$
barrel  $k_1 < 0$
pincushion $k_2$

tangential distortion

Rad-Tan model 
projection vs geometric distortion model
- FOV < $70^o$ 
- small distortions

equidistant model
- depends on $\theta$ 

OCamCalib
- Omnidirectional calibration 
- [[computer_vision/People#^437630|Davide]]

2018 - IROS
- double sphere model
- lens which are cheap 
	- poor quality

Fancier Calibration
- not even stereo
- 360* FOV
- 2 cameras
- cool math

#### Calibration
Checkerboard
- great corners

ChArUco
- Checkerboard + ArUco

Assymetric or symmetric circles



Skydio
- 6 200* cameras
- robotic arm 
- room full of aruco markers

DL
- might work 
- mightnot work


#### Get away without correction

Uses DL
- microsoft
- predict pose along with distortion
- loss function will be modeled along with distortion parameters


#### Vanishing points
parallel lines meet at $\infty$
why?
- farther things are smaller

connecting 2 vanishing points 
- horizon
- vanishing line
Vanishing line (horizon) tell us
- height: if horizon line is above image half it was lower than horizon
>this doesnt make much sense 


some cross product math
Duality
$X$ and $l$

lot of math

in DL era - VPGNet

Hawk eye technology
- multiview meterology

why is $0$ in $\pi$   
![[Pasted image 20221017140917.png]] ^0cd084

I am treating intersection of points as intersection of lines and it's confusing
for example 
$l = u_1 \times u_2$ is not so clear 
essentially this gives a vector which is out of plane, 
if $u_1$ and $u_2$ are measured from image axis then how does this give a plane normal?

on the other hand, if I assume that $l_1$ and $l_2$ are normal vectors then their cross product giving a point/3D ray is clear 

>questions #nitin_sanket 

but how are $l_1$,$l_2$ ,$u_1$,$u_2$ measured? 
	they are measured from camera coordinate with $z$ value as $1$, so vectors are not purely 2 dimensional
	but this still doesnt explain [[Lecture 12 Depth from 1 image and Projective Geometry#^0cd084|why 4th coord is 0 in pi]] slide 47
	and I think we keep normalizing wrt z so that we are always working on the image frame
	
in slide 48 point of intersection should pass through camera center

entire slide 51 is challenging my conventions of how coordinates are measured
2D point at $\infty$ slide number 53 is pretty confusing
	how is 3rd coordinate changing for parallel lines? 


how is perspective transform invariant to cross ratio? 
	what is perspective transform? slide 62

entire height estimation in slide 64
