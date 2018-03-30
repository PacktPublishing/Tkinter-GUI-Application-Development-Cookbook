import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Tkinter app")
        self.iconbitmap("python.ico")
        self.geometry("400x200+10+10")

if __name__ == "__main__":
    app = App()
    app.mainloop()
