"""
Author: Stefan Davis Smith-Steunenberg

Task 1 of week 7.

code showing a functional framework for a library mangement system, using basic object-oriented programming
"""
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.available = True  # Book is available by default

    def display_details(self):
        """Display the details of the book."""
        status = "Available" if self.available else "Checked out"
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Publication Year: {self.publication_year}\n"
                f"Status: {status}\n")


class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        """Add a book to the patron's list of borrowed books."""
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            return f"{self.name} borrowed '{book.title}'."
        else:
            return f"'{book.title}' is currently unavailable."

    def return_book(self, book):
        """Remove a book from the patron's list of borrowed books."""
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            return f"{self.name} returned '{book.title}'."
        else:
            return f"'{book.title}' was not borrowed by {self.name}."

    def list_borrowed_books(self):
        """List all books borrowed by the patron."""
        if self.borrowed_books:
            return [book.title for book in self.borrowed_books]
        else:
            return "No borrowed books."


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        """Add a new book to the library."""
        self.books.append(book)
        return f"Book '{book.title}' added to the library."

    def register_patron(self, patron):
        """Register a new patron with the library."""
        self.patrons.append(patron)
        return f"Patron '{patron.name}' registered."

    def find_book(self, title):
        """Find a book by title."""
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_patron(self, patron_id):
        """Find a patron by ID."""
        for patron in self.patrons:
            if patron.patron_id == patron_id:
                return patron
        return None

    def check_out_book(self, title, patron_id):
        """Check out a book to a patron."""
        book = self.find_book(title)
        patron = self.find_patron(patron_id)
        if book and patron:
            return patron.borrow_book(book)
        return "Book or Patron not found."

    def return_book(self, title, patron_id):
        """Return a book from a patron."""
        book = self.find_book(title)
        patron = self.find_patron(patron_id)
        if book and patron:
            return patron.return_book(book)
        return "Book or Patron not found."


# Example Usage
if __name__ == "__main__":
    # Create library
    library = Library()
    
    # Add books to the library
    book1 = Book("1984", "George Orwell", 1949)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
    
    library.add_book(book1)
    library.add_book(book2)
    
    # Register patrons
    patron1 = Patron("james", 1)
    patron2 = Patron("bond", 2)
    
    library.register_patron(patron1)
    library.register_patron(patron2)
    
    # Check out a book
    print(library.check_out_book("1984", 1))
    
    # List borrowed books for a patron
    print(patron1.list_borrowed_books())
    
    # Return a book
    print(library.return_book("1984", 1))
    
    # List borrowed books for a patron
    print(patron1.list_borrowed_books())
