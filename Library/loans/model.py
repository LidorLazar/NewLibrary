from Library import db,app

class Loans(db.Model):
    LoansID = db.Column('LoansID', db.Integer, primary_key=True)
    CusomerID = db.Column('CusomerID', db.Integer, db.ForeignKey('customers.CusomerID'), nullable=False)
    BookId = db.Column('BookId', db.Integer, db.ForeignKey('books.BookId'))
    LoanDate = db.Column('LoanDate', db.Date)
    ReturnDate = db.Column('ReturnDate', db.Date)
    

    def __init__(self, CusomerID, BookId, LoanDate, ReturnDate):
        self.CusomerID = CusomerID
        self.BookId = BookId
        self.LoanDate = LoanDate
        self.ReturnDate = ReturnDate


with app.app_context():
    db.create_all()