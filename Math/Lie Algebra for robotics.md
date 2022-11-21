## Resources

notes from the video link - [(7) Joan Solà - Lie theory for the Roboticist - YouTube](https://www.youtube.com/watch?v=QR1p0Rabuww&ab_channel=No%C3%A9mieJaquier)
quaternions visualization - [Visualizing quaternions (4d numbers) with stereographic projection - YouTube](https://www.youtube.com/watch?v=d4EgbgTm0Bg&ab_channel=3Blue1Brown)
axis - angle representation - [wiki]([Axis–angle representation - Wikipedia](https://en.wikipedia.org/wiki/Axis%E2%80%93angle_representation#Exponential_map_from_%F0%9D%94%B0%F0%9D%94%AC(3)_to_SO(3))
quaternions interactive visualization - [Visualizing quaternions, an explorable video series (eater.net)](https://eater.net/quaternions)


---

### Group
set G of elements ${X, Y, Z, T....}$ with an operation $\circ$ such that it follows the following [[Jargon#^0d6a88|axioms]]
1. Composition - stays in the group i.e $X \circ Y = T$ 
2. Identity element in the group - $X \circ E = E \circ X = X$
3. Inverse in the group $X^{-1}  \circ X = X \circ X^{-1} = E$
4. Operation is *associative*  $X \circ (Y \circ Z) = (X \circ Y) \circ Z$

Operation need not be commutative 


### Lie Group
it is also a smooth manifold 

manifold - hypersurface in space 
smooth manifold - surface which is smooth no spikes or edges 


Modern Definition of Lie Group
```
a lie group is a smooth manifold who elements satisfy the group axioms 
```

### Group Action
we use groups because they have the power to transform 
example: we use rotation matrices to rotate vectors which are part of different group

definition: groups can act on another set $V$ to transform it's elements with following axioms
1. Identity of the group ($E$) is a null action $E \circ v = v$ 
2. composition compatible $(X \circ Y) \circ v = X \circ (Y \circ v)$


## Topology of Lie Theory 

topology for unit complex numbers - unit circle
for quaternions - a 3D sphere embedded in a 4D space --- TODO how?

### Tangent space

on Identity element - tangent space is built
it is a linear space which is tangent to the manifold 
tangent space can be at any point but tangent space at identity element is called _lie algebra_
- it is unique 
- it is a vector space (and hence we can do calculus) `how is vector space and calculus related?`
- dimension of vector space == degrees of freedom of manifold
- tangent space at identity is called lie algebra

### Exponential map
takes a vector from tangent space and produces an element on the group (on manifold) (geodesic?) is called exponential map. 

logarithimic map is opposite

exponential map is wrapping the tangent from tangent space to a geodesic
logarithimic map is unwrapping a geodesic on manifold to the tangent in tangent space

based on [[Lie Algebra for robotics#^6d3baf|algebra below]] we can do the following


$$
\begin{align}
R^{T}\circ \dot{R} &= w_{\times} \\
\dot R &= R \circ w_{\times}\\
R &= R_{0} \circ exp(w_{\times}t) \\
R &= R_{0}\circ exp(\theta_{\times})
\end{align}
$$

with taylor expansion

$$
\begin{align}
R &= R_{0}\circ exp(\theta_{\times})\\
exp(\theta_{\times}) &= I cos(\theta) + 1_{\times} sin(\theta)
\end{align}
$$


#### Capitalized Exponential  and Logarithimic map

They are basically shortcuts to go from cartesian space to manifold and manifold to cartesian space

typically this is the process from cartesian space to manifold
cartesian space $\rightarrow$ using v representation $\rightarrow$ lie algebra $\rightarrow$ using exponential map $\rightarrow$ manifold
this is shortcircuited by 
cartesian space $\rightarrow$ using capital Exponential map $\rightarrow$ manifold

same process from manifold to cartesian space

### Algebra
for S1
differentiating wrt time


$$
\begin{align}
z^{*}\circ z &= 1 \\
z^{*}\circ \dot{z} + \dot{z^{*}} \circ z &= 0 \\
z^{*}\circ \dot{z} &= - \dot{z^{*}} \circ z \\
z^{*}\circ \dot{z} &= - (z^{*} \circ \dot z)^{*} -- \space commutative \\
z^{*}\circ \dot{z} &= iw
\end{align}

$$

two representations for tangent space
hat: $w^{\cap} = i \circ w$
vee: $w = -i \circ w^{v}$
>[!INFO]
basically hat representation is taking from cartesian space to lie algebra and vee representation is taking from lie algebra to cartesian space and these two representations are [[Jargon#^b1778b|isomorphic]]

for SO(3) ^6d3baf

$$
\begin{align}
R^{T}\circ R &= I \\
R^{T}\circ \dot{R} + \dot{R^{T}} \circ R &= 0 \\
R^{T}\circ \dot{R} &= - \dot{R^{T}} \circ R \\
R^{T}\circ \dot{R} &= - (R^{T} \circ \dot R)^{T} -- \space Transpose \\
R^{T}\circ \dot{R} &= w_{\times}
\end{align}

$$

In lie algebra i.e in tangent space for so(3)

$$
\begin{align}
R &= I \\
\dot R &= w_{\times} \\
\end{align}

$$
two representations for tangent space
hat: $\hat{w} = w_{\times}$
vee: $w = w_{\times}^{v}$


### Adjoint Matrix
it's a linear operator 
it maps elements of Manifold ($M$) at $\tau$  to elements of Manifold ($M$) at $\epsilon$  (identity according to the video)


## Calculus on Lie group