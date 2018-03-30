import threading
import subprocess
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="Ping!",
                                command=self.do_ping)
        self.output = tk.Text(self, width=80, height=15)
        
        self.entry.grid(row=0, column=0, padx=5, pady=5)
        self.button.grid(row=0, column=1, padx=5, pady=5)
        self.output.grid(row=1, column=0, columnspan=2,
                         padx=5, pady=5)

    def do_ping(self):
        self.button.config(state=tk.DISABLED)
        thread = AsyncAction(self.entry.get())
        thread.start()
        self.poll_thread(thread)

    def poll_thread(self, thread):
        if thread.is_alive():
            self.after(100, lambda: self.poll_thread(thread))
        else:
            self.button.config(state=tk.NORMAL)
            self.output.delete(1.0, tk.END)
            self.output.insert(tk.END, thread.result)
            

class AsyncAction(threading.Thread):
    def __init__(self, ip):
        super().__init__()
        self.ip = ip

    def run(self):
        self.result = subprocess.run(["ping", self.ip], shell=True,
                                     stdout=subprocess.PIPE).stdout

if __name__ == "__main__":
    app = App()
    app.mainloop()
