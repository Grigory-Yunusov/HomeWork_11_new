from collections import UserDict
import string

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):

    def __init__(self, value, name):
        super().__init__(value)
        self.name = name


class Phone(Field, Exception):
    def __init__(self, value, phones):
        super().__init__(value)
        if len(phones) != 10:
            raise ValueError("Phone mast be 10 sibl!!!")
        self.phones = phones







class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def add_phone(self, phone):
        self.phones.append(phone)

    pass

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    pass