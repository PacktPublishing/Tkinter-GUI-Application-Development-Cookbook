import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        group_1 = tk.LabelFrame(self, padx=15, pady=10,
                                text="Personal Information")
        group_1.pack(padx=10, pady=5)

        tk.Label(group_1, text="First name").grid(row=0)
        tk.Label(group_1, text="Last name").grid(row=1)
        tk.Entry(group_1).grid(row=0, column=1, sticky=tk.W)
        tk.Entry(group_1).grid(row=1, column=1, sticky=tk.W)

        group_2 = tk.LabelFrame(self, padx=15, pady=10,
                                text="Address")
        group_2.pack(padx=10, pady=5)

        tk.Label(group_2, text="Street").grid(row=0)
        tk.Label(group_2, text="City").grid(row=1)
        tk.Label(group_2, text="ZIP Code").grid(row=2)
        tk.Entry(group_2).grid(row=0, column=1, sticky=tk.W)
        tk.Entry(group_2).grid(row=1, column=1, sticky=tk.W)
        tk.Entry(group_2, width=8).grid(row=2, column=1,
                                        sticky=tk.W)

        self.btn_submit = tk.Button(self, text="Submit")
        self.btn_submit.pack(padx=10, pady=10, side=tk.RIGHT)

if __name__ == "__main__":
    app = App()
    app.mainloop()
