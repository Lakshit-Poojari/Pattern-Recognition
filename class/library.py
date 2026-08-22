class Book:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available

    def display_book(self,):
        if self.available:
            return "Name of book is " , self.title, "name of author is ",self.author, 
        else:
            return "Book not available"
        
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    print("Book borrowed successfully")
                else:
                    print("Book is already borrowed")
                return

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                print("Book returned successfully")
                return

    print("Book not found")

    def display_available_books(self):
        for book in self.books:
            if book.available:
                print(f"Name of book is {book.title}, name of author is {book.author}")


book1 = Book("Python", "John", True)
book2 = Book("Java", "James", True)

member1 = Member("Rahul", 101)

library = Library()

library.add_book(book1)
library.add_book(book2)

library.register_member(member1)

library.display_available_books()