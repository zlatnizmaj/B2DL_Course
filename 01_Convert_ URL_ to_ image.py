# check version of packages
# import the neccessary packages
import numpy as np
import urllib.request
import matplotlib.pyplot as plt
import cv2
import tensorflow as tf
import keras

# show version of packages

# python version
from platform import  python_version
print('Python version: {}'.format(python_version()))

# opencv version
print('OpenCV version: {}'.format(cv2.__version__))

# tensorflow version
print('Tensorflow version: {}'.format(tf.__version__))

# keras version
print('Keras version: {}'.format(keras.__version__))

# Convert URL to image with Python and OpenCV
# METHOD #1: OpenCV, NumPy, and urllib
def url_to_image(url):
    # download the image, convert it to a Numpy array, and then read
    # it into OpenCV format
    resp = urllib.request.urlopen(url)