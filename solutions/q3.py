'''Q3. Divide an image into n square parts and saves the output images.'''

# Importing necessary libraries
import cv2
import numpy as np
import os
import math

# Creating a directory to save the output images
if not os.path.exists('./output images/q3'):
    os.makedirs('./output images/q3')

# Reading the input image
img = cv2.imread('image1.png')

# Getting the dimensions of the input image
height, width, channels = img.shape

# Taking n as input
n = int(input("Enter a square number: "))

# Checking if n is a perfect square
if int(math.sqrt(n))**2 != n:
    print("Invalid number")
else:
    # Calculating the size of each square
    square_size = int(math.sqrt((height*width)/n))

    # Calculating the number of squares in each row and column
    num_squares = int(math.sqrt(n))

    # Dividing the image into squares and save the output images
    for i in range(num_squares):
        for j in range(num_squares):
            square_img = img[i*square_size:(i+1)*square_size, j*square_size:(j+1)*square_size]
            cv2.imwrite(f"./output images/q3/grid_{i*num_squares+j+1}.png", square_img)
