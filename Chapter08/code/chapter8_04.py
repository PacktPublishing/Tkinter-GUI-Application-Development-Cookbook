import os
import tkinter as tk
import tkinter.ttk as ttk

class App(tk.Tk):
    def __init__(self, path):
        super().__init__()
        self.title("Ttk Treeview")

        abspath = os.path.abspath(path)
        self.nodes = {}
        self.tree = ttk.Treeview(self)
        self.tree.heading("#0", text=abspath, anchor=tk.W)
        ysb = ttk.Scrollbar(self, orient=tk.VERTICAL,
                            command=self.tree.yview)
        xsb = ttk.Scrollbar(self, orient=tk.HORIZONTAL,
                            command=self.tree.xview)
        self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)

        self.tree.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        ysb.grid(row=0, column=1, sticky=tk.N + tk.S)
        xsb.grid(row=1, column=0, sticky=tk.E + tk.W)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.tree.bind("<<TreeviewOpen>>", self.open_node)
        self.populate_node("", abspath)

    def populate_node(self, parent, abspath):
        for entry in os.listdir(abspath):
            entry_path = os.path.join(abspath, entry)
            node = self.tree.insert(parent, tk.END, text=entry, open=False)
            if os.path.isdir(entry_path):
                self.nodes[node] = entry_path
                self.tree.insert(node, tk.END)

    def open_node(self, event):
        item = self.tree.focus()
        abspath = self.nodes.pop(item, False)
        if abspath:
            children = self.tree.get_children(item)
            self.tree.delete(children)
            self.populate_node(item, abspath)


if __name__ == "__main__":
    app = App(path=".")
    app.mainloop()
