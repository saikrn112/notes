## ORB

#### resources
opencv [link](https://docs.opencv.org/3.4/d1/d89/tutorial_py_orb.html#:~:text=ORB%20is%20basically%20a%20fusion,pyramid%20to%20produce%20multiscale%2Dfeatures.)

fusion of 
	FAST keypoint detection
	BRIEF descriptor


### FAST
resource - [link](https://docs.opencv.org/3.4/df/d0c/tutorial_py_fast.html)
it's a feature detector algorithm, like corner harris? 

FAST doesnt compute orientation
for rotation invariance
- intensity weighted centroid of the patch
- direction of this vector from corner point (or center of the corner) gives orientation

### BRIEF
resource - [link](https://docs.opencv.org/3.4/dc/d7d/tutorial_py_brief.html)
ORB uses BRIEF descriptor 
- remember that descriptor is basically encoding the keypoint patch
- but this encoding based comparison performs poorly with rotation
	- as in when the same patch is rotated it will not be able to identify