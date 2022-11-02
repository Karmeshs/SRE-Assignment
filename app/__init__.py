"""
The code below has following routes/apis
1. (/) home page to access list and add api's
2. (/list) to list aa users in db
3. (/add_data) takes you to form to enter user details
4. (/add) to add new user entries
5. ("/search/<int:account_number>") to show details for a specific account_number
"""
from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Karmesh Sharma/Desktop/airmeet-sre/test.db'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)
# Models
class Profile(db.Model):
    __tablename__ = 'users'
    account_number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(100)) 
    # repr method represents how one object of this datatable will look like
    def __repr__(self):
        return f"Name : {self.name}, DOB: {self.dob}, account_number: {self.account_number}, email: {self.email}"

# function to render index page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list')
def list():
    # Query all data and then pass it to the template
    profiles = Profile.query.all()
    return render_template('list_all.html', profiles=profiles)

@app.route('/add_data')
def add_data():
    return render_template('add_profile.html')

# function to add profiles
@app.route('/add', methods=["POST"])
def profile():
    # In this function we will input data from the
    # form page and store it in our database.
    # Remember that inside the get the name should
    # exactly be the same as that in the html
    # input fields
    name = request.form.get("name")
    email = request.form.get("email")
    dob = request.form.get("dob")
    account_number = request.form.get("account_number")

    # create an object of the Profile class of models
    # and store data as a row in our datatable
    if name != '' and email != '' and dob != '' and account_number is not None:
        p = Profile(name=name, email=email, dob=dob, account_number=account_number)
        db.session.add(p)
        db.session.commit()
        return redirect('/')
    else:
        return redirect('/')

@app.route("/search/<int:account_number>", methods=["GET"])
def search(account_number):
    user1 = Profile.query.filter_by(account_number=account_number).first_or_404()

    # if user1 is None:
    #     abort(404)
    # user1.name = request.json.get("name")
    # user1.email = request.json.get("email")
    # user1.dob = request.json.get("dob")
    #user1.account_number = request.json.get("account_number")
    return render_template('search.html', data=user1)
    return user1.account_number


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
