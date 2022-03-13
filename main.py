# SUBMITTED: 
# NIV DAGAN 205438203 
# OR SAAR 205476369


import tkinter as tk
from tkinter_custom_button import TkinterCustomButton
from Logic_of_action import Actions


def main():
    global action
    action = Actions('Alef_bet_images/Alef.jpg')

    root = tk.Tk()
    root.geometry("900x600")
    root.title('Letters Modifications')

    backgrounding = tk.PhotoImage(file="beautiful_Gui/image.png")
    label = tk.Label(root, image=backgrounding)
    label.place(x=0, y=0)

    options = {
        "א": "Alef_bet_images/Alef.jpg", "ב": "Alef_bet_images/Bet.jpg", "ג": "Alef_bet_images/Gimel.jpg",
        "ד": "Alef_bet_images/Daled.jpg", "ה": "Alef_bet_images/Hey.jpg"
        , "ו": "Alef_bet_images/Vav.jpg", "ז": "Alef_bet_images/Zain.jpg", "ח": "Alef_bet_images/Het.jpg",
        "ט": "Alef_bet_images/Tet.jpg"
        , "י": "Alef_bet_images/Yud.jpg", "כ": "Alef_bet_images/Kaf.jpg", "ל": "Alef_bet_images/Lamed.jpg"
        , "מ": "Alef_bet_images/Mem.jpg", "נ": "Alef_bet_images/Nun.jpg",
        "ס": "Alef_bet_images/Sameh.jpg", "ע": "Alef_bet_images/Haayin.jpg", "פ": "Alef_bet_images/Pey.jpg"
        , "צ": "Alef_bet_images/Tzadik.jpg", "ק": "Alef_bet_images/Kuf.jpg",
        "ר": "Alef_bet_images/Reish.jpg",
        "ש": "Alef_bet_images/Shin.jpg", "ת": "Alef_bet_images/Taf.jpg"}

    clicked = tk.StringVar(root)
    clicked.set("Click To Pick")
    letter_menu = tk.OptionMenu(root, clicked, *options.keys())
    letter_menu.config(bg="GRAY", fg="WHITE", width=30, height=2)
    letter_menu["menu"].config(bg="WHITE")
    letter_menu.place(x=180, y=170)

    def check_picked_letter(*args):
        global action
        for i, j in options.items():
            if i == clicked.get():
                action.url_setter(j)
                break

    clicked.trace('w', check_picked_letter)

    b_mirror_button = TkinterCustomButton(text="Mirror", corner_radius=0, command=action.mirroring)
    b_tilt_button = TkinterCustomButton(text="Tilt", corner_radius=0, command=action.tilt)
    b_blurring_button = TkinterCustomButton(text="Blur", corner_radius=0, command=action.blurring)
    b_waves_button = TkinterCustomButton(text="Waves", corner_radius=0, command=action.waves)
    b_rotate_button = TkinterCustomButton(text="Rotate", corner_radius=0, command=action.rotate)
    b_erosion_button = TkinterCustomButton(text="Erosion", corner_radius=0, command=action.erosion)
    b_dilation_button = TkinterCustomButton(text="Dilation", corner_radius=0, command=action.dilation)

    b_mirror_button.place(x=150, y=300)
    b_tilt_button.place(x=80, y=400)
    b_blurring_button.place(x=320, y=300)
    b_waves_button.place(x=240, y=400)
    b_rotate_button.place(x=400, y=400)
    b_erosion_button.place(x=150, y=500)
    b_dilation_button.place(x=320, y=500)

    root.mainloop()


def click():
    print("This Button Still in Progress")


if __name__ == '__main__':
    main()
