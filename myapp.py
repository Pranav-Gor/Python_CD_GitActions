from flask import Flask

app = Flask(__name__)

# Addition
@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    result = a + b
    return f"Addition of {a} and {b} is {result}"

if __name__ == '__main__':
    app.run(debug=True)