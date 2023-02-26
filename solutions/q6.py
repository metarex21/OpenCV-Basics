'''Q6. python program to change the resolution of an image from 1 bit to 8 bit.'''

# Importing necessary libraries
import cv2
import numpy as np
import os
import math

# Creating a directory to save the output images
if not os.path.exists('./output images/q6'):
    os.makedirs('./output images/q6')

# Reading the image
img = cv2.imread('image1.png')

def downscale(img,bits): #img or src image and bits is the required bits
    level = 2**bits - 1
    img_xbit = (img // (256//level)) * (256//level)
    return img_xbit

def dispXwrite(img,bits):
    imgx=downscale(img,bits)
    cv2.imshow(str(bits)+'-bit Image', imgx) #displays the image
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('./output images/q6/output_'+str(bits)+'bit.png', imgx) #writes the image with suitable name

for bits in range(8,0,-1):
    dispXwrite(img,bits)