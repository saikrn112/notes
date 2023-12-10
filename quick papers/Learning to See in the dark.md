New dataset 
- raw short exposure low light images
- corresponding long expsoure high quality reference images
what is "raw" here? 

less than 0.1 lux of illumination 
lux - lumens/second or watt/m2

denoising - remove noise
burst of images - burst alignment algorithms
demosaicing - is it debayring? yup!




## related work


### Denoising
denoising state of the art which works on real world dataset
- BM3D
- sparse coding

some deep learning techniques - evaluated on synthetic dataset


### Low light image enhancement
- histogram equalization
- gamma correction
- illumination map estimation 
- Retinex model

### Datasets
some datasets from [[Datasets#^74e619]]


filter arrays - Bayer, X-Trans

Sony α7S II x300 vs Fujifilm X-T2 x300

light meter for illuminance measurement


## Traditional Methods
![[seeing_in_the_dark_methods_comparison.png]]


>[!INFO]- what does subtracting black level even mean? 
>![[subtracting_black_level.png]]


## Training
flipping and rotation data augmentation


## Comparison

BM3D - non blind denoising - requires noise level as parameter

>[!INFO]- what is color distortion due to post hoc denoising?
>![[color-distortion-due-to-post-hoc-denoising.png]]

burst denoising 
- per pixel median

>[!INFO]- how is PSNR and SSIM calculated for original and reconstructed image?
>[[testing_metrics.py]]


couldnt learn historgram stretching
