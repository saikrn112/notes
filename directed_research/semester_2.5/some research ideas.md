currently where am I at ? 
looking at the report
- i tried a bunch of things to speed up 
- I need to profile and see how many are edge quantizable? 
- need to make experiments that can run on those 

there are a bunch of ideas that I discussed with Nitin to train optical flow 
- edge boundary based training 
- something to do with obstacles? no 
- one idea was to use dilated cost volume for fast optical flow 
- another idea 

target image idea for the presentation 

recording 
2023.05.02
- talking about presentation 
- cross verify the numbers again 

2023.04.12
- hack by shallow decoder 
- something with reshape to get original size 
- predicting global optical flow 3 x 1 with only decoder -- his other experimental paper 

2023.04.11 
- nanoflownet comparison 



----
comparison networks 
checkout todo list which prof sent


----
## 2023.06.30

>[!info]
>do the same thing as STDC seg network
>have a detail head at conv block 
>and then apply the detail loss 


>[!info]
>instead of low-level spatial information I will assume that optical flow deconv should give a motion boundary 
>apply conv block + upsampling as well 


----
## 2023.07.2
>[!Idea]
Idea is to analyse how much trade off we can tolerate in optical flow EPE accuracy for a robotics application. 



