from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db_path=r'C:\Users\krish\TODO\todo.db'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    msg = db.Column(db.String)

    def __repr__(self):
        return f'{self.msg}'

print(Todo.query.all())

@app.route("/")
def home():
    return render_template('index.html',title='Home')

@app.route("/about")
def about():
    return render_template('about.html',title='About')
if __name__=='__main__':
    app.run()