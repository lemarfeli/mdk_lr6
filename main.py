from book import Book
from user import User
from library import Library


def main():
    # Создаем библиотеку
    library = Library()

    # Добавляем книги
    book1 = Book("1984", "George Orwell", "Dystopian", "1234567890", 328)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction", "0987654321", 281)
    library.add_book(book1)
    library.add_book(book2)

    # Регистрируем пользователя
    user1 = User("Alice", 1)
    library.register_user(user1)

    # Список книг
    library.list_books()
    # Поиск книг по автору
    print("\nBooks by George Orwell:")
    books_by_orwell = library.find_books_by_author("George Orwell")
    for book in books_by_orwell:
        print(f" - {book}")

    # Пользователь берет книгу
    user1.borrow_book(book1)

    # Проверяем статус книг
    library.list_books()

    # Пользователь возвращает книгу
    user1.return_book(book1)

    # Проверяем статус книг
    library.list_books()

    # Попытка взять недоступную книгу
    user1.borrow_book(book1)
    user1.borrow_book(book1)
    
        # Генерация отчета
    library.generate_report()

    # Сохраняем данные библиотеки в файл
    library.save_to_file("library_data.json")
if __name__ == "__main__":
    main()
