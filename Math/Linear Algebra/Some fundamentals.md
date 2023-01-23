
conjugate Transpose -- transpose + complex conjugate
ran(A) - range spanned by A
ker(A) -- kernel of A


moore - penrose conditions
1. should map all column vectors of $A$ to themselves
$AA^{+}A = A$ 
2. act like weak inverse $A^{+}AA^{+} = A^{+}$
3. $(AA^{+})^{*}=AA^{+}$ --  is Hermitian
4. $(A^{+}A)^{*} = A^{+}A$ -- is also hermitian

Special Case, when $A$ is full rank $A$ is $min\{m,n\}$

$A^{+} = (A^{*}A)^{-1}A^{*}$ -- left inverse
$A^{+} = A^{*}(A^{*}A)^{-1}$ -- right inverse


SVD

if $A = U\Sigma V^{*}$ is SVD of $A$ 
then $A^{+} = V \Sigma^{+} U^{*}$  


what does matrix multiplication physically mean? 
	Matrix multiplication of $A$ with $x$ is generally a combination of rotation and stretching\


```ad-question
title: $M^{-1}AM$
why do we do this? and what is the implication of this?
is it similarity transformation? 
```

##### Orthogonal Matrix
$A^{-1} = A^{T}$

##### Symmetric Matrix
$A^{T} = A$

##### Positive Definite matrix
symmetric matrix where every eigenvalue is positive
$$
\forall \lambda\text{s} > 0
$$

**Positive Semi Definite**  ^6ceaa5
$$
\forall \lambda\text{s} \geq 0
$$

##### Lower Upper Decomposition
converts a square matrix to lower $L$ and upper $U$ triangular matrices


##### QR Decomposition
converts a square matrix to orthogonal matrix $Q$ and upper triangular matrix $R$

##### EigenValue - EigenVector Factorization

positive definite $M$
$Q$ - eigen vector matrix 
$\Lambda$ - diagonal eigen value matrix ^ae1d29

$M = Q\Lambda Q^{T}$ 


##### Consistent and Inconsistent Equations
equation $Ax = b$ called 
- consistent if there is atleast one solution that satisfies that equation
- inconsitent is there is no solution that satisfies that equation


**Rank of product of matrices**
https://math.stackexchange.com/questions/192164/rank-product-of-matrix-compared-to-individual-matrices


**Orthonormal Basis** -- [[Convolution.pdf]] #TOREAD
2 reasons
1. projection - easier to get individual components (free variables) that are independent of other variables just by using dot product with basis
2. length - length is as simple as sum of squares of coords
