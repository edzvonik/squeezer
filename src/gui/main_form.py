import tkinter as tk
import tkinter.font as tkFont
from tkinterdnd2 import DND_FILES, TkinterDnD

class Main:
    def __init__(self):
        self.root = TkinterDnD.Tk()

        #setting title
        self.root.title("Squeezer")
        #setting window size
        width=460
        height=350
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        self.button=tk.Button(self.root)
        self.button["bg"] = "#e9e9ed"
        ft = tkFont.Font(family="Monospace",size=16)
        self.button["font"] = ft
        self.button["fg"] = "#000000"
        self.button["justify"] = "center"
        self.button["text"] = "Сжать"
        self.button.place(x=10,y=270,width=440,height=65)

        self.listbox=tk.Listbox(self.root)
        self.listbox["borderwidth"] = "1px"
        ft = tkFont.Font(family="Monospace", size=5)
        self.listbox["font"] = ft
        self.listbox["fg"] = "#333333"
        self.listbox["justify"] = "left"
        self.listbox.place(x=10,y=10,width=440,height=249)
        self.listbox.insert(1, "Перенесите сюда файлы для сжатия")
        self.listbox.drop_target_register(DND_FILES)
        self.listbox.dnd_bind("<<Drop>>", self.add_paths)
        # self.listbox.pack(pady = 5)

        self.root.mainloop()

    def button_click(self):
        pass

    def add_paths(self, event):
        paths = event.data.split(" ")
        for path in paths:
            self.listbox.insert("end", path)

    # if __name__ == "__main__":
    #     root = tk.Tk()
    #     app = App(root)
    #     root.mainloop()

    # def __init__(self):
    #     self.__main = TkinterDnD.Tk()
    #     self.__main.minsize(450, 300)

    #     self.__listbox = tk.Listbox(__main)
    #     self.__listbox.insert(1, "Перенесите файлы для сжатия")

    #     self.__listbox.drop_target_register(DND_FILES)
    #     self.__listbox.dnd_bind("<<Drop>>", lambda e : __listbox.insert(tk.END, e.data))
    #     self.__listbox.pack(pady = 5)

    #     self.__main.mainloop()