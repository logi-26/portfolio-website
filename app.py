from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
  
@app.route("/cv")
def cv():
    return render_template("cv.html")
  
@app.route("/work")
def work():
    return render_template("work.html")
  
@app.route("/personal")
def personal():
    return render_template("personal.html")
  
if __name__ == "__main__":
    app.run(debug=False)