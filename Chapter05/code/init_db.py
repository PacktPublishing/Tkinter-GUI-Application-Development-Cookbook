import csv
import sqlite3

def main():
    with open("contacts.csv", encoding="utf-8", newline="") as f, \
        sqlite3.connect("contacts.db") as conn:
        conn.execute("""CREATE TABLE contacts (
                          last_name text,
                          first_name text,
                          email text,
                          phone text
                        )""")
        conn.executemany("INSERT INTO contacts VALUES (?,?,?,?)",
                         csv.reader(f))

if __name__ == "__main__":
    main()
