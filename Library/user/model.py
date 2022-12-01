from Library import db,app


class Users(db.Model):
    username = db.Column('username',db.String(50), primary_key=True)
    password = db.Column('password',db.String(50))
    email = db.Column('email',db.String(50))

    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

with app.app_context():
    db.create_all()
