import tkinter.ttk as ttk
from tkinter import *
from tkinter import font

from refresh import *

gray = '#383838'
yellow = '#D4AC3D'

bulbList = []


class enterName(Toplevel):
    def __init__(self, bulbList, parent):
        # super().__init__(parent)
        self.bulbName = bulb_names(bulbList)

        font_consolas = font.Font(family='Consolas', size=11)

        # TODO make me pretty
        self.new_window = Toplevel(parent, bg=gray)

        self.new_window.title("Change bulb's name")
        self.new_window.geometry("300x200")

        self.img_Approve = PhotoImage(file="icons/2714_20.png")
        self.img_Cancel = PhotoImage(file="icons/274C_20.png")

        self.frame = Frame(self.new_window, bg=gray)
        self.frame.pack(pady=10)

        self.frame1 = Frame(self.new_window, bg=gray)
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

    # def refresh_names():
    #     global bulbList
    #     bulbList = bulb_list()
    #     bulbName = bulb_names(bulbList)

    def _ok(self):
        bulb_num = self.chooser.current()
        new_name = self.entry.get()
        bulbList[bulb_num].set_name(new_name)

        # zmiana nazwy na liście bulbName:

        self.bulbName.pop(bulb_num)
        self.bulbName.insert(bulb_num, new_name)

        # ustawianie na combobox nowych nazw
        self.chooser['values'] = self.bulbName


    def _cancel(self):
        self.new_window.destroy()

    # def new_window(self):
    #     # TODO make me pretty
    #     new_window = Toplevel(bg=gray)
    #
    #     new_window.title("Change bulb's name")
    #     new_window.geometry("300x200")
    #
    #     img_Approve = PhotoImage(file="icons/2714.png")
    #     img_Cancel = PhotoImage(file="icons/274C.png")
    #
    #
    #     frame = Frame(new_window, bg=gray)
    #     frame.pack(pady=10)
    #
    #     frame1 = Frame(new_window, bg=yellow)
    #     frame1.pack(side=BOTTOM, pady=10)
    #
    #     lbl1 = Label(frame, text='Enter new name: ')
    #     lbl1.pack()
    #
    #     entry = Entry(frame)
    #     entry.pack()
    #
    #     lbl2 = Label(frame , text='Choose bulb: ')
    #     lbl2.pack()
    #
    #     chooser = tkk.Combobox(frame)
    #     chooser.pack()
    #     chooser['values'] = self.bulbName
    #
    #
    #     bttn_ok = Button(frame1,  text="change", command=self._ok, image=img_Approve, compound=RIGHT, bg=yellow, fg=gray)
    #     bttn_ok.pack(side=LEFT)
    #
    #     bttn_cancel = Button(frame1, text="cancel", command=self._cancel, image=img_Cancel, compound=RIGHT, bg=yellow, fg=gray)
    #     bttn_cancel.pack(side=LEFT)


if __name__ == '__main__':
    from tkinter import *

    win = Tk()
    enterName([], win)
    win.mainloop()
