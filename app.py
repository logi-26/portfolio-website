from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")
  
@app.route("/cv")
def var():
    user = "Geeksforgeeks"
    return render_template("cv.html", name=user)
  
@app.route("/work")
def ifelse():
    user = "Practice GeeksforGeeks"
    return render_template("work.html", name=user)
  
@app.route("/personal")
def for_loop():
    list_of_courses = ['Java', 'Python', 'C++', 'MATLAB']
    return render_template("personal.html", courses=list_of_courses)
  
if __name__ == "__main__":
    app.run(debug=False)