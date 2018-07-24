# Mosaic Maker
A mosaic maker implemented in Python. This program makes use of two mathematical concepts. I will give a brief description as to their ideas as well as how I use them:
* **stochastic sampling** 
  
  The term *stochastic sampling* is a composition of two mathematical concepts. To begin, *sampling* refers to the act of selecting pieces from a whole. In this program, the pieces are the pixels and the whole is the image. This is a relatively easy process when using the `PIL` module. The second term, *stochastic*, is another mathematical term which essentially describes randomness. In conjunction with the previously described concept, as well as the fact that I partition the image into *n*-partitions, this composition refers to the random selection of pixels from an *n*-partitions of the image. In order to improve run-time, we take *samples* from the image, rather than averaging based on *every* pixel in the image.
  
  Pro(s):
  * It is possible that given image(s) can have low variations in colors in specific sections (e.g. a square image circumscribing a black circle), even in separate partitions of the image(s). To deal with this possibility, we improve upon the typical form of *sampling*, which partitions and finds the average from the RGB color values from the *center of the partitions*. Using randomly selected pixels improves the chances that the overall average color from our samples will be representative of the actual overall color of the image.
  * As aforementioned, sampling improves the run-time of our program, since we don't have to access each individual pixel to grab its RGB color value.
  
  Con(s):
  * As is typical, *randomness* is an idea; stochastic implementations aren't perfect and my use of it could also be improved.
  * It is very well possible that using *randomness* to determine the average RGB color value of the entire image will lead to an average which is less than ideal, even less so than using normal sampling. However, this is a weak-"con", since imperfections tend to lend realism to photomosaics.
  
* **Euclidean metric**
  The *Euclidean metric*, also know as *Euclidean distance*, is a mathematical formula. The general form is `d(x, y) = sqrt( (x_1 - y_1)**2 + (x_2 - y_2)**2 + ... + (x_n - y_n)**2 )`. We shall be using this formula in 3-dimensions, to represent the RGB color vectors. In doing so, we merely calculate the distance between two RGB vectors and use this distance as a metric to determine the two RGB vectors' similarity, e.g. low distances indicate high color similarities while high distances indicate low color similarities. 
  
  Pro(s):
  * Easy to implement.
  
  Con(s):
  * One of many methods to calculate color similarities. See [here](https://stackoverflow.com/questions/9018016/how-to-compare-two-colors-for-similarity-difference). 

## Getting Started
To get started, make a clone of this repository in your local machine. 

* To clone with HTTPS, use the command `git clone -b https://github.com/natn2323/mosaic-maker-python.git`.

* To clone with SSH, use the command `git@github.com:natn2323/mosaic-maker-python.git`.

* Or download the repository directly, by using the download button.

## Prerequisites
This program makes use of the following non-built-in module(s): 
* `PIL` 

To install the non-built-in module(s), use the following command(s):
```
pip install Pillow
```

## Running the Program
Below is the usage for this program. 

```
usage: sampler.py [-h] [-i]

optional arguments:
  -h, --help         show this help message and exit
  -i, --interactive  interactive mode
```

In interactive mode, the program will provide suggestions for various parameters depending on the given inputs. For instance, in the case that the user asks for more partitions than are pixels in the given image, the program will ask for user input in order to correct the improper use case.

