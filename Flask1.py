from flask import Flask, redirect, url_for
    
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return "Hello admin"

@app.route('/guest/<guest>')
def hello_guest(guest):
    return "Hello %s as guest" % guest

@app.route('/user/<name>')
def hello_user(name):
    if name == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest",guest = name))
@app.route('/welcome/<name>')
def welcome(name):
    return "Welcome %s to the"
@app.route('/welcome/<name>')
def welcome(name):
    return "Welcome %s to the home page" % name

@app.route('/guest/<guest>')
def hello_guest():
    return "hello %s as guest "%guest


if __name__ == "__main__":
    app.run(debug=True)