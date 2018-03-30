import tkinter as tk
import tkinter.messagebox as mb

class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.protocol("WM_DELETE_WINDOW", self.confirm_delete)

        self.label = tk.Label(self, text="This is another window")
        self.button = tk.Button(self, text="Close", command=self.destroy)

        self.label.pack(padx=20, pady=20)
        self.button.pack(pady=5, ipadx=2, ipady=2)

    def confirm_delete(self):
        message = "Are you sure you want to close this window?"
        if mb.askyesno(message=message, parent=self):
            self.destroy()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.btn = tk.Button(self, text="Open new window",
                             command=self.open_about)
        self.btn.pack(padx=50, pady=20)

    def open_about(self):
        window = Window(self)
        window.grab_set()

if __name__ == "__main__":
    app = App()
    app.mainloop()
