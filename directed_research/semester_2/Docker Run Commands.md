3060TI
```
optical

python container/start_docker_instance.py \
--it \
--gpu \
--usb \
--workspace=/home/ramu/Personal/OpticalFlowOnTPU/
```


3090TI
```
ssh pear_group@130.215.219.83
or
pear3090ti

cd /home/pear_group/ramana/OpticalFlowOnTPU
or
optical


python3 container/start_docker_instance.py --it --display


cd optical/OpticalFlowOnTPU/

```