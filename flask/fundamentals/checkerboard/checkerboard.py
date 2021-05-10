from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard1():
    board = []
    for i in range(0, 8):
        row = []
        for j in range(0, 8):
            if (j + i) % 2 == 0:
                row.append(0)
            else:
                row.append(1)
        board.append(row)
    return render_template("index.html", x = 8, y = 8, board = board)

@app.route('/<int:y>')
def checkerboard2(y):
    board = []
    for i in range(0, y):
        row = []
        for j in range(0, 8):
            if (j + i) % 2 == 0:
                row.append(0)
            else:
                row.append(1)
        board.append(row)
    return render_template("index.html", x = 8, y = y, board = board)

@app.route('/<int:x>/<int:y>')
def checkerboard3(x, y):
    board = []
    for i in range(0, y):
        row = []
        for j in range(0, x):
            if (j + i) % 2 == 0:
                row.append(0)
            else:
                row.append(1)
        board.append(row)
    return render_template("index.html", x = x, y = y, board = board)

if __name__ == "__main__":
    app.run(debug=True)
