why fully connected layer in CNN? 

TODO
- [ ] **Unreasonable effectivenes**s of data - [Revisiting unreasonable effectiveness of data in deep learning era](https://arxiv.org/pdf/1707.02968.pdf)




bayesian optimization in reinforcement learning?


**Pooling** - is necessary 
1. network training computationally feasible 
2. more fundamentally, it allows aggregation of information over large areas of input images
drawbacks:
- reduces resolution 
> I thought it's aiding in network training because it reduces resolution, is that not why it is making training feasible?  ^bcb9ce


**Feed forward networks** [human pose estimation paper](https://arxiv.org/pdf/1507.06550.pdf)
- learns rich representations of the input space
- but do not explicitly model dependencies in the output space
- they fix this by giving output feedback to the network -- hence iterative error


**Bilinear Interpolation** ^4757d3
- this method is making warping operation differentiable -- need to understand more about this

**Cross Dataset Validation**
- train on 1 dataset
- even if we test on the same dataset as validation, the testset is more or less similar 
- this gives us how the model is overfit to the particular training set

**Self Supervised V unsupervised learning**
In unsupervised learning, we tend to group the data using techniques like k-means or k - mediods while in self supervised learning we dont perform this task. 
They generate some ==sort of self supervisory signal ==to solve some task ^af3218


**Representation Learning**
Representation learning is a class of machine learning approaches that allow a system to **discover the representations** required for feature detection or classification from raw data. ^d18447


**Feed Forward CNN** ^832a7f
