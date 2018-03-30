import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Finding canvas items")

        self.current = None
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.bind("<Motion>", self.mouse_motion)
        self.canvas.pack()

        self.update()
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        positions = [(60, 60), (w-60, 60), (60, h-60), (w-60, h-60)]
        for x, y in positions:
            self.canvas.create_rectangle(x-10, y-10, x+10, y+10,
                                         fill="blue")

    def mouse_motion(self, event):
        self.canvas.itemconfig(self.current, fill="blue")
        self.current = self.canvas.find_closest(event.x, event.y)
        self.canvas.itemconfig(self.current, fill="yellow")


if __name__ == "__main__":
    app = App()
    app.mainloop()
