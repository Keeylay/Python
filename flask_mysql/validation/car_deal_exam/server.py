from logging import debug
from flask_app import app
from flask_app.controllers import users, cars

if __name__ == "__main__":
    app.run(debug=True)