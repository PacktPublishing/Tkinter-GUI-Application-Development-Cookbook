import tkinter as tk

class ListFrame(tk.Frame):
    def __init__(self, master, items=[]):
        super().__init__(master) 
        self.list = tk.Listbox(self)
        self.scroll = tk.Scrollbar(self, orient=tk.VERTICAL,
                                   command=self.list.yview)
        self.list.config(yscrollcommand=self.scroll.set)
        self.list.insert(0, *items)
        self.list.pack(side=tk.LEFT)
        self.scroll.pack(side=tk.LEFT, fill=tk.Y)

    def pop_selection(self):
        index = self.list.curselection()
        if index:
            value = self.list.get(index)
            self.list.delete(index)
            return value

    def insert_item(self, item):
        self.list.insert(tk.END, item)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        months = ["January", "February", "March", "April",
                  "May", "June", "July", "August", "September",
                  "October", "November", "December"]
        self.frame_a = ListFrame(self, months)
        self.frame_b = ListFrame(self)
        self.btn_right = tk.Button(self, text=">",
                                   command=self.move_right)
        self.btn_left = tk.Button(self, text="<",
                                  command=self.move_left)

        self.frame_a.pack(side=tk.LEFT, padx=10, pady=10)
        self.frame_b.pack(side=tk.RIGHT, padx=10, pady=10)
        self.btn_right.pack(expand=True, ipadx=5)
        self.btn_left.pack(expand=True, ipadx=5)

    def move_right(self):
        self.move(self.frame_a, self.frame_b)

    def move_left(self):
        self.move(self.frame_b, self.frame_a)

    def move(self, frame_from, frame_to):
        value = frame_from.pop_selection()
        if value:
            frame_to.insert_item(value)

if __name__ == "__main__":
    app = App()
    app.mainloop()
