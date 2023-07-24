
segmented bar 
	end point - 386,319
	start point - 386,167
![[bar_horizontal_top-1.png]]
![[bar_horizontal_end.png]]
>[!Info] difference from counting pixels
difference - 152


bounding box 
```
"frame000039.png": {

"horizontal support": [
[0.0,155.0],
[640.0,155.0],
[0.0,331.0],
[640.0,331.0]]},
```

>[!Info] difference from bounding box
difference - 176


![[horizontal_bar_segmented.png]]

```
def get_depth_from_structure0(bb, horizontal_width, camera_matrix):
	horiz_up = abs(bb[0][1] - bb[1][1])
	horiz_down = abs(bb[2][1] - bb[3][1])
	if (horiz_up < 20 and horiz_down < 20): # since horizontal lines should be straight (no roll).
		if (bb[0][1] > 60 and bb[3][1] < 420):
			width_left = abs(bb[0][1] - bb[3][1])
			width_right = abs(bb[1][1] - bb[2][1])
			depth = 2 * camera_matrix[0][0] * horizontal_width / (width_left + width_right) # depth to shelf estimation
			return depth
return None
```

camera_matrix from calibration
```
M1 = np.array([ 495.41, 0.0,     317.24, 
				0.0,    495.56,  256.84, 
				0.0,    0.0,     1.0]).reshape(3,3)
```

camera_matrix after new optimal
```
[[450.65542603   0.         315.71335603]
 [  0.         449.89959717 255.65386415]
 [  0.           0.           1.        ]]

```

horizontal_width 
```
h = 14cm
```

with default camera calibration
```
width_left = abs(155.0 - 331) = 176
width_right = abs(155.0 - 331) = 176

depth = 2 * (495.51)* 0.14 / (176)*2
depth = 0.3941
```

with new optimal 
```
width_left = abs(155.0 - 331) = 176
width_right = abs(155.0 - 331) = 176

depth = 2 * (450.65)* 0.14 / (176)*2
depth = 0.358
```

with default and counted pixels 
```
width = 152
depth = 2 * (495.51)* 0.14 / (152)*2
depth = 0.4563
```

with new optimal 
```
width_left = abs(155.0 - 331) = 176
width_right = abs(155.0 - 331) = 176

depth = 2 * (450.65)* 0.14 / (152)*2
depth = 0.415
```

>[!Info] final verdict
>using default camera calibration is giving depth closer to the actual value


