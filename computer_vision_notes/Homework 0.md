pb detection

how is color discontinuity different from intensity discontinuity? 
>[!Info]
>this is similar to SSIM loss

>[!ERROR]
>how are probabilities that we get from pb different other edge detection based algo? 
>in usual edge detection algorithms we get 255 if the edge exists. however, here we get some value between 0-255 indicating the probability of boundary being present


>[!ERROR]
>how are they probabilities?
>

how is texture quantized? 
texture is represented by a texton map which is basically a cluster of filter responses

### DoG
how are sobel and laplacian high pass filters? arent they passing low frequencies? 

why are we taking a gaussian on sobel? 
	is it different from blurring the first order ? 
we are rotating so that we can get different orientations of edges
we are having different scales to identify different thickness of edges

### LM Filters 
how are 1st order LM filters fundamentally different from sobel filters? 
what is the purpose of considering different elongation factor of gaussians? 
laplacian is more stable but looses direction

### Gabor filters
they are just human like filters
these are more than enough and we can throw out the DoG and LM

### Texton Map 
it's a cluster all the filter responses 
binning them into 64 groups
	this doesnt mean that values are going from 0 to 63, rather different values are grouped into 64 categories 

### Brightness Map
grayscale brightness not color 

### Color Map
any color representation can be used for clustering


### Gradients of all these maps
>[!ERROR]
>how is different from applying DoG?


### Half disk masks
they are used to compute gradients
but how are they any different from DoG? 
in DoG we are just passing through various kernel sizes
