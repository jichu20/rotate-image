import cv2
import math
import numpy as np
from scipy import ndimage

# IMAGE_FILE_LOCATION = "./resources/IMG_3536.jpg"  # Photo by Amanda Jones on Unsplash
# input_img = cv2.imread(IMAGE_FILE_LOCATION)  # image read


#####################################################################################################
# ORIENTATION CORRECTION/ADJUSTMENT


def orientation_correction(img, save_image=False):
    # GrayScale Conversion for the Canny Algorithm
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Canny Algorithm for edge detection was developed by John F. Canny not Kennedy!! :)
    img_edges = cv2.Canny(img_gray, 100, 100, apertureSize=3)
    # Using Houghlines to detect lines
    lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=5)

    # Finding angle of lines in polar coordinates
    angles = []
    for x1, y1, x2, y2 in lines[0]:
        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
        angles.append(angle)

    # Getting the median angle
    median_angle = np.median(angles)

    # Rotating the image with this median angle
    img_rotated = ndimage.rotate(img, median_angle)

    if save_image:
        cv2.imwrite("orientation_corrected.jpg", img_rotated)
    return img_rotated


#####################################################################################################
