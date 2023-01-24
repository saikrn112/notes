Hi Ramana,

The goal of the project is to estimate the optical flow that is EdgeTPU compatible. The goal is to come up with a method (a combination of architecture, input/output representation and training methodology/dataset). Also, keep the inference speed at around 15 Hz on the Coral TPU. We also need to be comparable/better in accuracy (for similar or better speed) on the Intel Movidius NCS2. 

  

  

 Perform all your training in FlyingChairs2 and then fine-tune on FlyingThings3D (feel free to get creative here to change the datasets or training methodology). Test it on both FlyingThings3D and KITTI/Cityscapes (pick one).

  

  

Here are my expectations for your Directed Research Submission(s):  

1.  Weekly update meetings (time TBD).
2.  Maintain a progress update report on Slides, Excel, Word, Notion or Obsidian and send the link to me. 
3.  A conference quality report written in LaTeX in IEEETran Format (Feel free to use [Overleaf](https://nam11.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.overleaf.com%2Fgallery%2Ftagged%2Fieee&data=05%7C01%7Cspinnamaraju%40wpi.edu%7Ca923467db2b04a0d310408dafad4150a%7C589c76f5ca1541f9884b55ec15a0672a%7C0%7C0%7C638098086046146305%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=VVopHv%2FOLNAlaG4XDBsowknbQjO6JQcxao7YIK4An90%3D&reserved=0 "Original URL: https://www.overleaf.com/gallery/tagged/ieee. Click or tap if you trust this link.")'s templates to make life easier) and a 10min conference quality presentation at the end of every month. These should be submitted on Canvas on the dates specified. The earliest submission is on Jan 31st,  11:59:59PM and the final submission is on May 1st, 11:59:59PM.
4.  A GitHub repo with all your codebase to recreate your results along with a readme to run your codebase, **host this on the [pearwpi](https://nam11.safelinks.protection.outlook.com/?url=https%3A%2F%2Fgithub.com%2Fpearwpi&data=05%7C01%7Cspinnamaraju%40wpi.edu%7Ca923467db2b04a0d310408dafad4150a%7C589c76f5ca1541f9884b55ec15a0672a%7C0%7C0%7C638098086046146305%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=eELhfC8RoSevmx6J0Jc1r5w%2F7qH92SkFILM3xKF0BgA%3D&reserved=0 "Original URL: https://github.com/pearwpi. Click or tap if you trust this link.") organization**.
5.  All the images in the paper/report and presentation should be your own.
6.  Submission to IROS 2023 on March 1st.
7.  Include qualitative and quantitative evaluations as we will discuss in weekly meetings.

Do let me know if you have any questions.  

  

Best,

Nitin