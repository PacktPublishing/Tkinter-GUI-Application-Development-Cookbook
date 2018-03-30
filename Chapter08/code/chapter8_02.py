import tkinter as tk
import tkinter.ttk as ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ttk Combobox")
        colors = ("Purple", "Yellow", "Red", "Blue")

        self.label = ttk.Label(self, text="Please select a color")
        self.combo = ttk.Combobox(self, values=colors)
        btn_submit = ttk.Button(self, text="Submit",
                                command=self.display_color)
        btn_clear = ttk.Button(self, text="Clear",
                                command=self.clear_color)

        self.combo.bind("<<ComboboxSelected>>", self.display_color)

        self.label.pack(pady=10)
        self.combo.pack(side=tk.LEFT, padx=10, pady=5)
        btn_submit.pack(side=tk.TOP, padx=10, pady=5)
        btn_clear.pack(padx=10, pady=5)

    def display_color(self, *args):
        color = self.combo.get()
        print("Your selection is", color)

    def clear_color(self):
        self.combo.set("")

if __name__ == "__main__":
    app = App()
    app.mainloop()
