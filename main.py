import tkinter as tk
import cv2.cv2 as cv
from tkinter_custom_button import TkinterCustomButton
import numpy as np
import math
import os


# import Logic_of_action


# https://www.youtube.com/watch?v=YXPyB4XeYLA&ab_channel=freeCodeCamp.org


def main():
    global root, img_path_entry, img, rows, cols

    root = tk.Tk()

    main_label = tk.Label(root, text="Letters in Style", font=('Ariel', 50))
    main_label.place(x=0, y=0)
    root.geometry("900x600")
    # logic for backGround
    backGroundimg = tk.PhotoImage(file="beautiful_Gui/image.png")

    label = tk.Label(root, image=backGroundimg)
    label.place(x=0, y=0)

    options = {
        "Alef": "Alef_bet_images/Alef.jpg", "Bet": "Alef_bet_images/Bet.jpg", "Gimel": "Alef_bet_images/Gimel.jpg",
        "Daled": "Alef_bet_images/Daled.jpg", "Hey": "Alef_bet_images/Hey.jpg"
        , "Vav": "Alef_bet_images/Vav.jpg", "Zain": "Alef_bet_images/Zain.jpg", "Het": "Alef_bet_images/Het.jpg",
        "Tet": "Alef_bet_images/Tet.jpg"
        , "Yud": "Alef_bet_images/Yud.jpg", "Kaf": "Alef_bet_images/Kaf.jpg", "Lamed": "Alef_bet_images/Lamed.jpg"
        , "Mem": "Alef_bet_images/Mem.jpg", "Nun": "Alef_bet_images/Nun.jpg",
        "Sameh": "Alef_bet_images/Sameh.jpg", "Haayin": "Alef_bet_images/Haayin.jpg", "Pey": "Alef_bet_images/Pey.jpg"
        , "Tzadik": "Alef_bet_images/Tzadik.jpg", "Kuf": "Alef_bet_images/Kuf.jpg", "Reish": "Alef_bet_images/Reish.jpg",
        "Shin": "Alef_bet_images/Shin.jpg", "Taf": "Alef_bet_images/Taf.jpg"}

    #letter_optins_label = tk.Label(root, text="pick a letter")  # ,background ="blue")
    #letter_optins_label.place(x=0, y=70)
    clicked = tk.StringVar(root)
    clicked.set("Click To Pick")
    letter_menu = tk.OptionMenu(root, clicked, *options.keys())
    letter_menu.place(x=0, y=100)

    def check_picked_letter(*args):
        global img_path_entry
        for i, j in options.items():
            if i == clicked.get():
                img_path_entry = j
                print(j)

    clicked.trace('w', check_picked_letter)

    # img_path_label
    img_path_entry = tk.Entry()
    img_path_entry.focus_set()
    #img_path_entry.place(x=120, y=145, width=600, height=20)
    input_path_label = tk.Label(root, text="Enter image path:", font=('Ariel', 10))
    #input_path_label.place(x=0, y=140)

    b_mirror_button = TkinterCustomButton(text="Mirror", corner_radius=0, command=mirroring)
    b_tilt_button = TkinterCustomButton(text="Tilt", corner_radius=0, command=click)
    b_round_button = TkinterCustomButton(text="Round", corner_radius=0, command=click)
    b_stretch_button = TkinterCustomButton(text="Stretch", corner_radius=0, command=click)
    b_blurring_button = TkinterCustomButton(text="Blur", corner_radius=0, command=click)
    b_waves_button = TkinterCustomButton(text="Waves", corner_radius=0, command=waves)
    b_rotate_button = TkinterCustomButton(text="Rotate", corner_radius=0, command=rotate)
    b_erosion_button = TkinterCustomButton(text="Erosion", corner_radius=0, command=click)
    b_dilation_button = TkinterCustomButton(text="Dilation", corner_radius=0, command=click)

    # return_home = TkinterCustomButton(text="Home", corner_radius=10, command=click)

    b_mirror_button.place(x=100, y=300)
    b_tilt_button.place(x=200, y=400)
    b_round_button.place(x=300, y=300)
    b_stretch_button.place(x=400, y=400)
    b_blurring_button.place(x=500, y=300)
    b_waves_button.place(x=600, y=400)
    b_rotate_button.place(x=700, y=300)
    b_erosion_button.place(x=300, y=500)
    b_dilation_button.place(x=500, y=500)
    # while True:
    #     if img_path_entry.get() != '':
    print(img_path_entry.get())
    #         img = cv.imread(img_path_entry.get())
    #         cv.imshow("letter",img)
    #         cv.waitKey(0)
    #         rows, cols, _ = img.shape
    #         break
    root.mainloop()


def load_img():
    textImg = cv.imread(img_path_entry.get())


def click():
    print(img_path_entry.get())
    # img = cv.imread(img_path_entry.get())
    # cv.imshow("letter", img)
    # cv.waitKey(0)


def resize():
    img = cv.imread(img_path_entry.get())
    resized = cv.resize(img, (500, 500))
    cv.imshow('RESIZED', resized)
    cv.waitKey(0)


