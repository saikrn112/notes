Example line fit
1. blur
2. gradients
3. for every pixel > threshold, fit  ($r, \theta$) $r = x cos \theta + y sin \theta$ 
4. increment the counter in $r, \theta$ array
5. threshold $r, \theta$ array

good explanation https://docs.opencv.org/4.x/d6/d10/tutorial_py_houghlines.html
![[hough_transform_explanation.png]]