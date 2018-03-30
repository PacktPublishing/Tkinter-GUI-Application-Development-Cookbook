import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Drag and drop")

        self.dnd_item = None
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack()

        self.canvas.create_rectangle(30, 30, 60, 60, fill="green",
                                     tags="draggable")
        self.canvas.create_oval(120, 120, 150, 150, fill="red",
                                tags="draggable")

        self.canvas.tag_bind("draggable", "<ButtonPress-1>",
                             self.button_press)
        self.canvas.tag_bind("draggable", "<Button1-Motion>",
                             self.button_motion)

    def button_press(self, event):
        item = self.canvas.find_withtag(tk.CURRENT)
        self.dnd_item = (item, event.x, event.y)

    def button_motion(self, event):
        x, y = event.x, event.y
        item, x0, y0 = self.dnd_item
        self.canvas.move(item, x - x0, y - y0)
        self.dnd_item = (item, x, y)

if __name__ == "__main__":
    app = App()
    app.mainloop()
