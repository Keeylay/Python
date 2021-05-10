from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "asdfasdfasdfasdf"

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] += 1
    return render_template("index.html")

@app.route('/counter')
def increase_count():
    # session['counter'] += 1
    return redirect('/')

@app.route('/reset_counters')
def reset_counters():
    session['counter'] = 0
    return redirect('/')

@app.route('/counter_two')
def increase_count_two():
    session['counter'] += 1
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)