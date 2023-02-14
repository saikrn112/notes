## Compat or filter

operate only on subset of items
![[compat_formal_def.png]]
### why dense over sparse outputs? 

![[dense_over_sparse_compat.png]]
dont really see how it is useful.
we still have launch 52 threads
	in earlier case 13 threads are active
	now all 52 are active


### Compact steps

^e34d7a

![[compat_steps.png]]

in the 4th step we are scatter input to output address only if the predicate is true
see below example 
![[compact_algo_example.png]]

>[!question]
>how do we increment the addressses again? 
>does that not need atomic add? 


compat example for computer graphics triangles 
![[cgi_triangles.png]]


---
Allocation strategy using compact 
idea is to determine how much memory to allocate for every true input
instead of storing 1 or 0 and performing exclusive scan on that 
	we can store the number of memory that is needed and
	then perform exclusive scan
	the final element will give us the total memory that is needed
	and this will also give us the underlying memory address to use
	![[allocation_strategy_using_scan.png]]