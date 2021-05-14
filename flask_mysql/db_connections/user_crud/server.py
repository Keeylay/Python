from types import MethodDescriptorType
from flask import Flask, render_template, request, redirect
from flask.wrappers import Request
# from werkzeug import url_decode, useragents
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
        # 'user':request.form['user_id'],
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
    }

    new_user_id = mysql.query_db(query, data)

    return redirect('/users/' + str(new_user_id))

@app.route('/users/<int:user_id>', methods=['GET', 'POST'])
def single_user(user_id):
    mysql = connectToMySQL('users_schema')
    query = "SELECT * FROM users WHERE id = %(id)s;"

    data = {
        'id':user_id
    }

    show_user = mysql.query_db(query,data)
    return render_template("read_(one).html", show_user = show_user)

@app.route('/user_delete/<int:user_id>')
def delete_user(user_id):
    mysql = connectToMySQL('users_schema')
    query = "DELETE FROM users WHERE id = %(id)s;"
    
    data = {
        'id':user_id
    }

    connectToMySQL('users_schema').query_db(query, data)
    return redirect('/')

@app.route('/edit/<int:user_id>', methods=['GET','POST'])
def edit_user(user_id):
    mysql = connectToMySQL('users_schema')
    query2 = "SELECT * FROM users WHERE id = %(id)s;"
    data2 = {
        'id':user_id
    }
    user = mysql.query_db(query2, data2)[0]

    return render_template("edit.html", user = user)

@app.route('/update', methods = ['POST', 'GET'])
def actual_update():
    mysql = connectToMySQL('users_schema')
    query = "UPDATE users SET  first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"

    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'id':request.form['id']
    }

    update_user = mysql.query_db(query, data)
    print("mannanana")


    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)