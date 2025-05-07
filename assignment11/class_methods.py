# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def display_total_books(cls):
        print(f"Total books in the library: {cls.total_books}")


b1 = Book("To Kill a Mockingbird", "Harper Lee")
b2 = Book("1984", "George Orwell")
b3 = Book("The Great Gatsby", "F. Scott Fitzgerald")



b1.display_total_books()


