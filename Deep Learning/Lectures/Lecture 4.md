weight initilization is important. 
based on that training can be slow or fast

training for a long time on SGD could lead to overfit? 


problem with gradient descent - only considers slope of the function
	essentially higher order effects

it doesnt consider the curvature itself which could help training faster

>[!INFO]
either change the way the optimization work or change the loss functions

##### Optimization


Newton Raphson Method - [[Newton Raphson Method|link]]

###### Feature Transformation
examples are from _shallow machine learning_ models
	shallow here means 1 or 2 layer networks

he talked about covariance matrix
	why?
		loss function can be transformed for example ellipse to a neat circle 

we can know curvature of loss function
	turns out it is related to uncentered auto correlation of the data 


###### Whitening Transformations (T)

this pops up in the hessian of loss function

- _spherize_ the inputs based on auto correlation which will help faster convergence on the model

$$
\begin{align}
T &= \Lambda^{-\frac{1}{2}}\Phi^{T}\\
Y &= TX
\end{align}
$$

1. auto covariance of data $XX^{T}$
2. eigen decompose the auto covariance of $$ XX^{T}\Phi = \Phi \Lambda $$
3. get the transformation for which covariance is identity
4. 
