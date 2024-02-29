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




----
## Differentiable rendering in direct illumination

![[CVPR 2021 Tutorial-11.png]]
Leibinz rule with discontinuites with below example 

![[CVPR 2021 Tutorial-10.png]]

reynolds transport theorem: generalization of leibinz rule

![[CVPR 2021 Tutorial-12.png]]
boundary integral is a combination of discontinutiy and boundary itself
 ![[CVPR 2021 Tutorial-13.png]]
 - I is the rendering equation or reflection equation
 - In monte carlo sampling the final I is weighted by the probablity of selecting that particular ray direction, if the probability is high then it will appear a lot of times in samples so we dont have to worry, if the probability is low then we give a little bit of extra weight  

![[CVPR 2021 Tutorial-14.png]]
 
 - simplest form of physics based ray tracing based differentiable rendering 
 - since the local parameters changes are mostly continuous and they integrand dont depend on these parameters differentiation operator can be moved inside 
 - applying the same monte carlo estimator as before we can aggregate the differentiation value wrt to those parameters (assuming the pdf is not derived wrt these local parameters)
 - the above method is ==score estimator==
![[CVPR 2021 Tutorial-15.png]]
- basically what I said earlier. you can take differentiation either including both numerator and denominator or just numerator if the sampling is dependent on local parameters (say BRDF)

![[CVPR 2021 Tutorial-16.png]]
- we cant use the simpler version because of discontinuities 
- one such source for intuition is the emitter size shown below
![[CVPR 2021 Tutorial-17.png]]
- clearly integrand is dependent on the emitter size because at rest of the points it gives 0 and at incident light it is non zero
- so full reynolds transport treatment 
![[CVPR 2021 Tutorial-18.png]]
- here the intereion integral is always smooth on the surface excluding the boundary terms
- boundary terms have separate integral
- we can do change of basis to make the integrand continuous by changing from hemispherical integration to surface integral
![[CVPR 2021 Tutorial-19.png]]

![[CVPR 2021 Tutorial-20.png]]
- you will still have a boundary term but thats because the integration limits are now dependent on the parameters
![[CVPR 2021 Tutorial-21.png]]
>[!info]
>didnt fully understand what silhouette edges are sources of discontinuties 



![[CVPR 2021 Tutorial-22.png]]
- idea is to move the object up or down so that it will match the reference image
- if we dont have the boundary term we will have smooth gradient everywhere and it's mostly positive 
- making the object not move at all and getting stuck at optimization

![[CVPR 2021 Tutorial-23.png]]
- typical autograds although they work well with neural representations the scene might still have discontinuities which the autograds cant take into account


----
## Path Integral for global illumination
![[CVPR 2021 Tutorial-24.png]]
- effectively measure how the light is coming from the emitter to the pixel 
- aggregate of all such  paths is the final outcome 
- estimator can get super simple (from high level)
- ![[CVPR 2021 Tutorial-25.png]]

