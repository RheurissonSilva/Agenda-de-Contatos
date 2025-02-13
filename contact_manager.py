import json
from abc import ABC, abstractmethod

class Contact(ABC):
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    @abstractmethod
    def get_contact_type(self):
        pass

    def to_dict(self):
        return {
            "type": self.get_contact_type(),
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }

class PersonalContact(Contact):
    def __init__(self, name, phone, email, birthday):
        super().__init__(name, phone, email)
        self.birthday = birthday

    def get_contact_type(self):
        return "personal"

    def to_dict(self):
        data = super().to_dict()
        data["birthday"] = self.birthday
        return data

class BusinessContact(Contact):
    def __init__(self, name, phone, email, company):
        super().__init__(name, phone, email)
        self.company = company

    def get_contact_type(self):
        return "business"

    def to_dict(self):
        data = super().to_dict()
        data["company"] = self.company
        return data

class ContactManager:
    def __init__(self, filename="contacts.txt"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                contacts = []
                for item in data:
                    if item["type"] == "personal":
                        contacts.append(PersonalContact(item["name"], item["phone"], item["email"], item["birthday"]))
                    elif item["type"] == "business":
                        contacts.append(BusinessContact(item["name"], item["phone"], item["email"], item["company"]))
                return contacts
        except FileNotFoundError:
            return []

    def save_contacts(self):
        with open(self.filename, "w") as file:
            json.dump([contact.to_dict() for contact in self.contacts], file)

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def update_contact(self, index, contact):
        self.contacts[index] = contact
        self.save_contacts()

    def delete_contact(self, index):
        del self.contacts[index]
        self.save_contacts()

    def get_contacts(self):
        return self.contacts

