## Resources

notes from the video link - [(7) Joan Solà - Lie theory for the Roboticist - YouTube](https://www.youtube.com/watch?v=QR1p0Rabuww&ab_channel=No%C3%A9mieJaquier)
quaternions visualization - [Visualizing quaternions (4d numbers) with stereographic projection - YouTube](https://www.youtube.com/watch?v=d4EgbgTm0Bg&ab_channel=3Blue1Brown)

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



