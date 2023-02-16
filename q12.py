'''Q12. Convert the RGB image into CMY model and CMY model into RGB model.'''

# Importing necessary libraries
import cv2
import numpy as np

# Loading the RGB image
rgb_image = cv2.imread('image1.png')

# Converting the RGB image to CMY model
cmy_image = 255 - rgb_image

# Converting the CMY image to RGB model
rgb_image2 = 255 - cmy_image

# Saving the CMY image
cv2.imwrite("./output images/cmy_image.png", cmy_image)

# Saving the RGB image
cv2.imwrite("./output images/rgb_image3.png", rgb_image2)
