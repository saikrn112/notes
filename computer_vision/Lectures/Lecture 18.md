 **brightness constancy** - 

**receptive field** - how much of the image a neural network can see at a time. larger the receptive field, more the accurate

equation assumes rigid flow of the scene

$$
\begin{align}
\dot{p} = \frac{1}{Z}
\begin{bmatrix}
-1 &0 &x\\
0 &-1 &y
\end{bmatrix}
V

+
\begin{bmatrix}
xy & -(1+x^{2}) & y\\
1+y^{2} & -xy & -x
\end{bmatrix}
\Omega
\end{align}
$$

focus of expanse (FOE)
$$
FoE = 

\begin{bmatrix}
\frac{V_x}{V_z}\\
\frac{V_y}{V_z}
\end{bmatrix}
$$

Time To Contact (TTC)
$$
TTC = 
\frac{Z}{V_{Z}}
$$

from optical flow 
$$
\frac{V_{Z}}{Z}
 = 
 \frac{\lVert \dot{p}_{trans} \rVert}{\lVert \textbf{p} - \overrightarrow{FOE}\rVert}
$$
>[!INFO]
>points at same radial distance from FOE have flow vector lengths proportional to inverse depth( or inverse time to collision)

>this means that if we get flow vectors we can guage TTC based on it's length 
>larger the vector length, smaller the time to collision which makes sense 
