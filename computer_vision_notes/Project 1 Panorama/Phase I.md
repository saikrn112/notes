### David Lowe's ratio test
[computer vision - How does the Lowe's ratio test work? - Stack Overflow](https://stackoverflow.com/questions/51197091/how-does-the-lowes-ratio-test-work)


### RANSAC algorithm implementation

```
current_max_inliers = []
n_iterations = 10000
for i in range(n_iterations):
	if len(current_max_inliers) > len(features)x90%:
		break 
	select 4 random points from features
	compute H using 4 points
	add points whose SSD(p'i,hpi) < e to tmp_max_inliers
	if len(tmp_max_inliers) > len(current_max_inliers):
		current_max_inliers = tmp_max_inliers

least_squares_estimate of H based on current_max_inliers
```


### ToDos
- [ ] HomoGraphy implementation
	- [ ] confirm with prof
	- [ ] least squares implementation for homography estimate
- [x] I need to remove the zeros while dividing z component of the projection
- [x] figure out why the perspective transform of 1_3 is messed up. essentially it is cropping up the below portion which shouldnt happen
- [x] ransac homography
- [ ] run homography for all permutations and combinations
- [ ] stiching the images 
	- [x] ref_image affine transformation is not good
	- [ ] implement bundle adjustment for better stitching quality
	- [ ] speed up the image stitching during overlap
- [ ] blending
- [ ] refactoring the code with better numpy usage
- [ ] runtime statistics between classical and new approach
- [ ] accuracy statistic between old and new
- [ ] histogram based image scaling?
- [ ] implement ORB feature descriptor instead of histogram based scaling? 


### Stiching and Blending
what are the strategies in which they can be blended together? 
first lets try to stitch the images 
- [ ] reference image to stich on
- [ ] concatenating images
before that I need to find out why the transformation is applied to the other image


#### Stitching logic
from cmu ref https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15463-f08/www/proj4/www/dmillett/

```
To piece them together I used the alpha channel and for each image, feathered the alpha center from 1 in the center of the image to 0 to the outside of the image, leaving a square in the center that was all 1's. After overlaying all the images, I took a sum of all the alpha channels and divided each one by it so that the total alpha value would always be 1
```

Tentative Algo
```
def stitch_images(ref,to,H)
negative_translation = apply_H_on_ref_borders(ref,H)
H_new = apply_translation_to_H(H,negative_translation)
to_new,to_new_borders = apply_H_new_on_to(H_new,to)
ref_new,ref_new_borders = apply_translation_to_ref(ref,negative_translation)
intersection_coords = find_intersection(ref_new_borders,to_new_borders)
for i,j in new_image_shape:
	if (i,j) in intersection_coords:
		new_image[i,j] = ref_new[i,j]
	else:
		new_image[i,j] = ref_new[i,j] + to_new[i,j]


```






``
