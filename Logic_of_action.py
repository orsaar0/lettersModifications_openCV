import cv2.cv2 as cv
import numpy as np
import os
import math
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
from DilationOrErosion import DilationOrErosion
from Waves import Waves
from Mirror import Mirror


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
    waves()
    # mirroring()
    # rotate()
    # blurring()


def resize():
    global image
    image = cv.resize(image, (500, 500))
    # image = resized
    # cv.imshow('RESIZED', image)
    # cv.waitKey(0)


def rotate():
    rotate_degrees = input("rotate degrees optins are:(1-360) ")
    height, width = image.shape[:2]
    rotation_matrix = cv.getRotationMatrix2D((width / 2, height / 2), int(rotate_degrees) % 360, 1)
    rotated_image = cv.warpAffine(image, rotation_matrix, (width, height))
    cv.imshow('rotated', rotated_image)
    cv.waitKey(0)


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
    mirror.startMir()
    # # cv.imshow('fliped',ImageOps.mirror(bet))
    #
    # img = image
    # # Mirror in x direction (flip horizontally)
    # while True:
    #     pick_flip = input(
    #         "pick flip: \n 0\tflip horizontally\n 1\tflip vertically\n 2\tflip horizontally and vertically\n")
    #     if pick_flip == '0':
    #         imgX = np.flip(image, axis=1)
    #         cv.imshow('imgX', imgX)
    #         cv.waitKey(0)
    #         break
    #     # Mirror in y direction (flip vertically)
    #     elif pick_flip == '1':
    #         imgY = np.flip(image, axis=0)
    #         cv.imshow('imgY', imgY)
    #         cv.waitKey(0)
    #         break
    #     # Mirror in both directions (flip horizontally and vertically)
    #     elif pick_flip == '2':
    #         imgXY = np.flip(image, axis=(0, 1))
    #         cv.imshow('imgXY', imgXY)
    #         cv.waitKey(0)
    #         break
    #     else:
    #         print("smart guy? try again")


def blurring():
    while True:
        how_much_blur = input("0\t tiny blur\n1\t little blur\n2\t medium blur\n3\t big blur\n4\t mega blur\n ")
        if how_much_blur == '0':
            blur = cv.GaussianBlur(image, (3, 3), cv.BORDER_DEFAULT)
            cv.imshow('Blur letter', blur)
            cv.waitKey(0)
            break
        elif how_much_blur == '1':
            blur = cv.GaussianBlur(image, (5, 5), cv.BORDER_DEFAULT)
            cv.imshow('Blur letter', blur)
            cv.waitKey(0)
            break
        elif how_much_blur == '2':
            blur = cv.GaussianBlur(image, (7, 7), cv.BORDER_DEFAULT)
            cv.imshow('Blur letter', blur)
            cv.waitKey(0)
            break
        elif how_much_blur == '3':
            blur = cv.GaussianBlur(image, (11, 11), cv.BORDER_DEFAULT)
            cv.imshow('Blur letter', blur)
            cv.waitKey(0)
            break
        elif how_much_blur == '4':
            blur = cv.GaussianBlur(image, (15, 15), cv.BORDER_DEFAULT)
            cv.imshow('Blur letter', blur)
            cv.waitKey(0)
            break
        else:
            print("smart guy ha?")


def vertical_wave():
    img_output = np.zeros(image.shape, dtype=image.dtype)
    for i in range(height):
        for j in range(width):
            offset_x = int(25.0 * math.sin(2 * 3.14 * i / 180))
            offset_y = 0
            if j + offset_x < height:
                img_output[i, j] = image[i, (j + offset_x) % width]
            else:
                img_output[i, j] = 255
    cv.imshow('Vertical wave', img_output)
    cv.waitKey(0)


def horizontal_wave():
    img_output = np.zeros(image.shape, dtype=image.dtype)
    for i in range(height):
        for j in range(width):
            offset_x = 0
            offset_y = int(16.0 * math.sin(2 * 3.14 * j / 150))
            if i + offset_y < height:
                img_output[i, j] = image[(i + offset_y) % height, j]
            else:
                img_output[i, j] = 0
    cv.imshow('Horizontal wave', img_output)
    cv.waitKey(0)


def both_waves():
    img_output = np.zeros(image.shape, dtype=image.dtype)

    for i in range(height):
        for j in range(width):
            offset_x = int(20.0 * math.sin(2 * 3.14 * i / 150))
            offset_y = int(20.0 * math.cos(2 * 3.14 * j / 150))
            if i + offset_y < height and j + offset_x < width:
                img_output[i, j] = image[(i + offset_y) % height, (j + offset_x) % width]
            else:
                img_output[i, j] = 0
    cv.imshow('Multidirectional wave', img_output)
    cv.waitKey(0)


if __name__ == '__main__':
    main()
