
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

##### Eigen Values and Eigen Vectors
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

what does matrix multiplication physically mean? 
	Matrix multiplication of $A$ with $x$ is generally a combination of rotation and stretching\


```ad-question
title: $M^{-1}AM$
why do we do this? and what is the implication of this?
is it similarity transformation? 
```

##### Orthogonal Matrix
$A^{-1} = A^{T}$

Symmetric Matrix
$A^{T} = A$
