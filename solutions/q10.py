'''Q10. Read a RGB image and convert it to a YIQ model and reconvert it back to RGB.'''

# Importing necessary libraries
import cv2
import numpy as np
# Read the RGB image
img = cv2.imread('image1.png')

# Convert the RGB image to YIQ
img_yiq = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# Split the Y, I, and Q components
y, i, q = cv2.split(img_yiq)

# Convert the YIQ image back to RGB
img_rgb = cv2.cvtColor(img_yiq, cv2.COLOR_YCrCb2BGR)

# Display the original and converted RGB images
cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('YIQ model', img_yiq)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('Converted Image', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Writing the YIQ image
cv2.imwrite('YIQ model.png', img_yiq)

# Writing the Converted image
cv2.imwrite('RGB converted.png', img_rgb)