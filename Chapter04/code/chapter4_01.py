import tkinter as tk
import tkinter.messagebox as mb

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        btn_info = tk.Button(self, text="Show Info",
                             command=self.show_info)
        btn_warn = tk.Button(self, text="Show Warning",
                             command=self.show_warning)
        btn_error = tk.Button(self, text="Show Error",
                              command=self.show_error)

        opts = {'padx': 40, 'pady': 5, 'expand': True, 'fill': tk.BOTH}
        btn_info.pack(**opts)
        btn_warn.pack(**opts)
        btn_error.pack(**opts)

    def show_info(self):
        msg = "Your user preferences have been saved"
        mb.showinfo("Information", msg)

    def show_warning(self):
        msg = "Temporary files have not been correctly removed"
        mb.showwarning("Warning", msg)

    def show_error(self):
        msg = "The application has encountered an unknown error"
        mb.showerror("Error", msg)

if __name__ == "__main__":
    app = App()
    app.mainloop()
