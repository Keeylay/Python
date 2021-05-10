from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def data():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def results():
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    comments_from_form = request.form['comments']
    return render_template("results.html", name = name_from_form, location = location_from_form, language = language_from_form, comments = comments_from_form)

if __name__ == "__main__":
    app.run(debug=True)