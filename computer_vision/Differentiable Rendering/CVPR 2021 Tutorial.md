https://www.youtube.com/watch?v=Tou8or1ed6E&ab_channel=Physics-baseddifferentiablerendering-CVPR2021

Foward rendering
- rasterization
- ray tracing methods -- more in physics based rendering

### Ray Tracking
- ray surface intersection computations
- something about it being explicit -- mesh (where the ray is intersecting the triangle)
- vs implicit SDF based representations of the scene
	- implicit because we are parametrizing the scene into functions
- Used in path tracing , bidirectional path tracing etc

### Physics Based Forward Rendering
- Monte Carlo Integration

>[!question]
>how is integration coming into this? 

rendering equation is an integral equation
![[rendering_equation.png]]

![[CVPR 2021 Tutorial.png]]
>[!info] Thoughts!
>in forward rendering you are reconstrucing what the image is given scene parameters
>in inverse you are given image you want to estimate the scene parameters
>scene parameters could include the vertices, the shapes of triangles (if it rasterization based) or implicit SDF or neural nets based and other material properties like albedo refraction reflection etc.. 

^fb5481



![[CVPR 2021 Tutorial-1.png]]
in the above slide need to figure out what discontinuties means here  ^6452fe

![[CVPR 2021 Tutorial-3.png]]

in the above slide, antialiasing is performed by computing the energy the pixel recieves entierly (sort of like computing many rays emitted from a pixel)


![[CVPR 2021 Tutorial-4.png]]
this is the problem I was mentioning at [[CVPR 2021 Tutorial#^6452fe|here]]

![[CVPR 2021 Tutorial-5.png]]
very good summary of ray tracing vs rasterization
>[!info] Thoughts!
>rasterization is doing a lot of approximations to the gradients 
>how is ray tracing differentiation work with point cloud? NeRF!!! 

![[CVPR 2021 Tutorial-6.png]]
this confirms with my thought I mentioned earlier at [[CVPR 2021 Tutorial#^fb5481|here]]


![[CVPR 2021 Tutorial-7.png]]
why we need SfM as intiailization!! so that it wont get stuck at lot of local and global minimas or a learned intiailization like mentioned belwo 
![[CVPR 2021 Tutorial-8.png]]