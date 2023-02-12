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
1. reduction
2. downsweep
### Blelloch Scan
## Histogram
