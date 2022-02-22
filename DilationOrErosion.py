import cv2 as cv


# optional mapping of values with morphological shapes
def morph_shape(val):
    if val == 0:
        return cv.MORPH_RECT
    elif val == 1:
        return cv.MORPH_CROSS
    elif val == 2:
        return cv.MORPH_ELLIPSE


class DilationOrErosion:
    def __init__(self, src):
        self.src = src
        self.erosion_size = 0
        self.max_elem = 2
        self.max_kernel_size = 21
        self.title_trackbar_element_shape = 'Element:\n 0: Rect \n 1: Cross \n 2: Ellipse'
        self.title_trackbar_kernel_size = 'Kernel size:\n 2n +1'
        self.title_dilation_window = 'Dilation Demo'
        self.title_erosion_window = 'Erosion Demo'

    def startDel(self):
        cv.namedWindow(self.title_dilation_window)
        cv.createTrackbar(self.title_trackbar_element_shape, self.title_dilation_window, 0, self.max_elem,
                          self.dilatation)
        cv.createTrackbar(self.title_trackbar_kernel_size, self.title_dilation_window, 0, self.max_kernel_size,
                          self.dilatation)
        self.dilatation(0)
        cv.waitKey(0)

    def dilatation(self, val):
        dilatation_size = cv.getTrackbarPos(self.title_trackbar_kernel_size, self.title_dilation_window)
        dilation_shape = morph_shape(
            cv.getTrackbarPos(self.title_trackbar_element_shape, self.title_dilation_window))
        element = cv.getStructuringElement(dilation_shape, (2 * dilatation_size + 1, 2 * dilatation_size + 1),
                                           (dilatation_size, dilatation_size))
        dilatation_dst = cv.dilate(self.src, element)
        cv.imshow(self.title_dilation_window, dilatation_dst)

    def startEro(self):
        cv.namedWindow(self.title_erosion_window)
        cv.createTrackbar(self.title_trackbar_element_shape, self.title_erosion_window, 0, self.max_elem, self.erosion)
        cv.createTrackbar(self.title_trackbar_kernel_size, self.title_erosion_window, 0, self.max_kernel_size, self.erosion)

        self.erosion(0)
        cv.waitKey(0)

    def erosion(self, val):
        erosion_size = cv.getTrackbarPos(self.title_trackbar_kernel_size, self.title_erosion_window)
        erosion_shape = morph_shape(cv.getTrackbarPos(self.title_trackbar_element_shape, self.title_erosion_window))

        element = cv.getStructuringElement(erosion_shape, (2 * erosion_size + 1, 2 * erosion_size + 1),
                                           (erosion_size, erosion_size))

        erosion_dst = cv.erode(self.src, element)
        cv.imshow(self.title_erosion_window, erosion_dst)
