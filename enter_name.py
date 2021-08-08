import tkinter.ttk as tkk
from tkinter import *

from refresh import *

gray = '#383838'
yellow = '#D4AC3D'


def enterName(bulbList):
    bulbName = bulb_names(bulbList)

    def refresh_names():
        global bulbList
        bulbList = bulb_list()
        bulbName = bulb_names(bulbList)

    def ok():
        bulb_num = chooser.current()
        new_name = entry.get()
        bulbList[bulb_num].set_name(new_name)

        # zmiana nazwy na liście bulbName:

        bulbName.pop(bulb_num)
        bulbName.insert(bulb_num, new_name)

        # ustawianie na combobox nowych nazw
        chooser['values'] = bulbName

    def cancel():
        new_window.destroy()

    # TODO make me pretty
    new_window = Toplevel(bg=gray)

    new_window.title("Change bulb's name")
    new_window.geometry("300x200")

    frame = Frame(new_window, bg=gray)
    frame.pack(pady=10)

    frame1 = Frame(new_window, bg=yellow)
    frame1.pack(side=BOTTOM, pady=10)

    lbl1 = Label(frame, text='Enter new name: ')
    lbl1.pack()

    entry = Entry(frame)
    entry.pack()

    lbl2 = Label(frame, text='Choose bulb: ')
    lbl2.pack()

    chooser = tkk.Combobox(frame)
    chooser.pack()
    chooser['values'] = bulbName


    bttn_ok = Button(frame1, text="change", command=ok)
    bttn_ok.pack(side=LEFT)

    bttn_cancel = Button(frame1, text="cancel", command=cancel)
    bttn_cancel.pack(side=LEFT)

