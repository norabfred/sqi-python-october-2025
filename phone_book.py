# Project Overview:
# Create a simple phone book manager where users can add, view, update, and delete contacts
# in a file named `phone_book.py`.

# Requirements:
# Data Storage: Use a list of dictionaries to store contact information. Each contact should have the following attributes:
# Name (string)
# Phone Number (string)
# Favorite (boolean)
# Functions/Actions:
# add_contact(): Add a new contact to the phone book.
# view_contacts(): Display all the contacts in the phone book.
# update_contact(phone_number): Update the information of a contact given their phone number.
# delete_contact(phone_number): Remove a contact from the phone book using their phone
# number.
# search_contact(name): Search for a contact by their exact name.
# mark_favorite(phone_number): Mark a contact as a favorite.
# unmark_favorite(phone_number): Unmark a contact as a favorite.
# User Interface: Use a loop to display a menu and prompt the user for an action above until they choose to exit. Assume the user always inputs the correct data types.

# phone_book.py
# Simple phone book manager using a list of dictionaries
#--------------------------------ANSWER-------------------------------------------------------------

phone_book = []

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    # assume correct data types and unique phone numbers for simplicity
    contact = {"Name": name, "Phone Number": phone, "Favorite": False}
    phone_book.append(contact)
    print(f"Contact for {name} added.")

def view_contacts():
    if not phone_book:
        print("Phone book is empty.")
        return
    else:
        for contact in phone_book:
            fav = "★" if c["Favorite"] else " "
            print(f"{i}. {fav} Name: {c['Name']} | Phone: {c['Phone Number']}")

def find_contact_index_by_phone(phone_number):
    for index, contact in enumerate(phone_book):
        if contact["Phone Number"] == phone_number:
            return index
    return None

def update_contact(phone_number):
    idx = find_contact_index_by_phone(phone_number)
    if idx is None:
        print("No contact found with that phone number.")
        return
    contact = phone_book[idx]
    print(f"Updating contact: {contact['Name']} ({contact['Phone Number']})")
    new_name = input("Enter new name (leave blank to keep current): ").strip()
    new_phone = input("Enter new phone number (leave blank to keep current): ").strip()
    if new_name:
        contact["Name"] = new_name
    if new_phone:
        contact["Phone Number"] = new_phone
    phone_book[idx] = contact
    print("Contact updated.")

def delete_contact(phone_number):
    idx = find_contact_index_by_phone(phone_number)
    if idx is None:
        print("No contact found with that phone number.")
        return
    removed = phone_book.pop(idx)
    print(f"Removed contact: {removed['Name']}.")

def search_contact(name):
    matches = [c for c in phone_book if c["Name"] == name]
    if not matches:
        print("No contact found with that exact name.")
        return
    print("Search results:")
    for c in matches:
        fav = "★" if c["Favorite"] else " "
        print(f"Name: {c['Name']} | Phone: {c['Phone Number']} | Favorite: {fav}")

def mark_favorite(phone_number):
    idx = find_contact_index_by_phone(phone_number)
    if idx is None:
        print("No contact found with that phone number.")
        return
    phone_book[idx]["Favorite"] = True
    print(f"{phone_book[idx]['Name']} marked as favorite.")

def unmark_favorite(phone_number):
    idx = find_contact_index_by_phone(phone_number)
    if idx is None:
        print("No contact found with that phone number.")
        return
    phone_book[idx]["Favorite"] = False
    print(f"{phone_book[idx]['Name']} unmarked as favorite.")

def print_menu():
    print("\nPhone Book Menu")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Update contact (by phone number)")
    print("4. Delete contact (by phone number)")
    print("5. Search contact (by exact name)")
    print("6. Mark favorite (by phone number)")
    print("7. Unmark favorite (by phone number)")
    print("8. Exit")

def main():
    while True:
        print_menu()
        choice = input("Choose an option (1-8): ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            phone = input("Enter phone number to update: ").strip()
            update_contact(phone)
        elif choice == "4":
            phone = input("Enter phone number to delete: ").strip()
            delete_contact(phone)
        elif choice == "5":
            name = input("Enter exact name to search: ").strip()
            search_contact(name)
        elif choice == "6":
            phone = input("Enter phone number to mark favorite: ").strip()
            mark_favorite(phone)
        elif choice == "7":
            phone = input("Enter phone number to unmark favorite: ").strip()
            unmark_favorite(phone)
        elif choice == "8":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
#--------------------------------ANSWER-------------------------------------------------------------
