'''Q8. Read a gray scale image and negate the image.'''

# Importing necessary libraries
import cv2
import numpy as np

# Read the grayscale image
img = cv2.imread('image1.png', cv2.IMREAD_GRAYSCALE)

# Negating the image
negated_img = 255 - img

# Displaying the negated image
cv2.imshow('Negated Image', negated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Writing the negated image
cv2.imwrite('negated.png', negated_img)
