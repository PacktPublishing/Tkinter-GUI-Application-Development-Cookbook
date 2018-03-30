import tkinter as tk
from collections import namedtuple

User = namedtuple("User", ["username", "password", "user_type"])

class UserForm(tk.Toplevel):
    def __init__(self, parent, user_type):
        super().__init__(parent)
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.user_type = user_type

        label = tk.Label(self, text="Create a new " + user_type.lower())
        entry_name = tk.Entry(self, textvariable=self.username)
        entry_pass = tk.Entry(self, textvariable=self.password, show="*")
        btn = tk.Button(self, text="Submit", command=self.destroy)

        label.grid(row=0, columnspan=2)
        tk.Label(self, text="Username:").grid(row=1, column=0)
        tk.Label(self, text="Password:").grid(row=2, column=0)
        entry_name.grid(row=1, column=1)
        entry_pass.grid(row=2, column=1)
        btn.grid(row=3, columnspan=2)

    def open(self):
        self.grab_set()
        self.wait_window()
        username = self.username.get()
        password = self.password.get()
        return User(username, password, self.user_type)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        user_types = ("Administrator", "Supervisor", "Regular user")
        self.user_type = tk.StringVar()
        self.user_type.set(user_types[0])

        label = tk.Label(self, text="Please, select the type of user")
        radios = [tk.Radiobutton(self, text=t, value=t, \
                  variable=self.user_type) for t in user_types]
        btn = tk.Button(self, text="Create user", command=self.open_window)

        label.pack(padx=10, pady=10)
        for radio in radios:
            radio.pack(padx=10, anchor=tk.W)
        btn.pack(pady=10)

    def open_window(self):
        window = UserForm(self, self.user_type.get())
        user = window.open()
        print(user)

if __name__ == "__main__":
    app = App()
    app.mainloop()
