## Auto Encoders
1. train the network unsupervised unlabelled data using encoder and decoder 
2. the encoded data is useful for other tasks -> **unsupervised pre-training**
3. this network is **fine-tuned** for other classification or regression tasks 

loss functions has to be convex
if it has saddle points then it gradients are zero 
	but that point is neither local maxima nor local minima

Deep linear network for auto encoders surprisingly give rise to saddle points in the loss function wrt parameters


## Supervised pre-training
pretty useful for domains where there are very few labelled data
>[!question]
>are unsupervised pretraining also useful?  #whitehill

inputs should be "relatively" same? 
>[!question]
>why relatively similar ? shouldnt they be exactly same ? #whitehill 


## Universal function approximation theorem
$$
\begin{align}
\lVert f(x) - \hat{f}(x) \rVert < \epsilon \forall x
\end{align}
$$
This theorem is just saying that we can approximate any sort of multi dimensional function with just 3 layers (1 hidden layer) and with sufficient enough neurons

## Regularization
$L_{2}$ is popular 
there can be $L_{1}$ regularization

$L_{2}$ regularization is equivalent to **weight decay**
$L_{2}$ regularization is also equivalent to agumenting data with Gaussion noise (for a specific setting)

