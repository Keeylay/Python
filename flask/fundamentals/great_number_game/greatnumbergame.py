from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'asdfqw4r'

@app.route('/')
def index():
    if not 'answer' in session:
        session['answer'] = random.randint(1, 100)
    print(session['answer'])
    return render_template("index.html")

@app.route('/result', methods = ['POST'])
def result():
    number = int(request.form['number'])

    if number > session['answer']:
        session['message'] = "Too High!"
    
    elif number < session['answer']:
        session['message'] = "Too Low!"
    
    else:
        session['message'] = "Correct!"

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)