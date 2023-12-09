1. Derivative of Gaussian filter (not difference of gaussian)(in sobel it is sobel filter) - compute grad_x and grad_y
2. compute magintude and angle
3. bin the angle images
4. non max suppression on the magnitude using the angle - this will give thin line ![[canny_edge_slide.png]]
		![[canny_edge_nms.png]]


6. hystersis: edge intensity > high threshold - definitely edge, < low threshold - definitely not edge
	1. edges between high and low - could be edges 
	2. just check if they are connected to high intensity edges, if yes then they are otherwise no