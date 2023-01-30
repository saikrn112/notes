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
Euler Angle
Matrix
euler angles

