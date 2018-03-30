import re
import attr

def required(message):
    def func(self, attr, val):
        if not val: raise ValueError(message)
    return func

def match(pattern, message):
    regex = re.compile(pattern)
    def func(self, attr, val):
        if val and not regex.match(val):
            raise ValueError(message)
    return func

@attr.s
class Contact(object):
    last_name = attr.ib(validator=required("Last name is required"))
    first_name = attr.ib(validator=required("First name is required"))
    email = attr.ib(validator=match(r"[^@]+@[^@]+\.[^@]+",
                                    "Invalid email format"))
    phone = attr.ib(validator=match(r"\([0-9]{3}\)\s[0-9]{7}",
                                    "Invalid phone format"))
