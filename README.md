# SRE-Assignment
SRE Assignment for airmeet using flask 

The code below has following routes/apis
1. (/) home page to access list and add api's
2. (/list) to list aa users in db
3. (/add_data) takes you to form to enter user details
4. (/add) to add new user entries
5. ("/search/<int:account_number>") to show details for a specific account_number
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 Solution uses Sqlite db and class Profile(db.Model) to create table and rows in DB. 

 Templates Folder contains HTML pages rendered by routes.

All Api's are accessible via index page except search, to test search use http://127.0.0.1:5000/search/1 [1 is the account number we are searching for]

test.db is the sqlite db used

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Karmesh Sharma/Desktop/airmeet-sre/test.db' # You can add path to the DB as per your system to access it


