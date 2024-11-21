import uuid
import datetime

class Book:
    def __init__(self, title, author, isbn=None):
        self.id = uuid.uuid4()
        self.title = title
        self.author = author
        self.isbn = isbn or str(uuid.uuid4()) # Generate ISBN if not provided
        self.available = True
        self.borrow_date = None
        self.due_date = None
        self.borrower_id = None


    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {'Yes' if self.available else 'No'}"


    def borrow(self, borrower_id, due_days=14):
        if not self.available:
            raise ValueError("Book is not available")

        self.available = False
        self.borrow_date = datetime.date.today()
        self.due_date = datetime.date.today() + datetime.timedelta(days=due_days)
        self.borrower_id = borrower_id


    def return_book(self):
        self.available = True
        self.borrow_date = None
        self.due_date = None
        self.borrower_id = None



