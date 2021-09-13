import tkinter.ttk as ttk
from tkinter import *
from tkinter import font
from refresh import bulb_names

gray = '#383838'
yellow = '#D4AC3D'


class enterName(Toplevel):
    def __init__(self, bulbList, parent):
        super().__init__(parent, bg=gray)
        self.bulbName = bulb_names(bulbList)
        self.bulbList = bulbList

        font_consolas = font.Font(family='Consolas', size=11)

        self.title("Change bulb's name")
        self.geometry("300x200")

        img_Approve = PhotoImage(file="icons/2714_20.png")
        img_Cancel = PhotoImage(file="icons/274C_20.png")

        frame = Frame(self, bg=gray)
        frame.pack(pady=10)

        frame1 = Frame(self, bg=gray)
        frame1.pack(side=BOTTOM, pady=10)

        lbl1 = Label(frame, text='Enter new name: ', bg=gray, fg=yellow, font=font_consolas)
        lbl1.pack()

        self.entry = Entry(frame, width=30)
        self.entry.pack(pady=3)

        lbl2 = Label(frame, text='Choose bulb: ', bg=gray, fg=yellow, font=font_consolas)
        lbl2.pack()

        self.chooser = ttk.Combobox(frame, width=27)
        self.chooser.pack(pady=3)
        self.chooser['values'] = self.bulbName

        bttn_ok = Button(frame1, text="change", command=self._ok, image=img_Approve, compound=RIGHT,
                         bg=yellow, fg=gray)
        bttn_ok.pack(side=LEFT)

        bttn_cancel = Button(frame1, text="cancel", command=self._cancel, image=img_Cancel,
                             compound=RIGHT, bg=yellow, fg=gray)
        bttn_cancel.pack(side=LEFT)

    def _ok(self):
        self.bulb_num = self.chooser.current()
        self.new_name = self.entry.get()
        self.bulbList[self.bulb_num].set_name(self.new_name)

        # rename in bulbName list :

        self.bulbName.pop(self.bulb_num)
        self.bulbName.insert(self.bulb_num, self.new_name)

        # set in combobox new name
        self.chooser['values'] = self.bulbName

    def _cancel(self):
        self.destroy()


if __name__ == '__main__':
    win = Tk()
    enterName([], win)
    win.mainloop()
