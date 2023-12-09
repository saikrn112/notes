# Classical Method
## Corner Detection
some corners, 
- cornerHarris - [[Lecture 5 Features and Descriptors]]
	- harris threshold
		- take a patch
			- compute gradient in x and y using sobel operator
			- compute jacobian matrix surronding center of the image
			- compute eigen values of this matrix
![[corner_harris_1.png|300]]![[corner_harris_2.png|300]]![[corner_harris_3.png|300]]![[corner_harris_4.png|300]]

![[corner_harris_4-1.png|300]]
## ANMS
[[Stitching from Project 1#^f9e8a0]]
for all the strong corners
- find closest corner which is more stronger than current one
sort the corner indices in descending order of r 
take top K best corners

## Feature Descriptor
- MOPS multi scale oriented patches : 06_feature_slides.pdf from CMU
![[MOPS.png|300]]![[LFKLE.png|300]]

## Feature Matching 
SSD on the above devised feature descriptor
- perform lowe's test to remove redundant features
- closest match/second closest match ratio should be higher than a threshold
	- basically indicating that closest match is giving more information than second closest match

## RANSAC
perform RANSAC to remove outliers of the homography model 

## Blending 
Alpha blending / poisson blending

# Homography Net

## Data Generation
- random corners
- perturb by some values 
- take inverse homography between them
- extract patches 

## Network Details 
- Regression to 4 point differences 
	- L2 loss
- Classification
	- didnt understand 
- Unsupervised
	- predict 4 point H
	- using TensorDLT to get H
	- convert B to A using spatial transformer network
	- compute l2 photometric loss between those
- DSAC - differentiable RANSAC

### TensorDLT
[paper](https://arxiv.org/pdf/1709.03966.pdf)
![[TensorDLT.png|300]]
![[TensorDLT2.png|300]]
![[TensorDLT3.png|300]]
