from flask import Flask

app = Flask(__name__)

@app.route("/")
def add():
    a = 10
    b = 5
    result = a + b
    return f"Addition of {a} and {b} is {result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
