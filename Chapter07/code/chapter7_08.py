import random
import tkinter as tk

class App(tk.Tk):
    colors = ("red", "yellow", "green", "blue", "orange")

    def __init__(self):
        super().__init__()
        self.title("Removing canvas items")

        self.canvas = tk.Canvas(self, bg="white")
        frame = tk.Frame(self)
        generate_btn = tk.Button(frame, text="Generate items",
                                 command=self.generate_items)
        clear_btn = tk.Button(frame, text="Clear items",
                              command=self.clear_items)

        self.canvas.pack()
        frame.pack(fill=tk.BOTH)
        generate_btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        clear_btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.update()
        self.width = self.canvas.winfo_width()
        self.height = self.canvas.winfo_height()

        self.canvas.bind("<Button-1>", self.on_click)
        self.generate_items()

    def on_click(self, event):
        item = self.canvas.find_withtag(tk.CURRENT)
        self.canvas.delete(item)

    def generate_items(self):
        self.clear_items()
        for _ in range(10):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            color = random.choice(self.colors)
            self.canvas.create_oval(x, y, x + 20, y + 20, fill=color)

    def clear_items(self):
        self.canvas.delete(tk.ALL)

if __name__ == "__main__":
    app = App()
    app.mainloop()
