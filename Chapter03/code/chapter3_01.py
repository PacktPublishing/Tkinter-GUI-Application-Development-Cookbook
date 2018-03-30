from functools import partial

import tkinter as tk
from tkinter.colorchooser import askcolor

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Colors demo")
        text = "The quick brown fox jumps over the lazy dog"
        self.label = tk.Label(self, text=text)
        self.fg_btn = tk.Button(self, text="Set foreground color",
                                command=partial(self.set_color, "fg")) 
        self.bg_btn = tk.Button(self, text="Set background color",
                                command=partial(self.set_color, "bg"))

        self.label.pack(padx=20, pady=20)
        self.fg_btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.bg_btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def set_color(self, option):
        color = askcolor()[1]
        print("Chosen color:", color)
        self.label.config(**{option: color})

if __name__ == "__main__":
    app = App()
    app.mainloop()
