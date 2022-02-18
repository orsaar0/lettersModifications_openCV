import tkinter as tk
import cv2.cv2 as cv
from tkinter_custom_button import TkinterCustomButton
import numpy as np
import os


# https://www.youtube.com/watch?v=YXPyB4XeYLA&ab_channel=freeCodeCamp.org
def main():
    # bet = cv.imread('bet.jpg')
    # cv.imshow('bet', bet)
    root = tk.Tk()
    main_label = tk.Label(root, text="Letters in Style", font=('Ariel', 50))
    main_label.place(x=0, y=0)  # .grid(row=0, column=6)
    root.geometry("900x600")
    # logic for backGround
    backGroundimg = tk.PhotoImage(file="beautiful_Gui/option2.png")
    label = tk.Label(root, image=backGroundimg)
    label.place(x=0,y=0)
    # backGroundimgLabel =tk.Label()
    # backGroundimg.
    global img_path_entry
    img_path_entry = tk.Entry()
    img_path_entry.focus_set()
    img_path_entry.place(x=120, y=145, width=600, height=20)
    input_path_label = tk.Label(root, text="Enter image path:", font=('Ariel', 10))
    input_path_label.place(x=0, y=140)

    print(img_path_entry.get())

    mirror_button = tk.Button(root, text="Mirror", padx=30, pady=30, command="Need to put logic of mirror", fg="blue",
                              bg="white")
    tilt_button = tk.Button(root, text="Tilt", padx=30, pady=30, command="Need to put logic")
    round_button = tk.Button(root, text="Round", padx=30, pady=30, command="Need to put logic")
    stretch_button = tk.Button(root, text="Stretch", padx=30, pady=30, command=click)

    check_button = TkinterCustomButton(text="My Button Cool", corner_radius=10, command=click)
    check_button.place(relx=0.5, rely=0.5)
    mirror_button.place(x=100, y=300)  # .grid(row=5, column=0)
    tilt_button.place(x=100, y=400)  # .grid(row=5, column=3)
    round_button.place(x=300, y=400)  # .grid(row=5, column=9)
    stretch_button.place(x=400, y=400)  # .grid(row=5, column=12)

    root.mainloop()


def load_img():
    textImg = cv.imread(img_path_entry.get())


def click():
    print(img_path_entry.get())


# def build buttons():
# def display_buttons():

if __name__ == '__main__':
    main()
