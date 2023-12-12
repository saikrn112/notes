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
- set the singular values to $(1,1,0)$ - because of normalized coordinates
- recompute the E again with new singular values

>[!question]
> why is it (1,1,0)? one answer [here](https://stackoverflow.com/questions/51628483/why-does-essential-matrix-has-2-euqal-singular-values-and-1-zero-singular-values)

SVD - [[SVD]]

## 4. Estimating Camera Pose from Essential matrix

- To extract camera pose we need to decompose E via SVD
- T is nothing but left nullspace of E so u3 --> two solutions
- convert T to UMUT R = UDVT
- also represent R as USVT
- UMSVT = UDVT => MS = D => S --> two solutions --> two R solutions
- 4 poses from a single E

- disambiguate using chierality condition after linearly triangulating those points 

### 4.1 Linear Triangulation
- They neatly form an equation (lambda)u = K[R,T]X --> for a point
- using cross products u1 X P1X = 0 --> 3 equations for a point, 3 unknowns (X,Y,Z)
- but it's rank is 2 so 3rd equation is a linear combination of other 2
- we need one more point u2 X P2X = 0 --> 2 equations for a, 3 unknows 
- N views of the same point - 2N equations - 3 unknowns

### 4.2 Non Linear Triangulation
![[non_linear_triangulation.png|300]]
- geometric error