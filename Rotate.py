import cv2 as cv


class Rotate:
    def __init__(self, image):
        self.image = image
        self.rotate_window_title = 'Rotate'

    def start(self):
        cv.namedWindow(self.rotate_window_title)
        cv.createTrackbar('Angle', self.rotate_window_title, 0, 360,
                          self.rotate)
        self.rotate(1)
        cv.waitKey(0)

    def rotate(self, val):
        height, width = self.image.shape[:2]
        rotation_matrix = cv.getRotationMatrix2D((width / 2, height / 2), val % 360, 1)
        image_output = cv.warpAffine(self.image, rotation_matrix, (width, height))
        cv.imshow(self.rotate_window_title, image_output)
