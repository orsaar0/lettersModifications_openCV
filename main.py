import tkinter as tk
from tkinter_custom_button import TkinterCustomButton
from Logic_of_action import Actions


def main():
    global action
    action = Actions('Alef_bet_images/Alef.jpg')

    root = tk.Tk()
    root.geometry("900x600")

    backgrounding = tk.PhotoImage(file="beautiful_Gui/image.png")
    label = tk.Label(root, image=backgrounding)
    label.place(x=0, y=0)

    options = {
        "Alef": "Alef_bet_images/Alef.jpg", "Bet": "Alef_bet_images/Bet.jpg", "Gimel": "Alef_bet_images/Gimel.jpg",
        "Daled": "Alef_bet_images/Daled.jpg", "Hey": "Alef_bet_images/Hey.jpg"
        , "Vav": "Alef_bet_images/Vav.jpg", "Zain": "Alef_bet_images/Zain.jpg", "Het": "Alef_bet_images/Het.jpg",
        "Tet": "Alef_bet_images/Tet.jpg"
        , "Yud": "Alef_bet_images/Yud.jpg", "Kaf": "Alef_bet_images/Kaf.jpg", "Lamed": "Alef_bet_images/Lamed.jpg"
        , "Mem": "Alef_bet_images/Mem.jpg", "Nun": "Alef_bet_images/Nun.jpg",
        "Sameh": "Alef_bet_images/Sameh.jpg", "Haayin": "Alef_bet_images/Haayin.jpg", "Pey": "Alef_bet_images/Pey.jpg"
        , "Tzadik": "Alef_bet_images/Tzadik.jpg", "Kuf": "Alef_bet_images/Kuf.jpg",
        "Reish": "Alef_bet_images/Reish.jpg",
        "Shin": "Alef_bet_images/Shin.jpg", "Taf": "Alef_bet_images/Taf.jpg"}

    clicked = tk.StringVar(root)
    clicked.set("Click To Pick")
    letter_menu = tk.OptionMenu(root, clicked, *options.keys())
    letter_menu.config(bg="GRAY", fg="WHITE", width=30, height=2)
    letter_menu["menu"].config(bg="WHITE")
    letter_menu.place(x=350, y=150)

    def check_picked_letter(*args):
        global action
        for i, j in options.items():
            if i == clicked.get():
                action.url_setter(j)
                # img_path_entry = j
                break

    clicked.trace('w', check_picked_letter)
    # img_path_entry = tk.Entry()
    # img_path_entry.focus_set()

    b_mirror_button = TkinterCustomButton(text="Mirror", corner_radius=0, command=action.mirroring)
    b_tilt_button = TkinterCustomButton(text="Tilt", corner_radius=0, command=action.tilt)
    # b_round_button = TkinterCustomButton(text="Round", corner_radius=0, command=click)
    # b_stretch_button = TkinterCustomButton(text="Stretch", corner_radius=0, command=click)
    b_blurring_button = TkinterCustomButton(text="Blur", corner_radius=0, command=action.blurring)
    b_waves_button = TkinterCustomButton(text="Waves", corner_radius=0, command=action.waves)
    b_rotate_button = TkinterCustomButton(text="Rotate", corner_radius=0, command=action.rotate)
    b_erosion_button = TkinterCustomButton(text="Erosion", corner_radius=0, command=action.erosion)
    b_dilation_button = TkinterCustomButton(text="Dilation", corner_radius=0, command=action.dilation)

    b_mirror_button.place(x=100, y=300)
    b_tilt_button.place(x=250, y=400)
    # b_round_button.place(x=300, y=300)
    # b_stretch_button.place(x=400, y=400)
    b_blurring_button.place(x=400, y=300)
    b_waves_button.place(x=550, y=400)
    b_rotate_button.place(x=700, y=300)
    b_erosion_button.place(x=300, y=500)
    b_dilation_button.place(x=500, y=500)

    root.mainloop()


def click():
    print("This Button Still in Progress")


if __name__ == '__main__':
    main()
