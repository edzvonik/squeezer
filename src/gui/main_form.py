import tkinter as tk
import tkinter.font as tkFont
from tkinterdnd2 import DND_FILES, TkinterDnD

class Main:
    def __init__(self):
        
        # Root
        self.root = TkinterDnD.Tk()
        self.root.title("Squeezer")
        width=460
        height=400
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        # Buttons 
        button_font = tkFont.Font(family="Monospace",size=8)

        self.delete_button = tk.Button(
            self.root, text = "Удалить", 
            command = self.delete_button_click, 
            font = button_font
            )
        self.delete_button.place(x = 10, y = 270, width = 214, height = 41)

        self.deleteAll_button = tk.Button(
            self.root, text = "Удалить всё", 
            command = self.deleteAll_button_click, 
            font = button_font)
        self.deleteAll_button.place(x = 230, y = 270, width = 222, height = 41)

        self.button=tk.Button(
            self.root, 
            text = "Сжать!", 
            font = button_font, 
            justify = "center", 
            command = self.button_click
            )
        self.button.place(x = 10, y = 320, width = 440, height = 65)

        # ListBox
        listbox_font = tkFont.Font(family="Monospace", size=5)

        self.listbox=tk.Listbox(
            self.root, 
            selectmode = tk.MULTIPLE, 
            font = listbox_font,
            justify = "left",
            borderwidth = "1px"
            )
        self.listbox.place(x=10,y=10,width=440,height=249)
        self.listbox.insert("end", "Перенесите сюда файлы для сжатия")
        self.listbox.drop_target_register(DND_FILES)
        self.listbox.dnd_bind("<<Drop>>", self.add_paths)

        self.root.mainloop()

    def button_click(self):
        print("Click!")

    def delete_button_click(self):
        selected_checkboxs = self.listbox.curselection()
        for selected_checkbox in selected_checkboxs[::-1]:
            self.listbox.delete(selected_checkbox)

    def deleteAll_button_click(self):
        self.listbox.delete(0, "end")

    def add_paths(self, event):
        if (self.listbox.get(0) == "Перенесите сюда файлы для сжатия"):
            self.listbox.delete(0, "end")
        self.listbox.insert("end", event.data)