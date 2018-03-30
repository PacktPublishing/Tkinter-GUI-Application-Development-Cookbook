import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        fields = ["First name", "Last name", "Phone", "Email"]
        labels = [tk.Label(self, text=f) for f in fields]
        entries = [tk.Entry(self) for _ in fields]
        self.widgets = list(zip(labels, entries))
        self.submit = tk.Button(self, text="Print info",
                                command=self.print_info)

        for i, (label, entry) in enumerate(self.widgets):
            label.grid(row=i, column=0, padx=10, sticky=tk.W)
            entry.grid(row=i, column=1, padx=10, pady=5)
        self.submit.grid(row=len(fields), column=1, sticky=tk.E,
                         padx=10, pady=10)

    def print_info(self):
        for label, entry in self.widgets:
            print("{} = {}".format(label.cget("text"), "=", entry.get()))

if __name__ == "__main__":
    app = App()
    app.mainloop()
