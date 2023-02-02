### InOrder 
```
left inOrder(root->left)
root
right inOrder(root->right)
```

##### Uses:
	in BST - inOrder Traversal gives nodes in non decreasing order


##### Complexity:
	Time: O(N) - Number of nodes
	Memo: O(h) - height of the tree

### PreOrder 
```
root
left preOrder(root->left)
right preOrder(root->right)
```


##### Uses:
	copy of tree
	also to get prefix expresessions of an expression tree 
what is expression tree? - [GfG](https://www.geeksforgeeks.org/expression-tree/)


##### Complexity:
	Time: O(N) - Number of nodes
	Memo: O(h) - height of the tree

### PostOrder 
```
left preOrder(root->left)
right preOrder(root->right)
root
```


##### Uses:
	delete a tree
	also to get postfix expresessions of an expression tree 


##### Complexity:
	Time: O(N) - Number of nodes
	Memo: O(h) - height of the tree

Tree traversal complexity
- skewered tree - only one has nodes
- balanced tree - equal number of nodes
![[tree_traversal_complexity.png]]

### Level Order