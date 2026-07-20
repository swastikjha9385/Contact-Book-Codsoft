contacts = []


def add_contacts():
    print("\n--- ADD NEW CONTACT ---")

    name = input("Enter Name: ").strip()
    if not name:
        print("❌ Name cannot be empty.\n")
        return

    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("✅ Contact added successfully!\n")


def view_contacts():
    print("\n--- CONTACT LIST ---")

    if not contacts:
        print("No contacts found.\n")
        return

    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} - {contact['phone']}")
    print()


def search_contact():
    print("\n--- SEARCH CONTACT ---")

    search_term = input("Enter Name or Phone Number: ").lower()

    found = False

    for contact in contacts:
        if search_term in contact["name"].lower() or search_term in contact["phone"]:
            print("\n📞 Contact Found")
            print(f"Name    : {contact['name']}")
            print(f"Phone   : {contact['phone']}")
            print(f"Email   : {contact['email']}")
            print(f"Address : {contact['address']}\n")
            found = True

    if not found:
        print("❌ Contact not found.\n")


def update_contact():
    print("\n--- UPDATE CONTACT ---")

    name = input("Enter the Name of the Contact to Update: ").lower()

    for contact in contacts:

        if contact["name"].lower() == name:

            print("Leave blank to keep current value.")

            new_phone = input(f"New Phone ({contact['phone']}): ")
            new_email = input(f"New Email ({contact['email']}): ")
            new_address = input(f"New Address ({contact['address']}): ")

            if new_phone:
                contact["phone"] = new_phone

            if new_email:
                contact["email"] = new_email

            if new_address:
                contact["address"] = new_address

            print("✅ Contact updated successfully!\n")
            return

    print("❌ Contact not found.\n")


def delete_contact():
    print("\n--- DELETE CONTACT ---")

    name = input("Enter the Name of the Contact to Delete: ").lower()

    for contact in contacts:

        if contact["name"].lower() == name:
            contacts.remove(contact)
            print("🗑️ Contact deleted successfully!\n")
            return

    print("❌ Contact not found.\n")


def main():

    while True:

        print("========== CONTACT BOOK ==========")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nChoose an option (1-6): ")

        if choice == "1":
            add_contacts()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            print("\n👋 Exiting Contact Book. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()