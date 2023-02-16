[Histogram of Oriented Gradients explained using OpenCV (learnopencv.com)](https://learnopencv.com/histogram-of-oriented-gradients/)

it is a feature descriptor for pattern matching (all feature descriptors are)


### Uses:
- used in face recognition 

### Steps
1. resize to 64 x 128
2. calculate gradients using sobel x and y 
3. magnitude and direction using the gradients `H x W x 2`
4. calcuate histogram of gradients in `8 x 8` - into `9 bins`
	1. on a `8 x 8 patch` bin the direction values into `9 bins`
	2. at each binned value cell add the gradient intensity like below ![[hog_example.png]]
	3. if the angle is in between bins distribute the magnitude to two bins
5. `16 x 16` block normalization - gives `36 x 1` feature vector 
6. there are 7 horizontal and 15 vertical `16 x 16` blocks - `3780 x 1` feature vector