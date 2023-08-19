Given a matrix $A_{m \times n}$ where $m \neq n$ 
By default inverse doesn't make sense for such a non square matrix
but you can find a matrix $B_{n \times m}$ such that 
1. $A_{m \times n}B_{n \times m} = I_{m \times m}$ --> right inverse
2. $B_{n \times m}A_{m \times n} = I_{n \times n}$ --> left inverse

questions 
- when does right inverse exist?
- when does left inverse exist?
- can they both exist together ? 
	- if yes, what are the conditions apart from $m = n$ ? 

Theory in the wild: [here]([Invertible matrix - Wikipedia](https://en.wikipedia.org/wiki/Invertible_matrix#:~:text=Non%2Dsquare%20matrices%20(m%2D,such%20that%20BA%20%3D%20In.))
![[non_square_matrix_inverse.png|900]]

proof of why:
