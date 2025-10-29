class LibraryManagementSystem:
    """
    Base class representing a library management system user.
    
    Attributes:
        name (str): Name of the user.
        email (str): Email address of the user.
    """

    def __init__(self, name: str, email: str) -> None:
        """
        Initialize a library user with name and email.
        """
        self.name = name
        self.email = email


class Book(LibraryManagementSystem):
    """
    Represents a book management system that allows adding, renting, 
    and returning books for a library.
    
    Inherits from:
        LibraryManagementSystem
    """

    def __init__(self, name: str, email: str, books: list[str]) -> None:
        """
        Initialize the Book system with user details and available books.

        Args:
            name (str): Name of the user.
            email (str): Email address of the user.
            books (list[str]): Initial list of available books.
        """
        super().__init__(name, email)
        self.books = books
        self._rented_books: dict[str, str] = {}

    def add_book(self, book: str) -> str:
        """
        Add one or more books to the library.

        Args:
            book (str): Comma-separated string of book names.

        Returns:
            str: Confirmation message with count of added books.

        Raises:
            ValueError: If book input is empty.
        """
        if not book:
            raise ValueError("Please enter at least one book name.")

        books_to_add = [b.strip() for b in book.split(",") if b.strip()]
        self.books.extend(books_to_add)

        return f"{len(books_to_add)} book(s) added to the library."

    def rent_book(self, book: str) -> str:
        """
        Rent a book from the library.

        Args:
            book (str): Name of the book to rent.

        Returns:
            str: Status message about the rent operation.
        """
        if not book:
            raise ValueError("Please provide a book name.")

        if book in self._rented_books:
            return f"'{book}' is already rented by someone."

        if book not in self.books:
            return f"'{book}' is not available in the library."

        self.books.remove(book)
        self._rented_books[book] = f"Rented by {self.name}"
        return f"Book '{book}' has been rented by {self.name}."

    def list_books(self) -> str:
        """
        List total available books in the library.

        Returns:
            str: Count of available books.
        """
        return f"Total {len(self.books)} book(s) available in the library."

    def return_book(self, book: str) -> str:
        """
        Return a rented book to the library.

        Args:
            book (str): Name of the book to return.

        Returns:
            str: Status message of the return process.
        """
        if book not in self._rented_books:
            return f"'{book}' was not rented."

        if self._rented_books.get(book) != f"Rented by {self.name}":
            return f"'{book}' was not rented by {self.name}."

        del self._rented_books[book]
        self.books.append(book)
        return f"Book '{book}' successfully returned by {self.name}."

    def __str__(self) -> str:
        """
        String representation of the current user and library state.
        """
        return (f"User: {self.name} | Email: {self.email}\n"
                f"Available Books: {self.books}\n"
                f"Rented Books: {self._rented_books}")


if __name__ == "__main__":
    # Example usage
    b = Book(name="Ram", email="testing@example.com", books=[])

    print(b.add_book("Book1, Book2"))
    print(b.books)

    print(b.rent_book("Book1"))
    print(b.return_book("Book1"))
    print(b.list_books())
