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