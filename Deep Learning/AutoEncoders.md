blog followed - [link](https://www.jeremyjordan.me/autoencoders/)

Autoencoders are an unsupervised learning technique in which we leverage neural networks for the task of [[Deep questions on Deep learning#^d18447|representation learning]] .

Specifically, we'll design a neural network architecture such that we _impose a bottleneck in the network which forces a **compressed** knowledge representation of the original input_.

Reconstruction error so that hidden representation is same as the original input

If we didnt have a bottleneck layer, i.e if we had the layer that is same as the input layer, the network could simply memorize the input

Ideal autoencoder does the following things
- sensitive to inputs so that we can reconstruct most of the information
- insensitive to the inputs so that it wont memorize


Upgrade to this is **Variational Autoencoders**

TODOs
- [ ] finish reading the blog
- [ ] also read about variational autoencoders
- [ ] 