import csv
import tkinter as tk
from chapter5_01 import Contact
from chapter5_02 import ContactForm, ContactList
class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("CSV Contact list")
		self.list = ContactList(self, height=12)
		self.form = ContactForm(self)
		self.contacts = self.load_contacts()
		for contact in self.contacts:
			self.list.insert(contact)
		self.list.pack(side=tk.LEFT, padx=10, pady=10)
		self.form.pack(side=tk.LEFT, padx=10, pady=10)
		self.list.bind_doble_click(self.show_contact)
	def load_contacts(self):
		with open("contacts.csv") as f:
			return [Contact(*r) for r in csv.reader(f)]
	def show_contact(self, index):
		contact = self.contacts[index]
		self.form.load_details(contact)
if __name__ == "__main__":
	app = App()
	app.mainloop()