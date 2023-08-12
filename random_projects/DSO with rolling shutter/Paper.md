category : 
parent link : 

## Overview

### Indirect
pre computation and keypoint extraction
optimizes geometric error 
- point positions
- flow vectors

>[!ERROR]
>establishing correspondences using dence regularized optical flow


>[!info]-
> for depth cameras optimizes point positions is direct approach not indirect

### Direct 
optimizes photometric error

### Sparse
optimizes geometric error without geometric prior

### Dense
uses geometric prior


#### Sparse + Indirect
ORBSLAM2

	Dense + Indirect 
> need to check this 

#### Dense + Direct
LSDSLAM
DTAM
employs photometric error (direct)  with geometric prior (dense)

#### Direct + Sparse (This Paper)
opitmizes photometric error + geometric prior
using non linear optimization framework unlike EKF


### This Paper
## Introduction
### History
### Interesting References
## Details 
