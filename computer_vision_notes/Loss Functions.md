### Cross Entropy

### Huber loss
this combines - [wiki](https://en.wikipedia.org/wiki/Huber_loss)
- fast convergence properties of an $L_2$ norm optimization 
- with robustness of $L_{1}$ norm scheme

$$
L_{\delta}(a) = 
\begin{cases}
\frac{1}{2}a^{2} & \text{if} \space |a| \leq \delta,\\
\delta .(|a| - \frac{1}{2}\delta) & otherwise
\end{cases}
\\
$$
$$
\text{where} \space a = y - f(x)
$$

### Charbonnier loss
$$
charbonnier(x) = (x^{2} + \epsilon^{2})^{\alpha}
$$
$\alpha$ is typically set to $0.4$ for better convergence

### Structural Similarity Index Loss (SSIM)
compares how similar 2 images are 

https://medium.com/srm-mic/all-about-structural-similarity-index-ssim-theory-code-in-pytorch-6551b455541e

### Siamese Network Loss


### Softplus
relu over softplus - [link](https://stats.stackexchange.com/questions/146057/what-are-the-benefits-of-using-relu-over-softplus-as-activation-functions)
	- relu is better

$$
\begin{align}
softplus(x) &= log(1 + e^{x})\\
softminus(x) &= x - softplus(x)
\end{align}
$$

softplus, sigmoid, softminus, softplusinv - [link](https://jiafulow.github.io/blog/2019/07/11/softplus-and-softminus/)

### Sigmoid
$$
sigmoid(x) = \frac{1}{log(1 + e^{-x})}
$$