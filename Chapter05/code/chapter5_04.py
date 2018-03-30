import sqlite3
import tkinter as tk

from chapter5_01 import Contact
from chapter5_02 import ContactForm, ContactList


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


class App(tk.Tk):
    def __init__(self, conn):
        super().__init__()
        self.title("SQLite Contacts list")
        self.conn = conn
        self.selection = None
        self.list = ContactList(self, height=15)
        self.form = UpdateContactForm(self)
        self.btn_new = tk.Button(self, text="Add new contact",
                                 command=self.add_contact)
        self.contacts = self.load_contacts()

        for contact in self.contacts:
            self.list.insert(contact)
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)

        self.list.bind_doble_click(self.show_contact)
        self.form.bind_save(self.update_contact)
        self.form.bind_delete(self.delete_contact)

    def load_contacts(self):
        contacts = []
        sql = "SELECT rowid, last_name, first_name, email, phone FROM contacts"
        for row in self.conn.execute(sql):
            contact = Contact(*row[1:])
            contact.rowid = row[0]
            contacts.append(contact)
        return contacts

    def show_contact(self, index):
        self.selection = index
        contact = self.contacts[index]
        self.form.load_details(contact)

    def to_values(self, c):
        return (c.last_name, c.first_name, c.email, c.phone)

    def add_contact(self):
        new_contact = NewContact(self)
        contact = new_contact.show()
        if not contact:
            return
        values = self.to_values(contact)
        with self.conn as c:
            cursor = c.cursor()
            cursor.execute("INSERT INTO contacts VALUES (?,?,?,?)", values)
            contact.rowid = cursor.lastrowid
        self.contacts.append(contact)
        self.list.insert(contact)

    def update_contact(self):
        if self.selection is None:
            return
        rowid = self.contacts[self.selection].rowid
        contact = self.form.get_details()
        if contact:
            values = self.to_values(contact)
            with self.conn as c:
                sql = """UPDATE contacts SET
                         last_name = ?,
                         first_name = ?,
                         email = ?,
                         phone = ?
                     WHERE rowid = ?"""
                c.execute(sql, values + (rowid,))
            contact.rowid = rowid
            self.contacts[self.selection] = contact
            self.list.update(contact, self.selection)

    def delete_contact(self):
        if self.selection is None:
            return
        rowid = self.contacts[self.selection].rowid
        with self.conn as c:
            c.execute("DELETE FROM contacts WHERE rowid = ?", (rowid,))
        self.form.clear()
        self.list.delete(self.selection)
        self.selection = None

def main():
    with sqlite3.connect("contacts.db") as conn:
        app = App(conn)
        app.mainloop()


if __name__ == "__main__":
    main()
