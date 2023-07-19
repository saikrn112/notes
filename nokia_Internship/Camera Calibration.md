

hires skr1 640x480

```
Matrix
[334.8488618582481, 0, 314.5397778215423;
 0, 334.182188029819, 238.7207114810826;
 0, 0, 1]
Distortion
[0.04030267937999488;
 -0.03412182876828711;
 0.001600535055171807;
 -1.301299306343994e-05;
 0]
distortion_model: plumb_bob
Re-projection error reported by calibrateCamera: 0.302278
Calibration Succeded!

Writing data to: /data/modalai/opencv_hires_intrinsics.yml
Saved!
Exiting Cleanly


%YAML:1.0
---
M: !!opencv-matrix
   rows: 3
   cols: 3
   dt: d
   data: [ 3.3484886185824814e+02, 0., 3.1453977782154226e+02, 0.,
       3.3418218802981903e+02, 2.3872071148108259e+02, 0., 0., 1. ]
D: !!opencv-matrix
   rows: 5
   cols: 1
   dt: d
   data: [ 4.0302679379994877e-02, -3.4121828768287107e-02,
       1.6005350551718065e-03, -1.3012993063439942e-05, 0. ]
reprojection_error: 3.0227760474332460e-01
width: 640
height: 480
distortion_model: plumb_bob
calibration_time: "2023-07-19 19:43:21"


```

tracking skr1


```
Matrix
[274.6786480928074, 0, 282.2616390312837;
 0, 274.7744922509926, 245.6318408661183;
 0, 0, 1]
Distortion
[0.002923669741176137;
 0.001550202871327961;
 0;
 0]
distortion_model: fisheye
Re-projection error reported by calibrateCamera: 0.873913
Calibration Succeded!

Writing data to: /data/modalai/opencv_tracking_intrinsics.yml
Saved!
Exiting Cleanly


%YAML:1.0
---
M: !!opencv-matrix
   rows: 3
   cols: 3
   dt: d
   data: [ 2.7467864809280735e+02, 0., 2.8226163903128372e+02, 0.,
       2.7477449225099258e+02, 2.4563184086611827e+02, 0., 0., 1. ]
D: !!opencv-matrix
   rows: 4
   cols: 1
   dt: d
   data: [ 2.9236697411761372e-03, 1.5502028713279615e-03, 0., 0. ]
reprojection_error: 8.7391279056005033e-01
width: 640
height: 480
distortion_model: fisheye
calibration_time: "2023-07-19 20:18:11"


```