from ..cli import database
from flask import Flask, render_template

app = Flask(__name__)
list_of_todos = database.retrive_todo()


@app.route("/")
def home():
    return render_template('index.html', title='Home', data=list_of_todos)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


app.run(debug=True)
