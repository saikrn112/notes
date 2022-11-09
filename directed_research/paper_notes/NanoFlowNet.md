## Overview

- recent advances in semantic segmentation as an inspiration
- guide the learning of optical flow using motion boundary ground truth data
	- improves the performance
	- no impact on latency
- tested on GAP8 microprocessor 
- tested on [[Hardware List#^81bf61|Bitcraze Crazyflie]]


Is it following these [[Papers to read#^b83487|constraints]]?

Based on the abstract, these are the things to ponder on
>is motion boundary related to [[FlowNet Learning Optical flow with CNN#^f84ad4|this]] from flowNet? #TOCONFIRM
>how are they defining latency based on the loss function?
>	doesnt it depend on the architecture?
>is GAP8 microprocessor same as normal cpu? 
>	no it has only fixed point calculations
>then how did they compress the model or quantize the model to fit the GAP8? 
>if they already did then what research problem should I be working on ? 
>checkout their 
>	accuracy,
>	inference time
>	model size
>	supervised or unsupervised? 
>	data generalization
>how is research happening so far ?
>	test out some model,
>	they say they beat the benchmarks by some factor
>	or training differences
>	or targettig a different problem all toegether
>		for example:
>			this paper is targeting model size on drones
>				but for what application? 
>				depth estimation?
>				visual odometry? 
>				they are using this to obstacle avoidance
>				what exactly are they running their models for? #nitin_sanket 
>			maybe I can see different application
 



### This Paper
- inspired by [STDC-Seg](https://arxiv.org/pdf/2104.13188v1.pdf), [BiSeNet](https://arxiv.org/pdf/1808.00897.pdf)
- achieves real time inference on ultra low power GAP8 multi-core microprocessor on Bitcrase AI-deck
- runs at 5.5-9.3 FPS
- motion boundary ground truth as guide
- obstacle avoidance 
- optical flow as intermediate step

## Introduction
### History
handcrafted monocular optical flow estimation

so far previous networks runtime ranges from several to tens of frames per second

methods on nano quads
- model based reinforcement learning for hovering
- obstacle avoidance based on dedicated laser ranging sensors
- self motion estimation using optical flow from dedicated optical flow sensors
	- or with external multi camera setups

edge computing hardware 
- ASIC - application specific integrated circuits 
	- SLAM
	- visual inertial odometry

GAP8 already used in 
- integrate perception and navigation by directly regressing inputs through CNN into control commands 

this paper calculates optical flow as intermediate step
- direct control over vehicle behavior 
- supports multiple optical flow based tasks - simultaneously or interchangebly

## Details 