from flask import Blueprint, request, render_template
from Library import db
from Library.customer.model import Customers
from Library.loans.model import Loans

customer_table = Blueprint('Customers' ,__name__,template_folder="templates")

# Add new customer in library.
@customer_table.route('/addCustomer/', methods=['POST', 'GET'])
def add_customer():
    if request.method == 'POST':
        if 100 >= int(request.json['Age']) >= 1:
            NewCustomer = Customers(CusomerID=request.json['custID'],Name=request.json['Name'],
                                    City=request.json['City'], Age=request.json['Age'])
            try:
                db.session.add(NewCustomer)
                db.session.commit()
            except:
                pass
    else:
        pass


# Show all customers in library or show only customer you search.
@customer_table.route('/PrintAll/<customername>', methods=['GET','POST'])
@customer_table.route('/PrintAll/', methods=['GET','POST'])
def print_all_customer(customername=''):
    customer = []
    if request.method == 'POST':
        for name in Customers.query.all():
            customer.append({"CusomerID": name.CusomerID, "Name": name.Name, "City": name.City, "Age": name.Age})
            if request.form.get("SerachCust").title() == name.Name:
                customername = name.Name
            return customer
    for name in Customers.query.all():
        customer.append({"CusomerID": name.CusomerID, "Name": name.Name, "City": name.City, "Age": name.Age})
    print(customer)
    return customer

@customer_table.route("/deleteCustomer/<id>", methods=['DELETE', 'GET'])
def delete_customer(id=0):
        customerID=Customers.query.get(int(id))
        if customerID:
            try:
                db.session.delete(customerID)
                db.session.commit()
            except:
                return render_template('Eror.html')
            return render_template('ShowAllCust.html',print_all_customer = Customers.query.all())
