recap about whitening transformation
- essentially data is transformed to something else 
- this is because hessian of fmse loss ends up with a term $XX^{T}$

z - scoring
	dimesions are taken independently
	ignores the covariance
	and makes std dev to 1 


---
#### Binary Classification
- simplest logistic regression --- why logistic?
	- even though it's called regression it's actually used for classification
- predicts probablitiy of input being class 1


log loss

---
#### multiclass classifiction
softmax regression
we need to one hot encoding for this

why cant we assign simple numbers
	but distance metric is not accurate
	for example we are comparing happy and sad face
	and fmse to compare distance would grow as the number of classes grow and it doesnt make sense

>[!INFO]- how cross entropy naturally comes using MLE
>![[cross_entropy_v_mse.png]]

