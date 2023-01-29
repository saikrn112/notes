

### variable length inputs

- other NNs consider input to be fixed length
- but what if input is of variable length? 

possible strategies 
1. consider maximum length and fix the input size
2. consider minimum length, fix the input and discard other lengths
3. extract summary from the sequence and feed into NN
4. scan the input **one element at a time**, update, **remember (a hidden state)** across time steps to store most important information
5. Use attention mechanism to determine which elements of the input are important


### Hidden state role
- they are preactivated values of the neurons
- idea is that they "learn" how much to activate based on the task
- in the image classification task the final learn more or less learns which object it is 

In recurrent neural network hidden states are time dependent

$$
\begin{align}
h_{t} = f(x_t, h_{t-1})
\end{align}
$$

#### Typical representation

^ecd5e0

![[hidden_state_rep.png|500]]

#### Mathematical representation
$$
\begin{align}
\hat{y}_{t} = g(x_1, x_2 \dots , x_t; U, V, w) &= h_{t}^{T}w\\
h_{t} &= \sigma(Uh_{t-1} + Vx_{t})
\end{align}
$$
essentially 
	- $h_{t}$ is a combination of 
	- previous activation $h_{t-1}$ weighted with $V$ and 
	- current input $x_{t}$ weighted with $U$

### Activations 
Use [[Activation Functions#^bc8b68|tanh]]
2 reasons 
1. hidden states should be able to maintain it's value - [[Recurrent Neural Network (RNNs)#^a4578f|below]]
2. $tanh(x)$ is approximated by $y=x$ at $x=0$ [[Recurrent Neural Network (RNNs)#^b16211|below]]

### Training
same way as feed forward networks, **except**
	we **unroll** the computational graph, [[Recurrent Neural Network (RNNs)#^ecd5e0|above]] will change to following
	![[rnns_unrolled-1.png|500]] 

same $U$ weights are used at every time step

#### Losses
losses are summed at every time step
 - **Backpropagation through time**
$$
\begin{align}
J(U) &= \Sigma^{T}_{t=1} J_{t}(y_{t}, \hat{y}_t; U)
\end{align}
$$
### Depths
[[Recurrent Neural Network (RNNs)#^ecd5e0|above]] is base network with just one hidden state, but when unrolled depending on the timestamp $T$ it can be very deep

but base network itself can also be deep
![[rnns_two_layer.png|75]]
when unrolled 
![[unrolled_2_layer_rnn.png|500]]

## Appendix

>[!question] from Jacob's slides
>
>We want the hidden state to be able to maintain its value across many time steps (t=1, 2, 3, ...)
>
>

above question is explained in the next slide
![[why_tanh_over_sigmoid1_rnns.png|250]]
 ^a4578f
 ![[why_tanh_over_sigmoid_rnns2.png|250]]

learning will still occur even if hidden states have value $0$ whereas sigmoid wont allow that ^b16211