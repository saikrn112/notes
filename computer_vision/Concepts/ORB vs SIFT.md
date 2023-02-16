| Step                          | SIFT                                       | ORB                                                   |
|-------------------------------|--------------------------------------------|-------------------------------------------------------|
| Feature detection             | Difference of Gaussians (DoG)              | Features from Accelerated Segment Test (FAST)         |
| Scale-space extrema detection | DoG scale-space                            | DoG scale-space                                       |
| Orientation assignment        | Histogram of gradient directions           | Intensity centroid of local patch                     |
| Feature description           | Scale-invariant gradient-based descriptors | Binary robust independent elementary features (BRIEF) |
| Feature matching              | Euclidean distance of descriptor vectors   | Hamming distance of binary descriptor strings         |
| Robust matching               | Random Sample Consensus (RANSAC)           | Random Sample Consensus (RANSAC)                      |
