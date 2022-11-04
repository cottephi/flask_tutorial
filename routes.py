"""Routes for the app"""

from flask import render_template, redirect, url_for, flash, get_flashed_messages
from datetime import datetime

import forms
from app import app, db
from models import Task


@app.route("/")
@app.route("/index")
def index():
    """Index page"""
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["GET", "POST"])
def add():
    """Add a task page"""
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(task)
        db.session.commit()
        flash("Task added to the database")
        return redirect(url_for("index"))
    return render_template("add.html", form=form)


@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit(task_id):
    """Edit a task"""
    task = Task.query.get(task_id)
    form = forms.AddTaskForm()

    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash("Task has been updated")
            return redirect(url_for("index"))

        form.title.data = task.title
        return render_template("edit.html", form=form, task_id=task_id)
    flash("Task not found")
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["GET", "POST"])
def delete(task_id):
    """delete a task"""
    task = Task.query.get(task_id)
    form = forms.DeleteTaskForm()

    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash("Task has been deleted")
            return redirect(url_for("index"))

        return render_template("delete.html", form=form, task_id=task_id, title=task.title)
    flash("Task not found")
    return redirect(url_for("index"))
