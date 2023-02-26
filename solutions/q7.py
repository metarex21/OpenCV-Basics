'''Q7. Read an gray scale image and write a program to zoom and shrink the image using-

a. Pixel replication method.
b. Interpolation method.
Store the images as necessary.'''

# Importing necessary libraries
import cv2
import numpy as np
import os

# Creating a directory to save the output images
if not os.path.exists('./output images/q7'):
    os.makedirs('./output images/q7')

# Reading the input image
img = cv2.imread('image1.png', cv2.IMREAD_GRAYSCALE)

# Defining the zoom factor
zoom_factor = int(input("Enter Zoom Factor"))

# Resizing the image using pixel replication method
resized_pixel = np.zeros((img.shape[0]*zoom_factor, img.shape[1]*zoom_factor), dtype=np.uint8)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        for k in range(zoom_factor):
            for l in range(zoom_factor):
                resized_pixel[i*zoom_factor+k, j*zoom_factor+l] = img[i, j]

# Resizing the image using interpolation method
resized_interpolation = cv2.resize(img, None, fx=zoom_factor, fy=zoom_factor, interpolation=cv2.INTER_LINEAR)

# Defining the shrink factor
shrink_factor = int(input("Enter Shrink Factor"))

# Resizing the image using pixel replication method
resized_pixel_shrink = np.zeros((int(img.shape[0]/shrink_factor), int(img.shape[1]/shrink_factor)), dtype=np.uint8)
for i in range(0, img.shape[0], shrink_factor):
    for j in range(0, img.shape[1], shrink_factor):
        resized_pixel_shrink[int(i/shrink_factor), int(j/shrink_factor)] = img[i, j]

# Resizing the image using interpolation method
resized_interpolation_shrink = cv2.resize(img, None, fx=1/shrink_factor, fy=1/shrink_factor, interpolation=cv2.INTER_LINEAR)

# Saving the output images
cv2.imwrite('./output images/q7/resized_pixel.jpg', resized_pixel)
cv2.imwrite('./output images/q7/resized_interpolation.jpg', resized_interpolation)
cv2.imwrite('./output images/q7/resized_pixel_shrink.jpg', resized_pixel_shrink)
cv2.imwrite('./output images/q7/resized_interpolation_shrink.jpg', resized_interpolation_shrink)
