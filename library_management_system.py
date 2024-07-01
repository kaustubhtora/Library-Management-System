# Data structures to store book information and borrowed books
library = {}
borrowed_books = []

def add_book(title, author):
    """Adds a book to the library."""
    if title in library:
        print(f"The book '{title}' already exists in the library.")
    else:
        library[title] = author
        print(f"Book '{title}' by {author} added to the library.")

def lend_book(title, user):
    """Lends a book to a user."""
    if title in library and title not in borrowed_books:
        borrowed_books.append({'title': title, 'user': user})
        print(f"The book '{title}' has been lent to {user}.")
    else:
        print(f"The book '{title}' is either not available or has already been lent out.")

def return_book(title):
    """Returns a borrowed book."""
    for record in borrowed_books:
        if record['title'] == title:
            borrowed_books.remove(record)
            print(f"The book '{title}' has been returned.")
            return
    print(f"The book '{title}' was not borrowed.")

def display_books():
    """Displays all books in the library and their status."""
    print("\nLibrary Collection:")
    if not library:
        print("No books in the library.")
    for title, author in library.items():
        status = "Available"
        for record in borrowed_books:
            if record['title'] == title:
                status = f"Lent out to {record['user']}"
                break
        print(f"'{title}' by {author} - {status}")
    print()

def display_borrowed_books():
    """Displays all borrowed books."""
    print("\nBorrowed Books:")
    if not borrowed_books:
        print("No books are currently borrowed.")
    for record in borrowed_books:
        print(f"'{record['title']}' borrowed by {record['user']}")
    print()

# Example usage
def main():
    while True:
        print("Library Management System")
        print("1. Add Book")
        print("2. Lend Book")
        print("3. Return Book")
        print("4. Display All Books")
        print("5. Display Borrowed Books")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            add_book(title, author)
        elif choice == '2':
            title = input("Enter the book title: ")
            user = input("Enter the name of the borrower: ")
            lend_book(title, user)
        elif choice == '3':
            title = input("Enter the book title: ")
            return_book(title)
        elif choice == '4':
            display_books()
        elif choice == '5':
            display_borrowed_books()
        elif choice == '6':
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()