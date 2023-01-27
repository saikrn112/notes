

>[!INFO] Bias and regularization 
>
>## Question
>I was reading about why we dont regularize bias and encountered few statements that I am not able understand.  
> 1.  model with high bias have low variance and vice versa
> 2.  if variance is high then model could potentially be overfitted
> 3.  from DL book “_Also, regularizing the bias parameters can introduce a significant amount of underfitting.”_
> 
> In general, what is model variance and how is it related to bias and overfitting/underfitting?
> 
> ## Jacob's answer
> "Model variance" refers to how much the model's predictions (and the resulting prediction error) would change as a result of training the **same** model on a **different** sample from the same training distribution. A highly parameterized model will, all else being equal, be much more sensitive (in terms of the learned parameter values and the resulting predictions) to the particular sample of data it was trained on, compared to a less parameterized model.
> 
> "Model bias" refers to estimation error due to structural limitations in the mathematical functions a model can represent -- for instance, no linear regression model is going to do a great job in predicting quadratically structured data.
> 
> Confusingly, the term "bias" in the phrase "model bias" is very different from the term "bias" in the phrase "bias term", and is also very different from the term "bias" in "estimation bias".
> 
> If you do not include a **bias** **term**, then you are immediately increasing the **model bias** -- I showed an example of this during the first few lectures of the course, where a strictly linear predictor (yhat = x\*w) cannot accurately model a dataset whose mean is not at the origin. Similarly, if you highly regularize the bias term, then you are reducing how effective it is since its absolute value is discouraged from becoming far from 0. If the mean of the dataset is indeed far from the origin, then you have a similar problem as the one I showed.
> 
> ## Followup thought
> Got it. 
> 3rd point seems clear now. Like you said, I did confuse myself with Model bias and bias term here.
> as for 2nd point I posted above, correct me if I am wrong, here we are computing the model variance based on the prediction errors, right? 
> 
> so if the variance is high then it means that errors are changing too much for different training samples, that means model hasnt learnt a more generic value or _underfit_ the dataset
> 
> similarly, if the variance is low then it means that errors are not changing much so it could potentially _overfit_. 
> this inference is going against what I just posted. Can you clarify this?
 





