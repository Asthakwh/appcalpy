from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "secret123"

USERNAME = "admin"
PASSWORD = "1234"

@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:
            session["user"] = username
            return redirect("/game")
        else:
            return "Invalid Login"

    return render_template("login.html")

@app.route("/game")
def game():
    if "user" in session:
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        return render_template("game.html",num1=num1,num2=num2)
    return redirect("/")

app.run(debug=True)