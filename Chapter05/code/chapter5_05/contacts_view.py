import tkinter as tk

from contact import Contact


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


class NewContact(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.contact = None
        self.form = ContactForm(self)
        self.btn_add = tk.Button(self, text="Confirm", command=self.confirm)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)

    def confirm(self):
        self.contact = self.form.get_details()
        if self.contact:
            self.destroy()

    def show(self):
        self.grab_set()
        self.wait_window()
        return self.contact


class UpdateContactForm(ContactForm):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.btn_save = tk.Button(self, text="Save")
        self.btn_delete = tk.Button(self, text="Delete")
        
        self.btn_save.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_delete.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)

    def bind_save(self, callback):
        self.btn_save.config(command=callback)

    def bind_delete(self, callback):
        self.btn_delete.config(command=callback)


class ContactsView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SQLite Contacts list")
        self.list = ContactList(self, height=15)
        self.form = UpdateContactForm(self)
        self.btn_new = tk.Button(self, text="Add new contact")

        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)

    def set_ctrl(self, ctrl):
        self.btn_new.config(command=ctrl.create_contact)
        self.list.bind_doble_click(ctrl.select_contact)
        self.form.bind_save(ctrl.update_contact)
        self.form.bind_delete(ctrl.delete_contact)

    def add_contact(self, contact):
        self.list.insert(contact)

    def update_contact(self, contact, index):
        self.list.update(contact, index)

    def remove_contact(self, index):
        self.form.clear()
        self.list.delete(index)

    def get_details(self):
        return self.form.get_details()

    def load_details(self, contact):
        self.form.load_details(contact)
