def add_book():
    book_name=input("Enter book name: ").capitalize().strip()
    author=input("Enter author name: ").capitalize().strip()
    published_year=input("Enter published year")
    categories=[ 'romance', 'mystery', 'fantasy', 'science fiction', 'horror', 'historical fiction',  'thriller','kids']
    print("Please choose your book category")
    for i,c in enumerate(categories,start=1):
        print(f"{i}. {c}")
    cat=input(f"Enter your chosen category(1-{len(categories)}): ")
    
    while not cat.isdigit() or int(cat) not in range(1, len(categories) + 1) :
        print(f"{cat} is not option")
        cat=input(f"Enter your chosen category(1-{len(categories)}): ")
    cat=int(cat)
    Book={
        'Title':book_name,
        'Author':author,
        'Published Year':int(published_year),
        'Book Category':categories[cat-1]
    }
    Books=[]
    print("\n----------BOOK DETAILS----------")
    for i,b in Book.items():
        print(f"{i}: {b} ")
    Books.append(Book)
    print("Book saved successfully!!!")
    for i,c in enumerate(Books,start=1):
        print(f"{i} {c}")
    return Books

add_book()
"""
def search_book():
    choices=['Title', 'Author','Published Year', 'Book Category']
    print("Please choose your your preferred search filter")
    for i,c in enumerate(choices,start=1):
        print(f"{i}. {c}")
    search=input(f"What would you like to use to search(1-{len(choices)}): ")
    for i,c in enumerate(choices,start=1):
        while search not in i or not search.isdigit():
            print(f"{search} is not option")
            search=input(f"What would you like to use to search(1-{len(choices)}): ")
    category=[c for i,c in enumerate(categories) if i==int(cat)-1]


def delete_book():

def edit_book():

    
def borrow_book():"""