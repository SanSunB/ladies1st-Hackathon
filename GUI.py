from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from new_worker import new_worker


app = Flask(__name__)

# lunch the home page
@app.route('/')
def index():
    return render_template('html_main_form.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        worker = new_worker(result)
        print("IN GUI",worker)
        return render_template("result.html",result = worker)

if __name__ == "__main__":
    app.run()
