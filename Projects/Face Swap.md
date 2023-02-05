in this project given a video with faces, they are swapped
- got facial fiducials using dlib or manually clicked
- performed delanauy triangluation using voronoi diagram around the control points
	- now these triangles are one to one mapped across the images
	- and these triangles are assumed to be planar
	- barycentric cordinates are found at each point in triangle of image 1
	- using the bary coords and mapped triangles, mapped point on image2 is found 
	- take color from image2 using bilinear interpolation and put in image1 coord
- same thing but instead of delanauy triangluation we use thin plate splines
	- 
	- TPS equation is fit around the control points for both x and y coordinates![[face_swap_tps_equation.png]]
	- and inverse the color 

to replacing face
- find the polygon around the fiducials `cv2.convexHull`
- get the mask on which face has to be warped `cv2.fillConvexPoly`
- get the bounding box `cv2.boundingRect`
- blend and patch `cv2.seamlessClone`

