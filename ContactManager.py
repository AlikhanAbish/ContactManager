import json
from Contact import Contact


class ContactManager(Contact):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __init__(self, filename):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                contacts = json.load(file)
        except FileNotFoundError:
            contacts = []
        return contacts

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, surname, phone, email):
        contact = {
            'name': name,
            'surname': surname,
            'phone': phone,
            'email': email
        }
        self.contacts.append(contact)
        self.save_contacts()

    def delete_contact(self, name, surname):
        for contact in self.contacts:
            if contact['name'] == name and contact['surname'] == surname:
                self.contacts.remove(contact)
                self.save_contacts()
                return True
        return False

    def display_contacts(self):
        if self.contacts:
            print("Contacts:")
            for contact in self.contacts:
                print(f"Name: {contact['name']}, Surname: {contact['surname']}, Phone: {contact['phone']}, Email: {contact['email']}")
        else:
            print("No contacts available.")
