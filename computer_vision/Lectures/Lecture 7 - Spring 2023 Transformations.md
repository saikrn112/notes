
Homography
### Transformations

#### Rotation
invariant
- collinear
- length
- angle area
Number of variables (DoF) - 3
Number of Point pairs  - 2


#### Rotation and Translation

- robotics is mostly postmultiplication
- premultiplication only in computer graphics

$$
\begin{align}
H = H_{trans}H_{rot}
\end{align}
$$
the above equation is post multiplication

#### Shear

#### Similarity 
$$
\begin{align}
H = H_{scale}H_{trans}H_{rot}
\end{align}
$$

invariant
- length ratio
- angle
- shape
number of variables - 4 
numer of point pairs - 2

#### Affine
transforming out of plane
invariant
- collinearity
- parallelism
- length ratio
number of variables - 6
number of point pairs  - 3

#### Homography
invariant 
- lines
- cross ratios
- concurrency
- collinearity

number of variables (DoF) - 8
number of point pairs - 4


----
### Warping
#### Interpolation techniques
##### Biliear interpolation
![[bilinear_interp.png|200]]

###### Nearest Neighbour
![[nearest_neighbour_interp.png|200]]

---
### Blending

Simplest way
- alpha blending
	- average of overlapped tree
- blending in fourier domain

---
### Linear Algebra

----
Features in Deep learning era
Deep matching
- how to learn matching


LIFT - learned invariant feature matching
	biased towards phototourism dataset


what is magic point? 
