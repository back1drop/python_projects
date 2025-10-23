import os,json,hashlib,secrets
from getpass import getpass
print("Welcome to the login and registration System")
users=[]
currentuser=None
def load_users():
    global users
    if os.path.exists("login.json"):
        if os.path.getsize("login.json")>0:
            with open("login.json","r") as l:
                users=json.load(l)
        else:
            users=[]
    else:
        users=[]

def save_users():
    with open("login.json","w") as l:
        json.dump(users,l,indent=4)

def hash_pin(pin,salt):
    return hashlib.sha256((pin+salt).encode()).hexdigest()
def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()


def signup():
    while True:
        name = input("Enter your username: ").strip().lower()
        if any(u["username"] == name for u in users):
            print("A user with this name already exists. Please enter a unique username.")
        elif name == "":
            print("Username cannot be empty.")
        else:
            break
            
    pin=getpass("Enter a 4 digit pin: ").strip()
    while not pin.isdigit() or len(pin) !=4:
        print("Pin should only comprise of 4 digits only!")
        pin=getpass("Enter a 4 digit pin: ").strip()

    print("\n Set a security question for PIN recovery(example: What's your pet's name?) ")
    security_question=input("Enter your security question: ").strip()
    security_answer=input("Enter your answer: ").strip().lower()

    salt=secrets.token_hex(8)
    user={
        'username':name,
        'pin':hash_pin(pin,salt),
        'salt':salt,
        'failed_attempts':0,
        'locked':False,
        'security_question':security_question,
        'security_answer':hash_text(security_answer)

    }
    users.append(user)
    save_users()
    print("User added successfully,please proceed to login")
    login()


def login():
    global currentuser
    username=input("Enter your username: ").strip().lower()
    result=[u for u in users if u['username']==username]
    if not result:
        print(f"{username} does not exist")
        choice=input("Would you like to signup(yes/no): ").strip().lower()
        while choice not in['yes','no']:
            print("Invalid choice")
            choice=input("Would you like to signup(yes/no): ").strip().lower()
        if choice == 'yes':
            signup()
        elif choice=='no':
            print("Exitting system now")
            exit()
        return
    user=result[0]
    if user.get('locked',False):
        print("Your account is locked due to multiple failed login attempts. Please reset password or contact admin")
        return
    attempts=user.get('failed_attempts',0)
    while attempts<3:
        pin=getpass("Enter a 4 digit pin: ").strip()
        salt=user['salt']
        pin_hashed=hash_pin(pin,salt)
        if pin_hashed ==user['pin']:
            currentuser=user
            print("Login Successful!!")
            user['failed_attempts']=0
            save_users()
            dashboard(user['username'])
            break
        else:
            print("Invalid pin")
            attempts+=1
            user['failed_attempts']=attempts
            save_users()
    if attempts==3:
        print("Too many failed attempts! Your account has been locked.")
        user['locked']=True
        save_users()
        return



def reset_pin(user):
    print("=====RESET PIN=====")
    print(f"Security question: {user['security_question']}")    
    answer=input("Enter answer: ").strip().lower()
    if hash_text(answer) == user['security_answer']:
        new_pin = getpass("Enter your new 4-digit PIN: ").strip()
        while not new_pin.isdigit() or len(new_pin) != 4:
            print("PIN must be exactly 4 digits.")
            new_pin = getpass("Enter your new 4-digit PIN: ").strip()

        confirm = getpass("Confirm new PIN: ").strip()
        if new_pin != confirm:
            print("PINs do not match. Try again.")
            return
        new_salt=secrets.token_hex(8)

        user['pin'] = hash_pin(new_pin,new_salt)
        user['salt']=new_salt
        user['failed_attempts']=0
        user['locked']=False
        save_users()
        print("✅ Your PIN has been successfully reset. Please log in again.")
        login()
    else:
        print("❌ Incorrect answer. Cannot reset PIN.")


def unlocker(): 
    username=input("Enter your username to reset Pin: ").strip().lower()
    user=next((u for u in users if u['username']==username),None)
    if not user:
        print("User not found.")
        return
    reset_pin(user)


def change_pin():
    global currentuser
    if not currentuser:
        print("No user logged in.")
        return
    
    while currentuser:
        current_pin=getpass("Enter your current pin: ")
        salt=currentuser['salt']

        if hash_pin(current_pin,salt) != currentuser['pin']:
            print("Incorrect current PIN. Cannot change PIN.")
            return

        new_pin = getpass("Enter your new 4-digit PIN: ").strip()
        new_salt=secrets.token_hex(8)
        while not new_pin.isdigit() or len(new_pin) != 4:
            print("PIN must be exactly 4 digits.")
            new_pin = getpass("Enter your new 4-digit PIN: ").strip()

        confirm_pin = getpass("Confirm your new PIN: ").strip()
        if new_pin != confirm_pin:
            print("PINs do not match. Try again.")
            return

        currentuser['pin'] = hash_pin(new_pin,new_salt)
        currentuser['salt']=new_salt
        save_users()
        print("✅ Your PIN has been updated successfully!")


def dashboard(username):
    global currentuser
    print(f"Welcome ,{username}!")
    while True:
        print("1. Change Pin")
        print("2. Logout")
        print("3. Exit program")
        choice=input("What would you like to do(1-3): ").strip()
        while choice not in['1','2','3']:
            print("Invalid choice")
            choice=input("What would you like to do(1-3): ").strip()
        if choice=='1':
            change_pin()

        elif choice == '2':
            print("Logging out now byeeeee,,,,,")
            currentuser=None
            main()
            break
        elif choice=='3':
            currentuser=None
            print("Goodbye")
            exit()

def main():
    load_users()
    while True:
        print("Choose one of the options below to proceed")
        print("1. Login")
        print("2. Signup")
        print("3. Reset")
        print("4. Exit")
        choice=input("Enter your option(1-4): ").strip().lower()
        while choice not in["1","2","3","4"]:
            print("Invalid choice")
            choice=input("Enter your option(1-4): ").strip()
        
        if choice =='1':
            login()
        elif choice =='2':
            signup()
        elif choice == '3':
            unlocker()

        elif choice =='4':
            print("Goodbye")
            break

main()