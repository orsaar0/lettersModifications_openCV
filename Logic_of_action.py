import cv2.cv2 as cv
from lettersModifications_openCV.operations_classes.DilationOrErosion import DilationOrErosion
from lettersModifications_openCV.operations_classes.Waves import Waves
from lettersModifications_openCV.operations_classes.Mirror import Mirror
from lettersModifications_openCV.operations_classes.Blur import Blur
from lettersModifications_openCV.operations_classes.Rotate import Rotate



def main():
    global image, height, width
    image = cv.imread('Alef_bet_images/Words.jpg')
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # resize()
    height = image.shape[0]
    width = image.shape[1]
    cv.imshow('Original Letter Image', image)
    # rounding_corners()
    # inverted()
    # erosion()
    # dilation()
    # waves()
    # mirroring()
    rotate()
    # blurring()


def resize():
    global image
    image = cv.resize(image, (500, 500))
    # image = resized
    # cv.imshow('RESIZED', image)
    # cv.waitKey(0)


def rotate():
    rotate = Rotate(image=image)
    rotate.start()


def inverted():
    ret, thresh = cv.threshold(image, 120, 255, cv.THRESH_BINARY_INV)
    cv.imshow('Binary Threshold Inverted', thresh)
    cv.waitKey(0)


def rounding_corners():
    pass
    # maxCorners = 10
    # # Parameters for Shi-Tomasi algorithm
    # qualityLevel = 0.1
    # minDistance = 10
    # blockSize = 3
    # gradientSize = 3
    # useHarrisDetector = True
    # k = 0.04
    # corners = cv.goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance, None, \
    #                                  blockSize=blockSize, gradientSize=gradientSize,
    #                                  useHarrisDetector=useHarrisDetector, k=k)
    # x = []
    # y = []
    # for j in corners.shape[0]:
    #     for i in corners[j]:
    #         # for (j, k) in corners[]
    #         x.append(i[0])
    #         y.append(i[1])
    # X = np.array(x)
    # Y = np.array(y)
    # X_Y_Spline = make_interp_spline(x, y)
    #
    # # Returns evenly spaced numbers
    # # over a specified interval.
    # X_ = np.linspace(x.min(), x.max(), 500)
    # Y_ = X_Y_Spline(X_)
    #
    # # Plotting the Graph
    # plt.plot(X_, Y_)
    # plt.title("Plot Smooth Curve Using the scipy.interpolate.make_interp_spline() Class")
    # plt.xlabel("X")
    # plt.ylabel("Y")
    # plt.show()
    #
    # # radius = 5
    # # for i in range(corners.shape[0]):
    # #     print("corner indices: ", str(corners[i, 0, 0]), str(corners[i, 0, 1]))
    # #     image[int(corners[i, 0, 1]), int(corners[i, 0, 0])] = 255
    # #     cv.circle(image, (int(corners[i, 0, 0]), int(corners[i, 0, 1])), radius,
    # #               (256, 256, 256), cv.FILLED)
    # cv.imshow('rounded corners', image)
    # cv.waitKey(0)


def dilation():
    dilt = DilationOrErosion(src=image)
    dilt.startDel()


def erosion():
    dilt = DilationOrErosion(src=image)
    dilt.startEro()


def waves():
    wave = Waves(image)
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


def mirroring():
    mirror = Mirror(image=image)
    mirror.start()


def blurring():
    blur = Blur(image)
    blur.start()


if __name__ == '__main__':
    main()
