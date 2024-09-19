from flask import Flask

app = Flask(__name__)

@app.route("/")
def display_home():
    return "This is home"


if __name__ == "__main__":
    app.run()