from flask import Flask, redirect, render_template, request
from markupsafe import escape

from book import db
from book import Book,app

all_books = db.session.query(Book).all
print(all_books)
@app.route('/',methods=["GET","POST"])
def home():
    if request.method =="GET":
        all_books = Book.query.all()
        return render_template("index.html",book_list = all_books)
        
    if request.method == "POST":
        book_name = request.form["book_name"]
        author = request.form["book_author"]
        rating = request.form["rating"]
        book1 = Book(title=book_name,author=author,rating=float(rating))
        db.session.add(book1)
        db.session.commit()
        return redirect("/")


@app.route("/add",methods=["GET"])
def add():
    if request.method == "GET":
        return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)

