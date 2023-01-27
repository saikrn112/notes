Data shuffling is important so that we dont train on babies and test it on adults

why do we have to worry about best hyper parameters?
or rather which hyper parameters we are talking about? 

validation and data folds

double cross validation

why is k fold cross validation error estimate biased? 
	biased as in it is not within the acceptable range, what?? 
	it has to do with training on (K-1)/K what is he even talking about? 

how do we decide what is the ideal `K` ?
most common value is 5 to 10

new topic
#### Linear Auto regressive (AR) models
* popularly used in ChatGPT
* classic example of stock prediction
* AR of ARIMA

we are using past events to predict next event 
	can be applied recursively infinitely to predict future

single variate example 
$$
\begin{align}
x_3 &= 0.4*2 + (-0.5)*0\\
x_4 &= 0.4*x_3 + (-0.5)*x_2
\end{align}
$$


multivariate auto regression with `k = 2` example 
$$
\begin{align}
x_t = W_1  x_{t-1} + W_2  x_{t-2}
\end{align}
$$


#### Stochastic Gradient Descent 
instead of running through entire dataset and updating the weights, take mini batches of the dataset and run the gradient descent and update weights on them.
- with this gradients are noisy since every round in each epoch will have a different graident, hence _stochastic_

minibatch - a new hyper parameter

>[!INFO]
there is an interaction between learning rate and mini batch size

that noise gradient will lead to better generalization apparently


in order to guarantee that weights converge, we need to do **anneal** learning rate
- schedule it by multiplying (0,1) after every k rounds
- and maybe we dont need to go till local minima (as in local minima could be overfitting)

#### Regularization

penalize the large weights in the cost function -- why? 

>[!INFO]+ Why regularization?
>
>we can understand regularization by considering the following case 
> - we dont regularize, then weights are free and are unbounded. 
> - since they are unbounded they become unsensitive even for a feature that is not really contributing anything 
> 	- the final impulse could be pass through the activation barrier 
>- To make sure weights outputs are sensitive to inputs, we need to regularize

$L_2$ regularisation

$$
\begin{align}
f_{MSE}(w) = \frac{1}{2n} + \frac{\alpha}{2n}w^{T}w
\end{align}
$$

The regulariser will improve the closed form solution when it is degenerate making it uninvertible

>[!Warning]- Do we regularize bias term as well?
>No


#### Convexity
if the number of cuts is even then convex no matter how many times I cut
if it is odd then non convex? 

for higher dimensions **Hessian** determins the convexity or curvature
if it is positive semi definite (PSD) for every input **x** 
a matrix is positive definite when it satisfies the  [[Some fundamentals#^6ceaa5|conditions]]



