
### Resources 
https://github.com/NitinJSanket/prgeyeomni


1. understand optical flow outputs
2. understand optical flow dataset
3. need to see how the tensorboard will show networks using TF2

will try with the CIFAR10 model generated using TF1 again
check the accuracy of that output


### implementation details
scoping the layer to prevent ugliness


3 types of uncertainity 
- Aleatoric -- internal randomness - but how did they qualitatively adapt for optical flow? 
- Inlier
- LinearSoftPlus
they are being used for testing another paper

Loss functions 
- SL2-1 - supervised L2 loss
- SL1-1 - supervised L1 loss
- PhotoL1-1 - self supervised Photometric L1 loss
- PhotoChab-1 - self supervised Photometric Chabonier loss
- SSIM-1 - sturcture similarity index loss? 
- PhotoRobust - 

regression using int8
https://stackoverflow.com/questions/64447009/very-high-error-after-full-integer-quantization-of-a-regression-network

### Results

Optical Flow Photometric L2 
int8 model - 79.29372144199442
full model - 4.709523426622764

HSV Photometric L2 
int8 model  
total L1 Mean:84.33638314531349
total L2 Mean:106.72953766401498

![[Pasted image 20221206035817.png]]

full model 
total L1 Mean:86.50669585256865
total L2 Mean:110.5262273568818