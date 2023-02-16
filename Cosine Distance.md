that measures the angle between two vectors in a high-dimensional space. 

In the context of feature matching, cosine distance is often used as a measure of similarity between feature vectors. 

Given two feature vectors `u` and `v`, the cosine distance between them is defined as:

```
cosine_distance(u, v) = 1 - (u dot v) / (||u|| * ||v||)
```

will be invariant of magnitude of vectors, just measuring the similarity 