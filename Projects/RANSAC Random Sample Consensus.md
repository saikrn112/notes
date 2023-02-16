we have data samples to fit some model

1. take least number of random data samples required data samples for fitting the model 
2. using the above model check how many other data samples are falling within threshold 
3. keep track of the number of inliers
4. take another sample and repeat 2, 3
5. after few iterations or if the number of inliers is greater than certain threshold then stop RANSAC
