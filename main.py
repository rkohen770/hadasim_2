import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
# ‘/’ URL is bound with welcome() function.
def welcome():
    return render_template('welcome.html')


if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()

class Patient(db.Model):

    __tablename__ = "Patient"

    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.Text)
    l_name = db.Column(db.Text)
    address= db.Column(db.Text)
    date_of_birth=db.Column(db.Text)
    phone_number = db.Column(db.Integer, db.Text)
    mobile_phone_number = db.Column(db.Integer,db.Text)

    def __init__(self, id, f_name ,l_name, address, date_of_birth, phone_number, mobile_phone_number):
        self.id =id
        self.f_name =f_name
        self.l_name = l_name
        self.address = address
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.mobile_phone_number = mobile_phone_number

    def __repr__(self):
        return "name: {} {} \nid: {}\naddress:{}\ndate of birth: {}\nphone_number: {}\nmobile_phone_number:{}".format(self.f_name, self.l_name, self.id, self.age,self.address, self.date_of_birth, self.phone_number, self.mobile_phone_number)