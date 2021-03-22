from flask import Flask, url_for, redirect, render_template, request


app = Flask(__name__)
@app.route("/")
def home():
    return render_template("aimo.html")

@app.route("/login", methods=["POST", "GET"])
def log():
    return render_template("aimo4.html")
@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"




@app.route("/rules")
def rules():
    return render_template("aimo2.html")

if __name__ == "__main__":
    app.run()
