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

### Structural Similarity Index Loss (SSIM)
compares how similar 2 images are 

https://medium.com/srm-mic/all-about-structural-similarity-index-ssim-theory-code-in-pytorch-6551b455541e

### Siamese Network Loss