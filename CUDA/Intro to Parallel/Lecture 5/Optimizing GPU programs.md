APOD - systematic optimization
Analyse, 
Parallelize, 
Optimize
Deploy


Amdalh's law
max speed = 1/(1-p) p -- parallalizable time


## Transpose example
only memory moving 

![[is_bw_less_due_to_coalesce.png]]

reading is good coalesce but writing is bad coalesce
![[read_write.png]] 


>[!quote]
> always check if memory bandwidth is optimal > 75% for good parallizeation

### Tiled transpose 
![[tiled transpose.png]]
code
![[tiled_transpose_code.png]]

![[IMG_936EA40BF154-1.jpeg]]

we need `syncthreads` because they are not reading the same data 106 again at line 109. 


but that syncthreads is expensive since not all the threads are done processing 

## Little's Law
useful bytes delivered  = average latency * bandwidth

