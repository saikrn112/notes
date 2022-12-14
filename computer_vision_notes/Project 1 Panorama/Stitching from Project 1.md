
## Problem statement

## corner detection
using corner harris or Shi- Tomasi corners
how does any of the above work? 
how to detect a corner in the first place? 
compute the intensity gradients on the patch 
	using a sobel or difference of gaussian operators
	more robust since we are remving the noise
	
## ANMS
it's called adaptive because it's adaptively determining which are local maximas and suppressing them  


### Resources
one resource - [(1) Warping and Blending Images | Image Stitching - YouTube](https://www.youtube.com/watch?v=D9rAOAL12SY)

another book - [Computer Vision: Algorithms and Applications, 2nd ed. (szeliski.org)](http://szeliski.org/Book/)

## Notes from Book CVAA

### Image stitching
overview 
Section 8.2.1 - review basic models and introduces new models for panoramic stitching
chaper 7 - finding distinctive features and establish feature correspondences between image pairs
chaper 9 - direct pixel to pixel comparison with gradient descent to estimate these parameters
Section 8.3 - take advantage of these methods to create panoramas
Section 8.4.1 - final compositing surface for warping the aligned imaes
Section 8.4.2 - 8.4.4 - cut and blending overlapping images in conditions like parallax, lens distortion, scene motion and exposure differences

##### Parametric motion models 8.2.1
possible parametric models to establish relationship between pixel coordinates from one image to another 
- simple 2D transforms 
- planar perspective models
- 3D rotations
- lens distortions 
- mapping to non planar (cylindrical) surfaces

###### <font style="color:DarkRed">Confounding Sentence</font>
```
In particular, we saw in Section 2.1.4 how the parametric motion describing the deformation of a planar surface as viewed from different positions can be described with an eight-parameter homography (2.71) (Mann and Picard 1994; Szeliski 1996)
```
##### Planar perspective motion
pure translation and rotation model in 2D
Flickr calls under _panography_

###### whiteboard and document scanning
Idea is to take a series of pics of a large whiteboard or a document with overlapping features and perform a 2D transform to stitch a series of such images
- pairwise alignment process - as more and more pairs are aligned the solution may drift and it is no longer globally consistent. a _global optimization_ is required
- this _global optimization_ often needs to solve a large system of non-linear equations, except **linearized homographies** or **similarity transforms** -- ?

##### Rotational panoramas
stitching when camera is undergoing pure rotation.
In such scenarios and when focal length $f$ is known, Camera matrix boils down to just a simple Rotation matrix than a $8$ Dof homography matrix

###### Video summarizeation and compression
- can be thought of as a generalization of multiple image stitching **however** the following impose additional challenges
	- large presense of independent motion
	- camera zoom
	- desire to visualize dynamic events
- moving foreground objects can be removed using _median filtering_
- or foreground can be extracted into a different layer and composited back into stitched panorama

##### Cylindrical coordinates
alternative to using homography or 3D motion models to align images, first warp the images into _cylindrical_ coordinates and then use pure translational model to align them

Problem: it is restricted to camera known to be level and rotating around it's vertical axis

### Global Alignment
**Bundle adjustment** - given a set of images, find globally consistent set of pairs of images, extends "pairwise matching criteria" to a global energy function that has "per image pose" parameters 
**local adjustments** -- parallax removal, reduce double images, blurring due to local misregistrations
**Panorama recognition** -- given an unordered set of images, need to discover which images go together

#### Panorama recognition
Brown and Lowe - [ijcv2007.pdf (matthewalunbrown.com)](http://matthewalunbrown.com/papers/ijcv2007.pdf)

```
1. find all pairwise image overlaps using feature based method
2. find connected components in the overlap graph to recognize individual panoramas
3. feature based method 
	1. extracts SIFT feature locations and feature descriptors from all input images 
	2. places them in an indexing structure - section 7.1.3
```

#### Bundle adjustment
one way to register a large number of images is to add new images to the panorama one at at time
- problem is accumulated error may lead to the presence of a gap or excessive overlap
- can be fixed by stretching the alignment of all images -- process called _gap closing_
Better alternative:
	**simultaneously align** all the images using least squares framework to properly distribute any misregistration errors
	this process of adjusting pose parameters and 3D point locations for a large collection of overlapping images is called _bundle adjustment_
	



