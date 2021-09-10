import tkinter.ttk as ttk
from tkinter import *
from tkinter import font

import refresh
from refresh import *

gray = '#383838'
yellow = '#D4AC3D'


class enterName(Toplevel):
    def __init__(self, bulbList, parent):
        super().__init__(parent, bg=gray)
        self.bulbList = bulbList
        self.bulbName = bulb_names(bulbList)

        font_consolas = font.Font(family='Consolas', size=11)

        self.title("Change bulb's name")
        self.geometry("300x200")

        self.img_Approve = PhotoImage(file="icons/2714_20.png")
        self.img_Cancel = PhotoImage(file="icons/274C_20.png")

        self.frame = Frame(self, bg=gray)
        self.frame.pack(pady=10)

        self.frame1 = Frame(self, bg=gray)
        self.frame1.pack(side=BOTTOM, pady=10)

        self.lbl1 = Label(self.frame, text='Enter new name: ', bg=gray, fg=yellow, font=font_consolas)
        self.lbl1.pack()

        self.entry = Entry(self.frame, width=30)
        self.entry.pack(pady=3)

        self.lbl2 = Label(self.frame, text='Choose bulb: ', bg=gray, fg=yellow, font=font_consolas)
        self.lbl2.pack()

        self.chooser = ttk.Combobox(self.frame, width=27)
        self.chooser.pack(pady=3)
        self.chooser['values'] = self.bulbName

        self.bttn_ok = Button(self.frame1, text="change", command=self._ok, image=self.img_Approve, compound=RIGHT,
                              bg=yellow, fg=gray)
        self.bttn_ok.pack(side=LEFT)

        self.bttn_cancel = Button(self.frame1, text="cancel", command=self._cancel, image=self.img_Cancel,
                                  compound=RIGHT, bg=yellow, fg=gray)
        self.bttn_cancel.pack(side=LEFT)


    def _ok(self):
        self.bulb_num = self.chooser.current()
        self.new_name = self.entry.get()
        self.bulbList[self.bulb_num].set_name(self.new_name)

        # zmiana nazwy na liście bulbName:

        self.bulbName.pop(self.bulb_num)
        self.bulbName.insert(self.bulb_num, self.new_name)

        # ustawianie na combobox nowych nazw
        self.chooser['values'] = self.bulbName


    def _cancel(self):
        refresh.bulb_list()
        self.destroy()


if __name__ == '__main__':
    win = Tk()
    enterName([], win)
    win.mainloop()
