
`__global__` - C lang declarative specifier. this is how cuda know this is a gpu program and not cpu program

`threadIdx` - structure x , y, z  indices start from `0`

`__syncthreads();` -- barrier so that all threads stop here
`cudaDeviceSynchronize()` -- host waits for the device to finish execution
	by default when 2 kernels are called, the above keyword is applied

`__shared__` -- keyword for shared memory in a block

`atomicCAS()` - compare and swap
`atomicAdd()`