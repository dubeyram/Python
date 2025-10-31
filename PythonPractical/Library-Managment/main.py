from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict


class LibraryManagementSystem(ABC):
    """
    Abstract Base class representing a generic library management entity.
    
    Demonstrates:
        - Abstraction (via abstract methods)
        - Encapsulation (data hidden inside classes)
    """

    def __init__(self, name: str, email: str) -> None:
        """
        Initialize a library user with name and email.
        """
        self.name = name
        self.email = email

    @abstractmethod
    def list_books(self) -> str:
        """Abstract method to be implemented by subclasses."""
        pass


class Book(LibraryManagementSystem):
    """
    Represents a book management system that allows adding, renting,
    and returning books for a library.
    
    Demonstrates:
        - Inheritance (inherits from LibraryManagementSystem)
        - Polymorphism (overrides abstract method `list_books`)
        - Encapsulation (uses private attributes)
        - Class & Static methods
    """

    _library_name: str = "City Central Library"
    _transaction_log: List[str] = []

    def __init__(self, name: str, email: str, books: List[str]) -> None:
        """
        Initialize the Book system with user details and available books.
        """
        super().__init__(name, email)
        self.books = books
        self._rented_books: Dict[str, str] = {}

    # ---------- Class and Static Methods ----------
    @classmethod
    def get_library_name(cls) -> str:
        """Return the library name (shared across all instances)."""
        return cls._library_name

    @classmethod
    def view_transactions(cls) -> List[str]:
        """Return all transaction logs."""
        return cls._transaction_log

    @staticmethod
    def _log_transaction(action: str, book: str, user: str) -> None:
        """Internal helper to log all transactions with timestamps."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Book._transaction_log.append(f"[{timestamp}] {action}: '{book}' by {user}")

    # ---------- Core Book Management Methods ----------
    def add_book(self, book: str) -> str:
        """
        Add one or more books to the library.
        """
        if not book:
            raise ValueError("Please enter at least one book name.")

        books_to_add = [b.strip() for b in book.split(",") if b.strip()]
        self.books.extend(books_to_add)

        for b in books_to_add:
            self._log_transaction("Added", b, self.name)

        return f"{len(books_to_add)} book(s) added to the library."

    def rent_book(self, book: str) -> str:
        """
        Rent a book from the library.
        """
        if not book:
            raise ValueError("Please provide a book name.")

        if book in self._rented_books:
            return f"'{book}' is already rented by someone."

        if book not in self.books:
            return f"'{book}' is not available in the library."

        self.books.remove(book)
        self._rented_books[book] = f"Rented by {self.name}"
        self._log_transaction("Rented", book, self.name)
        return f"Book '{book}' has been rented by {self.name}."

    def return_book(self, book: str) -> str:
        """
        Return a rented book to the library.
        """
        if book not in self._rented_books:
            return f"'{book}' was not rented."

        if self._rented_books.get(book) != f"Rented by {self.name}":
            return f"'{book}' was not rented by {self.name}."

        del self._rented_books[book]
        self.books.append(book)
        self._log_transaction("Returned", book, self.name)
        return f"Book '{book}' successfully returned by {self.name}."

    def list_books(self) -> str:
        """
        List total available books in the library (Polymorphism demo).
        """
        return f"Total {len(self.books)} book(s) available: {self.books}"

    # ---------- Operator Overloading ----------
    def __len__(self) -> int:
        """Return number of available books (Operator overloading)."""
        return len(self.books)

    def __add__(self, other: "Book") -> "Book":
        """
        Combine two libraries together (demonstrates polymorphism & operator overloading).
        """
        if not isinstance(other, Book):
            raise TypeError("Can only merge with another Book instance.")
        combined_books = self.books + other.books
        return Book(name=self.name, email=self.email, books=combined_books)

    def __str__(self) -> str:
        """String representation of the current user and library state."""
        return (
            f"Library: {self.get_library_name()}\n"
            f"User: {self.name} | Email: {self.email}\n"
            f"Available Books: {self.books}\n"
            f"Rented Books: {self._rented_books}"
        )


if __name__ == "__main__":
    # Example usage
    user1 = Book(name="Ram", email="ram@example.com", books=["Python 101", "Django Mastery"])
    user2 = Book(name="Sita", email="sita@example.com", books=["Flask Essentials"])

    print(user1.add_book("AI for Beginners, ML in Practice"))
    print(user1.rent_book("Python 101"))
    print(user1.return_book("Python 101"))
    print(user1.list_books())

    # Demonstrate operator overloading
    merged_library = user1 + user2
    print("\nMerged Library Books:", merged_library.books)

    # View all transactions (class-level)
    print("\n--- Transaction Log ---")
    for log in Book.view_transactions():
        print(log)

    print(f"\nTotal books in merged library: {len(merged_library)}")
