atible with TensorFlow Lite models only and the model must be compiled for execution on the Edge TPU. For details about how to create a model that's compatible with the E
### Resources 
TPU getting started - [link](https://coral.ai/docs/dev-board/get-started/)
flashing through USB - [link](https://coral.ai/docs/dev-board/reflash/#flash-a-new-board)
install MDT and run models - [link](https://coral.ai/docs/dev-board/get-started/#install-mdt)
installing tensorflow docker - [link](https://www.tensorflow.org/install/docker)

tensorflow models on edge - [link](https://coral.ai/docs/edgetpu/models-intro/#compatibility-overview)
blog followed for converting the pytorch model - [link](https://towardsdatascience.com/my-journey-in-converting-pytorch-to-tensorflow-lite-d244376beed)

Prof NitinSanket's speed tests - [link](https://github.com/NitinJSanket/prg_prgncs)
https://github.com/NitinJSanket/prg_prgncs
https://github.com/NitinJSanket/prg_prgeye/
https://github.com/prgumd/EVPropNet
https://github.com/NitinJSanket/prgeyeomni


To connect to device 
```
mdt shell
```

To check if device is connected 
```
mdt devices
```

### Tasks
- [x] need to install tensorflow docker in my machine
- [x] need to understand tensor flow implementation
	- [x] copy resnet tensorflow from his repository
	- [x] run it on my own machine
- [x] run it on TPU
	- [x] convert to tensorflow lite
	- [x] interface with coral
- [ ] check accuracy of the ONNX model if needed after the following two
- [ ] check accuracy of the tensorflow model 
- [ ] check accuracy after tflite conversion

3090

### Questions

1. in this [file](https://github.com/NitinJSanket/prg_prgeye/blob/5780f9755c1da5551074920ce2147a92f623296d/Software/DeepLearning/SpeedTests/CreateNetwork.py) line 72, why are they representing model as 3 times more?
