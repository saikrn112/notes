

b - baseline (pixels)
fl - focal length (pixels)?? - should've been m
D  - difference in the feature distance (meters) 

Depth = frac{fl x b,disparity}

----
##### what makes a feature a good feature
Directional uniqueness - "corners"
-- one of the uses is in from disparity calculation

Bilinear form  vs Quadratic
[u v]M[u v]^T
M - autocorrelation matrix , jacobian of gradients

eigen value - spread of data around eigen vector

-----
harris corner - strong corners
shi - tomasi - can pick up weak corners

issues with harris corner
- intensity issues across the images -- illumination invariance
- doesnt work with directions
---
#### Feature Descriptor
