from flask import Blueprint, request, render_template
from Library import db
from Library.customer.model import Customers
from Library.loans.model import Loans

customer_table = Blueprint('Customers' ,__name__,template_folder="templates")


@customer_table.route('/addCustomer/', methods=['POST', 'GET'])
def add_customer():
    if request.method == 'POST':
        if 100 >= int(request.form['Age']) >= 1:
            NewCustomer = Customers(Name=request.form['Name'],
                                    City=request.form['City'], Age=request.form['Age'])
            db.session.add(NewCustomer)
            db.session.commit()
            return render_template('ShowAllCust.html',print_all_customer = Customers.query.all())
        else:
            return render_template('Eror.html')
    return render_template('AddCust.html')

@customer_table.route('/PrintAll/<customername>', methods=['GET','POST'])
@customer_table.route('/PrintAll/', methods=['GET','POST'])
def print_all_customer(customername=''):
    if request.method == 'POST':
        for name in Customers.query.all():
            if request.form.get("SerachCust").title() == name.Name:
                customername = name.Name
                return render_template('personalCust.html', customername = customername, print_all_customer= Customers.query.all())
        return render_template('ShowAllCust.html', print_all_customer = Customers.query.all())
    else:
        return render_template('ShowAllCust.html', print_all_customer = Customers.query.all())


@customer_table.route("/deleteCustomer/<id>", methods=['DELETE', 'GET'])
def delete_customer(id=0):
        customerID=Customers.query.get(int(id))
        if customerID:
            db.session.delete(customerID)
            db.session.commit()
            return render_template('ShowAllCust.html',print_all_customer = Customers.query.all())
