
parent array -> keeps the parent of individual nodes
rank array -> keeps the number of connected elements
union(n1,n2) -> finds out parent of the node n1,n2 -> if they are both same then do nothing
if they are not then merge them to the one which has lower rank 

find(n) -> finds out parent of node n using parent array (something about path optimization by assigning grand parent)
