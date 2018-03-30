import tkinter as tk
import tkinter as ttk

class App(tk.Tk):
    greetings = ("Hello", "Ciao", "Hola")

    def __init__(self):
        super().__init__()
        self.title("Tk themed widgets")

        var = tk.StringVar()
        var.set(self.greetings[0])
        label_frame = ttk.LabelFrame(self, text="Choose a greeting")
        for greeting in self.greetings:
            radio = ttk.Radiobutton(label_frame, text=greeting,
                                    variable=var, value=greeting)
            radio.pack()

        frame = ttk.Frame(self)
        label = ttk.Label(frame, text="Enter your name")
        entry = ttk.Entry(frame)

        command = lambda: print("{}, {}!".format(var.get(), entry.get()))
        button = ttk.Button(frame, text="Greet", command=command)

        label.grid(row=0, column=0, padx=5, pady=5)
        entry.grid(row=0, column=1, padx=5, pady=5)
        button.grid(row=1, column=0, columnspan=2, pady=5)

        label_frame.pack(side=tk.LEFT, padx=10, pady=10)
        frame.pack(side=tk.LEFT, padx=10, pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()
