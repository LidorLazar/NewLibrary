from Library import db,app


class Customers(db.Model):
    CusomerID = db.Column('CusomerID',db.Integer, primary_key=True)
    Name = db.Column('Name', db.String(50))
    City = db.Column('City', db.String(50))
    Age = db.Column('Age', db.Integer)
    CustomersToLoans = db.relationship('Loans', backref='customers')
                       
    def __init__(self, CusomerID, Name, City, Age):
        self.CusomerID = CusomerID
        self.Name = Name.title()
        self.City = City.title()
        self.Age = Age

with app.app_context():
    db.create_all()