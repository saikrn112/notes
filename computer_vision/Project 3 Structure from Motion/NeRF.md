## Overview
[paper](https://github.com/radhasaraf/rbe549-sfm-nerf/blob/main/references/NeRF.pdf) 
- synthezes novel views of complex scenes
- network training 
	- by optimzing underlying continuous volumetric scene functions
	- using sparse set of input views
- new scenes by
	- querying 5D coordinates along camera rays 
	- using classic volume rendering techniques to project output colors and densities into an image
- represents scene using a fully connected (non convolutional) deep network (MLP)
- network input 
	- ==continuous== 5D coordinate - spatial ($x,y,z$) and viewing direction($\theta,\phi$)
	- set of images with known camera poses
- network output
	- volume density 
	- view dependent emitted radiance at spatial location
- Volume rendering is ==naturally differentiable==
- describes how to effectively optimize nerf
	- to render photorealistic novel views of scenes with complicated geometry and appearance



>questions #TOCONFIRM

why is it called neural radiance field?

what is a continuous volumetric scene function? 
	what is continuous about it?
	how do you define a scene function? 
	why does it need only sparse input views?
		does it extrapolate using that? 
			how granular can it extrapolate?  ^72b064
  
does the distance from the structure have to be same? 
	with view alone changing? 

what are classical volume rendering techniques
	what is density of an image? 
	how do you project densities? 

need clarity on network architecture
	how is viewing direction defined? 
	how are photos sent as input while training and testing ? 
	does it have to be retrained for every view we want to generate views for? 
	what do they mean by continuous 5D coordinate? 
		is it related to the question [[NeRF#^72b064|above]]?

what is radiance defined as ? 

how is volume rendering naturally differentiable? 
	how is it related to input? 
	how does it affect the input if it wasnt differentiable?  ^6a9ad2

### This Paper

directly optimizes parameters of continuous 5D scene representation to minimize the error of rendering set of captured images
>so looks like this is a parametric form of scene representation
>	kinda like H4Pt from HomographyNet
>	the representation is called 5D neural radiance field representation
>questions #TOCONFIRM 
>	how to define error of rendering?
>		as in how well they are reproducing the set of captured images?
>		this is like representation learning? 

outputs
- radiance emitted in each direction ($\theta, \phi$) at each point ($x,y,z$) in space
>[!info]
>I am guessing radiance here describes RGB values and their intensities at each point in space 
- and density at each point 
	- acts like a ==differential== opacity controlling how much radiance is accumulated by a ray passing through ($x,y,z$)
>[!question]
>wouldnt RGB itself encode this value?  #TOCONFIRM 
> 	why would need additional opacity value in general? 	
> and what do they mean by differential opacity? 
> 	does it simply mean changing opacity? they couldve said varying opacity right? 

optimizes MLP using a regression that maps 
- maps single 5D coordinate 
- to a single volume density and view dependent RGB color 
>[!question]
>what is view dependent RGB color #TOCONFIRM 


to represent this NeRF from a particular viewpoint
- march camera rays through the scene to generate a sampled set of 3D points
>what do they mean by march camera rays? #TOCONFIRM  
>	are they travelling along a particular camera ray
>what does marching camera rays through the scene mean? 
>	like selecting a set of viewpoints and travelling along those viewpoint lines 
>	these rays can also intersect multiple points on the scene
>how is this process generating a sampled set of 3D points? 
>	by travelling in those viewpoint lines we get a set of 3D points and the RGB information corresponding those viewpoint lines
- uses those points and their corresponding 2D viewing directions as input to the NN to produce output set of colors and densities 
- use classical volume rendering techniques to ==accumulate== those colors and densities into a 2D image
>what does accumulate mean here? #TOCONFIRM 
>	is it aggregating colors from different points on a rays to a 2D image? 
>	like suppresing different Z coordinates to Z=0 plane
>how is volume rendering used for acculumation? 

more on representation learning [[Deep questions on Deep learning#^d18447|here]]
Volume rendering is naturally differentiable, so
- use gradient descent to optimize the model
- minimizes the error between each observed image and corresponding views rendered from our representation
- multiple views are needed for generalization (coherent model)
	- NN does this by assigning high volume densities and accurate colors to the locations that contain ==true== underlying scene content
>adding more questions to [[NeRF#^6a9ad2|this]] #TOCONFIRM 
>are there any other techniques that people use if the volume rendering wasnt differentiable? 
>what does true here mean? 
>	is it different from learning high order representation that is commonly used in representation learning? 
>	or is it actually saying that it assigns these values to a specific ($x,y,z$)

basic implementation of optimizing a NeRF representation for a complex scene 
- does not converge to a sufficiently high resolution representation
- is ineffecient in the required number of samples per camera ray

To resolve these 
- transforms input 5D coordinates with positional encoding 
	- enabling MLP to represent higher frequency functions (scene content)
>what is defined as high frequence scene content? #TOCONFIRM 
- hierarchial sampling procedure 
	- to reduce number of querires required to adequately sample this high frequency scene representation
	- is used to allocate the MLP's capacity towards space with visible scene content
>how is this sampling procedure helping for this #TOCONFIRM 

volumetric representation can 
- represent complex real world geometry and appearance
- is well suited for gradient based optimization using projected images
>adding more questions to again [[NeRF#^6a9ad2|this]] again #TOCONFIRM 
>how are projected images used in gradient based optimization?
- is much more space efficient as compared to discretized voxel grid representation


uses 5D radiance fields  ^262a93
- 3D volumes 
- 2D view dependent appearance
- represents higher resolution geometry and appearance to render photo realistic novel views of complex scenes

circumvents the problem of time and space complexities observed in [[NeRF#^5b24c3|discrete volumetric approaches]] by modelling the problem as a ==continuous== volume instead
advantages 
	- higher quality renderings 
	- only a fraction of storage cost of sampled or discrete volumetric representations ^2fa189

## Introduction

### History
encoding objects and scenes in the weights of MLP -- method 1
- that directly maps 
	- 3D spatial location 
	- to implicit representation of the shape as [[Set Theory#^cdfb3a|level set]]
		- such as signed distance at that location
		- occupancy fields
- but
	- couldnt reproduce realistic scenes with complex geometry with same fidelity
		- as discrete representations like triangular meshes or voxel grids -- method 2

other similar encoding
- images
- textured materials
- indirect illumniation values

##### Neural 3D shape representations
- differentiable rendering functions 
	- that allow neural implicit shape representations using only 2D images
- represent as 3D occupancy fields 
	- numerical method to find surface intersection for each ray
	- calculate exact derivative using implicit differentiation (chain rule)
- feature vector and RGB color at each continuous 3D coordinate
	- differentiable rendering function consistening of RNN 
		- that march along each ray to decide where the surface is location
>although above methods 
>	can represent complicated and high resolution geometry 
>	so far only limited to simpler geometries

proposed alternate method [[NeRF#^262a93|above]]

##### View Synthesis and image based rendering
dense sampling of views
	photorealistic novel views from a simple *light field sample interpolation* techniques

novel view from sparser view sampling
	CV and graphics communities predict traditional geometry and appearance representations from observed images
- mesh based represetantions of scenes  with either
		- diffuse appearance
		- or view dependent appearance
	- Differentiable rasterizers or pathtracers for optimization
	- but gradient based mesh optimization is difficult 
		- mostly because of poor loss landscape

volumetric representations 
	-advantages
		- ==realistically== represent complex shapes and materials 
		- well suited for gradient based optimization
		- less visually distracting artifacts than mesh based methods
	- early approachs
		- used observed images to directly color voxel grids
		- recent methods do following for generating novel views at test time
			- large datasets of multiple scenes 
			- train 
			- predict ==sampled== volumetric representation
			- alpha compositing
			- or learned compositing along rays
	- disadvantages
		- scale poorly for higher resolution imagery
			- because of poor time and space complexity 
				- due to discrete sampling
				- implies that to render high resolution image
					- need finer sampling of 3D space ^5b24c3


this paper circumvents this as described [[NeRF#^2fa189|here]]


## Details 


##### NeRF Scene Representation
input $(x,y,z,\theta,\phi)$ -- > $(\textbf{x},\textbf{d})$
output $(r,g,b,\sigma)$ -- > $(\textbf{c},\sigma)$
direction 3D cartesian unit vector $d$
>do they mean by viewing direction? #TOCONFIRM 
>	instead of $\theta,\phi$
>what is the reference of $\textbf{x}$?

MLP weights map input to output (duh!)


representation should be multiview consistent so
- restricting network to predict volume density $\sigma$ as a function of only location $\textbf{x}$
- but RGB is predicted using both location and direction
>what is volume density? and why is it only location dependent?
>assuming that reference is constant for all camera rays, #TOCONFIRM  
>	this doesnt make sense.
>	 if the camera ray is passing through 2 points 
>		 closer
>		 farther 
>		 both points should have different luminance volume density. 
>		 unless I didnt understand what volume density is


1. input 3D coordinate $\textbf{x}$ 
2. 8 fully connected layers - ReLU activation , 256 channels per layer
3. output $\sigma$ **and** 256 dimensional feature vector 
>how is this possible? #TOCONFIRM 
>	does it mean it has 257 channels? 
4. 256 feature vector + $\textbf{d}$ (concatenation)
5. 1 more fully connected layer  - ReLU activation, 128 channels
>is vector passed as input or individual elements of vector are passed as input? #TOCONFIRM 
>	I am guessing it is individual elements since it says fully connected layer
>	but does it matter though? 
>		dont think so, since it's ultimately going to be a linear combination of individual elements

**non Lambertian effects**
From [wikipedia](https://en.wikipedia.org/wiki/Lambertian_reflectance)
>Lambertian reflectance is **the property that defines an ideal "matte" or diffusely reflecting surface**. The apparent brightness of a Lambertian surface to an observer is the same regardless of the observer's angle of view

basically the figure 3 in the paper is representing how the viewing direction is non lambertian 


##### Volume rendering with radiance fields
