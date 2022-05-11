# import sqlite3
# db = sqlite3.connect("books-collections.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

from book import db
from book import Book
# db.create_all()
book1 = Book(title="Harry Potter",author= "J.K Rowling",rating=10.0)
db.session.add(book1)
db.session.commit()
