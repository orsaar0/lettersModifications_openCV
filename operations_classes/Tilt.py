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

    def tilt(self, val):
        srcTri = np.array([[0, val], [self.image.shape[1] - 1, val], [val, self.image.shape[0] - 1]]).astype(np.float32)
        dstTri = np.array([[val, self.image.shape[1] * 0.33], [self.image.shape[1] * 0.85, self.image.shape[0] * 0.25],
                           [self.image.shape[1] * 0.15, self.image.shape[0] * 0.7]]).astype(np.float32)
        warp_mat = cv.getAffineTransform(srcTri, dstTri)
        warp_dst = cv.warpAffine(self.image, warp_mat, (self.image.shape[1], self.image.shape[0]))
        cv.resize(warp_dst, (500, 500))
        # cv.imshow('Warp', warp_dst)
        # cv.waitKey()
        # Rotating the image after Warp
        center = (warp_dst.shape[1] // 2, warp_dst.shape[0] // 2)
        angle = -50
        scale = 0.6
        rot_mat = cv.getRotationMatrix2D(center, angle, scale)
        warp_rotate_dst = cv.warpAffine(warp_dst, rot_mat, (warp_dst.shape[1], warp_dst.shape[0]))
        background = np.zeros([600, 600, 3], dtype=np.uint8)
        background.fill(255)
        # cv.imshow('back', background)
        x_offset = y_offset = 50
        background[y_offset:y_offset + warp_dst.shape[0], x_offset:x_offset + warp_dst.shape[1]] = warp_dst
        # cv.imshow('Source image', self.image)
        cv.imshow(self.tilt_window_title, warp_dst)
        # cv.imshow('Warp + Rotate', warp_rotate_dst)
        # cv.waitKey()