
faster convergence guarantees if certain conditions are met
#### conditions
- function has to be [[Some fundamentals#^ae1d29|positive definite]]
		if a function is semi positive definite then it's not guaranteed that Newton Raphson will converge 


iterative method

1. essentially fits parabola instead of linear approximation.
2. get minima of parabola
3. that will be `K+1` th guess


Analytically, 
$$
\begin{align}
w = w^{k} - H^{-1} \nabla_{w}f(w^{k})
\end{align}
$$

2 assumptions
1. Hessian can be computed
2. and Hessian is invertible

point 1 - it is not feasible but have inspired other methods like Adam, AdamProp etc

earlier instead of $H^{-1}$ we had learning rate $\alpha$
now it is a matrix instead of a scalar 


