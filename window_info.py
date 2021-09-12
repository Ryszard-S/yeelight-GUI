from tkinter import *
from tkinter import ttk


class WindowInfo(Toplevel):
    def __init__(self, bulbList, parent):
        super().__init__(parent, bg='#D4AC3D')
        DEFAULT_PROPS = ["power", "bright", "ct", "rgb", "hue", "sat", "color_mode", "flowing", "delayoff", "music_on",
                         "name", "active_mode", 'current_brightness']

        tree = ttk.Treeview(self, column=[i for i in range(len(DEFAULT_PROPS))], show='headings')
        # Dodaje zerowa kolumnę wymaganą przez tkinter
        tree.column(f"#0", anchor=CENTER, width=0)
        tree.heading(f"#0", text=f"")
        # nagłówki kolumn
        for i, j in enumerate(DEFAULT_PROPS):
            tree.column(f"#{i + 1}", anchor=CENTER, width=80)
            tree.heading(f"#{i + 1}", text=f"{j}")

        tree.grid(row=0, column=0, sticky='ns')

        # add a scrollbar
        scrollbar_vertical = ttk.Scrollbar(self, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar_vertical.set)
        scrollbar_vertical.grid(row=0, column=1, sticky='ns')

        # Dodawanie wierszy
        for i in bulbList:
            lista = list(i.get_properties(DEFAULT_PROPS).values())
            tree.insert("", END, values=lista)


if __name__ == '__main__':
    import refresh

    root = Tk()
    bulbs = refresh.bulb_list()
    WindowInfo(bulbs, root)
    root.mainloop()
