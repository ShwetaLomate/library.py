class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_book = None


class Library:
    def __init__(self):
        self.book = Book("Pride And Prejudice", "Jane Austin")
        self.patron = Patron("Shruthi kumar")

    def display_details(self):
        print("\nBook Title:", self.book.title)
        print("Author:", self.book.author)
        print("Patron:", self.patron.name)
        if self.book.available:
            print("Status: Pride And Prejudice " \
            "Jane Austin")
        else:
            print("Status: Issued")

    def issue_book(self):
        if self.book.available:
            self.book.available = False
            self.patron.borrowed_book = self.book.title
            print("Book issued successfully.")
        else:
            print("Book is already issued.")

    def return_book(self):
        if not self.book.available:
            self.book.available = True
            self.patron.borrowed_book = None
            print("Book returned successfully.")
        else:
            print("Book is already available.")


library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Display Book Details")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.display_details()
    elif choice == "2":
        library.issue_book()
    elif choice == "3":
        library.return_book()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")