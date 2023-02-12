1. maximize arithmetic intensity
	1. $\frac{math}{memory}$
		1. maximize compute ops speed 
		2. minimize the time spent on memory access
			- use shared memories and local memory instead of global memory, caching is faster and speed of access is faster
			- use coalesed global memory
				- GPU is most efficient when threads read or write continguous memory locations 
1. Avoid thread divergence
	1. if else conditions
	2. or different for loop conditions
