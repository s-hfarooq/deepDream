# deepDream

Deep Dream model for any image size

View `python/input` to view the original images, and `python/output/IMAGE_NUM` to view the output of all layers for every example image.

To run, paste all input images into the `input` directory. They must be numerically named (starting at 1), and must only be `.jpg` files. The output files will be located in the `output` directory under whichever image number you desire.


## Example
### Image 1:
Input:
![input](input/1.jpg "Input1")


Output of layer 1
![output1](output/1/img1_L1.jpg)

Output of layer 2
![output2](output/1/img1_L2.jpg)

### Image 2:
Input:
![input](input/2.jpg "Input1")


Output of layer 1
![output1](output/2/img2_L1.jpg)

Output of layer 2
![output2](output/2/img2_L2.jpg)
