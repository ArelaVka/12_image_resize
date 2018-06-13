# Image Resizer

Script can help you to resize image as you wish...

# How to use

To use script you need specify full path to image. You can use arguments to resize image with special params:
```
usage: image_resize.py [-h] -I <path_to_file> [-W N] [-H N] [-S N]
                       [-O <output_directory>]

Image resize program

optional arguments:
  -h, --help            show this help message and exit
  -I <path_to_file>, --input_file <path_to_file>
                        full path to the image which you need to transform
  -W N, --width N       width of output image (pix)
  -H N, --height N      height of output image (pix)
  -S N, --scale N       scale of output image (from 0)
  -O <output_directory>, --output_directory <output_directory>
                        path to output file directory
```

Example (Windows):
```cmd
C:\>python C:\12_image_resize\image_resize.py -I C:\pic.jpg -S 0.5
```
Result - saved image "pic__375x211.jpg" with ratio 0.5. 

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
