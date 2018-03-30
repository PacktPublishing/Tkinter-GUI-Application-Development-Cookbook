import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Moving canvas items")

        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack()
        self.update()
        self.width = self.canvas.winfo_width()
        self.height = self.canvas.winfo_height()

        self.item = self.canvas.create_rectangle(30, 30, 60, 60,
                                                 fill="blue")
        self.pressed_keys = {}
        self.bind("<KeyPress>", self.key_press)
        self.bind("<KeyRelease>", self.key_release)
        self.process_movements()

    def key_press(self, event):
        self.pressed_keys[event.keysym] = True

    def key_release(self, event):
        self.pressed_keys.pop(event.keysym, None)

    def process_movements(self):
        off_x, off_y = 0, 0
        speed = 3
        if 'Right' in self.pressed_keys:
            off_x += speed
        if 'Left' in self.pressed_keys:
            off_x -= speed
        if 'Down' in self.pressed_keys:
            off_y += speed
        if 'Up' in self.pressed_keys:
            off_y -= speed

        x0, y0, x1, y1 = self.canvas.coords(self.item)
        pos_x = x0 + (x1 - x0) / 2 + off_x
        pos_y = y0 + (y1 - y0) / 2 + off_y
        if 0 <= pos_x <= self.width and 0 <= pos_y <= self.height:
            self.canvas.move(self.item, off_x, off_y)

        self.after(10, self.process_movements)

if __name__ == "__main__":
    app = App()
    app.mainloop()
