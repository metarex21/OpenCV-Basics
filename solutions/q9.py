'''Q9. Read a RGB image. Extract its red, green, and blue components and display it individually.'''
# Importing necessary libraries
import cv2
import numpy as np
import os
import math

# Creating a directory to save the output images
if not os.path.exists('./output images/q9/'):
    os.makedirs('./output images/q9/')
# Reading the RGB image
img = cv2.imread('image1.png')

# Extracting the red, green, and blue components
bx, gx, rx = cv2.split(img)

zeros = np.zeros(bx.shape, np.uint8)

# Merging zeros to make BGR image
b = cv2.merge([bx,zeros,zeros])
g = cv2.merge([zeros,gx,zeros])
r = cv2.merge([zeros,zeros,rx])

# Displaying the red component
cv2.imshow('Red Component', r)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Saving the red component as an image
cv2.imwrite('./output images/q9/red.png', r)

# Displaying the green component
cv2.imshow('Green Component', g)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Saving the green component as an image
cv2.imwrite('./output images/q9/green.png', g)

# Displaying the blue component
cv2.imshow('Blue Component', b)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Saving the blue component as an image
cv2.imwrite('./output images/q9/blue.png', b)
