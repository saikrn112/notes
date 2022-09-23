_multiplex graph_: graph with multiple layers; nodes are same across the layers but each layer has different connectivity

>how is convolutional network related to this? 
>how is this related to RNNs and Transformers?


Invariant and Equivariant Graph Neural Networks - [link](https://proceedings.neurips.cc/paper/2019/file/ea9268cb43f55d1d12380fb6ea5bf572-Paper.pdf)
sinkhorn distances for computation of optimal transport - [link](https://papers.nips.cc/paper/2013/file/af21d0c97db2e27e13572cbf59eb343d-Paper.pdf)


what is optimal transport problem? 

pytorch library - [link](https://github.com/pyg-team/pytorch_geometric)

#### Graph Convolutional Networks
Thomas Kipf - one of the first authors in this field - [blog]([Graph Convolutional Networks | Thomas Kipf | University of Amsterdam (tkipf.github.io)](https://tkipf.github.io/graph-convolutional-networks/))
RNNs and CNNs generalization on arbitrarily structured graphs is a challenging problem
>at least in CNNs we are making assumptions that image's pixel nodes are tightly connected to each other
>not sure how RNNs work nor did I understand why genaralization across the nodes is difficult

to make this feasible, GCNs known from spectral graph theory are used to define parameterized filters that are used in multi layer neural network model, similar to classical CNNs 
>now my huge question is, if edges are changing between the nodes, how to apply convolution? as in, how is kernel defined? how is convolution performed?  


#### Message passing formulation
>what is this formulation about?
>	it's about messages being passed across the nodes
>how does the network look like? 
>how does the training happen?  


##### Idea:
the below points are from [here](https://towardsdatascience.com/introduction-to-message-passing-neural-networks-e670dc103a87)
1. each node in the graph has a hidden state (dubbed as [[Feature Vector]])
2. lets say node $V_{k}$ is connected to say $V_{i \rightarrow l}$   
3. now, aggregate the **hidden states** and **edges** of all neighbouring nodes of $V_{k}$ using some function $M$
4. update the hidden state of $V_{k}$ using **both** the above aggregate (or using ==obtained message==) and previous hidden state of the node
>so message is nothing but information that is coming to the nodes from the neighbouring nodes. since we are passing that information to the nodes, we call it "Message Passing Formulation"

5. we repeat this process for a set number of times
6. finally reach readout phase
>why is it called readout phase?



##### Uses of this formulation
>need to still understand this

#### Feature extraction for Graphs

- [ ] need to read GNN_notes from Haozhi Qi which Karter shared
- [ ] need to read whitall notes which Karter shared
- [ ] understand what feature extraction from graph is all about from  [here](https://towardsdatascience.com/feature-extraction-for-graphs-625f4c5fb8cd)
- [ ] need to understand what attention is all about 
