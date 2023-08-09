previous [[directed_research/semester_2/Ideas|Ideas]]

## 2023.06.14

reviewing previous calls
goal should be to increase the speed and accuracy of the optical flow network. 

For tomorrow's meeting with him, 
- I want to go over some of the links 
- let's start with implementing DCVNet 
- train the network based on the gradient of the flow and uncertainity

>[!ERROR] URGENT
go over previous numbers and make sure they are correct 


what is happening in optical flow? 
- [Fast cost-volume filtering for visual correspondence and beyond | IEEE Conference Publication | IEEE Xplore](https://ieeexplore.ieee.org/document/5995372)
- [openaccess.thecvf.com/content_cvpr_2015/papers/Wulff_Efficient_Sparse-to-Dense_Optical_2015_CVPR_paper.pdf](https://openaccess.thecvf.com/content_cvpr_2015/papers/Wulff_Efficient_Sparse-to-Dense_Optical_2015_CVPR_paper.pdf)
- [[1606.00373] Deeper Depth Prediction with Fully Convolutional Residual Networks (arxiv.org)](https://arxiv.org/abs/1606.00373)



## 2023.06.21

I need to calculate where we stand on Sintel dataset so that we can see how much to improve 
for that I need to know where my models are and which ones to focus on 
I need a consolidated list of models or star models in my research so far


## 2023.06.24


multiscaling network with chunking for highest fps and accuracy

we can try with different resolutions 
I have already tried sintel with baseline and multiscale 
I need to try the same with multiscale chunking 
I havent tried sintel because I dont have a data loader 
ok I did try sintel because I do have the dataloader



## 2023.06.28

they achieved 7, but at what scale?
what is the image resolution? 


160 x 120


to use the edge detail loss, I need to figure out a loss function

## 2023.06.29
read some paper 

## 2023.06.30

^696784

I will try detail loss with 2 networks 
- multiscale 
- simple 

before that I need to create a loss function
and a data loader 

## 2023.07.02
did some coding for making sure detail loss is making sense 

## 2023.07.03

finally got the thing working 
need to wait for it to train

>[!Info] Prof Nitin
>- Results are not great, required accuracy 7px-10px
>- we need to train better
> ---
>- check evaluation to make sure EPE
>- use a pretrained network to confirm the numbers from existing paper 
>- try UNet with multiscale
>




## 2023.07.04

for multiscale motion boundary loss 
![[training_progress.png]]
![[trainig_progress.png]]


## 2023.07.24

I need different speeds with varying accuracies

do some research as to what are some good metrics for a task 
- go through Nitin's paper



## 2023.08.07

- flyingthings3d numbers
- navstack bebop



---

----

compare with depth 

- depth sensor d435



---
what am I trying to achieve ? 
-- still need to figure that out


---
