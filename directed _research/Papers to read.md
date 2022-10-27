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
|                                                                                                                                            |              |
