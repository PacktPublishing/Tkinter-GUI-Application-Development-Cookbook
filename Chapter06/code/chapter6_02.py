import time
import threading
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.button = tk.Button(self, command=self.start_action,
                                text="Wait 5 seconds")
        self.button.pack(padx=50, pady=20)

    def start_action(self):
        self.button.config(state=tk.DISABLED)
        thread = threading.Thread(target=self.run_action)
        print(threading.main_thread().name)
        print(thread.name)
        thread.start()
        self.check_thread(thread)

    def check_thread(self, thread):
        if thread.is_alive():
            self.after(100, lambda: self.check_thread(thread))
        else:
            self.button.config(state=tk.NORMAL)

    def run_action(self):
        print("Starting long running action...")
        time.sleep(5)
        print("Long running action finished!")

if __name__ == "__main__":
    app = App()
    app.mainloop()
