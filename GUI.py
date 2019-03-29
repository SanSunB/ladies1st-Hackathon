from random import randint
from time import strftime
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)


# lunch the home page
@app.route('/<name>')
def index(name):
    return render_template('html_main_form.html',name=name)


if __name__ == "__main__":
    app.run(debug=True)
