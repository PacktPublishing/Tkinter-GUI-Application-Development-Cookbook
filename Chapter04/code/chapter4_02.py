import tkinter as tk
import tkinter.messagebox as mb

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.create_button(mb.askyesno, "Ask Yes/No",
                           "Returns True or False")
        self.create_button(mb.askquestion, "Ask a question",
                           "Returns 'yes' or 'no'")
        self.create_button(mb.askokcancel, "Ask Ok/Cancel",
                           "Returns True or False")
        self.create_button(mb.askretrycancel, "Ask Retry/Cancel",
                           "Returns True or False")
        self.create_button(mb.askyesnocancel, "Ask Yes/No/Cancel",
                           "Returns True, False or None")

    def create_button(self, dialog, title, message):
        command = lambda: print(dialog(title, message))
        btn = tk.Button(self, text=title, command=command)
        btn.pack(padx=40, pady=5, expand=True, fill=tk.BOTH)

if __name__ == "__main__":
    app = App()
    app.mainloop()
