from ContactManager import ContactManager


if __name__ == '__main__':

    contact_manager = ContactManager("contacts.json")

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Display Contacts")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_manager.add_contact(name, surname, phone, email)
            print("Contact added successfully.")
        elif choice == '2':
            print("Please enter name and surname to delete:")
            name = input("Name: ")
            surname = input("Surname: ")
            if contact_manager.delete_contact(name, surname):
                print("Contact:", name, surname, "deleted successfully.")
            else:
                print("Contact not found.")
        elif choice == '3':
            contact_manager.display_contacts()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")