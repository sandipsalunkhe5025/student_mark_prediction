from flask import Flask
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return "Hello admin"