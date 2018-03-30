import tkinter as tk
import webbrowser

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Text tags demo")
        self.text = tk.Text(self, width=50, height=10)
        self.btn_link = tk.Button(self, text="Add hyperlink",
                                  command=self.add_hyperlink)

        self.text.tag_config("link", foreground="blue", underline=1)
        self.text.tag_bind("link", "<Button-1>", self.open_link)
        self.text.tag_bind("link", "<Enter>",
                           lambda _: self.text.config(cursor="hand2"))
        self.text.tag_bind("link", "<Leave>",
                           lambda e: self.text.config(cursor=""))

        self.text.pack()
        self.btn_link.pack(expand=True)

    def add_hyperlink(self):
        selection = self.text.tag_ranges(tk.SEL)
        if selection:
            self.text.tag_add("link", *selection)

    def open_link(self, event):
        position = "@{},{} + 1c".format(event.x, event.y)
        index = self.text.index(position)
        prevrange = self.text.tag_prevrange("link", index)
        url = self.text.get(*prevrange)
        webbrowser.open(url)

if __name__ == "__main__":
    app = App()
    app.mainloop()
    
