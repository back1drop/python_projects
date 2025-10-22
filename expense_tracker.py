import datetime,json,os
expenses=[]
CATEGORIES = {
    "1": "🍔 Food & Dining",
    "2": "🚗 Transport",
    "3": "🛒 Shopping",
    "4": "🏥 Health & Medical",
    "5": "✈ Travelling",
    "6": "🏫 Education",
    "7": "🎥 Entertainment",
    "8": "💡 Bills & Utilities",
    "9": "Others"
}
def load_expenses():
    global expenses
    if os.path.exists("expenses.json"):
        if os.path.getsize("expenses.json")>0:
            with open("expenses.json","r") as e:
                expenses=json.load(e)
        else:
            expenses=[]
    else:
        expenses=[]

def save_expense():
    with open("expenses.json","w") as e:
        json.dump(expenses,e,indent=4,default=str)

def add_expense():
    expense_name = input("Please enter expense name: ").strip().lower()
    cost = input(f"Please enter amount spent on {expense_name}: ")
    while not cost.isdigit():
        print("Cost should only be a number!!")
        cost = input(f"Please enter amount spent on {expense_name}: ")

    print("\nPlease select the category in which the expense falls under:")
    for key, value in CATEGORIES.items():
        print(f"{key}. {value}")
    category = input("Please enter the chosen category (1-9): ").strip()

    while category not in CATEGORIES:
        print("Invalid input. Please try again!!")
        category = input("Please enter the chosen category (1-9): ").strip()

    date = datetime.datetime.now().strftime("%m/%d/%Y")
    new_expense = {
        "expense_name": expense_name,
        "cost": cost,
        "category": CATEGORIES[category],
        "date": date
    }
    expenses.append(new_expense)
    save_expense()
    print("✅ Expense added successfully!\n")


def view_expense():
    if not expenses:
        print("No expenses found\n")
        return
    print("\n======EXPENSES======")
    for i,expense in enumerate(expenses,start=1):
        print(f"{i}. Name: {expense['expense_name']} | cost: {expense['cost']} | Category: {expense['category']} | date: {expense['date']}")
    print()


def filter_expenses():
    print("You can filter using 'date' or 'category' ")
    filterr=input("What do you want to filter using(date or category:" \
    ")").lower().strip()
    while filterr not in ['date','category']:
        print("Please enter a valid filter")
        filterr=input("What do you want to filter using(date or category:" \
    ")").lower().strip()
    
   
    if filterr=='date':
        datee=input("Enter the date (mm/dd/yy): ").strip()
        result = [e for e in expenses if e["date"] == datee]
    else:
        category=input("Enter the category to use: ").strip().lower()
        result = [e for e in expenses if e["category"].lower() == category]
        if result:
            print("\nFound expense(s):")
            for i, c in enumerate(result, start=1):
                print(f"{i}. Name: {c['expense_name']} | Cost: {c['cost']} | Category: {c['category']} | Date: {c['date']}")
            print()
            return result 
        else:
            print("❌ No matching expense found.\n")
            return None
    

def delete_expense():
    expense=filter_expenses()
    if not expense:
        return
    index=int(input("Enter the number of the expense you would like to delete: "))
    if 0 < index <= len(expense):
        expensed=expense[index-1]
        confirm=input(f"Are you sure you want to delete {expensed['expense_name']}? (yes/no): ").strip().lower()
        if confirm == 'yes':
            expenses.remove(expensed)
            save_expense()
            print("🗑️ Expense deleted successfully!\n")
        else:
            print("❎ Deletion cancelled.\n")
    else:
        print("Invalid input")


def edit_expense():
    expense=filter_expenses()
    if not expense:
        return
    index=int(input("Enter the number of the expense you would like to edit: "))
    if 0<index<=len(expense):
        expensed=expense[index-1]
        edit=input("Would you like to edit 'name','cost': ").strip().lower()
        while edit not in['name','cost']:
            print("Invalid input")
            edit=input("Would you like to edit 'name','cost': ").strip().lower()
        if edit =='name':
            name=input("Enter your new name: ").strip().lower()
            expensed['expense_name']=name
            print("Name updated successfully!!")
        else:
            cost=input("Enter your new cost: ").strip()
            while not cost.isdigit():
                print("Cost should only be a number!!")
                cost=input("Enter your new cost: ").strip()
            expensed['cost']=cost
            print("Cost updated successfully!!")
        save_expense()
            
    else:
        print("Invalid input")


def main():
    load_expenses()
    while True:    
        print("Select an option below to proceed: ")
        print("1. Add expense")
        print("2. Edit expense")
        print("3. Delete expense")
        print("4. Filter expenses")
        print("5. View expenses")
        print("6.Exit")
        option=input("Enter your select option(1-6): ").strip()
        while option not in ["1","2","3","4","5","6"]:
            print("Invalid input")
            option=input("Enter your select option(1-6): ").strip()
        if option=='1':
            add_expense()
        elif option=='2':
            edit_expense()
        elif option=='3':
            delete_expense()
        elif option=='4':
            filter_expenses()
        elif option=='5':
            view_expense()
        elif option=='6':
            print("Goodbye exitting now!!!")
            break

main()  