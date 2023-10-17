
- [[#Precision Recall|Precision Recall]]
- [[#F1 score|F1 score]]



## Precision Recall


Precision - out of number of predictions, how many are correct
>Example: 3 classes, A - 30, B - 30, C - 30
>example: out of 90 predictions, how many are correctly A, correctly B, correctly C 
> if model says 23 A: out of 23, how many are true positive / (true positive + false positive) (positive indicates class A)

Recall - out of total samples for a class how many did model get right
> example: out of 30 predictions for A, how many did model correctly predict that it's A
> if model says 10 A: out of 10, true positive / (true positive + false negative)

$$
\begin{align}
Precision &= \frac{TP}{TP+FP} \\
Recall &= \frac{TP}{TP+FN}
\end{align}
$$



## F1 score

- combines precision and recall 


$$
\begin{align}
F1 score &= \frac{1}{\frac{1}{Precision}+\frac{1}{Recall}} 
\end{align}
$$
