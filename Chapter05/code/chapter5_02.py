import tkinter as tk
import tkinter.messagebox as mb

from chapter5_01 import Contact


class ContactList(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)

        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insert(self, contact, index=tk.END):
        text = "{}, {}".format(contact.last_name, contact.first_name)
        self.lb.insert(index, text)

    def delete(self, index):
        self.lb.delete(index, index)

    def update(self, contact, index):
        self.delete(index)
        self.insert(contact, index)

    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)


class ContactForm(tk.LabelFrame):
    fields = ("Last name", "First name", "Email", "Phone")

    def __init__(self, master, **kwargs):
        super().__init__(master, text="Contact", padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.create_field, enumerate(self.fields)))
        self.frame.pack()

    def create_field(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry

    def load_details(self, contact):
        values = (contact.last_name, contact.first_name,
                  contact.email, contact.phone)
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

    def get_details(self):
        values = [e.get() for e in self.entries]
        try:
            return Contact(*values)
        except ValueError as e:
            mb.showerror("Validation error", str(e), parent=self)

    def clear(self):
        for entry in self.entries:
            entry.delete(0, tk.END)
