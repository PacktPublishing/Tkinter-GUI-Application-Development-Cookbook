import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.button = tk.Button(self, command=self.start_action,
                                text="Wait 5 seconds")
        self.button.pack(padx=50, pady=20)

    def start_action(self):
        self.button.config(state=tk.DISABLED)
        self.after(5000, lambda: self.button.config(state=tk.NORMAL))

if __name__ == "__main__":
    app = App()
    app.mainloop()
