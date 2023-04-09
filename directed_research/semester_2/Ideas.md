
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











