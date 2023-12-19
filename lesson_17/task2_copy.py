class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __str__(self):
        return f"{self.name} ({self.country}, born on {self.birthday})"

    def __repr__(self):
        return f"Author(name={self.name}, country={self.country}, birthday={self.birthday})"


class Book:
    total_books = 0  

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        author.books.append(self)
        Book.total_books += 1

    def __str__(self):
        return f"{self.name} ({self.year}) by {self.author.name}"

    def __repr__(self):
        return f"Book(name={self.name}, year={self.year}, author={repr(self.author)})"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __str__(self):
        return f"Library: {self.name}"

    def __repr__(self):
        return f"Library(name={self.name})"


# Example 
author1 = Author("J.K. Rowling", "United Kingdom", "July 31, 1965")
author2 = Author("George Orwell", "United Kingdom", "June 25, 1903")

library = Library("Awesome Library")

book1 = library.new_book("Harry Potter and the Philosopher's Stone", 1997, author1)
book2 = library.new_book("1984", 1949, author2)
book3 = library.new_book("Harry Potter and the Chamber of Secrets", 1998, author1)

print("Books in the library:")
for book in library.books:
    print(book)

print("\nBooks by J.K. Rowling:")
for book in library.group_by_author(author1):
    print(book)

print("\nBooks published in 1997:")
for book in library.group_by_year(1997):
    print(book)

print("\nTotal number of books in the library:", Book.total_books)
