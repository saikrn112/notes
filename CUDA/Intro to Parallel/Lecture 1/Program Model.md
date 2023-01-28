Host - CPU
Device - GPU

CUDA compiles the program to run on CPU and GPU

assuemes that GPU is coprocessor for CPU

CUDA assumes
	CPU and GPU has their memory

CPU directs the workflow
it is responsible for two main operations 
moving data CPU -> GPU and vice versa

`cudaMemcpu`
`cudaMallac`

programs that are invoked on GPU are called kernels

>[!quote] Jargon phrase 
>host launches kernels on the device

