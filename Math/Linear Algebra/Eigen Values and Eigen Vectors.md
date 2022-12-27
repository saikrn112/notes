## Definition
$AV = \lambda V$
$\lambda$ -- Eigen Value 
$V$ -- Eigen vector
- what does this mean physically?
	 Eigen Vectors are just scaled by eigen values for $A$

simple trick to find these values and vectors 
$(AV-\lambda IV) = O$
$|A-\lambda I| = O$

- how is it useful? 
	- basically eigen vectors are independent axis of the space spanned by $A$
	- eigen values are just "strength" of these eigen vectors

## How to Compute?
There are several ways to compute eigenvalues and eigenvectors of a matrix. Here are some steps for three common methods:

1.  Power method:
    -   Start with a random non-zero vector `x`
    -   Iterate the following steps until convergence:
        -   Compute `y = A * x`
        -   Normalize `y` to have unit length
        -   Set `x = y`
    -   The eigenvalue is the limiting value of the ratio `||A * x|| / ||x||`
    -   The eigenvector is the limiting value of `x`
2.  QR algorithm:
    -   Compute the QR decomposition of the matrix `A`
    -   Set `B = R * Q`
    -   Repeat the following steps until convergence:
        -   Compute the QR decomposition of `B`
        -   Set `B = R * Q`
    -   The eigenvalues of `A` are the diagonal entries of `B`
    -   The eigenvectors of `A` can be obtained by solving the system `A * x = lambda * x` for each eigenvalue `lambda`
3. Solving a system of linear equations for $|A - \lambda I| = 0$
4.  Eigendecomposition:
    -   Compute the eigendecomposition of the matrix `A`, which decomposes `A` into `A = P * D * P^(-1)`, where `P` is a matrix of eigenvectors and `D` is a diagonal matrix of eigenvalues
    -   The eigenvalues of `A` are the diagonal entries of `D`
    -   The eigenvectors of `A` are the columns of `P`

Note that these methods may not always converge, and may have different convergence rates and numerical stability properties. 

Also note that eigen decomposition is not unique when 2 eigen values are same, why? 