from tkinter import *
from tkinter import colorchooser, font, ttk

from yeelight import flows

import enter_name
import window_info
from refresh import *

gray = '#383838'
yellow = '#D4AC3D'
yellow1 = '#A8831B'




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


def change_name():
    x = enter_name.enterName(bulbList=bulbList, parent=win)
    x.wait_window()
    refresh()


def refresh():
    global bulbList
    bulbList = bulb_list()

    # Wstawianie nazw żarówek do listy wybieralnej
    listbox.delete(0, END)
    for bulb in bulb_names(bulbList):
        listbox.insert(END, bulb)


dict_mode = {'sunrise': flows.sunrise(), 'sunset': flows.sunset(), 'disco': flows.disco(), 'temp': flows.temp(),
             'strobe': flows.strobe(), 'pulse': flows.pulse(111, 222, 157), 'strobe_color': flows.strobe_color(),
             'alarm': flows.alarm(), 'police': flows.police(), 'police2': flows.police2(), 'lsd': flows.lsd(),
             'christmas': flows.christmas(), 'rgb': flows.rgb(), "random_loop": flows.random_loop(),
             'slowdown': flows.slowdown(), 'home': flows.home(), 'night_mode': flows.night_mode(),
             'date_night': flows.date_night(), 'movie': flows.movie(), 'romance': flows.romance(),
             'happy_birthday': flows.happy_birthday(), 'candle_flicker': flows.candle_flicker()}


def mode():
    mode = chooser.get()
    fcn = dict_mode.get(mode)
    for b in listbox.curselection():
        bulb = bulbList[b]
        bulb.start_flow(fcn)


def mode_stop():
    for b in listbox.curselection():
        bulb = bulbList[b]
        bulb.stop_flow()


def onselect(event):
    b = event.widget.curselection()[0]
    br = bulbList[b].get_properties().get('bright')
    ct = bulbList[b].get_properties().get('ct')
    scale_Brightness.set(br)
    scale_ColorTemp.set(ct)


def info_mode():
    window_info.WindowInfo(bulbList=bulbList, parent=win)


win = Tk()
win.title("Yeelight switch")

font_consolas_13 = font.Font(family='Consolas', size=13)
font_consolas_20 = font.Font(family='Consolas', size=20)

frame = Frame(bg=gray)
frame.pack(pady=10)

modeFrame = Frame(bg=gray)
modeFrame.pack(side=BOTTOM, pady=5)

brightnessFrame = Frame(bg=gray)
brightnessFrame.pack(side=BOTTOM, pady=10)

colorTempFrame = Frame(bg=gray)
colorTempFrame.pack(side=BOTTOM)

img_TurnOn = PhotoImage(file="icons/1F4A1_2.png")
img_TurnOff = PhotoImage(file="icons/1F4A1.png")
img_Color = PhotoImage(file="icons/1F308.png")
img_BrightnessMax = PhotoImage(file="icons/1F506.png")
img_BrightnessMin = PhotoImage(file="icons/1F505.png")
img_ColorTemp = PhotoImage(file="icons/1F321.png")
img_Refresh = PhotoImage(file="icons/1F504.png")
img_Start = PhotoImage(file="icons/25B61.png")
img_Stop = PhotoImage(file="icons/23F9.png")
img_ChangeName = PhotoImage(file='icons/E25D.png')
img_InfoMode = PhotoImage(file='icons/2139_20.png')

bttn_TurnOn = Button(frame, text="Turn On", command=fcn_turn_on, image=img_TurnOn, compound=BOTTOM, bg=yellow, fg=gray)
bttn_TurnOn.pack(side=LEFT)

bttn_TurnOff = Button(frame, text="Turn Off", command=fcn_turn_off, image=img_TurnOff, compound=BOTTOM, bg=yellow,
                      fg=gray)
bttn_TurnOff.pack(side=LEFT)

bttn_changename = Button(frame, text="Change name", command=change_name, image=img_ChangeName, compound=BOTTOM,
                         bg=yellow,
                         fg=gray)
bttn_changename.pack(side=LEFT)

bttn_Color = Button(frame, text="Choose color", command=set_color, image=img_Color, compound=BOTTOM, bg=yellow, fg=gray)
bttn_Color.pack(side=LEFT)

bttn_Refresh = Button(frame, text="Refresh", command=refresh, image=img_Refresh, compound=BOTTOM, bg=yellow, fg=gray)
bttn_Refresh.pack(side=LEFT)

bttn_ColorTemp = Button(colorTempFrame, text="Apply color\ntemperature", command=set_color_temp, image=img_ColorTemp,
                        compound=BOTTOM, width=100, bg=yellow, fg=gray)
bttn_ColorTemp.pack(side=LEFT)

bttn_Brightess = Button(brightnessFrame, text="Set brightness \n", command=set_brightness, image=img_BrightnessMin,
                        compound=BOTTOM, width=100, bg=yellow, fg=gray)
bttn_Brightess.pack(side=LEFT)

listbox = Listbox(frame, bg=gray, fg=yellow, font=font_consolas_20, selectmode=EXTENDED, height=3)
listbox.pack(side=LEFT)

scrollbar = Scrollbar(frame, orient='vertical', command=listbox.yview)
scrollbar.pack(side=LEFT, fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
listbox.bind('<<ListboxSelect>>', onselect)

scale_ColorTemp = Scale(colorTempFrame, from_=2700, to=6500, resolution=100, orient=HORIZONTAL,
                        label="Color temperature", length=500, font=font_consolas_13, bg=yellow, fg=gray, width=20)
scale_ColorTemp.pack(side=LEFT, fill=Y, pady=1)

scale_Brightness = Scale(brightnessFrame, from_=1, to=100, orient=HORIZONTAL, label='Brightness', length=500, bg=yellow,
                         fg=gray, font=font_consolas_13, width=20)
scale_Brightness.pack(side=LEFT, fill=Y, pady=1)

# Yeelight mode

label = Label(modeFrame, text='effects', font=font_consolas_20, bg=gray, fg=yellow)
label.pack(side=TOP, pady=5)

chooser = ttk.Combobox(modeFrame, font=font_consolas_13, width=10)
chooser.pack(side=LEFT)
chooser['values'] = list(dict_mode.keys())

bttn_start = Button(modeFrame, text="start", command=mode, image=img_Start, compound=RIGHT, bg=yellow1, fg=gray)
bttn_start.pack(side=LEFT)

bttn_stop = Button(modeFrame, text="stop", command=mode_stop, image=img_Stop, compound=RIGHT, bg=yellow1, fg=gray)
bttn_stop.pack(side=LEFT)

bttn_adv_mode = Button(modeFrame, text="Info", command=info_mode, image=img_InfoMode, compound=RIGHT, bg=yellow1,
                       fg=gray)
bttn_adv_mode.pack(side=RIGHT)

refresh()

win.iconphoto(True, img_TurnOn)
win.config(background=gray)

win.mainloop()
