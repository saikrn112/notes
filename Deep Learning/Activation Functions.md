##### Overview of popular ones 
![[activations_overview.png|500]]


* Stronger the activation response, stronger the rememberance


##### ReLU
what is it ? 
advantages
disadvantages
dying relu, neurons with negative outputs doesnt get good outputs

when to use?


##### Parametric ReLU
what is it ? 
parameterized version of Leaky ReLU
![[param_relu.png]]
>[!INFO]- difference between leaky relu and parametric relu
>![[leaky_v_parametric.png]]


advantages
leak factor is learnt by network

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
what is it?
$$
\begin{align}
softmax(z)_i = \frac{e^{z_i}}{\Sigma_{j=1}^{k} e^{z_i}}
\end{align}
$$
value range (0,1)
advantages
- multiclass classification

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
