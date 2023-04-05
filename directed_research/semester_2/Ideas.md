
optical flow loss + photometric loss? 
combination of decreasing the model size further and resizing image

chunking + 0.7MB model 
chunking + gaussian blur + metric 

```

So for the research, here's an additional point: we needed smaller networks that can be distributed also because bigger networks have a huge carbon footprint and a strain on the network bandwidth


I did think about that in the context of image chunking not sure if I understood your thought right. my thought was we can run parallel encoder networks for each chunk, combine the feature vectors at the lowest level and predict the final optical flow. not sure if we get any advantage of this but maybe worth a try. let me know your thoughts!
```



