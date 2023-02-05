instead of matrix multiplication for rotating a vector in 3D space, we can use this formulation given an axis and angle of rotation


$v_{rot} = vcos\theta + (k \times v)sin\theta + k(k\cdot v)(1-cos\theta)$

where 
	$k$ is a unit vector describing the axis of rotation
	$\theta$ is the amount of rotation in right hand rule $v$ incurs

[Rodrigues' rotation formula - Wikipedia](https://en.wikipedia.org/wiki/Rodrigues%27_rotation_formula)

in matrix notation
$$
\begin{align}
R &= I + (sin\theta)K + (1 - cos\theta)K^{2}\\
K & = \begin{bmatrix}
0 & -k_z & k_y\\
k_z & 0  & -k_x\\
-k_y & k_x & 0
\end{bmatrix}

\end{align}
$$
$k_x, k_y, k_z$ are components of axis unit vector


more rigorous 
[rodrigues.pdf (duke.edu)](https://courses.cs.duke.edu/fall13/compsci527/notes/rodrigues.pdf)
