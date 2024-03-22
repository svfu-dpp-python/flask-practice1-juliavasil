from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index_page():
    return render_template("index.html")
def index_page():
    return "<p>Hello, World!</p>"