## Overview 
optical flow estimation problem as a supervised learning task
proposes and compares 2 architecture
1. generic architecture 
2. another one includes a layer that correlates feature vectors at different image locations

trained using generated synthetic flying chairs dataset
- consists of random background images from Flickr
- overlayed segmented images of chairs
- generalizes well though -- sim 2 real

For optical flow, we need following things
- precise per-pixel localization - feature representations
- finding correspondences between two images - feature matching

earlier to this paper CNN was learning only feature representations?
since authors were not clear if CNNs would learn this, they created a correlation layer (guessing it is differentiable) that provides matching capabilities 

layers on top of this correlation layer were predicting `flow`
- and surprisingly (now unsurprising) that correlation layer was not required to do this
>[!INFO]
>good note here is that, earlier days of CNNs were still not that trustworthy.
>it is evident how the authors are handcrafting the architecture to make sure it is performing the task it is designed to.  
>now it is so common knowledge that NNs can learn any sort of representation given appropriate loss and data models


Results:
- 10 image pairs per second on full resolution of Sintel dataset

this is a straightforward encoder-decoder architecture since the contraction part is encoding higher level details and decoder part is expanding back to full image 

## History

Variational approach - Horn and Schunck 1981 -- dominated fields till 2015
>wow! they used for so many years!
>but what did they propose exactly? is it same as what Nitin Sanket said in his office?

- improvements
- focus till then was on large displacements
- and integrating combinatorial matching

Deep Matching and DeepFlow  ^f518e4
- feature information is aggregated from fine to coarse using sparse convolutions and max-pooling
- all parameters are set manually instead of learning
> how is it deep then?

