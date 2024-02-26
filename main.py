from ContactManager import ContactManager


if __name__ == "__main__":
    contact_manager = ContactManager("contacts.json")

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Display Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_manager.add_contact(name, surname, phone, email)
            print("Contact added successfully.")
        elif choice == '2':
            name = input("Enter name to delete: ")
            surname = input("Enter surname to delete: ")
            if contact_manager.delete_contact(name, surname):
                print("Contact deleted successfully.")
            else:
                print("Contact not found.")
        elif choice == '3':
            query = input("Enter name or surname: ")
            found_contacts = contact_manager.search_contact(query)
            if found_contacts:
                print("Found Contacts:")
                for contact in found_contacts:
                    print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            else:
                print("No contacts found.")

        elif choice == '4':
            name = input("Enter name of contact to edit: ")
            surname = input("Enter surname of contact to edit: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email address: ")
            if contact_manager.edit_contact(name, surname, new_phone, new_email):
                print("Contact edited successfully.")
            else:
                print("Contact not found.")
        elif choice == '5':
            contact_manager.display_contacts()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
