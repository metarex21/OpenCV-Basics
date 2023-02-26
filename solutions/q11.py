'''Q11. Convert an RGB image to indexed image and followed by RGB image.'''

# Importing necessary libraries
import cv2
import numpy as np
import os
import math

# Creating a directory to save the output images
if not os.path.exists('./output images/q11/'):
    os.makedirs('./output images/q11/')

# Loading the RGB image
rgb_image =cv2.imread('image1.png')

# Converting the RGB image to an indexed image with a maximum of 256 colors
indexed_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)
indexed_image = cv2.applyColorMap(indexed_image, cv2.COLORMAP_JET)

# Saving the indexed image
cv2.imwrite("./output images/q11/indexed_image.png", indexed_image)

# Converting the indexed image back to an RGB image
rgb_image2 = cv2.cvtColor(indexed_image, cv2.COLOR_BGR2RGB)

# Saving the RGB image
cv2.imwrite("./output images/q11/rgb_image2.png", rgb_image2)