EpicFlow ^474bd3
- more emphasis on quality of sparse matching as matches from [[FlowNet Learning Optical flow with CNN#^f518e4|above]] are merely interpolated to dense flow fields while respecting image boundaries
>I think what they mean by that is earlier paper focused too much on dense flow fields (as in how each pixel is moving) while this paper focuses on sparse matching of these flow fields? -- TODO confirm

---
**Current Paper**
- needs this variational approach for optional refinement of the predicted flow field
- doesnt need anyother handcrafted methods for aggregation, matching and interpolation
> aggregation as in aggregating nearby pixels orientation or something?

- directly predicts complete flow fields instead of patch based methods
- upconvolve coarse feature maps 

---
 Unsupervised learning
 - of disparity or motion between frames of videos
 - use multiplicative interactions to model relations between a pair of images
>what does multiplicative interactions mean? 

Boltzmann machines
synchrony autoencoder

_they work well but not competitive with classical methods on realistic videos_

Descriptor matching with CNN - Fischer, Dosovitskiy  2014
- extract features from CNN and match with Euclidean distance
Computing stereo matching cost with CNN - Y.LeCun 2014
- train CNN with _Siamese architecture_ to predict similarity of image patches

the above methods are patch based and leave _spatial aggregation_ to post processing
>what does spatial aggregation mean?

### Per Pixel prediction architectures

Simplest 
- apply CNN in a sliding window fashing and compute single prediction for each input image patch
drawbacks:
- high computational cost
- per patch nature -- not allowing to account for global output properties like sharp edges

Another simpler appraoch
- upsample all feature matches to the desired full resolution and stack
- results in per pixel feature vector which can be used to predict value of interest

2 other approaches which this paper adapted
- coarse depth prediction + actual image = finer coarse depth prediction
- deconvolutional layers for finer coarse depth prediction

current paper _upconvolves_ whole coarse feature maps instead of just prediction and concatenate the features from _contractive part_ of the network
>what is the difference between depth prediction vs feature maps?
>what is contractive part of the network

Question on pooling - [[Deep questions on Deep learning#^bcb9ce|isnt reduced resolution aiding in network training?]]

authors want both pooling and dimension shouldnt reduce, so for _refinement_ - as they call it - following tricks
>I understood refinement as converting some coarse to fine
>as in we predict the flow in patchy areas and let network define the entire flow
>but from what I understand they are talking about refinement as if to predict dense flow fields from averaged out feature map, how is it different from upscaling or upconvolving?
>even if they do, it doesnt align with my earlier understanding that reduction in feature map size as the network goes deeper is aiding in network training

authors use upconvolution and concatenation
- upconvolution ^71de6a
	- essentially, unpooling - extending the feature maps as opposed to pooling, ==is it just padding?==
	- convolution
- concatenation
	- with corresponding feature maps from ==contractive== part of the network
	- and upsampled coarser flow prediction (if available)
>what is contractive part of network? 
>	in the non generic architecture they proposed, first part spatially compreses the information and then after correlation they refind and expand the image to get optical flow fields
>what is upsampled coarser flow prediction? and why did they mention "if available" explicitly?
>	I think what they mean is, like in previous papers so far if they have a coarser prediction from some other network, they will integrate it with that as well. 
>	but what is a coarser prediction? how can they get that ? 
>	did authors do that? or just mention it ? 
>	how to train or network if number of inputs are changing in the middle of the network?

With these 2 steps, paper is achieving 
- preserving higher level information passed down in coarser feature maps 
- fine? local information provided in the lower layer feature maps
>what is 'fine' here ?
>	do they mean refine? 
>	or find? 
>what are lower layer feature maps ? 
>	are they the ones near the input? 
>	they might be near the input since, they are the ones that find local information from convolutions like edges, corners etc

how is each step increasing the resolution twice? 
>upconvolution is increasing the size, yes
>but concatenation is increasing the channel size alone

>[!Image Sizes of Network]
input     384x512     = 196608
output  136x320     =  43520
downsampled rate  =  4.5

and they are repeating this 4 times, resulting in a predicted flow for which the resolution is still 4 times smaller than the input
>didnt understand what they mean actually
>	they are basically increasing the size of feature maps after contraction 4 times
>	but the resulting image is still 4 times less than the actual image

from here they use bilinear upsampling since it is comparitively cheaper and more accurate than adding more deconvolving layers
>now, how does deconvolution even happen?
>

Alternatively, instead of upsampling, they tried variational approach without the matching term
>what is this approach?
> 	what are they not matching? 

using variational approach
1. start at 4 times downsampled image output of the network 
2. coarse to fine scheme with 20 iterations to bring flow field to full resolution
3. 5 more iterations on full image resolution
4. additionally compute image boundaries from this [[FlowNet Learning Optical flow with CNN#^f84ad4|paper details]]
5. respect the detected boundaries by changing the smoothness coefficients to [[FlowNet Learning Optical flow with CNN#^15a650|equation]]

$$\alpha = e^{-\lambda b(x,y)^{k}}$$ ^15a650

paper which they used for computing image boundaries - [link](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.295.579&rep=rep1&type=pdf) ^f84ad4

this approach is more expensive but gives benefits of variational methods to obtain smooth and subpixel accurate flow fields

how does motion blur affect optical flow or any algorithms? 
how to correct motion blur ? 


## Data 
### Data augumentation
not only variety of images but also variety of flow fields 
- same strong geometric transformation to both images of a pair 
- and additional smaller relative tranformation between the two images
>we are apply geometric transformation between the both to generalize across the images
>and then we are applying relative transformation so that network is learning the structure

## Experimental report

- Sintel -- fine tuning of networks and variational refinement of predicted flow fields
- KITTI 
- Middlebury
- Synthetic flying chairs 
- runtime report


#### Loss 
Endpoint Error (EPE) - standard error measure across optical flow estimation
euclidean distance between predicted flow _vector_ and ground truth, averaged over all the pixels


#### Exploding Gradients
>what is this problem? thought vanishing gradients is the problem due to chain rule
>how did they resolve this problem using smaller to larger learning rate?

#### optical color wheel 
> is the color indicating depth? 
> 	so background is given different depth and foreground is given different depth? 
> 	TODO need to confirm this hypothesis
> 	oh, it's a flow vector encoding wheel
> 		each color is describing the direction and it's magnitude is determining the strength of the flow
> on which image do you apply optical flow color changes?
> 	does it matter? 
> 	I think we can just take one image and apply how the flow is changing to that


upscaling the image dataset helped
> how ? is upscaling adding any new features?
> what is fine-tuning and why is it needed to perform for every target dataset?



Cost Volume