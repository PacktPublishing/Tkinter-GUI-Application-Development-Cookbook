import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Options demo")
        self.option_add("*font", "helvetica 10")
        self.option_add("*header.font", "helvetica 18 bold")
        self.option_add("*subtitle.font", "helvetica 14 italic")
        self.option_add("*Button.foreground", "blue")
        self.option_add("*Button.background", "white")
        self.option_add("*Button.activeBackground", "gray")
        self.option_add("*Button.activeForeground", "black")

        self.create_label(name="header", text="This is the header")
        self.create_label(name="subtitle", text="This is the subtitle")
        self.create_label(text="This is a paragraph")
        self.create_label(text="This is another paragraph")
        self.create_button(text="See more")

    def create_label(self, **options):
        tk.Label(self, **options).pack(padx=20, pady=5, anchor=tk.W)

    def create_button(self, **options):
        tk.Button(self, **options).pack(padx=5, pady=5, anchor=tk.E)

if __name__ == "__main__":
    app = App()
    app.mainloop()
