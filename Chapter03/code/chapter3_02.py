import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fonts demo")
        text = "The quick brown fox jumps over the lazy dog"
        self.label = tk.Label(self, text=text)

        self.family = tk.StringVar()
        self.family.trace("w", self.set_font)
        families = ("Times", "Courier", "Helvetica")
        self.option = tk.OptionMenu(self, self.family, *families)

        self.size = tk.StringVar()
        self.size.trace("w", self.set_font)
        self.spinbox = tk.Spinbox(self, from_=8, to=18,
                                  textvariable=self.size)

        self.family.set(families[0])
        self.size.set("10")
        self.label.pack(padx=20, pady=20)
        self.option.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.spinbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def set_font(self, *args):
        family = self.family.get()
        size = self.size.get()
        self.label.config(font=(family, size))

if __name__ == "__main__":
    app = App()
    app.mainloop()
