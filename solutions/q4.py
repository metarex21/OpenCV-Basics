'''Q4. Read a gray-scale image, modify the pixel intensities which are greater than 120 as white, less than 50 as black and rest as unmodified.'''

# Importing necessary libraries
import cv2
import numpy as np
import os
import math

# Creating a directory to save the output images
if not os.path.exists('./output images/q4'):
    os.makedirs('./output images/q4')


# Reading the grayscale image
img = cv2.imread('image1.png', cv2.IMREAD_GRAYSCALE)

# Modifying the pixel intensities
img[img > 120] = 255
img[img < 50] = 0

# Displaying the modified image
cv2.imshow('Modified Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Writing the modified image
cv2.imwrite('./output images/q4/output.png', img)
