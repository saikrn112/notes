different threads interact with each other using memory

how to map tasks(threads) and memory they are using to communicate

#### Map

`one to one op`

#### Gather

`many to one op`
each pixel taking other 4 pixels to compute average

#### Scatter

`one to many op`

rather than each pixel taking 4 other pixels the current pixel can write 1/3 of it's value to other neighbouring pixels. problem with it is multiple threads are writing to the same location potentially. need to lock this

#### Stencil 

`special case of gather (several to one)`
but it will be run for every pixel rather than selected pixels i.e no if conditions

tasks read input from a fixed neighbourhood in an array
makes convolution simple
many threads are reusing the same data
2D, 3D Von neumann
2D Moore pattern

>[!question]
>how many times are the pixels read in the above stencils


#### Transpose 
`special case of map`

Array of Structure (AoS)
Structure of Arrays (SoA)

AoS -> Transpose -> SoA

---

#### reduce 

`all to one`

#### scan or sort
`all to all`
