from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'My Secrets'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("I got your info")
    # print(request.form)
    session['username']= request.form['name']
    session['useremail']= request.form['email']
    return redirect("/show")

    # render_template("show.html", name_on_template = name_from_form, email_on_template=email_from_form)

@app.route("/show")
def show_user():
    print("Show the user the infor form the Form")
    print(request.form)
    return render_template("show.html", name_on_template = session['username'], email_on_template = session['useremail'])


if __name__ == "__main__":
    app.run(debug = True)