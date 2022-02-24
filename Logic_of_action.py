import cv2.cv2 as cv
from lettersModifications_openCV.operations_classes.DilationOrErosion import DilationOrErosion
from lettersModifications_openCV.operations_classes.Waves import Waves
from lettersModifications_openCV.operations_classes.Mirror import Mirror
from lettersModifications_openCV.operations_classes.Blur import Blur
from lettersModifications_openCV.operations_classes.Rotate import Rotate


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
        while True:
            pick_wave = input(
                "pick wave: \n 0\tvertical wave\n 1\thorizontally wave\n 2\thorizontally and vertically wave\n")
            if pick_wave == '0':
                wave.startVertical()
                break
            elif pick_wave == '1':
                wave.startHorizontal()
                break
            elif pick_wave == '2':
                wave.startBoth()
                break

    def mirroring(self):
        mirror = Mirror(image=self.image)
        mirror.start()

    def blurring(self):
        blur = Blur(self.image)
        blur.start()
