"""Forms for app"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddTaskForm(FlaskForm):
    """Form to add a new Task"""
    title = StringField("Title", validators=[DataRequired()])
    submit = SubmitField("Submit")


class DeleteTaskForm(FlaskForm):
    """Form to delete a Task"""
    submit = SubmitField("Delete")
