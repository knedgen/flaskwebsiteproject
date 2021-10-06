from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import  FileField, FileAllowed

class ProjectPostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    description = TextAreaField('Description',validators=[DataRequired()])
    link = StringField('Link',validators=[DataRequired()])
    submit = SubmitField("Add Project")
