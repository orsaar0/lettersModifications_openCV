import cv2 as cv


class Blur:
    def __init__(self, image):
        self.image = image
        self.blur_window_title = 'Blur'

    def start(self):
        cv.namedWindow(self.blur_window_title)
        cv.createTrackbar('Intense', self.blur_window_title, 0, 20,
                          self.blur)
        self.blur(1)
        cv.waitKey(0)

    # We used the simple function blur() which receives the source image and a kernel size
    # It simply takes the average of all the pixels under the kernel area
    def blur(self, val):
        image_output = cv.blur(self.image, (val, val))
        cv.imshow(self.blur_window_title, image_output)
