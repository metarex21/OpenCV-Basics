'''Q5. Find the mean of a gray-scale image and set it as the threshold value. Using the threshold value convert the image into binary image and display it.'''

# Importing necessary libraries
import cv2
import numpy as np

# Reading the grayscale image
img = cv2.imread('image1.png', cv2.IMREAD_GRAYSCALE)

# Finding the mean of the image
mean = np.mean(img)

# Setting the threshold value
threshold = mean

# Converting the image into binary using the threshold value
_, binary_img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

# Displaying the binary image
cv2.imshow('Binary Image', binary_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Writing the binary image
cv2.imwrite('output3.png', binary_img)

