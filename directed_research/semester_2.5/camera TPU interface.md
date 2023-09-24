```
v4l2-ctl --list-devices
v4l2-ctl --list-formats-ext --device /dev/video1


export DEMO_FILES="$HOME/demo_files"

edgetpu_classify_server --source /dev/video1:YUY2:640x480:30/1  --model ${DEMO_FILES}/mobilenet_v2_1.0_224_quant_edgetpu.tflite --labels ${DEMO_FILES}/imagenet_labels.txt
```