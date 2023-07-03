## 2023.06.30
[[Progress#^696784|daily_stuff]]

data loader is easy since motion boundaries are already present 
need to confirm if they are images or some other format 

for loss function, I need to use binary cross entropy with class imbalance problem 

>[!question] does applying motion boundary for both the images make sense? 
>- maybe it does, because we are trying to predict the forward flow of the optical flow 


from STDC paper 
![[stdc_detail_loss.png|400]]


from nanoflownet about implementation details 
![[nanoflownet_impl.png|400]]


## 2023.07.02

super inefficient 
BCEloss is off the charts and super negative 
it should be comparable to dice loss 
I am using sigmoid cross entropy
so value of sigmoid(0) is not 0 
so this will make network predict with an offset of -128 to 128

so in my test
for noisy image I will subtract 128 
dont add any noise 
and call bceloss 
it should be 0 

## 2023.07.03

I want to know if detail loss is well balanced among others. 
so I need to print the values during the training
but need to figure out how to do that in tf1


