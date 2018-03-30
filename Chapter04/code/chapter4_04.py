import tkinter as tk
import tkinter.filedialog as fd

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.text = tk.Text(self, height=10, width=50)
        self.btn_save = tk.Button(self, text="Save", command=self.save_file)

        self.text.pack()
        self.btn_save.pack(pady=10, ipadx=5)

    def save_file(self):
        contents = self.text.get(1.0, tk.END)
        new_file = fd.asksaveasfile(title="Save file", defaultextension=".txt",
                                filetypes=(("Text files", "*.txt"),))
        if new_file:
            new_file.write(contents)
            new_file.close()

if __name__ == "__main__":
    app = App()
    app.mainloop()
