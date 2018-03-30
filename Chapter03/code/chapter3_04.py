import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cursors demo")
        self.resizable(0, 0)
        self.label = tk.Label(self, text="Click the button to start")
        self.btn_launch = tk.Button(self, text="Start!",
                                    command=self.perform_action)
        self.btn_help = tk.Button(self, text="Help",
                                  cursor="question_arrow")

        btn_opts = {"side": tk.LEFT, "expand":True, "fill": tk.X,
                    "ipadx": 30, "padx": 20, "pady": 5}
        self.label.pack(pady=10)
        self.btn_launch.pack(**btn_opts)
        self.btn_help.pack(**btn_opts)

    def perform_action(self):
        self.btn_launch.config(state=tk.DISABLED)
        self.btn_help.config(state=tk.DISABLED)
        self.label.config(text="Working...")
        self.after(3000, self.end_action)
        self.config(cursor="watch")

    def end_action(self):
        self.btn_launch.config(state=tk.NORMAL)
        self.btn_help.config(state=tk.NORMAL)
        self.label.config(text="Done!")
        self.config(cursor="arrow")

    def set_watch_cursor(self, widget):
        widget._old_cursor = widget.cget("cursor")
        widget.config(cursor="watch")
        for w in widget.winfo_children():
            self.set_watch_cursor(w)

    def restore_cursor(self, widget):
        widget.config(cursor=widget.old_cursor)
        for w in widget.winfo_children():
            self.restore_cursor(w)

if __name__ == "__main__":
    app = App()
    app.mainloop()
