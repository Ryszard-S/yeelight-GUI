from yeelight import *
import time
from tkinter import *
from tkinter import colorchooser


gray='#383838'
yellow ='#D4AC3D'

def light_bulb(bulb_name):
    if bulb_name == bulb0_name:
        return bulb0
    if bulb_name == bulb1_name:
        return bulb1
    if bulb_name == bulb2_name:
        return bulb2
    if bulb_name == bulb3_name:
        return bulb3
    if bulb_name == bulb4_name:
        return bulb4


def fcn_turn_on():
    x=light_bulb(listbox.get(listbox.curselection()))
    x.turn_on()

def fcn_turn_off():
    x=light_bulb(listbox.get(listbox.curselection()))
    x.turn_off()


def setColorTemp():
    x=light_bulb(listbox.get(listbox.curselection()))
    x.set_color_temp(scale_ColorTemp.get())

def Color_choose():
    color=colorchooser.askcolor()
    col1=color[0]
    R=col1[0]
    G=col1[1]
    B=col1[2]
    x=light_bulb(listbox.get(listbox.curselection()))
    x.set_rgb(R,G,B)

def set_Brightness():
    brightness=scale_Brightness.get()
    x=light_bulb(listbox.get(listbox.curselection()))
    x.set_brightness(brightness)
    if brightness >=50 and brightness <=100:
        bttn_Brightess.config(image=img_BrightnessMax)
    else:
        bttn_Brightess.config(image=img_BrightnessMin)

def refresh():
    global bulb0_name
    global bulb1_name
    global bulb2_name
    global bulb3_name
    global bulb4_name
    listbox.delete(0, END)
    discover_bulbss  = discover_bulbs(3)
    if len(discover_bulbss)==0:
        listbox.insert(1,"0 LIGHTS! DETECTED")

    if len(discover_bulbss)==1:
        bulb0 = Bulb(discover_bulbss[0].get('ip'))
        bulb0_name = (discover_bulbss[0].get('capabilities')).get('name')
        listbox.insert(1,bulb0_name)

    if len(discover_bulbss)==2:
        bulb0=Bulb(discover_bulbss[0].get('ip'))
        bulb0_name=(discover_bulbss[0].get('capabilities')).get('name')
        bulb1=Bulb(discover_bulbss[1].get('ip'))
        bulb1_name=(discover_bulbss[1].get('capabilities')).get('name')
        listbox.insert(1,bulb0_name)
        listbox.insert(2,bulb1_name)

    if len(discover_bulbs)==3:
        bulb0=Bulb(discover_bulbs[0].get('ip'))
        bulb0_name=(discover_bulbs[0].get('capabilities')).get('name')
        bulb1=Bulb(discover_bulbs[1].get('ip'))
        bulb1_name=(discover_bulbs[1].get('capabilities')).get('name')
        bulb2=Bulb(discover_bulbs[2].get('ip'))
        bulb2_name=(discover_bulbs[2].get('capabilities')).get('name')
        listbox.insert(1,bulb0_name)
        listbox.insert(2,bulb1_name)
        listbox.insert(3,bulb2_name)

    if len(discover_bulbs)==4:
        bulb0=Bulb(discover_bulbs[0].get('ip'))
        bulb0_name=(discover_bulbs[0].get('capabilities')).get('name')
        bulb1=Bulb(discover_bulbs[1].get('ip'))
        bulb1_name=(discover_bulbs[1].get('capabilities')).get('name')
        bulb2=Bulb(discover_bulbs[2].get('ip'))
        bulb2_name=(discover_bulbs[2].get('capabilities')).get('name')
        bulb3=Bulb(discover_bulbs[3].get('ip'))
        bulb3_name=(discover_bulbs[3].get('capabilities')).get('name')
        listbox.insert(1,bulb0_name)
        listbox.insert(2,bulb1_name)
        listbox.insert(3,bulb2_name)
        listbox.insert(4,bulb3_name)

    if len(discover_bulbs)==5:
        bulb0=Bulb(discover_bulbs[0].get('ip'))
        bulb0_name=(discover_bulbs[0].get('capabilities')).get('name')
        bulb1=Bulb(discover_bulbs[1].get('ip'))
        bulb1_name=(discover_bulbs[1].get('capabilities')).get('name')
        bulb2=Bulb(discover_bulbs[2].get('ip'))
        bulb2_name=(discover_bulbs[2].get('capabilities')).get('name')
        bulb3=Bulb(discover_bulbs[3].get('ip'))
        bulb3_name=(discover_bulbs[3].get('capabilities')).get('name')
        bulb4=Bulb(discover_bulbs[4].get('ip'))
        bulb4_name=(discover_bulbs[4].get('capabilities')).get('name')
        listbox.insert(1,bulb0_name)
        listbox.insert(2,bulb1_name)
        listbox.insert(3,bulb2_name)
        listbox.insert(4,bulb1_name)
        listbox.insert(5,bulb2_name)


