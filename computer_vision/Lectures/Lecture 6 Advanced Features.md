double derivative  $\nabla^{2}$ has zero crossing
- easier to implement than max or min
- radially symmetric - so no directionality 



Hessian - optimization math 
Laplacian - image processing math

Laplacian edge detector
- take zero crossing
- end up with double borders since falling and rising edge


reality
- smooth since noise

LoG - David Marr 1989 ICCV
DoG - David Marr -- biological beings do this 

###### Detecting Blobs
characteristic scale -- scale at which we get maximum response
```
Nyquist criterion requires that the sampling frequency be at least twice the highest frequency contained in the signal
```
NLoG - Normalized Laplacian of Gaussian

###### Scale Space


Root filter -- didnt understand 

blob's interest point -- not exactly circle  
- location is centroid of it
- scale - size
- orientation -- gradient orientation
- description

derivatives - orientation
DoG - scales
how did we get interest points in DoG  for scales ? 

##### SIFT
checkit out [[Scale Invariant Feature Transforms (SIFT)|here]]

