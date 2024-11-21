class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available():
            book.borrow()
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}' to return.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f" - {book}")
        else:
            print(f"{self.name} has not borrowed any books.")
 def to_dict(self):
        return {
            "name": self.name,
            "user_id": self.user_id,
            "borrowed_books": [book.to_dict() for book in self.borrowed_books]
        }

    @staticmethod
    def from_dict(data):
        user = User(data["name"], data["user_id"])
        user.borrowed_books = [Book.from_dict(book) for book in data["borrowed_books"]]
        return user
