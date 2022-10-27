Bilinear form of matrix

Essential matrix $E = T_{\times}R$
- it is named that way because, it is essential that this is correct

2 frames A and B 
then 
$R$ - rotation from B to A
$T$ - translation from A to B

epipolar constraint 


chierality 

Fundamental matrix $F = K_{IM}^{-T}EK_{CM}^{-1}$
- it is named that way because, it is a fundamental quantity which is correct in image frame (our source of truth)


SVD cleanup


Stereo Rectification 

>[!question] 
> #nitin_sanket 

slide 15, I think **X** is marked incorrectly
![[Pasted image 20221022180607.png]]



what are $P_{IM}$ and $X_{IM}$? slides 27 - 28
for physical intuition of forward motion cameras could be facing each other or away from each other slides 38 
>[!question]
> how is scale related to degree of freedom in F? 
> didnt we already convert everything to image coordinates?
> how are gonna enforce rank 2 later?

>[!question]
>how does homography constraint and epipolar constraint fundamentally differ intuitively?
>in one case we just need 4 points but in other case we ned 8 points 

>[!question]
>in slide 41 we say $F$ is to scale
>	what does $F$ and $E$ intuitively mean? 

>[!question]
>slide 35, pinhole equation doesnt make sense 

