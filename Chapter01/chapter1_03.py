import tkinter as tk

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.username = tk.Entry(self)
        self.password = tk.Entry(self, show="*")
        self.login_btn = tk.Button(self, text="Log in",
                                   command=self.print_login)
        self.clear_btn = tk.Button(self, text="Clear",
                                   command=self.clear_form)        
        self.username.pack()
        self.password.pack()
        self.login_btn.pack(fill=tk.BOTH)
        self.clear_btn.pack(fill=tk.BOTH)

    def print_login(self):
        print("Username: {}".format(self.username.get()))
        print("Password: {}".format(self.password.get()))

    def clear_form(self):
        self.username.delete(0, tk.END)
        self.password.delete(0, tk.END)
        self.username.focus_set()

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
