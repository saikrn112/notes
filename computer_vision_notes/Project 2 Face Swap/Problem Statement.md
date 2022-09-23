## Objective:
End to End pipeline to swap faces both traditional and Deep learning approach

## Data Collection:
 1. 2 videos
	 1. One of yourself with just your face -- used to replace your face with celebrity's face
	 2. with your face and your friend's face in all the frames -- swap faces, if more than 2 faces then two largest faces
 2. convert them to `.avi` or `.mp4`
 3. save to `Data` folder

## Traditional Approach
1. Detect Face Fiducials
2. Warp to other/mean face
3. replace face
4. blending

### Facial Landmarks detection
1. detect facial landmarks to have have one to one correspondence between facial landmarks, -- similar to corner detection in panorama project, except this is across different faces
2. landmarks instead of all the points is to reduce the complexity, although all the points give better results (dense flow or meshgrid)
3. `dlib` library built in opencv gives the facial landmarks

### Face Warping Using Triangulation
ideally need to warp faces in 3D -- ==what does he mean by that?==
but we dont have 3D information, so make assumptions about 2D image to approximate 3D information
simplest way **Triangulation** using facial landmarks as corners
	Assumption -- each triangle the content is planar (i.e forms a plane in 3D)
		hence warping between triangles in 2 images affine

Forming triangular mesh over a 2D image is simple but need **fast** and **efficient** implementation
Using drawing ==dual of the **Voronoi Diagram**== 
	i.e. connecting each 2 neighbouring sites in the voronoi diagram
	**Delaunay Triangulation** - $\mathcal{O}(n\log{}n)$ -- tries to maximize the smallest angle in each triangle
	Consistent with image boundary so that texture regions wont fade into the background while warping

==How are to judge which one is good triangulation?==

### Face Warping Using Thin Plate Spline

problems with triangulation method
- it assumes we are using affine transformation