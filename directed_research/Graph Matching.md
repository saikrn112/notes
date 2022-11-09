Graph matching in CV and Pattern recognition is commonly between _data graph_ and _model graph_
>what will be the data graph and model graph according to [[Super Glue]]'s feature matching problem
>	if we assume nodes are features within one image
>	each node is connected to another node, so their edge represents how they are related?
>		but then every node could be related every other node
>		maybe the direction and length of the node represents the actual direction and distance of the other feature from current feature perspective? 
>		and then we apply a threshold saying all the nodes within some distance are linked -- TODO confirm
>	from here we get a structure of how all the nodes in the graph are interconnected
>	from 2 images we will have 2 graphs and we can try to match them? 
>		problem I see is if edge's orientation and length represents how the nodes are connected **and** if we try to match even these edges then different perspectives would fail.
>			then how are graph nodes connected? 
^super-glue-graph-matching


exact graph matching -- graph isomorphisim problem
exact matching of a graph to another part of graph -- subgraph isomorphism problem


Learning Graph matching - [link](http://robotics.stanford.edu/~quocle/CaeCheLeSmo07.pdf)
