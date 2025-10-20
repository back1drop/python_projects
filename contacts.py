import json
import os
contacts=[]
print("Welcome to your contact book:")
def load_contacts():
    global contacts
    if os.path.exists("contacts.json"):
        if os.path.getsize("contacts.json")>0:
            with open ("contacts.json","r") as c:
                contacts=json.load(c)
        else:
            contacts=[]
    else:
        contacts=[]

def save_contacts():
    with open("contacts.json","w") as c:
        json.dump(contacts,c,indent=4)

def add_contacts():
    name = input("Enter contact name: ").strip().lower()
    email = input("Enter email: ").strip().lower()
    number = input("Enter phone number: ").strip()

    while not number.isdigit() or len(number)!=10:
        print("❌ Invalid phone number.It must contain exactly 10 digits.")
        number=input("Enter phone number: ").strip().lower()
        
    if any (c["phone number"] == number for c in contacts):
        print("❌ Phone already exists already exists!")
        return
    
    new_phone={
        'name':name,
        'email':email,
        'phone number':number
    }
    contacts.append(new_phone)
    save_contacts()
    print("Contact added successfully")

def view_contacts():
    if not contacts:
        print("📭 No contacts found.\n")
        return
    print("\n======Contact List======")
    for i,c in enumerate(contacts,start=1):
        print(f"{i}. Name: {c['name']} | Email: {c['email']} | Phone: {c['phone number']}")
    print()


def search_contacts():
    choice=input("Search by 'phone' or 'name': ").strip().lower()

    while choice not in ['phone','name']:
        print("Invalid inputtt!!!Try again.")
        choice=input("Search by 'phone' or 'name': ").strip().lower()
        
    if choice == "phone":
        num = input("Enter phone number: ").strip()
        result = [c for c in contacts if c["phone number"] == num]
    else:
        name = input("Enter name: ").strip().lower()
        result = [c for c in contacts if c["name"] == name]

    if result:
        print("\nFound contact(s):")
        for c in result:
            print(f"Name: {c['name']} | Email: {c['email']} | Phone: {c['phone number']}")
        print()
        return result[0] 
    else:
        print("❌ No matching contact found.\n")
        return None

def delete_contact():
    contact=search_contacts()
    if not contact:
        return
    confirm=input(f"Are you sure you want to delete {contact['name']}? (yes/no): ").strip().lower()
    if confirm=='yes':
        contacts.remove(contact)
        save_contacts()
        print("🗑️ Contact deleted successfully!\n")
    else:
        print("❎ Deletion cancelled.\n")
    

def update_contact():
    contact=search_contacts()
    if not contact:
        return
    wish=input("What do you wish to change(phone ,email or name)?: ").strip().lower()
    while wish not in['phone','email','name']:
        print("Invalid choice")
        wish=input("What do you wish to change(phone ,email or name)?: ").strip().lower()

    if wish == "phone":
        num = input("Enter the new phone number (10 digits): ").strip()
        while not num.isdigit() or len(num) != 10:
            print("❌ Invalid phone number. Must be exactly 10 digits.")
            num = input("Enter the new phone number: ").strip()
        contact["phone number"] = num
        print("✅ Phone number updated successfully!")

    elif wish == "name":
        name = input("Enter the new name: ").strip().lower()
        contact["name"] = name
        print("✅ Name updated successfully!")

    elif wish == "email":
        email = input("Enter the new email: ").strip().lower()
        contact["email"] = email
        print("✅ Email updated successfully!")

    save_contacts()
    print()


def main():
    load_contacts()
    while True:
        
        print("Choose one of the options below to proceed: ")
        print("1. Add a contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Update a contact")
        print("5. Delete a contact")
        print("6.Exit")

        choice=input("Enter your option(1-6): ").strip()
        while choice not in['1','2','3','4','5','6']:
            print("Invalid choice")
            choice=input("Choose one of the options below to proceed(1-6): ").strip()
            break
        if choice == '1':
            add_contacts()
        elif choice=='2':
            view_contacts()
        elif choice=='3':
            search_contacts()
        elif choice=='4':
            update_contact()
        elif choice=='5':
            delete_contact()
        elif choice == "6":
            print("👋 Goodbye! Your contacts have been saved.")
            break
  
main()