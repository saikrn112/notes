
- need environment 
- PPO implementation 
	- custom vs  -- evaluating is hard
	- tensorflow agents
		- going through documentation is hard
- replay buffer
- what is one epoch defined as ? 
	- is this related with episodes?
- how is TD lambda involved here? 

3 steps 
- integrate environment into tf agents 
	- converting discrete action space to continuous
		- how to verify
- using ppo agent instead of dqn agent
	- corresponding parameters 

verification 
- are we using ppoagent correctly? 
	- cartpole - Swati

- data collection 
	- small trajectory 
	- multiple small trajectories 



overfit on 1 trajectory 
- generalize (stretch goal)

env -- Manoj
- rewards 
- actions
- states 

agent - PPO - code
policy 

train
- replay buffer



- [ ] setup the environment 
	- [ ] pull tf agents 
	- [ ] 






# PPO
proximal policy optimization
- how are the advantages computed 
- reward ratio mathematically 

observations -> policy - > actions

version of actor critic 
