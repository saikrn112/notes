
- get images in front of the checkerboard 
- get world corners 
- find homography between image plane and world plane
	- using 4 point algorithm
	- system of linear equations forming AX = 0
	- last column of X is homography elements
	- ofc using RANSAC find best points
	- final fit of H is best solution of AX = 0
- least squares solution using [[Optimization#^de3843|LM]] for MLE estimate
- 

![[instrinsic_camera_equations.png]]
![[closed_form.png]]