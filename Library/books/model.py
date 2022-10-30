from Library import db,app

class Books(db.Model):
    BookId = db.Column('BookId',db.Integer, primary_key=True)
    NameBook = db.Column('NameBook',db.String(50))
    Author = db.Column('Author',db.String(50), nullable=False )
    YearPublished = db.Column('YearPublished',db.String(50))
    Type = db.Column('Type',db.Integer)
    BooksToLoans = db.relationship('Loans', backref='books')

    def __init__(self, NameBook, Author, YearPublished, Type):
        self.NameBook = NameBook.title()
        self.Author = Author.title()
        self.YearPublished = YearPublished
        self.Type = Type
with app.app_context():
    db.create_all()