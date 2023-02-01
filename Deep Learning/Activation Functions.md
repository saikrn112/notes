##### Overview of popular ones 
![[activations_overview.png|500]]


* Stronger the activation response, stronger the rememberance


##### ReLU
what is it ? 
advantages
disadvantages
when to use?



##### Leaky ReLU
**what is it ?** 
instead of $0$ for $x<0$ we have a small slope
$$
f(y) = 
\begin{cases}
y & \text{if} \space y >0,\\
\alpha y & otherwise
\end{cases}
\\
$$

**advantages** and **when to use?**
useful when tasks are suffering from sparse gradients
Example:
	training GANs

**disadvantages**




##### Softmax activation

##### Sigmoid
what is it?
$$
\begin{align}
y = \frac{1}{1+e^{-x}}
\end{align}
$$
value range $(0,1)$   
advantages

disadvantages
when to use?

##### Tanh

^bc8b68

what is it ? 
$$
y = tanh(x)
$$

^d4b647

value range $(-1,1)$ 
derivative steeper than sigmoid

advantages?
it is more s
disadvantages
when to use?


##### ELU
exponential activation function
