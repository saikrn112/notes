Optical Flow- _apparent_ motion of the brightness pattern

good example to show difference between motion field and optical flow 
https://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/OWENS/LECT12/node4.html

good overview 
https://www.cse.iitb.ac.in/~ajitvr/CS763_Spring2017/OpticalFlow.pdf

aperture problem - barpole illusion
https://en.wikipedia.org/wiki/Barberpole_illusion

optical flow vs true motion
2 examples 
1. uniform sphere - rotation on an axis - constant light - 0 optical flow 1 true flow
2. uniform sphere - still - light rotating - 1 optical flow 0 true flow

all the below methods depends on the brightness constancy assumption

Horn and Schunck - resource http://people.csail.mit.edu/bkph/papers/Optical_Flow_OPT.pdf
- smoothness constraint
- this constraint is employed by assuming it's rigid flow field
- hence occlusion will create a problem
- this constraint is deployed by minimizing the optical flow gradients along x and y directions
- this problem is solved globally for all the pixels
- assumes some boundary conditions
- need to tune the regularization parameter which is used in minimzation equation
- noise sensitive
	- sinse it's solved globally, errors in estimation at one part is propagated to all the other parts

Assumptions
- brightness constancy 
- smoothness of the flow 
- flow is constant at all the points

how to inverse warp using the optical flow ?  ^8eb323

Lucas Kanade - resource ?
- assumes that small patch has same optical flow, thereby estimating the optical flow locally
- creates a many set of mini least squares solution which can be solved independently
- edges are real pain in the ass since it boils down to aperture problem - in this case they are saying to just use normal flow and interpolate parallel flow from surrounding, how?  ^8b4152
- there is some reliability talk
	- sometimes optical flow estimate from one patch is more reliable than others
	- it apparently depends on the structure tensor and does not need any information about next frame, how? 


small motion assumption - used in L-K method 
- eliminated by decreasing the resolution
- creating a pyramid of scales (coarse to fine)
- at each resolution estimated optical flow is propagated to more finer level 
-

how are both HS and LK methods helping in estimating the parallel flow? 