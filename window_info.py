from tkinter import *
from tkinter import ttk


class WindowInfo(Toplevel):
    def __init__(self, bulbList, parent):
        super().__init__(parent, bg='#D4AC3D')
        DEFAULT_PROPS = ["power", "bright", "ct", "rgb", "hue", "sat", "color_mode", "flowing", "delayoff", "music_on",
                         "name", "active_mode", 'current_brightness']

        tree = ttk.Treeview(self, column=[i for i in range(len(DEFAULT_PROPS))], show='headings', height=10)
        # Add the zero column required by the tkinter
        tree.column(f"#0", anchor=CENTER, width=0)
        tree.heading(f"#0", text=f"")
        # column headers
        for i, j in enumerate(DEFAULT_PROPS):
            tree.column(f"#{i + 1}", anchor=CENTER, width=80)
            tree.heading(f"#{i + 1}", text=f"{j}")

        tree.grid(row=0, column=0, sticky='ns')

        # add a scrollbar
        scrollbar_vertical = ttk.Scrollbar(self, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar_vertical.set)
        scrollbar_vertical.grid(row=0, column=1, sticky='ns')

        # adding lines
        for i in bulbList:
            list_values = list(i.get_properties(DEFAULT_PROPS).values())
            list_values[3] = self.RGB(list_values[3])
            tree.insert("", END, values=list_values)

    def RGB(self, liczba):
        x = bin(int(liczba))
        lenx = len(x)
        B = x[lenx - 8:lenx]
        G = x[lenx - 16:lenx - 8]
        R = x[:lenx - 16]
        BB = int(B, 2)
        GG = int(G, 2)
        RR = int(R, 2)
        return f"RGB=({RR}, {GG}, {BB})"


if __name__ == '__main__':
    import refresh

    root = Tk()
    bulbs = refresh.bulb_list()
    WindowInfo(bulbs, root)
    root.mainloop()
