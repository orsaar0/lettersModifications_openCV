import cv2 as cv
import numpy as np


def shape(val):
    if val == 0:
        return 0
    elif val == 1:
        return 1
    elif val == 2:
        return 0, 1


class Mirror:
    def __init__(self, image):
        self.image = image
        self.mirroring_window_title = 'Mirror'

    def start(self):
        cv.namedWindow(self.mirroring_window_title)
        cv.createTrackbar('axis', self.mirroring_window_title, 0, 2,
                          self.mirror)
        self.mirror(0)
        cv.waitKey(0)

    # Simply take the pixels array and flip it
    def mirror(self, val):
        axis = shape(val)
        imp_output = np.flip(self.image, axis=axis)
        cv.imshow(self.mirroring_window_title, imp_output)
