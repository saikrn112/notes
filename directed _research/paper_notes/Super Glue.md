## Overview

### Abstract
network to match two sets of local features 
*jointly* by finding correspondences and rejecting non-matchable points
>what do they mean by `jointly` here ? 

They achieve this by solving a _differentiable optimal transport problem_ whose `costs` are predicted by a graph neural network
> what are these costs and why are costs being `predicted` here? 

what did I understand from abstract? 
It's basically a feature matching networks giving out feature correspondences using Neural Network and using some techniques of optimization for that

### Introduction

their claim is that till 2020 feature matching involved 
1. learning ==task agnostic local features ==
2. then perform a simple matching heuristic  

Paper's contribution is basically **learning matching process** through super glue, some network of theirs 

Features:
1. middle end between hand crafted or learned front end and backend
2. handles partial point visibility and occlusion, producing _partial assignment_
>what is partial assignment?

learning feature matching -- finding partial assignment between two sets of local features

classical graph based strategy of matching by solving a _linear assignment problem_ which when relaxed to _optimal transport problem_ can be solved differentiably
> multiple keywords here 
> linear assignment problem
> relaxation to optimal transport problem

GNN - graph neural network is some how inspired from Transformer
>what is a transformer now? and how is it playing a role here ? 

it uses self - (intra-image) and cross - (inter-image) attention to leverage both spatial relationships of keypoints and their visual appearance 
> again multiple keypoints here
> do I need to understand attention models here? 
> I can undersand what keypoint spatial relationship mean but how is this reasoning about keypoint visual appearance?  

Formulatoin enforces `assignment structure` of the predictions
while 
- enabling the cost to learn complex priors 
- elegantly handling occlusion 
- and non repeatable keypoints
>what do they mean by enforcing assignment structure?
>what is an assignment structure?
>	I initially thought it is a feature correspondence but doesnt seem right and feels incomplete
>what are the priors here? 
>	I think they are just features
>why are priors complex? 
>	do they mean different variations of feature descriptors? 
>what are repeatable keypoints?


### Related Work

#### Classical methods
Local feature matching techniques developed in 2000s (mostly based on SIFT)
1. interest point detection
2. feature descriptors (visual descriptors)
3. Nearest Neighbor (NN) search -- how many neighbours? what metric to use to compute nearness?
4. filtering incorrect matches
5. estimating geometric transformation -- is it always homography or if we know the camera calibrations do we compute $4 \times 4$ Transfomation matrix?

#### Deep Learning methods
for matching, works focus on 

- learning better sparse detectors and local descriptors using CNN
> what does better sparse detectors mean? -- TODO paper references 
> what does local descriptors mean? is there anything called global descriptors? -- TODO paper references
> how are these contributing to the feature matching in anyways? arent they just improving front end 

- improve discriminativeness, some look at a wider context using regional features (semanticness?) or log polar patches
 > as in they focus on creating a better descriptors for a feature -- TODO paper reference 
 > but is regional features same as giving some semantic information? 
 > what are log polar patches?
 > same goes here, this is more of improving front end than improving feature matching? 

 `Unless there is an assumption that usually front ends perform the feature matching that's they above papers are included in the related works?`
 I think this makes sense also and matches with what they said in the Introduction part of it 

- learn filter matches by inlier and outlier classification
	- operate on a set of matches still estimated by NN
	- consequently ==ignore the assignment structure and discard visual info==
> simple, what does the highlight mean? 
> arent we encoding the visual info in the fd? 
> what is assignment structure?

- some works focus on dense matching or 3D point clouds, still exhibit same limitations
> what are the limitations here? 

#### Current Work focus
End-to-End architecture combines 
- context aggregation 
- matching
- filtering

>what does this even context aggregation?
>	is it fancy way of saying represting feature as feature descriptors? 
>		dont think so since this is supposed to be a middle end and that is a job of front end, `right?`

#### Graph Matching
>what is the graph composed of here?
>what is graph matching? 
- NP hard
- hence require expensive, complex and impractical solvers 
>why is this hard?
>why do we have impractical solvers if they not solving anything? 

To circumvent this CV literature uses handcrafted costs with heuristics, making it complex and brittle. 

some thoughts on graph matching here 
![[Graph Matching#^super-glue-graph-matching]]

we basically are trying to solve assignment problem as a optimizaton formulation. 
>need to understand how graph problem is formulated as optimization

the graph optimization is further simplified to linear assignment
>what is linear about this assignment? 
>	from what I am reading it's actually quadratic assignment problem where linear terms are to solve the node to node assignment and quadratic terms are to optimize edges -- still vague about it TODO

Now, within this linear assignment they are considering the _optimal transport_ problem which apparently is a _generalized linear assignment_
solution for this problem is computed using ==Sinkhorn algorithm==

#### Deep Learning for sets
lot of concepts
permutation equivariant or invariant functions 
global pooling
instance normalization
Attention -- apparently a more flexible solver since it can `focus` on specific elements and attributes, hence solving both global and data dependent local aggregation   
>what is focus here?
>what are the elements and attributes that they are talking about

how are graphs used in the context of deep learning 
what are graph neural networks and attention models?
wht is transductive and inductive learning?

#### Limitations of current approaches
one obvious limitation that was mentioned in the class is that if the view changes by front and back perspective, it cannot tag the same feature. what are the other limitations?

---
### Questions
why is this called Super Glue? 
> because it acts like a middle end for SLAM front-end (feature extraction) and backend (bundle adjustment or pose estimation)

what is geometric computer vision ? is optical flow not part of geometric CV? 
how good is their claim that feature matching involved only those steps and not much research on better matching algorithms? 
although, what are the current matching algorithms ? 
can this paper be extended to self supervised or unsupervised ? 


How do you define something as a challenging data set? 
>based on the accuracy that people got? 
>can we say this somehow by looking at the dataset that it's difficult? 
>why is this question important? 
>	to reason about how far away are algorithms or networks away from human level abstraction 


Predecessor
Super Point - what were the challenges over there?
>it's a front end feature builder, different from middle end this is doing

