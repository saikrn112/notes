---

kanban-plugin: basic

---

## Ideas

- [ ] Idea: UNet
- [ ] Idea: UNet with Multiscale
- [ ] Idea: Unet + Uncertainity
- [ ] Idea: UNet + multiscale + uncertainty
- [ ] Idea: Nanoflownet based MB impl
- [ ] Idea: Heuristic based optical flow training for cost volume
- [ ] Idea: Dilation rate as learnable parameter
- [ ] Idea: predict small scale along with chunks and combine


## Backlog

- [ ] try warping again with flownetwarp
- [ ] plot data distributions for<br>- [ ] FC2<br>- [ ] FT3D<br>- [ ] Sintel
- [ ] Task: for sintel full resolution chunk accross the images
- [ ] read nanoflownet again but this time for references
- [ ] some paper on consolidated methods for speed of the network
- [ ] Task: compare with same resolution with other papers


## Progress

- [ ] [[How fast is too fast]]


## training

- [ ] fine tune multiscale + uncertainity with FT3D


## Pause

- [ ] [[warping module edge tpu compatible]]
- [ ] [[recalculate all the metrics computed for previous models]]
- [ ] Task: warp and check<br>- [ ] plot the errors<br>- [x] plot artificial images and check
- [ ] Task: get 450 Epoch finetuned model from Aniket, Mandeep and Prof Nitin


## Done

- [ ] copy sintel data to 3080 in 4TB Nitin's hard disk
- [ ] [[Task  review existing pretrained model on sintel to compare numbers with my script and paper]]<br>- [x] impl RAFT evaluation to make sure numbers are correct<br>- [x] update presentation with numbers and images<br>- [x] check difference between resize and crop again<br>- [x] modify original code to make sure numbers for resize and crop are same as the previous
- [ ] [[Idea  Multiscale + Uncertainty + Motion Boundary]]
- [ ] Task: test the trained Multiscale + uncertainty+MB<br>[[Idea  Multiscale + Uncertainty + Motion Boundary]]
- [ ] Idea: MB train with Multiscale + uncertainity<br><br>[[Idea  Multiscale + Uncertainty + Motion Boundary]]


## Archive

- [ ] Aniket should tell final test_new script for FC2
- [ ] Modify/Add sintel data loaders for that
- [ ] Task: check if edge detection has been overfit by running tests
- [ ] print different loss components now
- [ ] Review: Focal Loss vs Detail Loss




%% kanban:settings
```
{"kanban-plugin":"basic"}
```
%%