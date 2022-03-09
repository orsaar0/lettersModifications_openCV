import cv2.cv2 as cv
from lettersModifications_openCV.operations_classes.DilationOrErosion import DilationOrErosion
from lettersModifications_openCV.operations_classes.Waves import Waves
from lettersModifications_openCV.operations_classes.Mirror import Mirror
from lettersModifications_openCV.operations_classes.Blur import Blur
from lettersModifications_openCV.operations_classes.Rotate import Rotate
from lettersModifications_openCV.operations_classes.Tilt import Tilt


class Actions:
    def __init__(self, url):
        self.image = cv.imread(url)
        self.resize()

    def url_setter(self, url):
        self.image = cv.imread(url)
        self.resize()

    def resize(self):
        self.image = cv.resize(self.image, (500, 500))

    def rotate(self):
        rotate = Rotate(image=self.image)
        rotate.start()

    def inverted(self):
        ret, thresh = cv.threshold(self.image, 120, 255, cv.THRESH_BINARY_INV)
        cv.imshow('Binary Threshold Inverted', thresh)
        cv.waitKey(0)

    def rounding_corners(self):
        pass

    def dilation(self):
        dilt = DilationOrErosion(src=self.image)
        dilt.startDel()

    def erosion(self):
        dilt = DilationOrErosion(src=self.image)
        dilt.startEro()

    def waves(self):
        wave = Waves(self.image)
        wave.start()

    def mirroring(self):
        mirror = Mirror(image=self.image)
        mirror.start()

    def blurring(self):
        blur = Blur(self.image)
        blur.start()

    def tilt(self):
        tilt = Tilt(self.image)
        tilt.start()
