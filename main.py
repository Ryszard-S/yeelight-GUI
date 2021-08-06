from tkinter import *
from tkinter import colorchooser, font

from refresh import *

gray = '#383838'
yellow = '#D4AC3D'


# TODO ustawianie wartości bightness i ct po wybraniu żarówki ??


# włącz wszystkie aktualnie zaznaczone światła
def fcn_turn_on():
    for b in listbox.curselection():
        bulb = bulbList[b]
        bulb.turn_on()


def fcn_turn_off():
    for b in listbox.curselection():
        bulb = bulbList[b]
        bulb.turn_off()


def set_color_temp():
    for b in listbox.curselection():
        bulb = bulbList[b]
        bulb.set_color_temp(scale_ColorTemp.get())


def set_color():
    color = colorchooser.askcolor()
    col1 = color[0]
    r = col1[0]
    g = col1[1]
    b = col1[2]
    for bulbb in listbox.curselection():
        bulb = bulbList[bulbb]
        bulb.set_rgb(r, g, b)


def set_brightness():
    brightness = scale_Brightness.get()
    for b in listbox.curselection():
        bulb = bulbList[b]
        bulb.set_brightness(brightness)

    if 50 <= brightness <= 100:
        bttn_Brightess.config(image=img_BrightnessMax)
    else:
        bttn_Brightess.config(image=img_BrightnessMin)

# TODO experimental funcition
# def change_name():
#     enter_Name.enterName()


def refresh():
    global bulbList
    bulbList = bulb_list()

    # Wstawianie nazw żarówek do listy wybieralnej
    i = 0
    listbox.delete(0, END)
    for bulb in bulb_names(bulbList):
        if bulb is not None:
            listbox.insert(END, bulb)
        else:
            listbox.insert(END, f'name{i}')
        i += 1


win = Tk()
win.title("Yeelight switch")

font_consolas_13 = font.Font(family='Consolas', size=13)
font_consolas_20 = font.Font(family='Consolas', size=20)

frame = Frame(bg=gray)
frame.pack(pady=10)

brightnessFrame = Frame(bg=gray)
brightnessFrame.pack(side=BOTTOM, pady=10)

colorTempFrame = Frame(bg=gray)
colorTempFrame.pack(side=BOTTOM)

img_TurnOn = PhotoImage(file="1F4A1_2.png")
img_TurnOff = PhotoImage(file="1F4A1.png")
img_Color = PhotoImage(file="1F308.png")
img_BrightnessMax = PhotoImage(file="1F506.png")
img_BrightnessMin = PhotoImage(file="1F505.png")
img_ColorTemp = PhotoImage(file="1F321.png")
img_Refresh = PhotoImage(file="1F504.png")

bttn_TurnOn = Button(frame, text="Turn On", command=fcn_turn_on, image=img_TurnOn, compound=BOTTOM, bg=yellow, fg=gray)

bttn_TurnOn.pack(side=LEFT)

# FIXME test this function
# bttn_changename = Button(frame, text="change name", command=change_name, image=img_TurnOn, compound=BOTTOM, bg=yellow,
#                          fg=gray, font=f)
#
# bttn_changename.pack(side=LEFT)


bttn_TurnOff = Button(frame, text="Turn Off", command=fcn_turn_off, image=img_TurnOff, compound=BOTTOM, bg=yellow,
                      fg=gray)

bttn_TurnOff.pack(side=LEFT)

bttn_Color = Button(frame, text="Choose Color", command=set_color, image=img_Color, compound=BOTTOM, bg=yellow, fg=gray)

bttn_Color.pack(side=LEFT)

bttn_Refresh = Button(frame, text="Refresh", command=refresh, image=img_Refresh, compound=BOTTOM, bg=yellow, fg=gray)

bttn_Refresh.pack(side=LEFT)

bttn_ColorTemp = Button(colorTempFrame, text="Applay Color\nTemperature", command=set_color_temp, image=img_ColorTemp,
                        compound=BOTTOM, width=100, bg=yellow, fg=gray)
bttn_ColorTemp.pack(side=LEFT)

bttn_Brightess = Button(brightnessFrame, text="Set Brightness", command=set_brightness, image=img_BrightnessMin,
                        compound=BOTTOM, width=100, bg=yellow, fg=gray)
bttn_Brightess.pack(side=LEFT)

listbox = Listbox(frame, bg=gray, fg=yellow, font=font_consolas_20, selectmode=EXTENDED)
listbox.pack(side=LEFT)
listbox.config(height=listbox.size())

scale_ColorTemp = Scale(colorTempFrame, from_=2700, to=6500, resolution=100, orient=HORIZONTAL,
                        label="Color Temperature", length=500, font=font_consolas_13, bg=yellow, fg=gray)
scale_ColorTemp.pack(side=LEFT)

scale_Brightness = Scale(brightnessFrame, from_=1, to=100, orient=HORIZONTAL, label="Brightness", length=500, bg=yellow,
                         fg=gray, font=font_consolas_13)
scale_Brightness.pack(side=LEFT)

refresh()

win.iconphoto(True, img_TurnOn)
win.config(background=gray)

win.mainloop()
