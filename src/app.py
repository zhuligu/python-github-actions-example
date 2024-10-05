from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world! A test by CUC."


if __name__ == "__main__":
    app.run()

