import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# ---------------- DATABASE ----------------
def init_db():
    connection = sqlite3.connect("shopping.db")
    cursor = connection.cursor()
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


# ---------------- GUI FUNCTIONS ----------------
def add_item():
    name = name_entry.get().lower().strip()
    quantity = quantity_entry.get().strip()
    price = price_entry.get().strip()
    category = category_entry.get().lower().strip()

    if name == "" or category == "":
        messagebox.showerror("Error", "Name and Category cannot be empty")
        return

    if not quantity.isdigit() or int(quantity) <= 0:
        messagebox.showerror("Error", "Quantity must be a positive integer")
        return

    try:
        price = float(price)
        if price <= 0:
            raise ValueError
    except:
        messagebox.showerror("Error", "Price must be a positive number")
        return

    connection = sqlite3.connect("shopping.db")
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO items(name, quantity, price, category) VALUES(?,?,?,?)",
                       (name, int(quantity), price, category))
        connection.commit()
        messagebox.showinfo("Success", f"{name} added successfully!")
        view_items()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Item already exists")
    finally:
        connection.close()


def view_items():
    for row in tree.get_children():
        tree.delete(row)

    connection = sqlite3.connect("shopping.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    connection.close()

    for item in items:
        item_total = item[2] * item[3]
        tree.insert("", tk.END, values=(item[0], item[1], item[2], item[3], item[4], item_total))


def delete_item():
    selected = tree.selection()
    if not selected:
        messagebox.showerror("Error", "Please select an item to delete")
        return

    item_id = tree.item(selected)["values"][0]

    connection = sqlite3.connect("shopping.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM items WHERE id=?", (item_id,))
    connection.commit()
    connection.close()

    view_items()
    messagebox.showinfo("Deleted", "Item deleted successfully")


def update_item():
    selected = tree.selection()
    if not selected:
        messagebox.showerror("Error", "Select an item to update")
        return

    item_id = tree.item(selected)["values"][0]
    name = name_entry.get().lower().strip()
    quantity = quantity_entry.get().strip()
    price = price_entry.get().strip()
    category = category_entry.get().strip().lower()

    if name == "" or category == "":
        messagebox.showerror("Error", "Name and Category cannot be empty")
        return

    if not quantity.isdigit() or int(quantity) <= 0:
        messagebox.showerror("Error", "Quantity must be a positive integer")
        return

    try:
        price = float(price)
        if price <= 0:
            raise ValueError
    except:
        messagebox.showerror("Error", "Price must be a positive number")
        return

    connection = sqlite3.connect("shopping.db")
    cursor = connection.cursor()
    cursor.execute("""
    UPDATE items
    SET name=?, quantity=?, price=?, category=?
    WHERE id=?
    """, (name, int(quantity), price, category, item_id))

    connection.commit()
    connection.close()
    view_items()
    messagebox.showinfo("Updated", "Item updated successfully")


# ---------------- GUI DESIGN ----------------
init_db()
window = tk.Tk()
window.title("Shopping List System")
window.geometry("750x450")

# Input fields
tk.Label(window, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

tk.Label(window, text="Quantity:").grid(row=1, column=0)
quantity_entry = tk.Entry(window)
quantity_entry.grid(row=1, column=1)

tk.Label(window, text="Price:").grid(row=2, column=0)
price_entry = tk.Entry(window)
price_entry.grid(row=2, column=1)

tk.Label(window, text="Category:").grid(row=3, column=0)
category_entry = tk.Entry(window)
category_entry.grid(row=3, column=1)

# Buttons
tk.Button(window, text="Add Item", command=add_item).grid(row=4, column=0, pady=10)
tk.Button(window, text="Update Item", command=update_item).grid(row=4, column=1)
tk.Button(window, text="Delete Item", command=delete_item).grid(row=4, column=2)

# Table (Treeview)
columns = ("ID", "Name", "Qty", "Price", "Category", "Total")
tree = ttk.Treeview(window, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=5, column=0, columnspan=5, sticky="nsew")

# Load data on startup
view_items()

window.mainloop()
