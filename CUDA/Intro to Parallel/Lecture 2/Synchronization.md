## Barrier

`__syncthreads();`

## Atomic
every thread will increment only when no other thread is active 

atomic add, sub, min, xor
CAS - anything can be implemented using this 


### limitations
no ordering 
	will be problematic for floating point operations

slow

