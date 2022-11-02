from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import datetime


###########################################
########## Def the app ####################
###########################################

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Libarary.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

###########################################
########## Def the DataBase ###############
###########################################
from Library.books.views import books_table
from Library.customer.views import customer_table
from Library.loans.views import loan_table
app.register_blueprint(books_table)
app.register_blueprint(customer_table)
app.register_blueprint(loan_table)

with app.app_context():
    db.create_all()

##########################################
########## Add details in DataBase ########
###########################################
from Library.books.model import Books
from Library.customer.model import Customers
from Library.loans.model import Loans
customer_one = Customers(CusomerID = 1, Name='lidor', City='yavne', Age=22)
book_one = Books(NameBook='Peter Pan', Author='J. M. Barrie', YearPublished=1990, Type=1)
loans_one = Loans(CusomerID=1, BookId=1, LoanDate=datetime.datetime.strptime('2022-10-26', '%Y-%m-%d'),ReturnDate=datetime.datetime.strptime('2022-10-30', '%Y-%m-%d'))

from sqlalchemy.exc import IntegrityError

try:
    with app.app_context():
        db.session.add(customer_one)
        db.session.add(book_one)
        db.session.add(loans_one)
        db.session.commit()
except IntegrityError:
    with app.app_context():
        db.session.rollback()
