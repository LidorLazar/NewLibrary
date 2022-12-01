from flask import Blueprint, request, render_template
from Library import db
from Library.user.model import Users


user_table= Blueprint('Users' ,__name__,template_folder="templates")

@user_table.route("/print_user/", methods=['GET'])
def all_u_in_lib():
    all_users = []
    user = Users.query.all()
    for i in user:
      all_users.append({"username": i.username, "password": i.password, "email": i.email})
    return all_users


@user_table.route('/registeruser/', methods=['POST', 'GET'])
def add_customer():
      if request.method == 'POST':
            NewUser = Users(username=request.json['username'],password=request.json['password'],
            email=request.json['email'])
            try:
                  db.session.add(NewUser)
                  db.session.commit()
            except:
                  pass
      else:
            pass
      return 'good'

