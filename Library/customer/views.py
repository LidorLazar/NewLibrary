from flask import Blueprint, request, render_template
from Library import db
from Library.customer.model import Customers
from Library.loans.model import Loans

customer_table = Blueprint('Customers' ,__name__,template_folder="templates")


@customer_table.route('/addCustomer/', methods=['POST', 'GET'])
def AddCustomer():
    if request.method == 'POST':
        if int(request.form['ID']) >= 1 and 100 >= int(request.form['Age']) >= 1 :
            NewCustomer = Customers(CusomerID=request.form['ID'], Name=request.form['Name'],
                                    City=request.form['City'], Age=request.form['Age'])
            db.session.add(NewCustomer)
            db.session.commit()
            return render_template('AddCust.html')
        else:
            return render_template('Eror.html')
    return render_template('AddCust.html')

@customer_table.route('/PrintAll/<customername>', methods=['GET','POST'])
@customer_table.route('/PrintAll/', methods=['GET','POST'])
def PrintAllCustomer(customername=''):
    if request.method == 'POST':
        for name in Customers.query.all():
            if request.form.get("SerachCust").title() == name.Name:
                customername = name.Name
                return render_template('personalCust.html', customername = customername, PrintAllCustomer= Customers.query.all())
        return render_template('ShowAllCust.html', PrintAllCustomer = Customers.query.all())
    else:
        return render_template('ShowAllCust.html', PrintAllCustomer = Customers.query.all())


@customer_table.route("/deleteCustomer/<id>", methods=['DELETE', 'GET'])
def deleteCustomer(id=0):
        customerID=Customers.query.get(int(id))
        custInLoan=Loans.query.all()
        for id_cust in custInLoan:
            return render_template('Eror.html')
        else: 
            db.session.delete(customerID)
            db.session.commit()
        return render_template('ShowAllCust.html', PrintAllCustomer = Customers.query.all())