def rotate():
    img = cv.imread(img_path_entry.get())
    rotate_degrees = input("rotate degrees optins are:(1-360) ")
    height, width = img.shape[:2]
    rotation_matrix = cv.getRotationMatrix2D((width / 2, height / 2), int(rotate_degrees) % 360, 1)
    rotated_image = cv.warpAffine(img, rotation_matrix, (width, height))
    cv.imshow('rotated', rotated_image)
    cv.waitKey(0)


def rounding():
    pass


def fat_word():
    textImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    _, thres = cv.threshold(textImg, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
    contours, hierarchy = cv.findContours(thres, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cv.imshow('shintzel', img)
    for cnt in contours:
        cv.drawContours(img, [cnt], 0, 0, round(4))
    cv.imshow('kuf', img)
    cv.waitKey(0)


def erosion():
    img = cv.imread(img_path_entry.get())
    kernel = np.ones((5, 5), np.uint8)
    img_erosion = cv.erode(img, kernel, iterations=1)
    cv.imshow('Erosion', img_erosion)
    cv.waitKey(0)


def dilation():
    img = cv.imread(img_path_entry.get())
    kernel = np.ones((5, 5), np.uint8)
    img_dilation = cv.dilate(img, kernel, iterations=1)
    cv.imshow('Dilation', img_dilation)
    cv.waitKey(0)


def waves():
    img = cv.imread(img_path_entry.get())
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
    img = cv.imread(img_path_entry)
    #img = cv.imread(img_path_entry.get())
    while True:
        pick_flip = input(
            "pick flip: \n 0\tflip horizontally\n 1\tflip vertically\n 2\tflip horizontally and vertically\n")
        if pick_flip == '0':
            imgX = np.flip(img, axis=1)
            imgX = img[:, ::-1, :]
            cv.imshow('imgX', imgX)
            cv.waitKey(0)
            break
        # Mirror in y direction (flip vertically)
        elif pick_flip == '1':
            imgY = np.flip(img, axis=0)
            imgY = img[::-1, :, :]
            cv.imshow('imgY', imgY)
            cv.waitKey(0)
            break
        # Mirror in both directions (flip horizontally and vertically)
        elif pick_flip == '2':
            imgXY = np.flip(img, axis=(0, 1))
            imgXY = img[::-1, ::-1, :]
            cv.imshow('imgXY', imgXY)
            cv.waitKey(0)
            break
        else:
            print("smart guy? try again")


def blurring():
    img = cv.imread(img_path_entry.get())
    while True:
        how_much_blur = input("0\t tiny blur\n1\t little blur\n2\t medium blur\n3\t big blur\n4\t mega blur\n ")
        if how_much_blur == '0':
            blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
            cv.imshow('Blur letter', blur)
            cv.waitKey(0)
            break
        elif how_much_blur == '1':
            blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
            cv.imshow('Blur letter', blur)
            cv.waitKey(0)
            break
        elif how_much_blur == '2':
            blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
            cv.imshow('Blur letter', blur)
            cv.waitKey(0)
            break
        elif how_much_blur == '3':
            blur = cv.GaussianBlur(img, (11, 11), cv.BORDER_DEFAULT)
            cv.imshow('Blur letter', blur)
            cv.waitKey(0)
            break
        elif how_much_blur == '4':
            blur = cv.GaussianBlur(img, (15, 15), cv.BORDER_DEFAULT)
            cv.imshow('Blur letter', blur)
            cv.waitKey(0)
            break
        else:
            print("smart guy ha?")


def vertical_wave():
    img = cv.imread(img_path_entry.get())
    img_output = np.zeros(img.shape, dtype=img.dtype)

    for i in range(rows):
        for j in range(cols):
            offset_x = int(25.0 * math.sin(2 * 3.14 * i / 180))
            offset_y = 0
            if j + offset_x < rows:
                img_output[i, j] = img[i, (j + offset_x) % img]
            else:
                img_output[i, j] = 0
    cv.imshow('Vertical wave', img_output)
    cv.waitKey(0)


def horizontal_wave():
    img_output = np.zeros(img.shape, dtype=img.dtype)

    for i in range(rows):
        for j in range(cols):
            offset_x = 0
            offset_y = int(16.0 * math.sin(2 * 3.14 * j / 150))
            if i + offset_y < rows:
                img_output[i, j] = img[(i + offset_y) % rows, j]
            else:
                img_output[i, j] = 0
    cv.imshow('Horizontal wave', img_output)
    cv.waitKey(0)


def both_waves():
    img_output = np.zeros(img.shape, dtype=img.dtype)

    for i in range(rows):
        for j in range(cols):
            offset_x = int(20.0 * math.sin(2 * 3.14 * i / 150))
            offset_y = int(20.0 * math.cos(2 * 3.14 * j / 150))
            if i + offset_y < rows and j + offset_x < cols:
                img_output[i, j] = img[(i + offset_y) % rows, (j + offset_x) % cols]
            else:
                img_output[i, j] = 0
    cv.imshow('Multidirectional wave', img_output)
    cv.waitKey(0)


if __name__ == '__main__':
    main()
