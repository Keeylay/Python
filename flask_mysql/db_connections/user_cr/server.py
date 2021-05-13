from types import MethodDescriptorType
from flask import Flask, render_template, request, redirect
from flask.wrappers import Request
from mysqlconnection import connectToMySQL

app = Flask(__name__)
@app.route('/')
def index():
    mysql = connectToMySQL('users_schema')
    users = mysql.query_db('SELECT * FROM users;')
    print(users)
    return render_template("read_all.html", users = users)

@app.route('/create_user')
def create_users():
    return render_template("create.html")
    
@app.route('/create', methods=['POST'])
def create():
    mysql = connectToMySQL('users_schema')
    query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"

    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
    }

    new_user_id = mysql.query_db(query, data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)