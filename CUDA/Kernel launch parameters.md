```
kernel <<< dim3(bx, by, bz) , dim3(tx, ty, tz), shmem >>> (args)
```

```
dim3(x,y,z)
	dim3(w,1,1) == dim3(w) == w

shmem - shared memory per block in bytes
```

so essentially we can launch 1, 2 or 3 dimensional blocks or threads

every kernel has access to these dimensionality structures
```
threadIdx  -
blockDim   -
blockIdx   -
gridDim    -
```

### Example
```
square <<< 1, 64 >>> (d_out, d_in);
1  - block
64 - threads
```

1. can run many blocks at once 
2. maximum number of `threads/block` old (512), new (1024)

if we want to launch with 1280 threads 
then 
```
a. square <<< 10, 128 >>> (...)
b. square <<< 5, 256 >>> (...)
c. square <<< 1, 1280 >>> (...)
```
`a` and `b` are valid but `c` is not


![[Kernel_launch_parameters.png]]