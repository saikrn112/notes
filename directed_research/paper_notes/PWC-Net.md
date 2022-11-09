## Overview
[[7_pwcnet.pdf|paper]]

By Nvidia
design principles
- Pyramidal processing
- warping
- use of cost volume


Warps ==CNN features== of the second image using current optical flow estimate
17 times smaller than [[FlowNet2.0 Evolution of optical flow networks|FlowNet2]]
2 times faster inference than FlowNet2
==easier== to train than SpyNet
35 FPS @ 1024 x 436 resolution

>Questions
>what does warping CNN features mean? 
>	are they warping intermediate feature maps?
>how to say which is easier to train?
>	based on model?
>	based on loss function?
>	stability of the loss function maybe?


### This Paper
- Focuses more on speed and memory of the network
- constructes "partial" cost volume by limiting search space at each pyramidal level  [[PWC-Net#^e77c35|here]]

## Introduction

Problems with FlowNet2
- Large models are prone to overfitting problem,
	hence subnetworks in FlowNet2 have to be trained squentially
- 640MB model footprint
	- not good for edge devices

Problems with SpyNet ^c72b63
- combines deep learning with classical OF estimation problems
	- Spatial Pyramid network for warp one onto another
	- motion between warped images is usually small

 `Combining domain knowledge with DL gives small models and better accuracy`

 Cost Volume  ^e77c35
 - special case of stereo matching
 - more discriminative representation of disparity than raw images or eatures 
 - constructing full cost volume is comp expensive, so no real time
 - constructes "partial" cost volume by limiting search space at each pyramidal level  
 - and finally warp each layer to estimate large displacement flow - breaks the [[PWC-Net#^c72b63|assumption]] of spynet

 >what exactly is this?

### History
most of it is already captured in [[Self supervised learning of Optical Flow|history of self flow]]

**Cost Volume**
- stores data matching costs for associating a pixel with its corresponding pixels
- more discriminative representation of optical flow

**CNN Models**
- [[Denoising Autoencoders]] for dense prediction tasks -- how?
- above network with skip connections [[UNet]] 
- dialated convolution layers 13,57
- DenseNet architecture 22,27


## Details

fixed image pyramid -> learnable image pyramid
>what are the uses of image pyramid? 
>how to make it learnable? does it have to differentiable for that?

warping as a layer
>how does it help in estimating large motion

cost volume - as a layer

finally use contextual information to refine the flow ^26b87c
- median filtering
- bilateral filtering

**Feature Pyramid extractor**
- uses convolution to downsample
- increases feature channels as downsampling increases
- also for making them invariant to shadows and lighting changes

>how is it different from traditional CNNs?


**Warping Layer**
at $l$th level warp features of second image toward the first image 
this is done using the $\times 2$ upsampled flow from $l+1$th level as reference
>what do they mean by warping can compensate for some geometric distortions?
>	do they mean camera calibration?
>	what are geometric distortions?


**Cost Volume Layer**
use the features to construct a cost volume that stores the matching costs for associating a pixel with it's corresponding pixels at next frame
>here features are all the pixels in the frame?
>is it being compared with all the pixels in the frame? 
>or only surrounding neighbours ?
>	yes, answer below
>basically what is the strategy for comparison

$d$ pixels
- computing partial cost volume based on limited range 

>so it's deriving feature maps of let's say $l$ layers
>and $d$ pixels are considered for flow comparison
>for each feature map at each layer it is constructing a cost volume of $d^2\times H^l\times W^l$


**Optical flow estimator**
- runs for each pyramid level
- each CNN Layer has feature channels of 128,128,96,64,32
- multi layer CNN 
- input - cost volume, features of first image and upsampled optical flow
- output - flow $w^l$ at $l$th level

>how is the optical flow upsampled ?
>bilinear interpolation?
>another CNN?
>		uses context network


**Context Network**
- inspired from post processing using contextual info like described [[PWC-Net#^26b87c|above]]
- [[Deep questions on Deep learning#^832a7f|feed forward CNN]]
- dilated convolutions
>how is this different from [[FlowNet Learning Optical flow with CNN#^71de6a|upconvolution]] ?


**Training Loss**
same as the one proposed in flownet 
- multi scale training loss
>how is it multi scale training loss though?

>how are we getting supervision signal?
>	
>how do we get it for each pyramid layer?


### Implementation Details
Ground truth
- scale the original ground truth by 20
- downsample it to obtain different supervision signals at different levels
- they dont further scale the supervision signal, instead they upscale the upsampled optical flow at each layer
- they are only training to predict quarter of the original optical flow
	- then use biliear interpolation to obtain the full resolution

>when they scale the ground truth
>	I think they mean they scaled the values by 20 
>	this will make sure that downsampling wont result in smaller magnitudes?

