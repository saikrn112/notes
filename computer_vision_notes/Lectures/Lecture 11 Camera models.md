point spread function - how the point is observed as the focus is changed. 
pin hole model
- it is essentially allowing only 1 light ray per scene point to pass through
- because of that it is low light
- need long exposure
- very very suseptible to motions on the scene

to account for this use lens 
- they take multiple rays from same scene point and focus it back on other plane. 
- this gives bright picture on the focal plane

aperture 
- $D = \frac{f}{N}$
- where, as $N$ increases aperture size decreases 

blur circle
- where points outside world plane of focus appear as blur on the image plane

In robotics 
- we move the lens instead of sensor since we loose calibration 
- but wont moving lens also lead to loss of calibration? 


Depth of field 
- range where there is acceptable sharpness is called depth of field 
- width where it is acceptably sharp from both sides of focal plane
- more the opening lesser the depth of field 
- smaller the opening more the depth of field 

Assumptions 
- infinte depth of field 
- tiny aperture for acceptable sharpness
- enough light for good enough shutter speed 
- always infitely thin long lens model 

at focal length if we assume it is a pin hole model then we get all those nice properties 

using blur circle to spoof depth 
if we know how the blurriness varies with depth of the object, 
we can sort of estimate the depth of the object based on the image 

metric projection 
- projecting world coordinates to camera coordinates (to sensor)

pixel projection 
- camera coordinates (sensor) to pixel coordinates 

as focal length increases, Field of View (FoV) decreases 
evidently, since $u_{CCD} = f_{m} \frac{X}{Z}$, $u_{CCD}$ increases to capture the same $X,Y,Z$ coordinate on the sensor

since we cant change the sensor size for different focal lengths, our field of view decreases as a consequence 

how is sharpness measured as a metric? #nitin_sanket 

Dolly Zoom
- because of changing the camera distance, farther objects and objects near to those farther objects all start to appear as they are on the same plane 
- but because we are changing the focus, thereby changing the field of view, we are able to see how those farther objects fall onto the near to farther objects

**metric projection**

$$
\begin{bmatrix}
u_{CCD}\\
v_{CCD}
\end{bmatrix}

= 

\begin{bmatrix}
f_{m}\frac{X}{Z}\\
f_{m}\frac{Y}{Z}
\end{bmatrix}
$$


**pixel projection**
$$
\begin{bmatrix}
u_{img}\\
v_{img}
\end{bmatrix}

= 

\begin{bmatrix}
u_{CCD}\frac{w_{img}}{w_{CCD}} + p_{x}\\
v_{CCD}\frac{h_{img}}{h_{CCD}} + p_{y}\\
\end{bmatrix}
$$

clubbing both of them

$$
\begin{bmatrix}
u_{img}\\
v_{img}
\end{bmatrix}

= 

\begin{bmatrix}
f_{m}\frac{w_{img}}{w_{CCD}} \frac{X}{Z} + p_{x}\\
f_{m}\frac{h_{img}}{h_{CCD}} \frac{Y}{Z} + p_{y}
\end{bmatrix}
$$

more generally, $f_{px}$ and $f_{py}$ are focal length in pixels and $f_{mx}$ and $f_{my}$ are focal length in $mm$
$$
\begin{align}
f_{px} &= f_{mx}\frac{w_{img}}{w_{CCD}}\\
f_{py} &= f_{my}\frac{h_{img}}{h_{CCD}}
\end{align}
$$

Finally
$$
\begin{bmatrix}
u_{img}\\
v_{img}
\end{bmatrix}

= 

\begin{bmatrix}
f_{px} \frac{X}{Z} + p_{x}\\
f_{py} \frac{Y}{Z} + p_{y}
\end{bmatrix}
$$

more generally
$$
\begin{align}
Z
\begin{bmatrix}
u_{img}\\
v_{img}\\
1
\end{bmatrix}

&= 
\begin{bmatrix}
f_{px} &0  &p_{x}\\
0 &f_{py} & p_{y}\\
0 &0 & 1\\
\end{bmatrix}
\begin{bmatrix}
X\\
Y\\
Z\\
\end{bmatrix}
\end{align}
$$
finally, since depth is not always known and the point will be anywhere on the ray $Z$ can be replaced by $\lambda$
$$
\begin{align}
\lambda
\begin{bmatrix}
u_{img}\\
v_{img}\\
1
\end{bmatrix}

&= 
\begin{bmatrix}
f_{px} &0  &p_{x}\\
0 &f_{py} & p_{y}\\
0 &0 & 1\\
\end{bmatrix}
\begin{bmatrix}
X\\
Y\\
Z\\
\end{bmatrix}
\end{align}
$$
above transformation is called perspective projection

projection matrix
$$
\begin{align}
\lambda
\begin{bmatrix}
u_{img}\\
v_{img}\\
1
\end{bmatrix}

&= 
\begin{bmatrix}
f_{px} &0  &p_{x}\\
0 &f_{py} & p_{y}\\
0 &0 & 1\\
\end{bmatrix}
\begin{bmatrix}
R_{W}^{C} | T_{W}^{C}
\end{bmatrix}
\begin{bmatrix}
X\\
Y\\
Z\\
\end{bmatrix}
\end{align}
$$