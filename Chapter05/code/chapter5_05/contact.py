import re

def required(value, message):
    if not value:
        raise ValueError(message)
    return value

def matches(value, regex, message):
    if value and not regex.match(value):
        raise ValueError(message)
    return value

class Contact(object):
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    phone_regex = re.compile(r"\([0-9]{3}\)\s[0-9]{7}")

    def __init__(self, last_name, first_name, email, phone):
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.phone = phone

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = required(value, "Last name is required")

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = required(value, "First name is required")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = matches(value, self.email_regex, "Invalid email format")

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = matches(value, self.phone_regex, "Invalid phone format")
