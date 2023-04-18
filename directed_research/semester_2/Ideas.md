
optical flow loss + photometric loss? 
combination of decreasing the model size further and resizing image

chunking + 0.7MB model 


```

So for the research, here's an additional point: we needed smaller networks that can be distributed also because bigger networks have a huge carbon footprint and a strain on the network bandwidth


I did think about that in the context of image chunking not sure if I understood your thought right. my thought was we can run parallel encoder networks for each chunk, combine the feature vectors at the lowest level and predict the final optical flow. not sure if we get any advantage of this but maybe worth a try. let me know your thoughts!
```

## 2023.04.05
chunking + gaussian blur + metric 
chunking with overlap
- amend the test code 

new network architecture similar to mask rcnn
![[discussion_2023_04_05.jpeg]]

>[!INFO] bounding boxes idea similar to mask rcnn
> given an image of smaller size (M/4 and N/4)
> we feed it into 0.7MB model 
> we get some output of same size (M/4 and N/4) and also bounding boxes as to where to focus more
> we use the bounding boxes and crop the region where we should focus and feed to another network for finer flow






##### Chunking with overlap
- run test inference with slightly more than half of the image size
	- new branch from baseline_xy
- stack them along the dimension
- code for overlap and check

## 2023.04.06

 ![[2023.04.06_DR_discussion.jpg]]
>[!INFO] Algorithmic task evaluation
>
>so this will be the main theme of the paper 
>idea is if we can develop a neural network which can minimize a certain metric defined for a specific task
>
>so in the picture we have **x** which is given to algorithm **A** and gives out **y**
>- now this algorithm is specific for a task like navigating through cluttered environment
>- this task is evaluated with a metric **M**
>  
>  task is to create a neural network which approximates **both** algorithm **A** and evaluation metric **M** and try to minimize this metric if give some noise to the input
>  
>  basically we want to understand how to change the input so that metric is minimal
>  in what instances is the algorithm failing to perform 


<div class="my-section">
## this is another section
- hellow 
</div>



white-box attacks vs black-box attacks 
> attacks on known models vs unknown models

references: 
[one pixel attack](https://arxiv.org/pdf/1710.08864.pdf)
[attacking optical flow](https://arxiv.org/pdf/1910.10053.pdf)



>[!INFO]
>small model bottleneck could be loading and unloading data 
>
>getting close to ICRA 
>bottleneck  on noise characterization
>given architecture is fixed, changing 







Cost volume - explanation



![[correlation_block_orig_impl.png]]



## 2023.04.12

deconv could be the reason for slowness
avoid deconv using
```
first I need to create a network which removes the deconv layers 
or rather we will have only 1 deconv layer 
and upsampling from then on 
like in GAN we will basically use only resblocks 
prior to resblock we will have conv and then bn relu and add the resized values so convolution is not changing the shape in this case 
```

GAN 
resize - resblock add
convex upsampling

train on uncertainity 
- linear softplus


pixel shuffling

## 2023.04.14

if we train a neural network to predict image motion

## 2023.04.15
train the baseline network with scaled down optical flow values
train the resizing network with a lot of init neurons
