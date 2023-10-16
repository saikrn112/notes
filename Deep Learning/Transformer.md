Interesting Tutorial: http://jalammar.github.io/illustrated-transformer/
The game changer: "Attention is all you need" - [[attention_is_all_you_need.pdf]]


>[!info] Key Component of Transformer
>**Attention**
>both cross attention and self attention


# Attention: Explained

>[!ERROR] Abstract
>Latent space is a space in which input data is embedded
>Value is vector in latent space 
>Keys like hashing keys (rsa or sha) is used to transform query into a unique ID that can be related to value. 
>In attention case, queries (generated from cross or self) along with keys are used to give weights in latent space


Step 1: 3 vectors Query ($q$), Key ($k$), and Value ($v$) are generated using Wq, Wk, Wv

![[key_value_query_gen.png]]

Step 2: 


![[key_query_value.png]]


Step Decode: 
![[decode.png]]