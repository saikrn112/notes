A matrix is rotation matrix if it satisfies the following conditions
1. determinant is 1, indicating that it is an orthogonal matrix
2. $R^{T}R = RR^{T} = I$ orthonormality
3. preserves the length of the vector after transformation

[Slerp - Wikipedia](https://en.wikipedia.org/wiki/Slerp)
other resources 
- Lie Algebra - [[Lie Algebra for robotics]]
- shanon rotation averaging - [[Shanon Rotation Averaging]]
- rodrigues formula - [[Rodrigue's rotation formula]]
- rodrigues more rigorous - [rodrigues.pdf (duke.edu)](https://courses.cs.duke.edu/fall13/compsci527/notes/rodrigues.pdf)

need to understand pros and cons of different rotation formats
how to use them 


### Quaternions

for rotating a vector $p$ using rotation quaternion $q$

active rotation -- rotate point wrt coordinate system
$$
p' = q^{-1}pq 
$$

passive rotation -- rotate coordinate system wrt point
$$
p' = qpq^{-1}
$$

>[!question]
>how is rotation of a point wrt coordinate system and vice versa different? 
>are they mathematically different somehow? 



## Representations
Quaternions
Euler Angle -- singularities since it doesnt have a one to one mapping
Rotation Matrix
Angle Axis -- singularities when $\theta = 0 \text{ or } \pi$ 

	in calculations, singularities cause problems for conversions, calculating derivatives, and interpolation.
