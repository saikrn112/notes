
keeps elements in min sorted way in the binary tree 
every level has increasing nodes compared to the parent 


insert -> insert into the last element of the array and then perform heapifyUp
delete -> swap the first and last element and perform heapifyDown

heapifydown
- get left child of i using 2*i+1 
- get the smallest of left and right child (if it exists)
	- if the right child exists and is smaller than left child then keep it tag
- swap with smaller child 
- and repeat until condition of childern being smaller stops or there are no children anymore 
heapifyup
- get parent of node i using (i-1)/2
- see if the parent element is greater than current node 
- if yes, then swap
- do it until there are no more parents or condition of parent being great exists