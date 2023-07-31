from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")
  
@app.route("/cv")
def var():
    return render_template("cv.html")
  
@app.route("/work")
def ifelse():
    return render_template("work.html")
  
@app.route("/personal")
def for_loop():
    return render_template("personal.html")
  
if __name__ == "__main__":
    app.run(debug=False)