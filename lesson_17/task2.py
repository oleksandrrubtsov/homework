"""
Library

Write a class structure that implements a library. Classes:

1) Library - name, books = [], authors = []

2) Book - name, year, author (author must be an instance of Author class)

3) Author - name, country, birthday, books = []

Library class

Methods:

- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.

- group_by_author(author: Author) - returns a list of all books grouped by the specified author

- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.

Also, the book class should have a class variable which holds the amount of all existing books
"""

class Library:
    def __init__(self,name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        if not isinstance(author, Author):
            raise ValueError("Author must be an istance of Author class")
        book = Book(name, year, author)
        self.books.append(book)
        return book
    
    def group_by_author(self, author):
        return [ book for book in self.books if book.author == author ]

    def group_by_year(self, year:int):
        return [ book for book in self.books if book.year == year]
    
    def __repr__(self):
        return f"Library(name = '{self.name}', books = {self.books}, authors = {self.authors})"


class Book:
    all_books = []

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        self.__class__.all_books.append(self)

    def __repr__(self):
        return f"Book(name = '{self.name}', year = {self.year}, author = '{self.author.name}')"
    
class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author(name = ' {self.name}', country = '{self.country}', birthday = {self.birthday})"



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

print("\nTotal number of books in the library:", Book.all_books)