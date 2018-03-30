import tkinter as tk


class LineForm(tk.LabelFrame):
    arrows = (tk.NONE, tk.FIRST, tk.LAST, tk.BOTH)
    colors = ("black", "red", "blue", "green")

    def __init__(self, master):
        super().__init__(master, text="Line options")

        self.arrow = tk.StringVar()
        self.arrow.set(self.arrows[0])
        arrow_label = tk.Label(self, text="Arrow style")
        arrow_option = tk.OptionMenu(self, self.arrow, *self.arrows)

        self.color = tk.StringVar()
        self.color.set(self.colors[0])
        color_label = tk.Label(self, text="Fill color")
        color_option = tk.OptionMenu(self, self.color, *self.colors)

        line_width_label = tk.Label(self, text="Line width")
        self.line_width = tk.Spinbox(self, values=(1, 2, 3, 4), width=5)

        arrow_label.grid(sticky=tk.W, row=0, column=0)
        arrow_option.grid(row=0, column=1, pady=10)
        color_label.grid(sticky=tk.W, row=1, column=0)
        color_option.grid(row=1, column=1, pady=10)
        line_width_label.grid(sticky=tk.W, row=2, column=0)
        self.line_width.grid(row=2, column=1, pady=10)

    def get_arrow(self):
        return self.arrow.get()

    def get_color(self):
        return self.color.get()

    def get_width(self):
        return int(self.line_width.get())


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Basic canvas")

        self.line_start = None
        self.form = LineForm(self)
        self.render_btn = tk.Button(self, text="Render canvas",
                                    command=self.render_canvas)
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.bind("<Button-1>", self.draw)

        self.form.grid(row=0, column=0, padx=10, pady=10)
        self.render_btn.grid(row=1, column=0)
        self.canvas.grid(row=0, column=1, rowspan=2)

    def draw(self, event):
        x, y = event.x, event.y
        if not self.line_start:
            self.line_start = (x, y)
        else:
            x_origin, y_origin = self.line_start
            self.line_start = None
            line = (x_origin, y_origin, x, y)
            arrow = self.form.get_arrow()
            color = self.form.get_color()
            width = self.form.get_width()
            self.canvas.create_line(*line, arrow=arrow,
                                    fill=color, width=width)

    def render_canvas(self):
        self.canvas.postscript(file="output.ps", colormode="color")

if __name__ == "__main__":
    app = App()
    app.mainloop()
