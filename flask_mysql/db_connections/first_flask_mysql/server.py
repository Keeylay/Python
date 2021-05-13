from flask import Flask, render_template, redirect, request
from flask.wrappers import Request
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL('friends_schema')	        # call the function, passing in the name of our db
    friends = mysql.query_db('SELECT * FROM friends;')  # call the query_db function, pass in the query as a string
    print(friends)
    return render_template("index.html", all_friends = friends)

@app.route("/create_friend", methods=["POST"])
def add_friend_to_db():
    mysql = connectToMySQL('friends_schema')	        # call the function, passing in the name of our db
    
    query = "INSERT INTO friends (first_name, last_name, occupation) VALUES (%(first_name)s, %(last_name)s, %(occupation)s);"

    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'occupation':request.form['occupation'],
    }

    new_friend_id = mysql.query_db(query, data)
    return redirect('/')

    print(request.form)
    # QUERY: INSERT INTO first_flask (first_name, last_name, occupation, created_at, updated_at) 
    #                         VALUES (fname from form, lname from form, occupation from form, NOW(), NOW());

if __name__ == "__main__":
    app.run(debug=True)

# query = "SELECT * FROM users WHERE email = %(email)s;"
# data = { 
#     'email' : request.form['email'] 
# }
# result = mysql.query_db(query, data)