alignment and aggregation of the pixels 
align-and-merge process

### This work 
- proposes versatile layered neural image representation
- with projective camera model
- novel neural spline flow parametrization


reconstructed scene separated into 
- transmission 
- obstrcution image planes

decomposes pixel motion between burst frames into 
- planar motion
- from camera's pose change in 3D space a generic flow components which account for
		- depth parallalax
		- scene motion 
		- other effects
	- these flows are modeled as NSFs
		- networks which take input coords --> spline control points
			- interpolated at sample ts to produce flow field values

![[nsf_comparison.png|300]]![[nsf_shine1.png|300]]


- uses MLP to fit the NSF 
- forward model similar to multiplanar imaging