import sqlite3

def init_db():
    connection=sqlite3.connect("shopping.db")
    cursor=connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        quantity INTEGER,
        price REAL,
        category TEXT
    );
    """)
    connection.commit()
    connection.close()

def add_items():
    connection = sqlite3.connect("shopping.db")
    cursor=connection.cursor()

    name=input("Enter item name: ").lower().strip()
    cursor.execute("SELECT * FROM items WHERE name = ?",(name,))
    item=cursor.fetchone()

    if item:
        print(f"An item called {name} already exists")
        edit=input("Would you like to edit it instead(yes/no): ").lower().strip()
        if edit == 'yes':
            update_items()
        connection.close()
        return

    quantity=input(f"How many {name}(s) would you like to buy: ").strip()
    while not quantity.isdigit() or int(quantity)<=0:
        print("Quantity should be a digit and greater than zero")
        quantity=input(f"How many {name}(s) would you like to buy: ").strip()
    quantity=int(quantity)
    price=input(f"Enter price for each {name}: ").strip()
    while True:
        try:
            price=float(price)
            if price <= 0:
                raise ValueError
            break
        except ValueError:
            print("Price must be a positive number")
            price=input(f"Enter price for each {name}: ").strip()

    category=input("Enter category (e.g., food, cleaning, drinks): ").lower().strip()
    while category == "":
        print("Category cannot be empty")
        category=input("Enter category: ").lower().strip()

    cursor.execute("INSERT INTO items (name, quantity, price, category) VALUES (?, ?, ?, ?)",(name, quantity, price, category))
    connection.commit()
    connection.close()
   
    print(f"✅ '{name}' added successfully to your list")

def view_items():
    connection=sqlite3.connect("shopping.db")
    cursor=connection.cursor()

    print("\nHow would you like to sort the list?")
    print("1. Name (A-Z)")
    print("2. Quantity (High → Low)")
    print("3. Category")

    choice = input("Choose sorting option (1-3): ").strip()

    if choice == '1':
        cursor.execute("SELECT * FROM items ORDER BY name ASC")
    elif choice == '2':
        cursor.execute("SELECT * FROM items ORDER BY quantity DESC")
    elif choice == '3':
        cursor.execute("SELECT * FROM items ORDER BY category ASC")
    else:
        cursor.execute("SELECT * FROM items")

    items = cursor.fetchall()

    if not items:
        print("🛒 Your list is empty\n")
        return

    print("\n========== SHOPPING LIST ==========")
    total_cost = 0
    for i in items:
        item_total = i[2] * i[3]
        total_cost += item_total
        print(f"{i[0]}. {i[1].capitalize()} - {i[2]} pcs @ {i[3]} each | Category: {i[4]} | Total: {item_total}")

    print(f"\n💰 **TOTAL COST:** {total_cost} KES")
    print("=================================\n")

    connection.close()



def search_items():
    connection=sqlite3.connect("shopping.db")
    cursor=connection.cursor()
    
    name=input("Enter item name: ").strip().lower()
    while name=="":
        print("Item name should not be empty")
        name=input("Enter item name: ").strip().lower()
    cursor.execute("SELECT * FROM items WHERE name=?",(name,))
    item=cursor.fetchone()
    
    if not item:
        print("❌ Item not found.")
        connection.close()
        return None
    print("=====Item Found=====\n")
    print(f"✅ {item[1].capitalize()} | Quantity: {item[2]} | Price: {item[3]} | Category: {item[4]}\n")

    connection.close()
    return item

def remove_item():
    item=search_items()
    if not item:
        return
    confirm = input(f"Delete '{item[1]}'? (yes/no): ").lower().strip()
    if confirm=='yes':
        connection=sqlite3.connect("shopping.db")
        cursor=connection.cursor()
        cursor.execute("DELETE FROM items WHERE id=?",(item[0],))
        connection.commit()
        connection.close()
        print("🗑️ Item deleted successfully!\n")
    else:
        print("❎ Deletion cancelled.\n")

def clear_list():
    confirm = input("Delete ALL items? (yes/no): ").lower().strip()
    if confirm == "yes":
        connection = sqlite3.connect("shopping.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM items")
        connection.commit()
        connection.close()
        print("🧹 All items cleared!")

    else:
        print("❎ Deletion cancelled.\n")

def update_items():
    item=search_items()
    if not item:
        return
    while True:
        item_id=item[0]
        connection=sqlite3.connect("shopping.db")
        cursor=connection.cursor()
        choice=input("Edit what? (name / quantity / price / category): ").lower().strip()
        while choice not in ["name", "quantity", "price", "category"]:
            print("Choose from: name, quantity, price, category")
            choice=input("Edit what? (name / quantity / price / category): ").lower().strip()

        if choice=='name':
            name=input("Enter new item name: ").lower().strip()
            while name=="":
                print("Name should not be empty")
                name=input("Enter the new item name: ").lower().strip()
            cursor.execute("UPDATE items SET name = ? WHERE id = ?",(name,item_id))
            print("✅====Name updated successfully====")
        elif choice=='quantity':
            quantity=input("Enter the new quantity: ").strip()
            while not quantity.isdigit() or  int(quantity)<=0:
                print("Quantity should be a number and should be greater than zero")
                quantity=input("Enter the new quantity: ").strip()
            quantity=int(quantity)
            cursor.execute("UPDATE items SET quantity=? WHERE id=?",(quantity,item_id))
            print("✅====Quantity updated successfully====")
        elif choice=='price':
            price=input("Enter the new price: ").strip()
            while not price.isdigit() or  int(price)<=0:
                print("Price should be a number and should be greater than zero")
                price=input("Enter the new price: ").strip()
            price=int(price)
            cursor.execute("UPDATE items SET price=? WHERE id=?",(price,item_id))
            print("✅====Price updated successfully====")
        elif choice=='category':
            category=input("Enter the new category: ").strip().lower()
            while category=="":
                print("Category should not be empty")
                category=input("Enter the new category: ").strip().lower()
            cursor.execute("UPDATE items SET category=? WHERE id=?",(category,item_id))
            print("✅====Category updated successfully====")
        connection.commit()
        connection.close()

        confirm=input("Would you like to edit more items? (yes/no): ").strip().lower()
        if confirm=='no':
            break

def main():
    init_db()
    print("========SHOPPING LIST SYSTEM========")
    while True:
        print("Choose one of the options below to proceed: ")
        print("\n1. Add an item")
        print("2. View all items")
        print("3. Search for an item")
        print("4. Update an item")
        print("5. Delete an item")
        print("6. Clear List")
        print("7.Exit\n")

        choice=input("Enter your option(1-7): ").strip()
        while choice not in['1','2','3','4','5','6','7']:
            print("Invalid choice")
            choice=input("Choose one of the options below to proceed(1-7): ").strip()
            break
        if choice == '1':
            add_items()
        elif choice=='2':
            view_items()
        elif choice=='3':
            search_items()
        elif choice=='4':
            update_items()
        elif choice=='5':
            remove_item()
        elif choice=='6':
            clear_list()
        elif choice == "7":
            print("👋 Goodbye! Your items have been saved.")
            break
  
main()