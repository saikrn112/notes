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
- always thin lens model 

using blur circle to spoof depth 
if we know how the blurriness varies with depth of the object, 
we can sort of estimate the depth of the object based on the image 


at focal length if we assume it is a pin hole model 
let's 