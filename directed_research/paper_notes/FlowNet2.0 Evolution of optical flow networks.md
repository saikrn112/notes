## Overview 
successor of [[FlowNet Learning Optical flow with CNN]]
paper [[5_flownet2.pdf]]

**problems** with previous papers, 
speed was ok
accuracy was still off the mark compared to variational approach
error was quite off for small displacements
 
**good things** about previous paper
flownetS is generalizing well compared to flownetC
even though error is off, it's more granular
speed is good since it is well parallelized


### This paper 
- advance end to end optical flow learning and make it work ==well==
- large improvements in quality and speed 
	- schedule of presenting data during training is important
	- stacked structure that includes warping of second image with intermediate optical flow
	- small displacement elaboration - sub network specializing on small motions
- this net is marginally slower than original flownet but decreases the estimation error by 50%
- on par with state-of-the-art models while running at _interactive_ frame rates
- faster variants - upto 140fps with flownet accuracy

network architecture includes
- warping layers that compensate for already estimated preliminary motion in the second image
- somehow uses curriculum learning - which apparently gives dramatic performance on optical fow estimation
---
## Introduction
several evolutionary but decisive modifications that are not trivially connected to the observed problems
1. learning schedule:
	1. schedule consisting of multiple datasets improves results significantly
	2. in this paradigm flowNetC outperforms flownetS [[FlowNet2.0 Evolution of optical flow networks#^9bd029|ref]]
2. warping operation:
	1. stacking multiple networks using this operation improves the results [[FlowNet2.0 Evolution of optical flow networks#^78cbcd|ref]]
	2. depth of stack and size of individual components --> different networks with size and runtime -- trade-off between accuracy and resources --> 8 to 140FPS
3. small, subpixel motion and real world data:
	1. special training dataset - training on this gives good performance on small motions typical for real world videos 
	2. specialized network - learns to fuse the former stacked network with small displacement network [[FlowNet2.0 Evolution of optical flow networks#^49721c | ref]]


>what is a learning schedule?

^9bd029


>how does it fuse two networks?
>what is a displacement network?
>	it is a small displacement network to identify small displacements

^49721c
---
### History
FlowNet - Dosovitskiy and Broxx
similar models
- 3D convolutional network
- unsupervised learning objective 
- rotationally invariant architectures
- pyramidal approach - coarse to fine idea of variational methods
^^none of them outperform flownet though

matching image patches
- Deep Matching
- learn image patch description using Siamese network architectures
^^ 
pros - good accuracy
cons - needs exhaustive matching and slow for practical apps
	- doesnt see the _bigger picture_ since they see only the patch

per pixel prediction
- noisy or blurry results
	- need post processing like variational approach
- refinement using neural networks: 
	- Chen and Pock 2016 - formulate reaction diffusion model as a CNN 
		- denoising 
		- deblocking [[FlowNet2.0 Evolution of optical flow networks#^a4f268|ref]]
		- superresolution
- similar refinement by stacking CNNs  ^78cbcd
	- human pose estimation [hourglass nets](https://arxiv.org/pdf/1603.06937.pdf) [iterative error feedback nets](https://arxiv.org/pdf/1507.06550.pdf)
	- semantic instance segementation

>what is deblocking and superresolution?
>	superresolution can be to add more info and add granularity

^a4f268

warping:
- warping concept is common to all contemporary variational optical flow methods and goes back Lucas & Kanade
- warping correspond to a numerical fixed point iteration scheme coupled with a continuation method [[FlowNet2.0 Evolution of optical flow networks#^2e7cac|questions]]

curriculum learning: ^e5ccb1
- a training strategy where ML models are trained with a series of gradually increasing tasks 
- idea dates back to [Elman](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.478.9032&rep=rep1&type=pdf)
- 

>what is fixed point iteration scheme?
>what is continutation method?
>how is warping even related to this? 
>	should I check this [paper](https://www.mia.uni-saarland.de/Publications/brox-eccv04-of.pdf)?
>	is this even relevant to this paper?

^2e7cac

flow fields - [paper](1.  lowfields:Densecorre- spondence fields for highly accurate large displacement op- tical flow estimation.)
- state-of-the-art

---

## Details
### Dataset Schedules
- not just the kind of data 
- but order in which data is presented matters!

Flying chairs dataset includes only affine transformations of background and chairs
- that means no rotations?

FlowNet models were trained in a different fashion
datasets used 
- flying chairs
- Things3D [[FlowNet2.0 Evolution of optical flow networks#^478d02|question]]

trained using 
- equal mixtures of samples from both datasets using different learning rate schedules

>Things3D is new dataset ? 
>	is it synthetic dataset or real one?

^478d02


based on this dataset and different learning rate, they got different results

> how did they come up with different learning rates? 
> 	how did they estimate when to change the learning rate and by how much?


training on Things3D alone gave bad performance
but training on chairs and fine tuning gave a better performance on things3D
- this model also outperforms training on mixture of both chairs and things3D


>but why could that happen?
>justification that authors give, training simple things first and complicated things next like mentioned in [[FlowNet2.0 Evolution of optical flow networks#^e5ccb1|curriculum learning]]

- they contradict on how flownetC outperforms flownetS with same conditions as [[FlowNet Learning Optical flow with CNN]]


### Stacking Networks

state-of-the-art (classical at that time) are based on iterative methods
>what are they iterating on?
>	are they iterating on the optical flow estimate?


- Biliear interpolation - really cool operation [[Deep questions on Deep learning#^4757d3|notes]]


### Two networks stacking
same networks FlowNetS has been stacked
primary - first net recieving the images
subs_i - other nets recieving the images from previous nets (starts from 2:N)

fixing primary net weights and training subs_2 with warping gradients is giving better results

cross data set validation tell us how the dataset is overfit

 intermediate loss after Net1 is advantageous when training the stacked network end-to-end
 >do they mean they add this loss to the final loss and backpropagate along with it?  


### Stacking diverse networks
idea is to stack different types of networks (flownet correlation and flownet simple)
==reducing the size of networks is also another option==
>how to justify this intuitively though?
>is there any size of the network vs EPE plot?

different ways to treat weights of the stacked networks
- easier to train


>if people have already done that what do you generally do? 


takeaway: different stacks with different channels


### Smaller displacements
- need to distinguish between noise and actual subpixel motion
	- add convolutions between upconvolutions [related paper](https://arxiv.org/pdf/1512.02134.pdf) 
>any intuitive explanation as to how this is helping?

### Fusion
>are they using same strategy as correlation network to fuse the images? 
>	I think they just stacked the images

no more classical methods to extrapolate, fully neural networks to retrieve the original image

## Results
FlowNet2.0 advantages
- robust to homogenous regions 
- image and compression artifacts
>what are compression artifcats?
>	how do we identify them? 
>	should we include such data during training? 


it's giving amazing results compared to other methods presented in the paper

