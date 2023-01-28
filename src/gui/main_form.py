import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD

class Main:

    

    def __init__(self):
        self.__main = TkinterDnD.Tk()
        self.__main.minsize(450, 300)

        self.__listbox = tk.Listbox(__main)
        self.__listbox.insert(1, "Перенесите файлы для сжатия")

        self.__listbox.drop_target_register(DND_FILES)
        self.__listbox.dnd_bind("<<Drop>>", lambda e : __listbox.insert(tk.END, e.data))
        self.__listbox.pack(pady = 5)

        self.__main.mainloop()