import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        frame = tk.Frame(self, bg="green",
                         height=100, width=100)
        frame.bind("<Button-1>", self.print_event)
        frame.bind("<Double-Button-1>", self.print_event)
        frame.bind("<ButtonRelease-1>", self.print_event)
        frame.bind("<B1-Motion>", self.print_event)
        frame.bind("<Enter>", self.print_event)
        frame.bind("<Leave>", self.print_event)
        frame.pack(padx=50, pady=50)

    def print_event(self, event):
        position = "(x={}, y={})".format(event.x, event.y)
        print(event.type, "event", position)

if __name__ == "__main__":
    app = App()
    app.mainloop()
