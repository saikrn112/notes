

Disparity
	how the location of the point would change based on the depth as the camera moves
		for example: far away point would change less compared to the nearest point
This is very useful since based on this one can calculate the depth and 
> would stereo fail in the open places if the points are too far away? 

Image Plane:
	Camera image plane where the lines are projecting on
BaseLine:
	line joining camera centers
Epipolar Plane:
	plane containing baseline and world point
Epipolar Line:
	intersection of epipolar plane with image planes
		so 2 epipolar lines at any given time
Epipole:
	image planes intersecting on epipolar line
Epipolar Constraint:
	features point pairs observed by 2 different cameras should satisfy this condition
	$x^{1}E_{2}^{1}x^{2} = 0$  
		- $E_{2}^{1}$  -- Essential matrix which transforms from camera 2 to camera 1
		- $x^{1}$   -- coordinate measured from camera 1 optical center
		- $x^{2}$   -- coordinate measured from camera 2 optical center

Verged Camera Configuration:
	randomly oriented cameras, where optical axis intersect with each other
Parallel Optical axis:
	like in stereo

Epipolar Error:
	For two cameras arranged in stereo a point in one camera view must fall along a line in a second camera view. This line is that point's epipolar line. **The distance between a point's epipolar line and its corresponding point in that second camera view** is the epipolar error.

>how is epipolar error different from projection error?
>is epipolar error projected distance or actualy 3d point to line distance? 
>	does it matter? 
>		yes, based on the depth the distance value would be scaled