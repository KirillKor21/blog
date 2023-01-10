from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:secret@192.168.31.92:5432/blog_db"

db.init_app(app)



class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    text = db.Column(db.String(64))

    def __init__(self, username, text):
        self.username = username
        self.text = text


with app.app_context():
    db.create_all()

messages = {}


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", messages=Note.query.all())


@app.route("/add_message", methods=['POST'])
def add_message():
    name = request.form['name']
    text = request.form['text']

    messages = Note(username=name, text=text)
    db.session.add(messages)
    db.session.commit()

    return redirect("/")


app.run(host="0.0.0.0")
