Hi Ramana,

The goal of the project is to estimate the optical flow that is EdgeTPU compatible. You will need to work on figuring out 5 different output representations that can make this work. Also, keep the model size <=10MB. Perform all your training in FlyingChairs2 and then fine-tune on FLyingThings3D. Test it on both FlyingThings3D and KITTI/Cityscapes (pick one).

  

  

Here are my expectations for your Directed Research Submission:  

1.  A conference quality report written in LaTeX in IEEETran Format (Feel free to use [Overleaf](https://nam11.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.overleaf.com%2Fgallery%2Ftagged%2Fieee&data=05%7C01%7Cspinnamaraju%40wpi.edu%7C72748492968e4924b3b408dac8248832%7C589c76f5ca1541f9884b55ec15a0672a%7C0%7C0%7C638042356493291088%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=HtY8kWja9p7sPuGekzC%2Bv9TCqE%2BIAPP2Z1%2FLsE39BOA%3D&reserved=0 "Original URL: https://www.overleaf.com/gallery/tagged/ieee. Click or tap if you trust this link.")'s templates to make life easier).
2.  A GitHub repo with all your codebase to recreate your results along with a readme to run your codebase.
3.  All the images in the paper/report should be your own.
4.  Include qualitative and quantitative evaluations as described below:

1.  Float32 Model
2.  Float16 TensorFlowLite Model
3.  Float16 TensorFlowLite Model NCS Compiled
4.  UInt8 TensorFlowLite Model
5.  UInt8 TensorFlowLite Model CoralTPU Compiled
6.   Report results on all the above-mentioned model types for all 5 different output representations you come up with on the metrics of EPE and Inference time (both only deep learning inference time and total time to obtain optical flow from feeding in input).
7.    
    

6.  All these should be submitted by Dec 16, 11:59:59PM on Canvas.

Do let me know if you have any questions