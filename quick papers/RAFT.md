# Summary
- as usual projects image features to latent space
- it computes correlations at each scale at reference coordinates
- uses the correlations and flow to compute ==motion features==
- using context features as reference, GRU network finds out which pixels are correlated with previous inputs and which are not
- these outputs (coarse flow, upsampling mask and state) from GRU is used in next ==iteration== to refine the predictions. hence coarse to fine
	- so the coarse_flow is used to predict where the coordinates fall in the next frame and get correlations with respect to those coords, if the coordinates are correct then correlations will be high. 
	- if the correlations are high then GRU block will allow all the previous state outputs or atleast give equal weights to current and previous state output
	- upsampling mask is used to upsample the lower scale flow fields to higher scale using convex upsampling strategy

![[raft_update_block.png]]

main architecture 
![[raft_archi.png]]


## Convex Upsampling
it learns how to upscale by taking some weighted linear combination, except weights are coming from the network
how is it different from convTranspose? 
- very different, in ConvTranspose we apply convolutions and upscale it 
- here we are taking a linear combination
![[convex_upsampling.png]]