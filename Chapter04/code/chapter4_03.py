import tkinter as tk
import tkinter.filedialog as fd

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        btn_file = tk.Button(self, text="Choose file",
                             command=self.choose_file)
        btn_dir = tk.Button(self, text="Choose directory",
                             command=self.choose_directory)
        btn_file.pack(padx=60, pady=10)
        btn_dir.pack(padx=60, pady=10)

    def choose_file(self):
        filetypes = (("Plain text files", "*.txt"),
                     ("Images", "*.jpg *.gif *.png"),
                     ("All files", "*"))
        filename = fd.askopenfilename(title="Open file", initialdir="/",
                                      filetypes=filetypes)
        if filename:
            print(filename)

    def choose_directory(self):
        directory = fd.askdirectory(title="Open directory", initialdir="/")
        if directory:
            print(directory)

if __name__ == "__main__":
    app = App()
    app.mainloop()
