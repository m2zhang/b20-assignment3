from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
@app.route('/home')
def home():
    pagename='home'
    return render_template("create_acc.html", pagename=pagename)


if __name__ == "__main__":
    app.run(debug=True)