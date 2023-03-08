## Overview
- end to end monocular 3D lane detector
- transformer based spatial feature transformation module
- adopts unified 2D/3D anchor design XXXXXXX
- auxillary task to detect 2D/3D lanes
	- multi task learning
>[!question]
>how is it multi task learning? 
>	is it because it's detecting both 2D and 3D lanes




### This Paper
perspective transformer by considering
- camera parameters to generate BEV features
>[!question]
>how is it using camera parameters?

- cross attention to model view transformation

unifies 2D/3D lane detection tasks
>[!question]- 3D Lanes
>- what are they? 
>	lanes in 3D settings like uphill/downhill etc
>- detect?
>	3D sensors, stereo lidar etc



models spatial feature transformation as learning that has attention mechanism
- to capture local region in the front view 
- between front view to BEV (Bird's Eye View)
this gives us fine grained BEV feature representation

uses deformable attention mechanism 
- reduces memory requirement
- dynamically adjust keys through cross-attention module

## Introduction
need to project lanes to BEV for downstream applications. 
2 conventional ways to do this
- project perspective lanes to BEV space
- cast perspective features to BEV by camera in/extrinsic parameters XXXXXXX

BEV space is often considered to be planar which is not the case
- uphill
- downhill
- bump
- crush turn

This is better than dumb Inverse Perspective Mapping (IPM) because 
- resultant features are more representative
- robust 
since it "attends" surrounding local context and aggregates relevant information
>[!info]
>in this case local context is how the height is changing etc



### History
Vision Transformers in BEV
- this method has become more dominant and better performance
- cross attention scheme in ViT is really elegant for learning transformations across different views
Domains
- 3D object detection
- prediction
- planning

previous works which consider BEV but not using cross attention
- 3D LaneNet
	- generates lanes in 3D space
	- uses camera in/extrinsics 
	- IPM to generate virtual BEV representation
- GeoLaneNet
	- builds on top of 3D Lane Net
	- 2 stage design - decouples segmentation and 3D lane prediction head
- DETR3D 
	- considers camera geometry
	- learnable 3D to 2D query search with attention scheme

Problems with above 
- improper feature transformation
- unsatisfying performance in curving and crush turns 
- there is no explicit BEV modelling for **robust feature representation**


## Details 

### Convention
![[convention.png|500]]

