# Motivation
understand the concept 
implement a basic or similar variant




good tutorial : https://aras-p.info/blog/2023/09/27/Making-Gaussian-Splats-more-smaller/

>[!info] Summary
>Gaussian Splats are, basically, “**a bunch of blobs in space**”. Instead of representing a 3D scene as polygonal meshes, or voxels, or distance fields, it represents it as (millions of) particles:
>- Each particle (“a 3D Gaussian”) has position, rotation and a non-uniform scale in 3D space
>- Each particle also has an opacity, as well as color (actually, not a single color, but rather 3rd order Spherical Harmonics coefficients – meaning “the color” can change depending on the view direction).
>- For rendering, the particles are rendered (“splatted”) as _2D Gaussians_ in screen space, i.e. they are _not_ rendered as scaled elongated spheres, actually! More on this below.
>

----
# Questions


What is the point density?
what are points granularity
effectively either neural net or gaussian splats we are trying to find color and opacity at a particular point using ray tracing.
how is it different from distance fields?
what is splatting in this?

rasterization pipeline

how does support vector graphics (SVG) work? 

---
# keywords
rasterizer
anisotropic
splatting
spherical harmonics




