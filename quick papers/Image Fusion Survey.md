parallelax in CV 
scale differences how are they affecting the image fusion


3 types of Deep Fusion 
- AE
- CNN
- GAN


FusionGAN- Infrared and visible iamge fusion
- need to understand the loss functions in Gans
pretty neat loss 
generator - fusion gan + content loss 
discriminator - 

how do you measure entropy between two histograms? 


DeepFuse - nice fusion of multiple focused images


GANFuse - fuses multi exposure shots
- supervised
- compares the content with pixel wise and gradient wise
	- along with discriminator and generative loss


![[gan_stable_training.png]] [here](https://machinelearningmastery.com/how-to-train-stable-generative-adversarial-networks/)

Sharpening Fusion
- multi spectral sharpening
- hyper spectral sharpening

**Multispectral Sharpening:**
- **Definition:** Multispectral sharpening involves enhancing the spatial resolution of a lower-resolution multispectral image by incorporating details from a higher-resolution panchromatic (grayscale) image.
- **Process:** The high-resolution panchromatic image is fused with the lower-resolution multispectral image to create a new multispectral image with improved spatial details.
- **Application:** This technique is commonly used in satellite image processing, where a panchromatic image with high spatial resolution is fused with multispectral images to create a high-resolution multispectral image.

U2Fusion 
- unsupervised
- multi-modal, multi-exposure, multi-focus