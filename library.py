class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def register_user(self, user):
        self.users.append(user)
        print(f"User '{user.name}' registered.")

    def list_books(self):
        print("Books in the library:")
        for book in self.books:
            status = "Available" if book.is_available() else "Borrowed"
            print(f" - {book} [{status}]")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None