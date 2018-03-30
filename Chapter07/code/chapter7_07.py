import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Detecting collisions between items")

        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack()
        self.update()
        self.width = w = self.canvas.winfo_width()
        self.height = h = self.canvas.winfo_height()

        pos = (w/2 - 15, h/2 - 15, w/2 + 15, h/2 + 15)
        self.item = self.canvas.create_rectangle(*pos, fill="blue")  
        positions = [(60, 60), (w-60, 60), (60, h-60), (w-60, h-60)]
        for x, y in positions:
            self.canvas.create_rectangle(x-10, y-10, x+10, y+10,
                                         fill="green")
          
        self.pressed_keys = {}
        self.bind("<KeyPress>", self.key_press)
        self.bind("<KeyRelease>", self.key_release)
        self.process_movements()

    def key_press(self, event):
        self.pressed_keys[event.keysym] = True

    def key_release(self, event):
        self.pressed_keys.pop(event.keysym, None)

    def process_movements(self):
        all_items = self.canvas.find_all()
        for item in filter(lambda i: i is not self.item, all_items):
            self.canvas.itemconfig(item, fill="green")

        x0, y0, x1, y1 = self.canvas.coords(self.item)
        items = self.canvas.find_overlapping(x0, y0, x1, y1)
        for item in filter(lambda i: i is not self.item, items):
            self.canvas.itemconfig(item, fill="yellow")

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

        
        pos_x = x0 + (x1 - x0) / 2 + off_x
        pos_y = y0 + (y1 - y0) / 2 + off_y
        if 0 <= pos_x <= self.width and 0 <= pos_y <= self.height:
            self.canvas.move(self.item, off_x, off_y)

        self.after(10, self.process_movements)

if __name__ == "__main__":
    app = App()
    app.mainloop()
