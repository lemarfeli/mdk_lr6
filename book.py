class Book:
    def __init__(self, title, author, genre, isbn, pages, available=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.pages = pages
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author} (Genre: {self.genre}, ISBN: {self.isbn})"

    def is_available(self):
        return self.available

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True

