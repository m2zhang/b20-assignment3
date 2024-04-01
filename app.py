from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from flask_bcrypt import Bcrypt

app = Flask(__name__)

@app.route("/")
@app.route('/home')
def home():
    pagename='home'
    return render_template("create_acc.html", pagename=pagename)


if __name__ == "__main__":
    app.run(debug=True)