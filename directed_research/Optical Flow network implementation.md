
### Resources 
https://github.com/NitinJSanket/prgeyeomni


1. understand optical flow outputs
2. understand optical flow dataset
3. need to see how the tensorboard will show networks using TF2

will try with the CIFAR10 model generated using TF1 again
check the accuracy of that output

### Dataset
brief description from official website -- [link](https://lmb.informatik.uni-freiburg.de/resources/datasets/FlyingChairs.en.html)
2 images 
2 image object IDs -- ??
suffix_flow_01 and suffix_flow_10 -- forward and backward flows -- This is of interest
suffix_occ_01 and suffix_occ_10 -- occlusions 
suffix_occ_weights_01 and suffix_occ_weights_10 -- ?? 
suffix_mb_01 and suffix_mb_10 -- motion boundaries 
suffix_mb_weights_01 and suffix_mb_weights_10 -- motion boundary weights


### Implementation details
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
- SSIM-1 - sturcture similarity index loss
- PhotoRobust - 

regression using int8
https://stackoverflow.com/questions/64447009/very-high-error-after-full-integer-quantization-of-a-regression-network

### Results

Optical Flow Photometric L2 
```
int8 model - 79.29372144199442
full model - 4.709523426622764
```

HSV photometric 
```
int 8 model 
total L1 Mean:9.952038832631455
total L2 Mean:15.960667593762867

full model 
total L1 Mean:9.499303572683623
total L2 Mean:15.627450042493416
```

Training
![[Pasted image 20221206035817.png]]
Prediction

![[Pasted image 20221206055235.png]]

## Flow Tests

### clipping flow values
histogram of 800 image flows from flying chairs2
```
mean_x = -0.2
mean_y = 0.3
std_x = 12.9
std_y = 13.6
```

histogram before and after standardizing 0-255
![[before_after_hist.png]]
histogram -- `OutputStats.ipynb`
![[Pasted image 20221206215715.png]]

![[clip_sudden_loss_fall.png]]

![[after_full_train.png]]

before flow
![[before_flow.png]]


![[after_standardize_flow.png]]

flow_hsv after 70 epochs with gradeint clip and regularization
![[Pasted image 20221210083644.png]]

flow with hsv without scalling 
SL-1
200 epochs
800 images train data
![[Pasted image 20221210111845.png]]


so photochab has also not worked. 
what are the next steps? 
I am trying the model which NJ gave. 

apart from that I can try binning data. I was expecting the HSV thing to work though. 
why could it not work? 
UNet is probably thing I can try 

implemented UNet architecture
![[Pasted image 20221211163144.png]]

implemented only 1 layer since more than one is not working for some reason
more straight than anything else

![[Pasted image 20221211175717.png]]


![[loss_unet_l5_32k.png]]

![[unet_l5_32k.png]]


next steps
- report
- pyramidal structure can be tried 

Hashing 
- learn a hash function (see if a normal NN is able to learn this representation


HSV flow without standardization
```
total L1 Mean:29.699766159057617
total L2 Mean:37.74184036254883
```
quantized model on CPU
```
Time consumed in working:  2.364023447036743
```

quantized model on TPU
```
Time consumed in working:  0.4540226459503174
```



flow viz proof

![[Pasted image 20221214194113.png]]