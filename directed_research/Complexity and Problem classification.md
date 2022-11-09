Wiki [link](https://en.wikipedia.org/wiki/Time_complexity#Quasi-polynomial_time) for this

Logarithmic - $\mathcal{O}(logn)$
Linear - $\mathcal{O}(n)$
Quasilinear - log-linear time - $\mathcal{O}(n log^{k} n)$ -- in place merge sort
					if $k=1$ then linearithmic time

sub-quadratic time - $o(n^{2})$

Polynomial time - $\mathcal{O}(n^{k})$ - running time is upper bounded by a polynomial expression in the size of the input
Example - maximum matchings in graphs
>[!INFO]
	Problems for which deterministic polynomial time algo exists belong to the complexity class P
	Polynomial time -- tractable, feasible, efficient or fast

Super polynomial time - these algos are impractical 


Quasi-polynomial time - $2^{\mathcal{O}log^{c}n}$ - algos that run longer than polynomial time but not exponential 
	if $c =1$ -- it's polynomial time
	   $c < 1$ sub linear time 
	they typically arise when _NP-hard_ problem is reduced to another problem 

Exponential time - $2^{poly(n)}$


Complexity classes
1. **P** - complexity class of _decision_ problems that can be solved on _deterministic turing machine_ in polynomial time
2. **NP** - that can be solved on a _non-deterministic turing machine_ in polynomial time. These set of problems where the answer is "yes" have proofs _verfiable_ in polynomial time by a deterministic turing machine. on the otherhand, these are a set of problems that can be _solved_ in polynomial time. 
3. **ZPP** - that can be solved with zero error on _probabilistic turing machine_ in polynomial time



P vs NP Problem
does every problem whose solution can be quickly verified can also be quickly solved? 

![[Pasted image 20220920180427.png]]