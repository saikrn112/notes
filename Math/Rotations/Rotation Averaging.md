paper: [[rotation_averaging.pdf]]
category : 
parent link : 

## Overview
Talks mainly about 
1. **single rotation averaging**: single rotation from several measurements
2. **multiple rotation averaging**: absolute orientations from several relative orientation measurements
3. **conjugate rotation averaging**: relates pair of coordinate frames (hand-eye coordination problem) and multiple camera calibration

## Single Rotation Averaging
single rotation from several measurements
![[single_rotation_averaging.png|400]]

## Conjugate Rotation Averaging
given a set of rotations $R_{i}$ and $L_{i}$ we need to find rotation $S$ such that 
$$
R_i = S^{-1}L_{i}S
$$
effectively $S$ is a transformation relating coordinate frames in which $R_i$ and $L_i$ are measured
![[conjugate_rotation_avging_opt.png|300]]

## Multiple Rotation Averaging
given many relative rotations $R_{ij}$ compute $n$ absolute rotations $R_i$ 

![[multi_rotation_avging_opt.png|300]]

-- lost in karcher mean

## Introduction
### History
### Interesting References
## Details 
