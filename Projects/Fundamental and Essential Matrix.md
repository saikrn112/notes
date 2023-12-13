Essential matrix
it followes the [[Epipolar Geometry#^e136f8|epipolar constraint]]

$$
\begin{align}
E_{2}^{1} = T_{2 \times}^{1}R_{2}^{1} 
\end{align}
$$
Properties:
- rank 2 - because of skew symmetric matrix - intuitively it's because one of the vector is mapped to null space
- left null space - epipole of 1st camera from 2nd camera frame

Fundamental Matrix ^31ea40
$$
\begin{align}
F_{2}^{1} &= K_{1}^{-T}E_{2}^{1}K_{2}^{-1} \\
E_{2}^{1} &= K_{1}^{T}F_{2}^{1}K_{2} 
\end{align}
$$

epipolar constraint using F 
$$
\begin{align}
u^{1}F_{2}^{1}u^{2} = 0
\end{align}
$$
![[fundamental_matrix_constraint.png|500]]


#### Some thoughts

![[WhatsApp Image 2023-02-04 at 6.36.22 PM.jpeg|500]]



![[7_point_algo.png]]
![[7_point_algo_opencv.png]]


## Homography Matrix

rank - 3
algorithm - 4 point
DLT
TensorDLT
