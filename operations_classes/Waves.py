import cv2 as cv
import math
import numpy as np


class Waves:
    def __init__(self, image):
        self.image = image
        self.height = image.shape[0]
        self.width = image.shape[1]
        self.vertical_window_title = 'Vertical'
        self.horizontal_window_title = 'Horizontal'
        self.both_window_title = 'Both Horizontal & Vertical'


    def start(self):
        pass

    def startVertical(self):
        cv.namedWindow(self.vertical_window_title)
        cv.createTrackbar('value', self.vertical_window_title, 0, 25,
                          self.vertical)
        self.vertical(0)
        cv.waitKey(0)

    def vertical(self, val):
        img_output = np.zeros(self.image.shape, dtype=self.image.dtype)
        for i in range(self.height):
            for j in range(self.width):
                offset_x = int(val * math.sin(2 * 3.14 * i / 180))
                offset_y = 0
                if j + offset_x < self.height:
                    img_output[i, j] = self.image[i, (j + offset_x) % self.width]
                else:
                    img_output[i, j] = 255
        cv.imshow(self.vertical_window_title, img_output)

    def startHorizontal(self):
        cv.namedWindow(self.horizontal_window_title)
        cv.createTrackbar('value', self.horizontal_window_title, 0, 16,
                          self.horizontal)
        self.horizontal(0)
        cv.waitKey(0)

    def horizontal(self, val):
        img_output = np.zeros(self.image.shape, dtype=self.image.dtype)
        for i in range(self.height):
            for j in range(self.width):
                offset_x = 0
                offset_y = int(val * math.sin(2 * 3.14 * j / 150))
                if i + offset_y < self.height:
                    img_output[i, j] = self.image[(i + offset_y) % self.height, j]
                else:
                    img_output[i, j] = 255
        cv.imshow(self.horizontal_window_title, img_output)

    def startBoth(self):
        cv.namedWindow(self.both_window_title)
        cv.createTrackbar('value', self.both_window_title, 0, 20,
                          self.both)
        self.both(0)
        cv.waitKey(0)

    def both(self, val):
        img_output = np.zeros(self.image.shape, dtype=self.image.dtype)
        for i in range(self.height):
            for j in range(self.width):
                offset_x = int(val * math.sin(2 * 3.14 * i / 150))
                offset_y = int(val * math.cos(2 * 3.14 * j / 150))
                if i + offset_y < self.height and j + offset_x < self.width:
                    img_output[i, j] = self.image[(i + offset_y) % self.height, (j + offset_x) % self.width]
                else:
                    img_output[i, j] = 255
        cv.imshow(self.both_window_title, img_output)
