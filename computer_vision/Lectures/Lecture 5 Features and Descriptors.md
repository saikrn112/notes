what is lens vignetting?


features
- appearance
- geometric

TaXel - tactile element
PiXel - picture element


Tuning threshold parameters smartly in sobel edge detection

-----


#### "Theory" of computer vision
Classified based on a convention
Low - Level - edges                                         |
Mid - Level - patterns on noses or mouths   |
High - Level - faces

template matching will be done for mid and high level for pattern search
using cross correlation ? 

theory is to chunk the scene into multiple components

David Marr -- person who proposed the theory
CVPR
ICCV -- best paper award : Marr prize

------

#### Canny Edge Detection Overview
John Canny
- most cited
- single author paper
- left field after his seminal work

steps - [[Canny Edge]]

1. DoG
2. Sobel
3. Magnitude
4. Edge orientation - bin
5. NMS
	1. local gradients
	2. dominent direction - avg, voting etc
		1. How do you get dominant direction? 
6. remove values in non dominent direction - thinning operation
7. Edge linking using **hysteresis**
	1. adaptively switch thresholds
8. Optimal Robust Step detector


#### NN for edge detection
##### Bias
- semantic edges ???
- Object boundary edges
- contrast edges ???

##### Morphological operation 
erosion -- remove half of the data where white pixels 
dilation -- grow back the data 

##### Contours/Region properties 
get the properties of binary image and apply geometry


