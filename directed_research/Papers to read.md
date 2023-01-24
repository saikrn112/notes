##### Deep Visual Inertial Odometry

| Paper                                                                        | Interal Link                                                 | year | prominent author |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------ | ---- | ---------------- |
| [Super Glue](https://arxiv.org/pdf/1911.11763.pdf)| [[Super Glue\|notes]] | 2021 |             |
| [TLIO](https://arxiv.org/pdf/2007.01867.pdf) |      |  | MagicLeap            |


---
##### Deep Optical Flow

| Paper                                                                                          | Interal Link                                             | year | prominent author |
| ---------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ---- | ---------------- |
| [NanoFlowNet](https://arxiv.org/pdf/2209.06918.pdf)     very close to what we are trying to do |             [[NanoFlowNet\|notes]]                                             | 2022 |                  |
| A Lightweight Optical Flow CNN — Revisiting Data Fidelity and Regularization                   |                                                          | 2020 |                  |
| SelFlow: Self-Supervised Learning of Optical Flow                                              | [[Self supervised learning of Optical Flow\|notes]]      | 2019 |                  |
| Models Matter, So Does Training: An Empirical Study of CNNs for Optical Flow Estimation        |                                                          | 2018 |                  |
| LiteFlowNet: A Lightweight Convolutional Neural Network for Optical Flow Estimation            | [[LiteFlowNet1\|notes]]                                  | 2018 |                  |
| PWC-Net: CNNs for Optical Flow Using Pyramid, Warping, and Cost Volume                         | [[PWC-Net\|notes]]                                       | 2017 |                  |
| FlowNet 2.0: Evolution of Optical Flow Estimation with Deep Networks                           | [[FlowNet2.0 Evolution of optical flow networks\|notes]] | 2016 | Broxx            |
| Optical Flow Estimation using a Spatial Pyramid Network                                        |                                                          | 2016 |                  |
| FlowNet: Learning Optical Flow with Convolutional Networks                                     | [[FlowNet Learning Optical flow with CNN\|notes]]        | 2015 | Broxx            |
| RAFT: Recurrent All Pairs Field Transforms for Optical Flow                                    |                                                          |      |                  |
| Disentangling architecture and training for optical flow                                       |                                                          |      |                  |

[Github Awesome Collection](https://github.com/hzwer/Awesome-Optical-Flow)

Goal:
- fit the optical flow nets on TPS and other edge devices
- applications?
	- depth estimation - why cant we use monocular estimation for this?
	- motion segmentation
	- action recognition
	- video editing - ==how?==
	- autonomous driving

Problems:
An optical flow paper is marked complete if it address the following challenges  ^b83487
- Occlusion
- Large Displacement
- Temporal information
- Intensity variations?
- network should generalize well outside of it's training without fine tuning
- low lighting conditions

To evaluate each Network, we need data which accounts the above problems as benchmarks

what exactly is intelligence in smaller drones? #nitin_sanket 
what was done so far? 
what needs to be done? 
- is obstacle avoidance the only usage of smaller drones?

any time network object dispartiy

---


| Paper                                                                                                                                      | Interal Link |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------ |
| [Rotation Avging](https://users.cecs.anu.edu.au/~hartley/Papers/PDF/Hartley-Trumpf:Rotation-averaging:IJCV.pdf)     rotation avging matrix |              |
| [dual quaternion](https://en.wikipedia.org/wiki/Dual_quaternion)                                                                           |              |
| [least squares](https://textbooks.math.gatech.edu/ila/least-squares.html)                                                                  |              |
|  [general and adaptive loss](https://arxiv.org/abs/1701.03077)    (jon barron)                                                                                                                           |              |


---
The goal of your directed research is to perform the following task:
Input(s): RGB Camera data and IMU data (Known extrinsic and intrinsic)
Output(s): Relative Pose (Odometry)
Constraint(s): Has to be Float16 and Intel NCS compatible, generalize to novel scenes (train in the simulation if you want).  

Here are the papers:

VINet: Visual-Inertial Odometry as a Sequence-to-Sequence Learning Problem ([https://arxiv.org/abs/1701.08376](https://arxiv.org/abs/1701.08376 "https://arxiv.org/abs/1701.08376")) 

  

DeepVIO: Self-supervised Deep Learning of Monocular Visual Inertial Odometry using 3D Geometric Constraints ([https://arxiv.org/abs/1906.11435](https://arxiv.org/abs/1906.11435 "https://arxiv.org/abs/1906.11435"))

  

Unsupervised Deep Visual-Inertial Odometry with Online Error Correction for RGB-D Imagery ([https://ieeexplore.ieee.org/document/8691513](https://ieeexplore.ieee.org/document/8691513 "https://ieeexplore.ieee.org/document/8691513"))

  

SelfVIO: Self-Supervised Deep Monocular Visual-Inertial Odometry and Depth Estimation ([https://arxiv.org/abs/1911.09968v2](https://arxiv.org/abs/1911.09968v2 "https://arxiv.org/abs/1911.09968v2"))

  

CUAHN-VIO: Content-and-Uncertainty-Aware Homography Network for Visual-Inertial Odometry ([https://arxiv.org/abs/2208.13935](https://arxiv.org/abs/2208.13935 "https://arxiv.org/abs/2208.13935"))

  

Deep Learning for Visual-Inertial Odometry: Estimation of Monocular Camera Ego-Motion and its Uncertainty ([https://github.com/ElliotHYLee/Deep_Visual_Inertial_Odometry](https://github.com/ElliotHYLee/Deep_Visual_Inertial_Odometry "https://github.com/ElliotHYLee/Deep_Visual_Inertial_Odometry"))

  

Efficient Deep Visual and Inertial Odometry with Adaptive Visual Modality Selection ([https://arxiv.org/abs/2205.06187](https://arxiv.org/abs/2205.06187 "https://arxiv.org/abs/2205.06187"))

Xception: DL with seperable Convolutions( 
https://arxiv.org/abs/1610.02357)

---