import cv2.cv2 as cv
import numpy as np
import os
import math


def main():
    global img, bet, rows, cols, kuf
    bet = cv.imread('Alef_bet_images/bet.jpg')
    kuf = cv.imread('Alef_bet_images/kuf.jpg')
    rows, cols, _ = bet.shape
    cv.imshow('kuf1', kuf)

    #erosion()
    #dilation()
    # cv.imshow('bet', bet)
    # waves()
    # mirroring()
    # rotate()
    # blurring()
    # resize()


def resize():
    resized = cv.resize(bet, (500, 500))
    cv.imshow('RESIZED', resized)
    cv.waitKey(0)


def rotate():
    rotate_degrees = input("rotate degrees optins are:(1-360) ")
    height, width = bet.shape[:2]
    rotation_matrix = cv.getRotationMatrix2D((width / 2, height / 2), int(rotate_degrees) % 360, 1)
    rotated_image = cv.warpAffine(bet, rotation_matrix, (width, height))
    cv.imshow('rotated', rotated_image)
    cv.waitKey(0)


def rounding():
    pass


def fat_word():
    textImg = cv.cvtColor(kuf, cv.COLOR_BGR2GRAY)
    _, thres = cv.threshold(textImg, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
    contours, hierarchy = cv.findContours(thres, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cv.imshow('shintzel', kuf)
    for cnt in contours:
        cv.drawContours(kuf, [cnt], 0, 0, round(4))
    cv.imshow('kuf', kuf)
    cv.waitKey(0)


def erosion():
    kernel = np.ones((5, 5), np.uint8)
    img_erosion = cv.erode(kuf, kernel, iterations=1)
    cv.imshow('Erosion', img_erosion)
    cv.waitKey(0)

def dilation():
    kernel = np.ones((5, 5), np.uint8)
    img_dilation = cv.dilate(kuf, kernel, iterations=1)
    cv.imshow('Dilation', img_dilation)
    cv.waitKey(0)


def waves():
    while True:
        pick_wave = input(
            "pick wave: \n 0\tvertical wave\n 1\thorizontally wave\n 2\thorizontally and vertically wave\n")
        if pick_wave == '0':
            vertical_wave()
            break
        elif pick_wave == '1':
            horizontal_wave()
            break
        elif pick_wave == '2':
            both_waves()
            break


def mirroring():
    # cv.imshow('fliped',ImageOps.mirror(bet))

    #img = bet
    # Mirror in x direction (flip horizontally)
    while True:
        pick_flip = input(
            "pick flip: \n 0\tflip horizontally\n 1\tflip vertically\n 2\tflip horizontally and vertically\n")
        if pick_flip == '0':
            imgX = np.flip(bet, axis=1)
            imgX = img[:, ::-1, :]
            cv.imshow('imgX', imgX)
            cv.waitKey(0)
            break
        # Mirror in y direction (flip vertically)
        elif pick_flip == '1':
            imgY = np.flip(bet, axis=0)
            imgY = img[::-1, :, :]
            cv.imshow('imgY', imgY)
            cv.waitKey(0)
            break
        # Mirror in both directions (flip horizontally and vertically)
        elif pick_flip == '2':
            imgXY = np.flip(bet, axis=(0, 1))
            imgXY = img[::-1, ::-1, :]
            cv.imshow('imgXY', imgXY)
            cv.waitKey(0)
            break
        else:
            print("smart guy? try again")


def blurring():
    while True:
        how_much_blur = input("0\t tiny blur\n1\t little blur\n2\t medium blur\n3\t big blur\n4\t mega blur\n ")
        if how_much_blur == '0':
            blur = cv.GaussianBlur(bet, (3, 3), cv.BORDER_DEFAULT)
            cv.imshow('Blur letter', blur)
            cv.waitKey(0)
            break
        elif how_much_blur == '1':
            blur = cv.GaussianBlur(bet, (5, 5), cv.BORDER_DEFAULT)
            cv.imshow('Blur letter', blur)
            cv.waitKey(0)
            break
        elif how_much_blur == '2':
            blur = cv.GaussianBlur(bet, (7, 7), cv.BORDER_DEFAULT)
            cv.imshow('Blur letter', blur)
            cv.waitKey(0)
            break
        elif how_much_blur == '3':
            blur = cv.GaussianBlur(bet, (11, 11), cv.BORDER_DEFAULT)
            cv.imshow('Blur letter', blur)
            cv.waitKey(0)
            break
        elif how_much_blur == '4':
            blur = cv.GaussianBlur(bet, (15, 15), cv.BORDER_DEFAULT)
            cv.imshow('Blur letter', blur)
            cv.waitKey(0)
            break
        else:
            print("smart guy ha?")


def vertical_wave():
    img_output = np.zeros(bet.shape, dtype=bet.dtype)

    for i in range(rows):
        for j in range(cols):
            offset_x = int(25.0 * math.sin(2 * 3.14 * i / 180))
            offset_y = 0
            if j + offset_x < rows:
                img_output[i, j] = bet[i, (j + offset_x) % cols]
            else:
                img_output[i, j] = 0
    cv.imshow('Vertical wave', img_output)
    cv.waitKey(0)


def horizontal_wave():
    img_output = np.zeros(bet.shape, dtype=bet.dtype)

    for i in range(rows):
        for j in range(cols):
            offset_x = 0
            offset_y = int(16.0 * math.sin(2 * 3.14 * j / 150))
            if i + offset_y < rows:
                img_output[i, j] = bet[(i + offset_y) % rows, j]
            else:
                img_output[i, j] = 0
    cv.imshow('Horizontal wave', img_output)
    cv.waitKey(0)


def both_waves():
    img_output = np.zeros(bet.shape, dtype=bet.dtype)

    for i in range(rows):
        for j in range(cols):
            offset_x = int(20.0 * math.sin(2 * 3.14 * i / 150))
            offset_y = int(20.0 * math.cos(2 * 3.14 * j / 150))
            if i + offset_y < rows and j + offset_x < cols:
                img_output[i, j] = bet[(i + offset_y) % rows, (j + offset_x) % cols]
            else:
                img_output[i, j] = 0
    cv.imshow('Multidirectional wave', img_output)
    cv.waitKey(0)


if __name__ == '__main__':
    main()
