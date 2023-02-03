'''Q2. Mirror and flip an Image.'''

# Importing necessary libraries
import cv2
import numpy as np

# Reading the image
img = cv2.imread('image1.png')

# Mirroring the image horizontally
img_mirror = cv2.flip(img, 1)

# Flipping the image vertically
img_flip = cv2.flip(img, 0)

# Displaying the mirrored image
cv2.imshow('Mirrored Image', img_mirror)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Writing the mirrored image
cv2.imwrite('mirrored.png', img_mirror)

# Displaying the flipped image
cv2.imshow('Flipped Image', img_flip)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Writing the flipped image
cv2.imwrite('flipped.png', img_flip)
