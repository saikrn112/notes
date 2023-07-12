![[before randomize.png|400]]




```
python extract_rosbag_hires.py \
--bag MH_Test_Hires_07_10_2023/2023-07-10-14-48-18.bag \
--output MH_Test_Hires_07_10_2023_output_dir/ \
--topic_list /SKR3/odom /SKR4/hires \
--image_list /SKR4/hires /SKR3/stereo/right
```