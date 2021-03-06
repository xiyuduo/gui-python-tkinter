# -*- coding: utf-8 -*-
"""."""
import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(string='Janela principal')
        icon_png = tk.PhotoImage(file='../assets/icons/icon.png')
        self.iconphoto(False, icon_png)

        width = round(number=self.winfo_screenwidth() / 2)
        height = round(number=self.winfo_screenheight() / 2)
        self.geometry(newGeometry=f'{width}x{height}')
        self.minsize(width=width, height=height)

        self.create_widgets()

    def create_widgets(self):
        MyFrame(master=self)


class MyFrame(ttk.Frame):
    options = ['Opção 1', 'Opção 2', 'Opção 3']

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.radio_button_value = tk.IntVar()

        self.create_widgets()

    def create_widgets(self):
        for index, value in enumerate(self.options):
            radiobutton = ttk.Radiobutton(
                master=self,
                text=value,
                variable=self.radio_button_value,
                value=index,
                command=self._on_checked,
            )
            radiobutton.pack()

    def _on_checked(self):
        value = self.options[self.radio_button_value.get()]
        print(f'{value} selecionada.')


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
