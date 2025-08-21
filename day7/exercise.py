class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"{self.title} by {self.author} - {status}"



class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to {self.name}.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print(f"\nBooks in {self.name}:")
            for book in self.books:
                print(book)

    def lend_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print(f"You have borrowed '{book.title}'.")
                    return
                else:
                    print(f"'{book.title}' is currently not available.")
                    return
        print(f"No book with title '{title}' found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    print(f"Thank you for returning '{book.title}'.")
                    return
                else:
                    print(f"'{book.title}' was not borrowed.")
                    return
        print(f"No book with title '{title}' found.")

      
my_library = Library("City Library")


book1 = Book("1984", "George Orwell")
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book3 = Book("To Kill a Mockingbird", "Harper Lee")


my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)


my_library.display_books()


my_library.lend_book("1984")
my_library.display_books()

my_library.return_book("1984")
my_library.display_books()

