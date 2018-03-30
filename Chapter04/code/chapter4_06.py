import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.checked = tk.BooleanVar()
        self.checked.trace("w", self.mark_checked)
        self.radio = tk.StringVar()
        self.radio.set("1")
        self.radio.trace("w", self.mark_radio)
        
        menu = tk.Menu(self)
        submenu = tk.Menu(menu, tearoff=0)

        submenu.add_checkbutton(label="Checkbutton", onvalue=True,
                                offvalue=False, variable=self.checked)
        submenu.add_separator()
        submenu.add_radiobutton(label="Radio 1", value="1",
                                variable=self.radio)
        submenu.add_radiobutton(label="Radio 2", value="2",
                                variable=self.radio)
        submenu.add_radiobutton(label="Radio 3", value="3",
                                variable=self.radio)

        menu.add_cascade(label="Options", menu=submenu)
        menu.add_command(label="Quit", command=self.destroy)
        self.config(menu=menu)

    def mark_checked(self, *args):
        print(self.checked.get())

    def mark_radio(self, *args):
        print(self.radio.get())

if __name__ == "__main__":
    app = App()
    app.mainloop()
