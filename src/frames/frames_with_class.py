# -*- coding: utf-8 -*-
"""."""
import tkinter as tk


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
        MyFrame1(master=self)
        MyFrame2(master=self)


class MyFrame1(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self['bg'] = 'red'
        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(master=self, text='Frame 1', bg='red')
        label.pack(expand=True, fill=tk.BOTH, )


class MyFrame2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self['bg'] = 'blue'
        self.pack(expand=True, fill=tk.BOTH, padx=10, pady=(0, 10))

        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(master=self, text='Frame 2', bg='Blue')
        label.pack(expand=True, fill=tk.BOTH)


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
