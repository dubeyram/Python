class LibraryManagementSystem:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email


class Book(LibraryManagementSystem):
    def __init__(self, name, email, books) -> None:
        super().__init__(name, email)
        self.books = books
        self._rented_books = {}
    
    def add_book(self, book):
        if not book:
            raise Exception("Please enter the atleast 1 book")
        books_to_add = book.strip().split(",")
        self.books.extend(books_to_add)

        return f"{len(books_to_add)} books added to the Book Library"

    def rent_book(self, book):
        if not book:
            raise Exception("Please enter the atleast 1 book")
        if book not in self.books:
            if book not in self._rented_books:
                return f"{book} is not availiable in Library."
            return f"{book} is already rented by someone."
        self.books.remove(book)
        self._rented_books.update({f"{book}": f"Rented by {self.name}"})
        return f"Book Name: {book}, is rented by {self.name}."

    def list_books(self):
        return f"Total {len(self.books)} book is availiable in the Library."

b = Book(name="Ram", email="testing", books=[])

print(b.add_book("1,2"))
print(b.books)

print(b.rent_book("1"))
print(b.rent_book("1"))
print(b.list_books())



if __name__=="__main__":
    print("")

