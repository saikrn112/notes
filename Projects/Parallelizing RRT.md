high level walk through
- copy the nodes between nodeA and nodeB to GPU
- kernel is just checking if the node is obstacle or not
	- they write this information to shared memory of the thread block
- and all the threads in tandem run reduce the max
- 