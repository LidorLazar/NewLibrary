from flask import Blueprint, request, render_template
from Library.customer.model import Customers
from Library.books.model import Books
from Library.loans.model import Loans
from datetime import datetime, timedelta
from Library import db


loan_table = Blueprint('Loans' ,__name__,template_folder="templates")

@loan_table.route("/AddLoan/", methods=['GET', 'POST'])
def add_new_loan():
    dayLoan = datetime.utcnow().date()
    id_cust = (request.form.get('CustID'))
    for id in Customers.query.filter_by(CusomerID=request.form.get("CustID")):
        if request.method == 'POST':
            if (int(id_cust) == id.CusomerID):
                for book in Books.query.filter_by(NameBook=request.form.get("bookname")):
                    if book.Type == 1:
                        ReturnDate = dayLoan + timedelta(days=10)
                    elif book.Type == 2:
                        ReturnDate = dayLoan + timedelta(days=5)
                    else:
                        ReturnDate = dayLoan + timedelta(days=2)
                    NewLoans = Loans(CusomerID=request.form['CustID'],
                                    BookId=book.BookId, LoanDate=dayLoan,
                                    ReturnDate=ReturnDate)
                    db.session.add(NewLoans)
                    db.session.commit()
                return render_template('ShowAllLoan.html', print_all_loan=Loans.query.all()) 
            else:
                return render_template('Eror.html')
    return render_template('FormLoan.html', Onlybook = Books.query.all())

@loan_table.route("/AllLoans/",methods=['GET'])
def print_all_loan():
    return render_template('ShowAllLoan.html', print_all_loan=Loans.query.all())

@loan_table.route("/ReturnBook/<LoansID>", methods=['DELETE', 'GET'])
def return_book(LoansID=0):
        DeleteFromDB = Loans.query.get(int(LoansID))
        if int(LoansID) > 0:
            db.session.delete(DeleteFromDB)
            db.session.commit()
            return render_template('ShowAllLoan.html', print_all_loan=Loans.query.all()) 
        return render_template('Eror.html')

@loan_table.route("/lateLoans/", methods = ['GET'])
def late():
    results = []
    table_loan = Loans.query.all()
    for date in table_loan:
        if date.ReturnDate < datetime.utcnow().date():
            results.append(date)
    return render_template('LateLoan.html', results = results)
