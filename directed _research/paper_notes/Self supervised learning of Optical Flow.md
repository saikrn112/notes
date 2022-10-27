## Overview
[[7_selfflow.pdf|paper]] 
previous related papers and their notes can be found [[Papers to read|here]]

- learn optical for hallucinated occlusions using predictions from non occluded points as ground truth ^105e4e
- uses temporal information for better flow estimates
- best performance for unsupervised optical flow learning

self supervised v unsupervised - [[Deep questions on Deep learning#^af3218|here]]

### This paper
- targets mostly occlusion 
- self supervised approach can learn to estimate optical flow with any form of occlusion from unlabelled data 
- [[Self supervised learning of Optical Flow#^105e4e|very interesting point]]
- uses the concept of super pixel for that
- doesnt make temporal assumptions said in [[Self supervised learning of Optical Flow#^dbf21b|here]]
- 


`If my guess is right, they come up with a unique loss function to optimize the occluded optical flow ` 


## Introduction 

#### traditional approaches 
- mitigate occlusion by smoothing visually similar non occluded points and regularizing incoherent motion 
> good idea for a loss function
- but slow

#### comtemporary CNN methods
flownet
optical flow using spatial pyramid network
flownet2
lightweight cnn for optical flow estimation
pwc net

all the above methods need data for supervised learning. This data is hard to get for optical flow and it's even harder when we need occlusions 

More data $\propto$ better results

If data is less -> generate synthetic data -> fine tune on the real data (flownet2.0)

##### Unsupervised approach
- warp the image towards the reference
- reduce the photometric loss

doesnt work really well if the pixels are occluded

for that some methods 
- exclude the occluded pixels when computing loss
- added spatial temporal smootheness to regularize the flow


DDFlow - employs random cropping to create occlusions for self supervision
>page 1 highlight
>need to learn more about this

the above method wont generalize well for all natural occulsions
>what do they mean by natural occlusions?



### History
**Traditional** - variational approach Horn and Schmuck
Faster traditional by feature matching to initialize sparse matching and dense flow interpolation
- Large displacement optical flow
- [[FlowNet Learning Optical flow with CNN#^474bd3|EpicFlow]]
- [[FlowNet Learning Optical flow with CNN#^f518e4|DeepFlow]]

**Recent CNNs** 
- improve sparse matching by learning an effective feature embedding
	- CNN based patch matching for optical flow with thresholded hinge embedding loss
	- Accurate Optical Flow via Direct Cost Volume Processing.
- but computationally expensive 
- are not end to end solutions

To improve robustness and accuracy
- incorporate temporal information from multiple frames
- add temporal constraints such as 
	- constant velocity
	- constant accleration
	- low dimensional linear subspace 
	- rigid/non-rigid segmentation
>what is low dimensional linear subspace
>rigid and non rigid segmentation
> ^dbf21b

**Recent Supervised Learning**
FlowNet
FlowNet2.0
SpyNet - proposes to warp images at multiple scales to cope with large displacement 
PWC-Net - warp features from CNNs
LiteFlowNet - warp features from CNNs

However need
- large synthetic data 
- specific training schedules

**Unsupervised Approach**
basic principles same as Horn and Schuck
- brightness constancy 
- spatial smoothness
Back to basics Unsupvervised appraoch [this](https://arxiv.org/pdf/1608.05842.pdf)

The above net uses photometric loss which is ==not applicable if pixels are occluded==

Workaround?
- exclude those occluded pixels in the loss inference
- data distillation to learn optical flow of occluded pixel (DDFlow)
	- works very wel for pixels near boundaries
^ above methods handle only specific cases of occlusion

**Self Supervised Approach**
generates supervisory signal from data
widely used in 
- feature representation from unlabelled data

a pretext task is usually employed such as
- image inpainting
- image colorization
- solving jigsaw puzzles
- exploring low level motion based cues to learn feature representations

## Details
2 Networks of same architecture
- based on PWC-Net
- NOC Model - accurate flow estimation for non occluded pixels
- OCC Model - learns to predict optical flow for all pixels

NOC is used to train OCC
- only reliable non occluded flow estimations are used

**Only** OCC model is needed during evaluation


extends to multi frame optical flow estimation
>do they mean temporal data?
>	they are combining temporal data by considering frames at 3 different timestamps


input - 3 images $I_{t-1}, I_t, \tilde{I}_{t+1}$
ouput - $\tilde{\textbf{w}}, \tilde{O}, \tilde{I}^w$ - optical flow, occlusion map, warped image

#### Network for multi frame flow estimation
- built on top of [[PWC-Net]]

Modifications on top it 
- 3 images as input at $t-1,t,t+1$
- computes backward flow, backward cost volume apart from forward flow, forward cost volume
	- this information is also used since frame at $t-1$ might have ==information== about occluded pixels at $t+1$
- for forward flow, stack
	- $\dot{w}_{t \rightarrow t+1}^l - \dot{w}_{t+1 \rightarrow t}^{l}$  initial (foward - backward) flow
		- initial flow here is the flow from previous pyramid level
	- feature of reference image $F_{t}^{l}$
	- forward cost volume
	- backward cost volume
- for backward flow, **exact same thing as above** but swap the flow and cost volume order
	- $\dot{w}_{t+1 \rightarrow t}^l - \dot{w}_{t \rightarrow t+1}^{l}$  initial (foward - backward) flow
	- feature of reference image $F_{t}^{l}$
	- backward cost volume
	- forward cost volume

>here information is loosely defined and is very abstract
>what is feature of reference image?
>	it's the output of the Pyramid CNNs 

#### Occlusion estimation
if 2 frame optical flow estimation,
	swap two images as input to get forward and backward flow
from here occlusion map is generated base don
	forward-backward consistency prior

for 3 frame optical flow which current paper talks about,
	5 consecutive frames are used
>essentially, each triplet ($I_{l-1}, I_l, \tilde{I}_{l+1}$) where $l=t-1,t,t+1$ produces a backward and forward flow
>	in that the paper uses flow estimations $w_{l \rightarrow l+1}$ where $l = t-1,t$ and produce Occlusion maps at $O_{k \rightarrow k+1}$ 

constraint for occlusion map doesnt make much sense
- it's based on triangle inequality
- but doesnt satisfy the base the condition with given $\alpha_1$ and $\alpha_2$ #nitin_sanket

I dont think this is used in any part of training. but just a mask 

#### Occlusion Hallucination
simple way 
- randomly select a rectangle crop
- fill the rectangle crop with noise
problems
- such an occlusion rarely exist in the real world
- so NN might not generalize for different shapes of occlusions

solution
- superpixel
- select random superpixels
- fill them with noise
advantages
- shape is random so NN _can_ generalize
- superpixels are often part of object boundaries (interesting!)
	- because of this each pixel within super pixel belong to same object or in otherwords will have similar flow fields  [[Self supervised learning of Optical Flow#^d8fc5c|question_ref]]
- this makes super pixels more realistic
- prior research has found that low level segmentation is helpful for flow estimation [[Self supervised learning of Optical Flow#^d8fc5c|question_ref]]
 
>how is superpixel belonging to same object or having similar flow fields an advantage?
>how is low level segmentation helpful? 
>how does the occlusion map look like if the entire scene changes

^d8fc5c


>another insight
>	it's not completely unsupervised. 
>	they are first training the NOC model which needs manual supervision
>		no, using photometric loss even NOC model is fully unsupervised
>	OCC is fully unsupervised

#### Loss
for NOC, Photo metric loss
![[Pasted image 20221010231906.png]]




for OCC, 
- first consider loss only with the mask for synthetically occluded pixels, called self supervision loss
![[Pasted image 20221010232720.png]]
- with this it will try to learn optical flow for the occluded pixels
- and then add $L_p+L_o$ for totoal

>what if I had given loss for synthetic and non synthetic occlusions? 
>using this L_o loss function is like saying that NN should only learn optical flow for occluded pixels alone, 
>	how does it converge? 
>	so it's internally learning how should the opical flow of nearby pixels be if the occluded pixels optical flow is this
>	how should the occluded pixels be based on this

- the above loss function doesnt assume any spatial or temporal consistent assumptions
- fine tuning has a different loss based on whethere the optical flow pixel has a ground truth or noth



#### Implementation

scaling and normalizing each channel to be standard normal distribution for supervised fine tuning #nitin_sanket 
Census Transform #nitin_sanket 