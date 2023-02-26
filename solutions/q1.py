'''Q1. Read, write and display an Image.'''

# Importing necessary libraries
import cv2
import numpy as np
import os

# Creating a directory to save the output images
if not os.path.exists('./output images/q1'):
    os.makedirs('./output images/q1')

# Reading the image
img = cv2.imread('image1.png')

# Displaying the image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Writing the image
cv2.imwrite('./output images/q1/output.png', img)
