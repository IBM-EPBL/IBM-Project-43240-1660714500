
from flask import Flask,render_template,url_for,redirect

app=Flask(__name__,template_folder="temps",static_folder="static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def jana():
    return render_template("login.html")

@app.route('/about')
def about():
    return render_template("about-us.html")

@app.route("/signin")
def signup():
    return render_template("signin.html")




if __name__=="__main__":
    app.run(host="0.0.0.0",port=5555,debug=True)