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

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_books_by_author(self, author):
        found_books = [book for book in self.books if book.author.lower() == author.lower()]
        return found_books

def generate_report(self):
        print("\nLibrary Report:")
        print("\nAvailable Books:")
        available_books = [book for book in self.books if book.is_available()]
        for book in available_books:
            print(f" - {book}")

        print("\nUsers and Borrowed Books:")
        for user in self.users:
            print(f" - {user.name}:")
            if user.borrowed_books:
                for book in user.borrowed_books:
                    print(f"    - {book}")
            else:
                print("    No borrowed books.")
