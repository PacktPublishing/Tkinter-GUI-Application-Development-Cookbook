import json
import threading
import urllib.request
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HTTP request example")
        self.label = tk.Label(self, text="Click 'Start' to get a random value")
        self.button = tk.Button(self, text="Start",
                                command=self.start_action)

        self.label.pack(padx=60, pady=10)
        self.button.pack(pady=10)

    def start_action(self):
        self.button.config(state=tk.DISABLED)
        thread = AsyncAction()
        thread.start()
        self.check_thread(thread)

    def check_thread(self, thread):
        if thread.is_alive():
            self.after(100, lambda: self.check_thread(thread))
        else:
            text = "Random value: {}".format(thread.result)
            self.label.config(text=text)
            self.button.config(state=tk.NORMAL)


class AsyncAction(threading.Thread):
    def run(self):
        self.result = None
        url = "http://localhost:8080"
        with urllib.request.urlopen(url) as f:
            obj = json.loads(f.read().decode("utf-8"))
            self.result = obj["random"]


if __name__ == "__main__":
    app = App()
    app.mainloop()
