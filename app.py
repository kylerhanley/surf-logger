from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/date")
def date_page():
    return render_template("date.html")
@app.route("/spot")
def spot_page():
    return render_template("spot.html")

@app.route("/log", methods = ["GET","POST"])
def log_session():
    if request.method == "POST":
        spot = request.form.get("spot")
        return render_template("submission.html",spot=spot)
    return render_template("log_session.html")




if __name__ == "__main__":
    app.run(debug=True)