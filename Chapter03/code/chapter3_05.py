import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Text demo")
        self.resizable(0, 0)
        self.text = tk.Text(self, width=50, height=10)
        self.btn_clear = tk.Button(self, text="Clear text",
                                   command=self.clear_text)
        self.btn_insert = tk.Button(self, text="Insert text",
                                    command=self.insert_text)
        self.btn_print = tk.Button(self, text="Print selection",
                                   command=self.print_selection)
        self.text.pack()
        self.btn_clear.pack(side=tk.LEFT, expand=True, pady=10)
        self.btn_insert.pack(side=tk.LEFT, expand=True, pady=10)
        self.btn_print.pack(side=tk.LEFT, expand=True, pady=10)

    def clear_text(self):
        self.text.delete("1.0", tk.END)

    def insert_text(self):
        self.text.insert(tk.INSERT, "Hello, world")

    def print_selection(self):
        selection = self.text.tag_ranges(tk.SEL)
        if selection:
            content = self.text.get(*selection)
            print(content)

if __name__ == "__main__":
    app = App()
    app.mainloop()
