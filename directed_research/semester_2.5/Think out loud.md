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
```
detail loss[116.575287]
optical loss[43.6578903]
unc accum loss[150603.781]
```

## 2023.07.04

scared that research might not go anywhere. 
need to implement atleast one different idea everyday so that I have something quantifiable by the end of month

so nanoflownet is using focal loss instead of detail loss as mentioned in the STDC network paper 

another difference between nanoflownet and my current implementation
- instead of trying to force the optical flow to learn motion boundary, I am predicting a new channel altogether

>[!idea1]
>start simple, 
>use a simple conv deconv block 
>at the encoder take a separate differernt conv and use that for motion boundary? 
>do the same thing but at decoder 
>


need to evaluate sintel with best model 400 epochs 
the other was trained for 100 epochs


- [x] flying chairs wo chunking
- [x] flying chairs w chunking
- [x] sintel clean wo chunking
- [x] sintel final wo chunking
- [x] sintel clean w chunking
- [x] sintel final w chunking


[[Multiscale + Uncertainity 400 Epochs (Best Model)]]



for visualiation issue 
this should work 
```
python Train.py \
--ExperimentFileName="multiscale_uncertainity_2" \
--NetworkName=Network.MultiScaleResNet \
--MiniBatchSize=32 \
--LoadCheckPoint=0 \
--LR=1e-4 \
--InitNeurons=32 \
--LossFuncName=MultiscaleSL1-1 \
--UncType=LinearSoftplus \
--NumSubBlocks=2 \
--NumEpochs=1
```

## 2023.07.11
yesterday made som modifications to the metrics class 