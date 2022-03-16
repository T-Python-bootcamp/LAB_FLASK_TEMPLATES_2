from flask import Flask, redirect, request, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "it's working!"

@app.route("/quizz", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        q1 = request.form["ursula"]
        q2 = request.form["scar"]
        q3 = request.form["malefacent"]
        q4 = request.form["hades"]
        if q1 and q2 and q3 and q4 == "true":
            return redirect(url_for("winner"))
        else:
            return redirect(url_for("loser"))
 
    return render_template("index.html")

@app.route("/quizz/winner")
def winner():
    return render_template("pass.html")

@app.route("/quizz/loser")
def loser():
    return render_template("fail.html")