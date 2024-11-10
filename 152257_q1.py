class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.borrow()
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title} by {book.author}")
        else:
            print(f"{book.title} is already borrowed")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title} by {book.author}")
        else:
            print(f"{self.name} did not borrow {book.title}")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has not borrowed any books")

def main():
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    member1 = LibraryMember("Alice", "1234")

    print("Welcome to the library!")
    while True:
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. List borrowed books")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("Which book would you like to borrow?")
            print("1. The Great Gatsby")
            print("2. To Kill a Mockingbird")
            book_choice = input("Enter the number of the book you want to borrow (1-2): ")
            if book_choice == "1":
                member1.borrow_book(book1)
            elif book_choice == "2":
                member1.borrow_book(book2)
            else:
                print("Invalid choice")
        elif choice == "2":
            print("Which book would you like to return?")
            print("1. The Great Gatsby")
            print("2. To Kill a Mockingbird")
            book_choice = input("Enter the number of the book you want to return (1-2): ")
            if book_choice == "1":
                member1.return_book(book1)
            elif book_choice == "2":
                member1.return_book(book2)
            else:
                print("Invalid choice")
        elif choice == "3":
            member1.list_borrowed_books()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()