import time
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.button = tk.Button(self, command=self.start_action,
                                text="Wait 5 seconds")
        self.cancel = tk.Button(self, command=self.cancel_action,
                                text="Stop", state=tk.DISABLED)
        self.button.pack(padx=30, pady=20, side=tk.LEFT)
        self.cancel.pack(padx=30, pady=20, side=tk.LEFT)

    def start_action(self):
        self.button.config(state=tk.DISABLED)
        self.cancel.config(state=tk.NORMAL)
        self.scheduled_id = self.after(5000, self.init_buttons)

    def init_buttons(self):
        self.button.config(state=tk.NORMAL)
        self.cancel.config(state=tk.DISABLED)

    def cancel_action(self):
        print("Canceling scheduled", self.scheduled_id)
        self.after_cancel(self.scheduled_id)
        self.init_buttons()

if __name__ == "__main__":
    app = App()
    app.mainloop()
