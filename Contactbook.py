# Step 1: Define list to store contacts
contacts = []

# Step 2: Define functions for each feature

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    
    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    contacts.append(contact)
    print(f"Contact {name} added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contacts():
    search_name = input("Enter the name to search: ")
    found_contacts = [contact for contact in contacts if search_name.lower() in contact['name'].lower()]
    
    if not found_contacts:
        print("No contacts found.")
    else:
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def delete_contact():
    search_name = input("Enter the name to delete: ")
    global contacts
    contacts = [contact for contact in contacts if search_name.lower() not in contact['name'].lower()]
    print(f"Contacts with the name {search_name} deleted.")

def main_menu():
    while True:
        print("\nContact Book Menu")
        print("1. Add a contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Delete a contact")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Step 3: Run main menu
if __name__ == "__main__":
    main_menu()
    
