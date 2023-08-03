
Agenda:
- Background 
	- explaining the motivation
	- problem statement
- Approaches
	- Stereo - which didnt work
	- ToF
	- Demo of how we are able to get estimates


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
 Work
	- we started with a simple stereo camera 
	- how stereo camera works
	- show a sample RGB image and corresponding depth from jupyter notebook
		- used a simple scanmatching algorithm 
		- viola show the depth from sample stereo image
		- brighter the closer
		- darker the farther (or couldnt estimate the depth precisely)
	- ran opencv algorithm (show the GiF)
		- on our dataset
		- clearly it is not great
		- primary reasons for why this algorithm is failing
			- lack of sufficient texture
	- Tried to improvise
		- custom algorithm based on heuristics
			- works better for depth range of 0.3m-1m
			- but results are not robust enough
			- used a bag of tricks 
			- came up with a neat little architecture
	- ToF
		- show the algorithm
			- explain a little as to what is happening
				- use ros pictures if need to show the registration
				- used rgb mask
				- cropped the output
				- fit a plane and depth/yaw estimates
			- `see how I can modify it to show more global picture`
		- show some sample results of the demo as a gif
		- give the live demo
			- this is a manual flight but as the estimates get better and better with segmentation we can easily integrate this pipeline


