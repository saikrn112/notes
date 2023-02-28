base line loss function used 

$$
\begin{align}
L(P, G) = \lVert (G + 50) - P \rVert_1
\end{align}
$$

polar coordinates 
$$
\begin{align}
L(P_{r\theta\_noramlized},G_{xy}) = \lVert F_{r\theta \rightarrow xy}(F_{denorm}(P_{r\theta\_noramlized})) - G_{xy} \rVert_1 
\end{align}
$$


multi scale final loss
$$
\begin{align}
L(P_l,G) =  \lVert \Sigma_{l=0}^{l=k}P_l -G \rVert
\end{align}
$$

multi scale multi accmulator loss

$$
\begin{align}
L(P_l,G) =  \Sigma_{j=0}^{j=k}\lVert \Sigma_{l=0}^{l=j}P_l -G_{j} \rVert_1
\end{align}
$$

multi scale multi loss
$$
\begin{align}
L(P_l,G) =  \Sigma_{l=0}^{l=k}\lVert P_l -G_{l} \rVert_1
\end{align}
$$