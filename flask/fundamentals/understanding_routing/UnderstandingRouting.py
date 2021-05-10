from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def hello_name(name):
    return f'Hello {str(name)}!'

@app.route('/<int:num>/<name>') # URL defaults to string, need to add "int:" to make it an int
def num_times_name(num, name):
    return str(name) * num 

if __name__ == "__main__":
    app.run(debug=True)