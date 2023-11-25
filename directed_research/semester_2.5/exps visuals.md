

football 
- [x] exp1 - 82 - 97 -- great
- [x] d850: 0:06 - 0:11
`ffmpeg -i D850/DSC_3802.MP4 -ss 00:00:06 -to 00:00:12 -c copy exp1_football/D850.MP4`
- [x] d7100:  
`ffmpeg -i D7100/DSC_0900.MOV -ss 00:00:08 -to 00:00:14 -c copy exp1_football/d7100.MOV`
- [ ] coral
```
args.frames_range_low = 82
args.frames_range_high = 97
args.control_threshold = 1
args.threshold = .5
```


- [ ] exp2 - 107 - 114 -- not great

```
args.frames_range_low = 107
args.frames_range_high = 114
args.control_threshold = 1
args.threshold = .7
```
- [ ] exp3 - 156 - 171 -- great
- [x] d850: 0:13-0:18
`ffmpeg -i D850/DSC_3804.MP4 -ss 00:00:13 -to 00:00:18 -c copy exp3_football/D850.MP4`
- [x] d7100: 0:15 - 0:20
`ffmpeg -i D7100/DSC_0902.MOV -ss 00:00:15 -to 00:00:21 -c copy exp3_football/D7100.MOV`
```
args.frames_range_low = 156
args.frames_range_high = 171
args.control_threshold = 1
args.threshold = .7
```

car
- [ ] exp1 - 207 - 257 -- final frame
```
args.frames_range_low = 207
args.frames_range_high = 257
args.control_threshold = 1
args.threshold = .5
```
- [ ] exp2 - 270-285 -- great
- [x] d850:3803, 0:15,22
`ffmpeg -i D850/DSC_3803.MP4 -ss 00:00:15 -to 00:00:21 -c copy exp2_car/D850.MP4`
- [x] d7100:901, 0:17,23
`ffmpeg -i D7100/DSC_0901.MOV -ss 00:00:17 -to 00:00:23 -c copy exp2_car/D7100.MOV`
```
args.frames_range_low = 270
args.frames_range_high = 285
args.control_threshold = 1
args.threshold = .5
```
- [ ] exp3 - 340-365 -- hand
```
args.frames_range_low = 340
args.frames_range_high = 365
args.control_threshold = 1
args.threshold = .4
```
aeroplane
- [ ] exp2 - 456 - 469 -- nothing
```

args.frames_range_low = 457
args.frames_range_high = 469
args.control_threshold = 5
args.threshold = .65
```
- [ ] exp3 - 515-529 -- hand
```
args.frames_range_low = 515
args.frames_range_high = 529
args.control_threshold = 5
args.threshold = .7
```


let's start with threshold 0 


right side 

football
- [ ] exp 4 - 123 - 128 - okish
```
args.frames_range_low = 123
args.frames_range_high = 128
args.control_threshold = 1
args.threshold = 0.7
args.negate_y_flow = True
```
- [ ] exp 5 - 141 - 161 -- not great
```
args.frames_range_low = 151
args.frames_range_high = 161
args.control_threshold = 1
args.threshold = 0.7
args.negate_y_flow = False
```
- [ ] exp 6 - 104 - 114 -- okish
```
args.frames_range_low = 104
args.frames_range_high = 114
args.control_threshold = 0.8
args.threshold = 0.7
args.negate_y_flow = True
```


car
- [ ] exp 4 - 325 - 347 - one frame
```
args.frames_range_low = 325
args.frames_range_high = 347
args.control_threshold = 1
args.threshold = 0.5
args.negate_y_flow = True
```
- [ ] exp 5 - 418 - 428  -- not great
```
args.frames_range_low = 418
args.frames_range_high = 428
args.control_threshold = 1
args.threshold = 0.7
args.negate_y_flow = False
```
- [ ] exp 6 - 260 - 267 -- nothing
```
args.frames_range_low = 260
args.frames_range_high = 267
args.control_threshold = 0.8
args.threshold = 0.3
args.negate_y_flow = False
```


aeroplane
- [ ] exp 4 - 505 - 529 --great
- [ ] d850:DSC3806,24-30
`ffmpeg -i D850/DSC_3806.MP4 -ss 00:00:24 -to 00:00:30 -c copy exp4_aeroplane/D850.MP4`
- [x] d7100:DSC0903, 30 - 35
`ffmpeg -i D7100/DSC_0903.MOV -ss 00:00:30 -to 00:00:35 -c copy exp4_aeroplane/D7100.MOV`
```
args.frames_range_low = 505
args.frames_range_high = 529
args.control_threshold = 1
args.threshold = 0.5
args.negate_y_flow = True
```
- [ ] exp 5 - 614 - 624 -- nothing
```
args.frames_range_low = 614
args.frames_range_high = 624
args.control_threshold = 1
args.threshold = 0.7
args.negate_y_flow = False
```
- [ ] exp 6 - 411 - 421 -- nothing
```
args.frames_range_low = 411
args.frames_range_high = 421
args.control_threshold = 0.8
args.threshold = 0.7
args.negate_y_flow = False
```



- [ ] RAFT check 



- [x] exp1 - 82 - 97 -- great
- [x] d850: 0:06 - 0:11
`ffmpeg -i D850/DSC_3802.MP4 -ss 00:00:06 -to 00:00:12 -c copy exp1_football/D850.MP4`
- [x] d7100:  
`ffmpeg -i D7100/DSC_0900.MOV -ss 00:00:08 -to 00:00:14 -c copy exp1_football/d7100.MOV`
- [x] coral
```
args.frames_range_low = 82
args.frames_range_high = 97
args.frames_range_high = 198 # extended_cut
args.control_threshold = 1
args.threshold = .5
```


- [ ] exp3 - 156 - 171 -- great
- [x] d850: 0:13-0:18
`ffmpeg -i D850/DSC_3804.MP4 -ss 00:00:13 -to 00:00:18 -c copy exp3_football/D850.MP4`
- [x] d7100: 0:15 - 0:20
`ffmpeg -i D7100/DSC_0902.MOV -ss 00:00:15 -to 00:00:21 -c copy exp3_football/D7100.MOV`
```
args.frames_range_low = 156
args.frames_range_high = 171
args.frames_range_high = 239 # extended_cut
args.control_threshold = 1
args.threshold = .7
```

- [ ] exp2 - 270-285 -- great
- [x] d850:3803, 0:15,22
`ffmpeg -i D850/DSC_3803.MP4 -ss 00:00:15 -to 00:00:21 -c copy exp2_car/D850.MP4`
- [x] d7100:901, 0:17,23
`ffmpeg -i D7100/DSC_0901.MOV -ss 00:00:17 -to 00:00:23 -c copy exp2_car/D7100.MOV`
```
args.frames_range_low = 270
args.frames_range_high = 285
args.frames_range_high = 366 # exteded_cut
args.control_threshold = 1
args.threshold = .7
```


- [ ] exp 4 - 505 - 529 --great
- [ ] d850:DSC3806,24-30
`ffmpeg -i D850/DSC_3806.MP4 -ss 00:00:24 -to 00:00:30 -c copy exp4_aeroplane/D850.MP4`
- [x] d7100:DSC0903, 30 - 35
`ffmpeg -i D7100/DSC_0903.MOV -ss 00:00:30 -to 00:00:35 -c copy exp4_aeroplane/D7100.MOV`
```
args.frames_range_low = 505
args.frames_range_high = 529
args.frames_range_high = 604 # exteded_cut
args.control_threshold = 1
args.threshold = 0.5
args.negate_y_flow = True
```