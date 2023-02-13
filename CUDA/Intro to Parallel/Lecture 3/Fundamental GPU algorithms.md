## Reduce
Properties to perform reduce
1. set of elements 
2. reduction operator 
	1. binary
	2. associative
serial implementation
![[reduce_parallel.png]]
`logn` computes 

## Scan
addresses a set of problems which are otherwise difficult to parallelize
Inputs
1. input array
2. binary associatve operator
3. identity element <-- additional apart from reduce
2 popular flavors
1. inclusive - includes current element in the scan operation
2. exclusive - excludes current element
Inclusive scan 
![[inclusive_scan_complexity.png]]
### Hillis and Steele
work - nlogn
steps - logn
`logn`th neighbour add
![[IMG_3AE4AF7C0653-1.jpeg]]

### Blelloch Scan

1. reduction - keep the intermediate results of reduction
	1. work - n
	2. steps - logn
2. insert an identity element at the right most end
3. downsweep
	1. work - n
	2. steps - logn
![[IMG_178BE5D9F6BD-1.jpeg]]
![[IMG_51D4A70B7F62-1 1.jpeg]]


## Histogram
1. atomics - but they do limit the computation, lesser the number of bins more computation time it is
2. local histogram + reduction
3. sort and "reduce by key" -- algorithms are not yet covered