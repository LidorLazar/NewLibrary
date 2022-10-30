from flask import Blueprint, request, render_template
from Library import db
from Library.books.model import Books


books_table= Blueprint('Books' ,__name__,template_folder="templates")


@books_table.route('/addBook/', methods=['POST', 'GET'])
def AddBook():
    if request.method == 'POST':
        if  1 <= int(request.form['Type']) <= 3:
            NewBook = Books(NameBook=request.form['NameBook'],
                                Author = request.form['Author'], YearPublished =request.form['YearPublished'],
                                Type = request.form['Type'])
            db.session.add(NewBook)
            db.session.commit()
            return render_template('ShowAllBooks.html', PrintAllBook = Books.query.all())
        else:
            return render_template('Eror.html')
    return render_template('AddBook.html')

@books_table.route('/Book/<bookname>', methods=['GET'])
@books_table.route('/Book/', methods=['GET', 'POST'])
def PrintAllBook(bookname=''):
    if request.method == 'POST':
        for OneBook in Books.query.all():
            if request.form.get("SerachBook").title() == OneBook.NameBook:
                bookname = OneBook.NameBook
                return render_template('personalBook.html', bookname=bookname, PrintAllBook=Books.query.all())
    return render_template('ShowAllBooks.html', PrintAllBook = Books.query.all())

@books_table.route("/deleteBook/<id>",methods=['DELETE','GET'])
def deleteBook(id=0):
    book = Books.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return render_template('ShowAllBooks.html', book = Books.query.all())
    return f"the id book doesn't exist"