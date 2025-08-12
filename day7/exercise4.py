class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def list_books(self):
        return [book.display_info() for book in self.books]


lib = Library()

book1 = Book("Silent Spring", "Rachel Carson", "9780618249060")
book2 = Book("The Alchemist", "Paulo Coelho", "9780061122415")
book3 = Book("Sapiens", "Yuval Noah Harari", "9780099590088")

lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)

for info in lib.list_books():
    print(info)

lib.remove_book("9780061122415")

print("--- After removal ---")

for info in lib.list_books():
    print(info)
