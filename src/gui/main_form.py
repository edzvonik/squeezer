import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD

class Main:
    def __init__(self):
        main = TkinterDnD.Tk()
        main.minsize(450, 300)

        listbox = tk.Listbox(main)
        listbox.insert(1, "Перенесите файлы для сжатия")

        listbox.drop_target_register(DND_FILES)
        listbox.dnd_bind("<<Drop>>", lambda e : listbox.insert(tk.END, e.data))
        listbox.pack(pady = 5)

        main.mainloop()