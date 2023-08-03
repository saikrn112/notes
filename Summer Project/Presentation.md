


story time:
background slides 
- what is the problem we are trying to solve 
	- navigation in indoor warehouse
	- we are working in an envs like warehouse where there are no/less features
	- qvio drifts 
	- so we need a way to correct this drift
	- so Howard, Pratyush, Yoni, Bharat came up with Structure Aided Visual Localization
		- which makes use of the elements present in the environment
- My Job 
	- is enhance this algorithm with the help of additional sensors 
	- like stereo and ToF
	- effectively we need a way to compute the depth, yaw and pitch measurements more accurately. (show the picture I have)
- Work
	- we started with a simple stereo camera 
	- how stereo camera works
	- show a sample RGB image and corresponding depth from jupyter notebook
		- used a simple scanmatching algorithm 
		- viola show the depth from sample stereo image
	- ran opencv algorithm (show the GiF)
		- brighter the closer
		- darker the farther (or couldnt estimate the depth precisely)
		- 


