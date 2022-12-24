other tensorflow [link](https://pyimagesearch.com/2021/11/24/computer-graphics-and-deep-learning-with-nerf-using-tensorflow-and-keras-part-3/)
pytorch nerf [link]([pytorch nerf - Google Search](https://www.google.com/search?q=pytorch+nerf&oq=pytorch+nerf&aqs=edge..69i57j0i512l2j0i22i30l4j69i60l2.2222j0j4&sourceid=chrome&ie=UTF-8))

colab link - [link](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/vision/ipynb/nerf.ipynb#scrollTo=xrEM_tS4ImDE)
first need to understand how to load data 
how does data look like 
from what I understand test set should contain positions and viewing angles
and we also need images to compare against

in the colab link that was shared

from main dataset [here](https://drive.google.com/drive/folders/1JDdLGDruGNXWnM1eqY1FNL9PlStjaKWi)
```
Structure:
  SCENE_NAME
    -train
      r_*.png
    -val
      r_*.png
    -test
      r_*.png
      r_*_depth_0000.png
      r_*_normal_0000.png
    transforms_train.json
    transforms_val.json
    transforms_test.json

Transform json details:
camera_angle_x: The FOV in x dimension
frames: List of dictionaries that contain the camera transform matrices for each image.
```

how do you use the camera_angle_x, do we get pitch and roll from it? 
we already have rotation matrix, so we know everything about camera frame wrt ground frame
we also have translation vector 