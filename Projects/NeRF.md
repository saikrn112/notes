[[NeRF Implementation]]
[[computer_vision/Project 3 Structure from Motion/NeRF|NeRF]]

simple network 
input is $x, y, z, \theta$ 
output is $r, g, b, \sigma$
at every point network is computing color and transmittance 
using volumetric rendering
volumetric render discrete equation
![[nerf_render_equation.png|500]]
volumetric render continuous equation
![[nerf_render_continuous_equation.png|500]]
Transmittance is calculating how much does the color at that point influence final color 
kinda like how cloud blocks the rays

algo
project rays
discrete points
find color at each 
propagate the losses

tricks
- positional encoding
- hierarchial volume sampling using fine network. 
	- using inverse sampling, points which has more probable color is sampled
- ![[nerf_network.png]]