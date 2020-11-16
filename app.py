from flask import Flask
from flask import render_template
from flask import request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/treasure_hunt'
app.config['SECRET_KEY'] = os.urandom(12)


@app.route('/', methods=['GET'])
def login():
    db = SQLAlchemy(app)
    rs = db.engine.execute("SELECT username FROM users;")

    for row in rs:
        print (row[0])

    return render_template('login.html')

@app.route('/zagonetke', methods=['GET'])
def zagonetke():
    return "dobrodoso frende"

@app.route('/auth', methods=['POST'])
def auth():
    username = request.values.get('username', '')
    password = request.values.get('password', '')
    if (username == "admin") and password == "admin":
        return redirect(url_for("zagonetke"))
    else:
        flash("Username and password incorrect")
        return redirect(url_for("login"))

if __name__ == '__main__':
    app.run()
