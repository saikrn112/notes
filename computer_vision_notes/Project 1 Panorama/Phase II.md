
### Data Generation
```
load one image
reize it to 320 x 240
take a patch of size 128 x 128
make some random perturbations
calculate homography between the perturbed image points and acutal points Cb - Ca -- H_a^{b}
run inverse homography on the actual image to make the perturbed image square
store the patches Ca and Cb along with H_{4pt} = Cb-Ca

```


https://discuss.pytorch.org/t/unable-to-backpropagate-the-network-with-custom-layer/86400/6
