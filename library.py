#classes act as a blueprint for creating objects
# this is a simple python code to list books in a library, add books and to remove books as well.
# it will cover mainly classes as objects 
class Library:
    def __init__(self):
        # Initialize with an empty list of books
        self.books = []

    # List all the books available
    def available_books(self):
        if self.books:
            print("Books available in the library:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("No books are currently available.")

    # Add a book
    def add_book(self):
        new_book = input("Enter the title of the book you want to add: ")
        self.books.append(new_book)
        print(f'"{new_book}" has been added to the library.')

    # Remove a book
    def remove_book(self):
        book_to_remove = input("Enter the title of the book you want to remove: ")
        if book_to_remove in self.books:
            self.books.remove(book_to_remove)
            print(f'"{book_to_remove}" has been removed from the library.')
        else:
            print(f'"{book_to_remove}" is not in the library.')

# Create an instance of Library
library_section = Library()

# Interact with the library
while True:
    print("\nLibrary Menu:")
    print("1. View available books")
    print("2. Add a book")
    print("3. Remove a book")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        library_section.available_books()
    elif choice == "2":
        library_section.add_book()
    elif choice == "3":
        library_section.remove_book()
    elif choice == "4":
        print("Exiting the library system.")
        break
    else:
        print("Invalid choice. Please select from the menu options.")
