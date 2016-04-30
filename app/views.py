from datetime import datetime
from app import app
from flask import render_template, request, redirect
from models import Todo

@app.route('/')
def index():
    todos = Todo.objects.all()
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    content = request.form.get("content")
    status = request.form.get("status")
    todo = Todo(content=content, status=status)
    todo.save()
    # return redirect("/")
    todos = Todo.objects.all()
    return render_template("index.html", todos=todos)

@app.route("/done/<string:todo_id>")
def done(todo_id):
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.status = 1
    todo.update_at = datetime.now()
    todo.save()
    todos = Todo.objects.all()
    return render_template("index.html", todos=todos)

@app.route("/undone/<string:todo_id>")
def undone(todo_id):
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.status = 0
    todo.update_at = datetime.now()
    todo.save()
    todos = Todo.objects.all()
    return render_template("index.html", todos=todos)

@app.route("/delete/<string:todo_id>")
def delete(todo_id):
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.delete()
    todo.save()
    todos = Todo.objects.all()
    return render_template("index.html", todos=todos)
