import sqlite3

from contacts_repository import ContactsRepository
from contacts_view import ContactsView
from contacts_controller import ContactsController


def main():
    with sqlite3.connect("contacts.db") as conn:
        repo = ContactsRepository(conn)
        view = ContactsView()
        ctrl = ContactsController(repo, view)

        view.set_ctrl(ctrl)
        ctrl.start()

if __name__ == "__main__":
    main()
