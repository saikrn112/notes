resources 
[Batch Norm Explained Visually — How it works, and why neural networks need it | by Ketan Doshi | Towards Data Science](https://towardsdatascience.com/batch-norm-explained-visually-how-it-works-and-why-neural-networks-need-it-b18919692739)
[Batch Norm Explained Visually — Why does it work? | by Ketan Doshi | Towards Data Science](https://towardsdatascience.com/batch-norm-explained-visually-why-does-it-work-90b98bcc58a0)

## Working
1. compute latest mean and std for new activations
2. normalize the activations based on these new activations
3. scale and add mean to the activations so that they are not zero centered and unit variance anymore (learnable)
4. compute Exponential Moving Average to be used during inferences

![[batch_Normalization_notes.png]]

## Instance Normalization
instance normalization applies only one sample 
![[instance_normalization.png]]