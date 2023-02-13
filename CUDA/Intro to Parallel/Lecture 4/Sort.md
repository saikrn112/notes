efficient parallel algos are
- keep hardware busy 
- limit branch divergence
- coalesed access 

## Parallel Merge
![[parallel_merge.png]]
each thread will launch per element
each thread knows where that element is corresponding to that list using `threadId.x`
it will do binary search in other list to know it's location in other list 
final location of that element is list1 loc + list2 loc


## merge sort overview

![[merge_sort.png]]