win = Tk()
win.title("Yeelight switch")

frame =Frame(bg=gray)
frame.pack(pady=10)

brightnessFrame = Frame(bg=gray)
brightnessFrame.pack(side=BOTTOM, pady=10)

colorTempFrame= Frame(bg=gray)
colorTempFrame.pack(side=BOTTOM)



img_TurnOn = PhotoImage(file="1F4A1_2.png")
img_TurnOff = PhotoImage(file="1F4A1.png")
img_Color=PhotoImage(file="1F308.png")
img_BrightnessMax=PhotoImage(file="1F506.png")
img_BrightnessMin=PhotoImage(file="1F505.png")
img_ColorTemp=PhotoImage(file="1F321.png")
img_Refresh=PhotoImage(file="1F504.png")




bttn_TurnOn = Button(frame, text="Turn On", command=fcn_turn_on,image=img_TurnOn,compound=BOTTOM,bg=yellow,fg=gray)
bttn_TurnOn.pack(side=LEFT)

bttn_TurnOnOff = Button(frame, text="Turn Off", command=fcn_turn_off,image=img_TurnOff,compound=BOTTOM,bg=yellow,fg=gray)
bttn_TurnOnOff.pack(side=LEFT)

bttn_Color = Button(frame, text="Choose Color", command=Color_choose,image=img_Color,compound=BOTTOM,bg=yellow,fg=gray)
bttn_Color.pack(side=LEFT)

bttn_Refresh = Button(frame, text="Refresh", command=refresh,image=img_Refresh,compound=BOTTOM,bg=yellow,fg=gray)
bttn_Refresh.pack(side=LEFT)

bttn_ColorTemp = Button(colorTempFrame, text="Applay Color\nTemperature", command=setColorTemp,image=img_ColorTemp,compound=BOTTOM,width=100,bg=yellow,fg=gray)
bttn_ColorTemp.pack(side=LEFT)



bttn_Brightess = Button(brightnessFrame, text="Set Brightness", command=set_Brightness,image=img_BrightnessMin,compound=BOTTOM,width=100,bg=yellow,fg=gray)
bttn_Brightess.pack(side=LEFT)

listbox = Listbox(frame,bg=gray,fg=yellow,font=('Times New Roman',22))
listbox.pack(side=LEFT)
listbox.config(height=listbox.size())

scale_ColorTemp=Scale(colorTempFrame,from_=2700,to=6500,font=('Consolas',12),resolution=100,orient=HORIZONTAL,label="Color Temperature",length=500,bg=yellow,fg=gray)
scale_ColorTemp.pack(side=LEFT)

scale_Brightness=Scale(brightnessFrame,from_=1,to=100,font=('Consolas',12),orient=HORIZONTAL,label="Brightness",length=500,bg=yellow,fg=gray)
scale_Brightness.pack(side=LEFT)

refresh()








win.iconphoto(True, img_TurnOn)
win.config(background=gray)

win.mainloop()
