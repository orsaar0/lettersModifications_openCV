import cv2 as cv


class Blur:
    def __init__(self, image):
        self.image = image
        self.blur_window_title = 'Blur'

    def start(self):
        cv.namedWindow(self.blur_window_title)
        cv.createTrackbar('Intense', self.blur_window_title, 0, 10,
                          self.blur)
        self.blur(1)
        cv.waitKey(0)

    def blur(self, val):
        kernel_size = 2 * val + 1
        image_output = cv.GaussianBlur(self.image, (kernel_size, kernel_size), cv.BORDER_DEFAULT)
        cv.imshow(self.blur_window_title, image_output)
