

`T_wv_to_map` : Transformation matrix from World viz frame to Map frame -- Need from Howard

from this all the world viz poses are computed to map frame
- world viz markers
- fiducial markers

from this all the 3 markers pose can be computed in Map frame 
from these 3 markers pose I can compute harness frame pose

`T_harness_to_optical` : Transformation from Harness frame to camera optical frame -- calibration

From fidloc we know exactly where the camera is with respect to the markers, 
we know where markers are with respect to the map frame 
