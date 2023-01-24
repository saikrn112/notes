
Phase I
- [ ] custom sets
- [ ] tune the number of features for better homography
- [ ] identify what other parameters to tune
- [ ] blending part
- [ ] if condition for not using an image if features are less
- [ ] checkout poisson blending
- [ ] **implement own findHomography**
- [ ] need to figure out why test 2 with 3rd image is going crap
- [ ] run it on test set 3

Phase II
- [ ] adapt the data generation code to run on my windows machine
- [ ] homography net check why it is not converging
- [x] write the TensorDLT code
- [ ] use kornia's STN
- [ ] concatenate models

Submission Guidelines
- [ ] folder structure
- [ ] `ModelType` argument
- [ ] size of submission file shouldnt be more than 100MB

**Report**
Phase I
- [ ] input and output images after each component
- [ ] how did we blend common region
- [ ] how images are rejected
Phase II
- [ ] supervised homography for any 4 images from Train/Val/Test
- [ ] unsupervised homography for any 4 images from Train/Val/Test
- [ ] average EPE ($L_{2}$ loss) for supervised 
- [ ] average EPE ($L_{2}$ loss) for unsupervised 
- [ ] runtime forward pass of the network after the graph has been initalized
- [ ] Input and Output panoramas for test images from Phase I test set