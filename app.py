from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return """
        <h1>Hello from Quantm</h1>
        <h1>Hello from Quantm</h1>
    """


if __name__ == "__main__":
    app.run(debug=False, port=8080)