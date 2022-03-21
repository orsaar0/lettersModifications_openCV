import cv2 as cv
import numpy as np


class Tilt:
    def __init__(self, image):
        self.image = image
        self.tilt_window_title = 'Tilt'

    def start(self):
        cv.namedWindow(self.tilt_window_title)
        cv.createTrackbar('value', self.tilt_window_title, 0, 100,
                          self.tilt)
        self.tilt(0)
        cv.waitKey(0)

    # Tilt the image using getAffineTransform() which takes as input the three
    # Define the 3 pairs of corresponding points srcTri and dstTri
    # Calculate the transformation matrix using cv2.getAffineTransform()
    # Apply the affine transformation using cv2.warpAffine() to express scale operation
    # The size and orientation of the triangle defined by the 3 points change.
    def tilt(self, val):
        srcTri = np.array([[0, val], [self.image.shape[1] - 1, val], [val, self.image.shape[0] - 1]]).astype(np.float32)
        dstTri = np.array([[val, self.image.shape[1] * 0.33], [self.image.shape[1] * 0.85, self.image.shape[0] * 0.25],
                           [self.image.shape[1] * 0.15, self.image.shape[0] * 0.7]]).astype(np.float32)
        warp_mat = cv.getAffineTransform(srcTri, dstTri)
        warp_dst = cv.warpAffine(self.image, warp_mat, (self.image.shape[1], self.image.shape[0]))
        cv.resize(warp_dst, (500, 500))
        cv.imshow(self.tilt_window_title, warp_dst)
