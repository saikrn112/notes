# Overview 
1. Feature Extraction, Description and Matching
2. Outlier rejection using RANSAC and Estimating Fundamental Matrix (F)
3. Estimating Essential Matrix (E) from Fundamental Matrix (F)
4. Estimating Camera Pose from Essential Matrix
5. Check for Cheirality condition using Triangulation
6. Perspective-n-Point
7. Bundle Adjustment

## 1. Feature Extraction, Description and Matching
In this step we extract features and their descriptors
[[Scale Invariant Feature Transforms (SIFT)|SIFT]] is a robust one

feature matching is force  $O(N^{2})$ or $O(NlogM)$

## 2. Outlier Rejection Using RANSAC

epipolar geometry
- [[Epipolar Geometry]]
- [[Lecture 13 Stereo and Epipolar]]
- [[Fundamental and Essential Matrix]]

In this step we use [[RANSAC Random Sample Consensus| RANSAC]] to identify the inliers
model used - [[Fundamental and Essential Matrix#^31ea40|Fundamental Matrix]]
minium point matches needed - 8 and solve $Ax = 0$ 
standard SVD to find the solution

tricks used -
- scale the solution found in SVD
- F should be rank 2 so after taking SVD we need to enforce this constraint
- this is enforced by taking SVD of F again and setting last singular value to 0

## 3. Estimating Fundamental Matrix (F)

Essential from fundamental is [[Fundamental and Essential Matrix#^31ea40|simple]]
tricks used -
- take SVD of E again
- set the singular values to $(1,1,0)$ 
- recompute the E again with new singular values

>[!question]
> why is it (1,1,0)? one answer [here](https://stackoverflow.com/questions/51628483/why-does-essential-matrix-has-2-euqal-singular-values-and-1-zero-singular-values)

SVD - [[SVD]]

## 4. Estimating Camera Pose from Essential matrix


