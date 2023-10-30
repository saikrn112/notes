##### Probabilistic Estimation
>inferring the characteristics of the current uncertainty exposed by r.v.s from the observation of the values they yield.
-MadrigalBlanco Book

##### Probability function 
maps random events to a value in interval $[0,1]$  
value is based on frequentist paradigm - bayesian paradigm

Mutual exclusion vs Mutual Independence 
Two random events are 
- Mutually exclusive: if they cannot occur simultaneously 
- Mutually independent: if their occurance is not dependent on each other
hence exclusion implies independence but not the other way around.

![[mutually_exclusive_vs_independence.png|500]]

##### Summary of  Formulation
> a probability space formally defines 
> - the set of individual outcomes of the stochastic process of interest ( Ω ), 
> - a useful and well-formed grouping for those outcomes into random events ( E ) and 
> - a probability measure over those events ( P ).


##### Random Variable
>A random variable (r.v. for short) is just a function that translates the outcomes of a given probability space (Ω, E , P ) into real numbers or vectors of real numbers.




##### Independent and Identically Distributed (IID) random variables
a collection is IID if each random variable
- has same probability distribution as the others
- all are mutually independent

##### Likelihood
blog referred - [link](https://towardsdatascience.com/maximum-likelihood-vs-bayesian-estimation-dd2eb4dfda8a)
how likely something can happen
in probability theory we try to estimate how likely an observation from random variable can occur given a probability distribution function 
if $D_1,D_2,D_3,D_4.. D_n$ define observed data 
and $\theta_1,\theta_2,\theta_3,\theta_4,...\theta_n$ define parameters of the underlying random variable probability function $f$
then Likelihood is 
$$L(\theta_1,...,\theta_n|D_1,D_2,...D_n) = f(D_1,D_2,...D_n|\theta_1,...,\theta_n)$$

##### Maximum Likelihood Estimation
blog referred - [link](https://towardsdatascience.com/maximum-likelihood-vs-bayesian-estimation-dd2eb4dfda8a)
the process of maximizing the likelihood of these observations by chaning parameters is the MLE 
taking log likelihood since derivatives of product of probabilities is hard to compute 
