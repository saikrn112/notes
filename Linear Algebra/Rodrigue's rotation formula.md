instead of matrix multiplication for rotating a vector in 3D space, we can use this formulation given an axis and angle of rotation


$v_{rot} = vcos\theta + (k \times v)sin\theta + k(k\cdot v)(1-cos\theta)$

where 
	$k$ is a unit vector describing the axis of rotation
	$\theta$ is the amount of rotation in right hand rule $v$ incurs

[Rodrigues' rotation formula - Wikipedia](https://en.wikipedia.org/wiki/Rodrigues%27_rotation_formula)
