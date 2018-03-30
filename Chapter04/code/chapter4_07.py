import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.menu = tk.Menu(self, tearoff=0)
        self.menu.add_command(label="Cut", command=self.cut_text)
        self.menu.add_command(label="Copy", command=self.copy_text)
        self.menu.add_command(label="Paste", command=self.paste_text)
        self.menu.add_command(label="Delete", command=self.delete_text)

        self.text = tk.Text(self, height=10, width=50)
        self.text.bind("<Button-3>", self.show_popup)
        self.text.pack()

    def show_popup(self, event):
        self.menu.post(event.x_root, event.y_root)

    def cut_text(self):
        self.copy_text()
        self.delete_text()

    def copy_text(self):
        selection = self.text.tag_ranges(tk.SEL)
        if selection:
            self.clipboard_clear()
            self.clipboard_append(self.text.get(*selection))

    def paste_text(self):
        self.text.insert(tk.INSERT, self.clipboard_get())

    def delete_text(self):
        selection = self.text.tag_ranges(tk.SEL)
        if selection:
            self.text.delete(*selection)


if __name__ == "__main__":
    app = App()
    app.mainloop()
