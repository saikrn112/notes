>[!ERROR]
>need to write in given template

### Question - 1

ellipse fit 
https://stackoverflow.com/questions/47873759/how-to-fit-a-2d-ellipse-to-given-points
why we need 5 points 
https://math.stackexchange.com/questions/3063610/how-many-points-are-needed-to-uniquely-define-an-ellipse


https://math.stackexchange.com/questions/3103023/viewing-a-circle-from-different-angles-is-the-result-always-an-ellipse

unanswered
https://math.stackexchange.com/questions/2636998/transform-ellipse-back-to-circle


somewhat close 
https://math.stackexchange.com/questions/3103023/viewing-a-circle-from-different-angles-is-the-result-always-an-ellipse

https://math.stackexchange.com/questions/2388747/formula-for-ellipse-formed-from-projecting-a-tilted-circle-onto-the-xy-plane?rq=1


tilted circle
https://math.stackexchange.com/questions/2388747/formula-for-ellipse-formed-from-projecting-a-tilted-circle-onto-the-xy-plane


problem description  - [[rbe549_exam_q1_1.jpeg]]
problem solution - [[rbe549_exam_q1_2.jpeg]]


### Question - 2
dispartiy vs depth error
https://www.flir.com/support-center/iis/machine-vision/application-note/stereo-accuracy-and-error-modeling/

disparity vs x and y error 
https://robotics.stackexchange.com/questions/19070/disparity-error-to-x-and-y-accuracy

### Question - 3
depth is from 1st frame
http://www.cns.nyu.edu/~david/handouts/motion.pdf

b. 
are they 2 images? or 2 pairs of images? 
should we assume the equation given in part a? 
that is we have known v_{t0} and w_{t0}?
do we know disparity? 
can we assume stereo camera is rectified? 
can we do feature matching for disparity?

depth from optical flow 
https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=590045


[hons_0608.pdf (canterbury.ac.nz)](https://www.csse.canterbury.ac.nz/research/reports/HonsReps/2006/hons_0608.pdf)
c. 
identify common region
how to do that? 

how to solve for lambdas $IR$ and $RGB$ 
can I assume the camera centers as well? 

### Question - 4

road plane would have more granularity 
fit planes wherever possible on the ground
check for largest plane 

https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0215159

https://ieeexplore.ieee.org/document/7378662

convert to elevation maps 
construct navigable terrain based on few filters 
point density to filter nearby regions
intensity thresholding
road consists of two parallel lines 
and z closer to 0 


https://www.mathworks.com/help/lidar/ug/lane-detection-in-3d-lidar-point-cloud.html

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6467419/

refine the search using black points on the road
and lanes

### Question - 5
uses pedestrians as stick to calibrate
https://easychair.org/publications/preprint/sGQh


### Question - 7
from ID we need to get position and velocities at each step 
because of moving objects, we need to interpolate the optical flow? 
assuming rigid flow 
