import sqlite3

# ================= DATABASE SETUP =================
con = sqlite3.connect("library.db")
cur = con.cursor()

#  Categories table
cur.execute("""
CREATE TABLE IF NOT EXISTS Categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT UNIQUE
)
""")

#  Books table
cur.execute("""
CREATE TABLE IF NOT EXISTS Books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT UNIQUE,
    Author TEXT,
    PublishedYear INTEGER,
    Category TEXT,
    Borrowed INTEGER DEFAULT 0
)
""")
con.commit()

# Insert your original categories (only once)
default_categories = [
 'romance', 'mystery', 'fantasy', 'science fiction', 'horror',
 'historical fiction', 'thriller', 'kids'
]

for cat in default_categories:
    try:
        cur.execute("INSERT INTO Categories (Name) VALUES (?)", (cat,))
    except:
        pass
con.commit()

def choose_category():
    cur.execute("SELECT * FROM Categories")
    cats = cur.fetchall()

    print("\nPlease choose your book category:")
    for cid, name in cats:
        print(f"{cid}. {name.capitalize()}")

    choice = input("Enter category number: ").strip()
    while not choice.isdigit() or int(choice) not in [c[0] for c in cats]:
        print(f"{choice} is not a valid option.")
        choice = input("Enter category number: ").strip()

    cur.execute("SELECT Name FROM Categories WHERE id=?", (choice,))
    return cur.fetchone()[0]


# ================= CORE FUNCTIONS =================

def add_book():
    title = input("Enter book title: ").capitalize().strip()
    author = input("Enter author name: ").capitalize().strip()
    year = input("Enter published year: ").strip()

    while not year.isdigit():
        print("Year must be a number")
        year = input("Enter published year: ").strip()

    category = choose_category()

    try:
        cur.execute("INSERT INTO Books (Title, Author, PublishedYear, Category) VALUES (?, ?, ?, ?)",
                    (title, author, int(year), category))
        con.commit()
        print("\n✅ Book added successfully!\n")
    except sqlite3.IntegrityError:
        print("\n❌ A book with that title already exists.\n")


def view_books():
    cur.execute("SELECT * FROM Books")
    books = cur.fetchall()

    if not books:
        print("\n📭 No books found.\n")
        return

    print("\n====== Books List ======")
    for bid, t, a, y, c, b in books:
        status = "Borrowed" if b else "Available"
        print(f"{bid}. {t} | {a} | {y} | {c.capitalize()} | {status}")
    print()


def search_book():
    choices = ['Title', 'Author', 'PublishedYear', 'Category']
    print("\nSearch by:")
    for i, c in enumerate(choices, start=1):
        print(f"{i}. {c}")

    search = input(f"Choose filter (1-{len(choices)}): ").strip()
    while not search.isdigit() or int(search) not in range(1, len(choices)+1):
        print("Invalid choice.")
        search = input(f"Choose filter (1-{len(choices)}): ").strip()

    search = int(search)
    value = input("Enter search value: ").capitalize().strip()

    column = choices[search-1]
    cur.execute(f"SELECT * FROM Books WHERE {column} LIKE ?", ('%' + value + '%',))
    books = cur.fetchall()

    if books:
        print("\nFound Book(s):")
        for bid, t, a, y, c, b in books:
            status = "Borrowed" if b else "Available"
            print(f"{bid}. {t} | {a} | {y} | {c.capitalize()} | {status}")
        print()
        return books
    else:
        print("❌ No matches found.\n")
        return None


def delete_book():
    books = search_book()
    if not books:
        return

    ids = [b[0] for b in books]
    pos = input(f"Enter the ID of the book to delete: ").strip()

    while not pos.isdigit() or int(pos) not in ids:
        print("Invalid ID.")
        pos = input("Enter book ID: ").strip()

    cur.execute("DELETE FROM Books WHERE id=?", (pos,))
    con.commit()
    print("🗑️ Book deleted successfully!\n")


def edit_book():
    books = search_book()
    if not books:
        return

    ids = [b[0] for b in books]
    pos = input("Enter the ID of the book to edit: ").strip()

    while not pos.isdigit() or int(pos) not in ids:
        print("Invalid ID.")
        pos = input("Enter book ID: ").strip()

    fields = ["Title", "Author", "PublishedYear", "Category"]
    print("\nWhat would you like to edit?")
    for i, f in enumerate(fields, start=1):
        print(f"{i}. {f}")

    part = input("Choose option: ").strip()
    while not part.isdigit() or int(part) not in range(1, len(fields)+1):
        print("Invalid.")
        part = input("Choose option: ").strip()

    part = int(part)
    new_value = input("Enter new value: ").strip()

    if fields[part-1] == "PublishedYear":
        while not new_value.isdigit():
            print("Year must be a number.")
            new_value = input("Enter published year: ").strip()

    if fields[part-1] == "Category":
        new_value = choose_category()

    cur.execute(f"UPDATE Books SET {fields[part-1]}=? WHERE id=?", (new_value, int(pos)))
    con.commit()
    print("✅ Book updated successfully!\n")


def borrow_book():
    books = search_book()
    if not books:
        return

    ids = [b[0] for b in books]
    pos = input("Enter book ID to borrow: ").strip()
    while not pos.isdigit() or int(pos) not in ids:
        pos = input("Enter valid book ID: ")

    cur.execute("SELECT Borrowed FROM Books WHERE id=?", (pos,))
    status = cur.fetchone()[0]

    if status == 1:
        print("❌ This book is already borrowed.\n")
    else:
        cur.execute("UPDATE Books SET Borrowed=1 WHERE id=?", (pos,))
        con.commit()
        print("✅ Book borrowed successfully!\n")


def return_book():
    books = search_book()
    if not books:
        return

    ids = [b[0] for b in books]
    pos = input("Enter book ID to return: ").strip()
    while not pos.isdigit() or int(pos) not in ids:
        pos = input("Enter valid book ID: ")

    cur.execute("UPDATE Books SET Borrowed=0 WHERE id=?", (pos,))
    con.commit()
    print("✅ Book returned successfully!\n")


# ================= MAIN MENU =================
def main():
    while True:
        print("""
========= LIBRARY SYSTEM =========
1. Add Book
2. View Books
3. Search Book
4. Edit Book
5. Delete Book
6. Borrow Book
7. Return Book
8. Exit
""")

        choice = input("Enter option (1-8): ").strip()

        if choice == '1': add_book()
        elif choice == '2': view_books()
        elif choice == '3': search_book()
        elif choice == '4': edit_book()
        elif choice == '5': delete_book()
        elif choice == '6': borrow_book()
        elif choice == '7': return_book()
        elif choice == '8':
            print("👋 Goodbye!")
            break
        else:
            print("Invalid option.\n")

main()
