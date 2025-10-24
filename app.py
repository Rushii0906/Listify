from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import calendar

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    completed = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

    allTodo = Todo.query.order_by(Todo.date_created.desc()).all()
    total = len(allTodo)
    completed = len([todo for todo in allTodo if todo.completed])

    today = datetime.now().strftime("%A %d %B, %Y")
    return render_template("index.html", allTodo=allTodo, total=total, completed=completed, today=today)

@app.route("/delete/<int:Sno>")
def delete(Sno):
    todo = Todo.query.filter_by(Sno=Sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

@app.route("/toggle/<int:Sno>")
def toggle(Sno):
    todo = Todo.query.filter_by(Sno=Sno).first()
    todo.completed = not todo.completed
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
