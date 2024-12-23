class Library:
    # Class attribute to store the list of books
    book_list = []

    @classmethod
    def entry_book(cls, book):
        """Insert an object of the Book class into the book_list."""
        cls.book_list.append(book)

# Example usage:
# Define a Book class for testing purposes
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Create book objects
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

# Add books to the library
Library.entry_book(book1)
Library.entry_book(book2)

# Print the list of books in the library
for book in Library.book_list:
    print(f"Title: {book.title}, Author: {book.author}")
    