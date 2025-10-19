
import json
import os

print("Welcome to my bank account system !!")

users=[]
current_user=None

def load_users():
    global users
    if os.path.exists("users.json"):
        with open("users.json","r") as file:
            users=json.load(file)
    else:
        users=[]

def save_users():
    with open("users.json","w") as file:
        json.dump(users,file,indent=4)
    


def signup():
    username=input("Enter your username: ").lower().strip()

    if any(u["username"] == username for u in users):
        print("❌ Username already exists! Try logging in.")
        return
    
    pin=input("Enter your 4-digit pin: ").strip()
    if not pin.isdigit() or len(pin) !=4:
        print("❌ Invalid pin.It must contain exactly 4 digits.")
        return
    
    try:
        balanc=int(input("Deposit any amount to activate your account: "))
        if balanc<=0:
            print("❌ Deposit must be greater than zero")
            return
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")
        return
    
    new_user = {
        "username": username,
        "pin": pin,
        "balance": balanc
    }

    users.append(new_user)
    save_users()
    print(f"✅ User '{username}' added successfully with Ksh.{balanc} balance.")



def login():
    global current_user
    username=input("Please enter your username: ").lower().strip()
    result=[u for u in users if u["username"] == username]

    if not result:
        print("❌ Username does not exist")
        choice=input("Would you like to sign up?(yes/no): ").lower().strip()
        if choice == "yes":
            signup()
        return
    user=result[0]
    pin=input("Please enter a 4 digit pin: ").strip()
    if pin == user['pin']:
        current_user=user
        print(f"Welcome back {current_user['username']}!!")
        account_menu()
    else:
        print("Incorrect pin")

def account_menu():
    global current_user
    while current_user:
        print("\n 📃Please select an action to perform from the menu below: ")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Check Balance")
        print("4. Exit")
        action=input("Enter your choice(1-4): ").strip()
        while action not in["1","2","3","4"]:
            print("Invalid choice please re-enter again")
            action=input("Enter your choice(1-4): ").strip()
            break
    
        if action=="1":
            withdraw()
        elif action=="2":
            deposit()
        elif action=="3":
            check_balance()
        elif action=="4":
            print(f"👋 Logging out {current_user['username']}...\n")
            current_user = None
            break


def withdraw():
    global current_user
    try:
        amount=int(input("Please enter the amount you wish to withdraw: "))
        if amount>0:
            if current_user["balance"]>amount:
                current_user["balance"]-=amount
                save_users()
                print(f"Success Ksh.{amount} has  been withdrawn!!")
                print(f"Your new balance is Ksh.{current_user['balance']}")
                
            else:
                print("You have insufficient funds")
        else:
            print("Invalid amount entered!!")
    except ValueError:
        print("❌ Please enter a valid numberr")



def deposit():
    global current_user
    try:
        added=int(input("Please enter the amount you wish to deposit: "))
        if added<=0:
            print("❌ Deposit must be greater than zero.")
            return
        current_user['balance']+=added
        save_users()
        print(f"Success Ksh.{added} has  been deposited into your account!!")
        print(f"Your current balance is Ksh.{current_user['balance']}")
    except ValueError:
        print("❌ Please enter a valid number.")


def check_balance():
    global current_user
    print(f"Your current balance is Ksh.{current_user['balance']}")


def main():
    load_users()

    while True:
        print("Choose one of the options below to proceed")
        print("1. Login")
        print("2. Signup")
        print("3. Exit")

        choice=input("Enter your choice(1-3): ").strip()
        while choice not in ['1','2','3']:
            print("Invalid choice")
            choice=input("Enter your choice(1-3): ").strip()
            break

        if choice=="1":
            login()
        elif choice=="2":
            signup()
        elif choice=="3":
            print("Goodbye👋🏾")
            break

main()





    
   








    
