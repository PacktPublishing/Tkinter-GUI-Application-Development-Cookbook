import time
import queue
import threading
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Progressbar example")
        self.queue = queue.Queue()
        self.progressbar = ttk.Progressbar(self, length=300,
                                           orient=tk.HORIZONTAL)
        self.button = tk.Button(self, text="Start",
                                command=self.start_action)

        self.progressbar.pack(padx=10, pady=10)
        self.button.pack(padx=10, pady=10)

    def start_action(self):
        self.button.config(state=tk.DISABLED)
        thread = AsyncAction(self.queue, 20)
        thread.start()
        self.poll_thread(thread)

    def poll_thread(self, thread):
        self.check_queue()
        if thread.is_alive():
            self.after(100, lambda: self.poll_thread(thread))
        else:
            self.button.config(state=tk.NORMAL)
            mb.showinfo("Done!", "Async action completed")

    def check_queue(self):
        while self.queue.qsize():
            try:
                step = self.queue.get(0)
                self.progressbar.step(step * 100)
            except queue.Empty:
                pass


class AsyncAction(threading.Thread):
    def __init__(self, queue, steps):
        super().__init__()
        self.queue = queue
        self.steps = steps

    def run(self):
        for _ in range(self.steps):
            time.sleep(1)
            self.queue.put(1 / self.steps)


if __name__ == "__main__":
    app = App()
    app.mainloop()
