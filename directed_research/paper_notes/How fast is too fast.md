category : Optical Flow Research
parent link : [[How fast is too fast]]

## Overview
- provides baseline for design tradeoffs in autonomous navigation -- agnostic to sensor and robot type (some assumptions though)
- maximum latency with safety is related to speed, range of sensing, actual limitation of quadrotor.
- validate analysis using quadrotor equipped with event camera

### This Paper
- theoretical analysis of coupling between sensing latency and actuation limitation in a robotic platform
- Derives closed form expression for maximum speed robot can reach as a function of its perception and actuation parameters, and study its sensitivity to such parameters.

>[!ERROR] Questions
>why are obstacles modeled as squares instead of circles?



## Introduction
### Assumptions
1. robot is modelled as a linear system 
	1. bounded inputs 
	2. moves in a plane
	3. relies on onboard sensing for static obstacle detection
2. robot is holonomic
3. sensing and actuation is ideal (no uncertainities in any of them)

on point 1
![[assumption_1.png|300]]
> what is linearization through static or dynamic feedback?  
> interesting that this kind of linearization is not like jacobian


on point 2 
non holonomic has  coupling between longitudinal and lateral dynamics 
> I am not sure how this would break the assumptions on the model 


### History
### Interesting References
Real-Time Camera Tracking: When is High Frame-Rate Best? - [link]([Real-Time Camera Tracking: When is High Frame-Rate Best? | SpringerLink](https://link.springer.com/chapter/10.1007/978-3-642-33786-4_17))
SPEED-RANGE DILEMMAS FOR VISION-BASED NAVIGATION IN UNSTRUCTURED TERRAIN - [link]([SPEED-RANGE DILEMMAS FOR VISION-BASED NAVIGATION IN UNSTRUCTURED TERRAIN - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1474667016346778))
	by YanLeCun


## Details 

### Problem Formulation

#### Modelling

![[schematics.png|350]]


##### Robot Model

- there is no accleration in longitudinal direction
- this is backed up by some reference stating 
	- lateral avoidance maneuvers require less time at high speed
	- allowing faster navigation along longitudinal axis

##### Obstacle Model
- costmap formulation

##### Sensor Model

sensing latency depends on 
- sensor itself
- time necessary to process
	- algorithm used
	- computation power 
$$\tau \in \mathbb{R}^+$$  
sensing range
$$
\begin{align}
s &\in \mathbb{R}^+ \\
\alpha &\geq 2arctan(\frac{r_o}{2s})
\end{align}
$$  
#### Obstacle Avoidance
##### Time to contact and avoidance Time
##### Time optimal Avoidance


1020
6624
3525

