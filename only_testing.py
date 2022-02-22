from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse
import random as rng

source_window = 'Image'
maxTrackbar = 100
rng.seed(12345)


def goodFeaturesToTrack_Demo(val):
    maxCorners = max(val, 1)
    # Parameters for Shi-Tomasi algorithm
    qualityLevel = 0.1
    minDistance = 10
    blockSize = 3
    gradientSize = 3
    useHarrisDetector = True
    k = 0.04
    # Copy the source image
    copy = np.copy(src)
    # Apply corner detection
    corners = cv.goodFeaturesToTrack(src_gray, maxCorners, qualityLevel, minDistance, None, \
                                     blockSize=blockSize, gradientSize=gradientSize,
                                     useHarrisDetector=useHarrisDetector, k=k)
    # Draw corners detected
    print('** Number of corners detected:', corners.shape[0])
    radius = 4
    for i in range(corners.shape[0]):
        print("corner indices: ", str(corners[i, 0, 0]) , str(corners[i, 0, 1]))
        copy[int(corners[i, 0, 1]), int(corners[i, 0, 0])] = 255
        # cv.circle(copy, (int(corners[i, 0, 0]), int(corners[i, 0, 1])), radius,
        #           (256, 256, 256), cv.FILLED)
    # Show what you got
    cv.namedWindow(source_window)
    cv.imshow(source_window, copy)


# Load source image and convert it to gray
parser = argparse.ArgumentParser(description='Code for Shi-Tomasi corner detector tutorial.')
parser.add_argument('--input', help='Path to input image.', default='pic3.png')
args = parser.parse_args()
src = cv.imread('Alef_bet_images/bet.jpg')
if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
# Create a window and a trackbar
cv.namedWindow(source_window)
maxCorners = 10  # initial threshold
# for i in range(8):
cv.createTrackbar('Threshold: ', source_window, maxCorners, maxTrackbar, goodFeaturesToTrack_Demo)
# cv.imshow(source_window, src)
# goodFeaturesToTrack_Demo(maxCorners)
cv.waitKey()
