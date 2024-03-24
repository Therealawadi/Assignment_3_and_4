# Import necessary modules and classes from Flask-WTF and WTForms
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, Email

# Define a form class for capturing student progress feedback
class StudentProgressForm(FlaskForm):
    # StringField for capturing student's name, with DataRequired validator to ensure it's not empty
    name = StringField('Name', validators=[DataRequired()])
    # StringField for capturing student's number, with DataRequired validator to ensure it's not empty
    student_number = StringField('Student Number', validators=[DataRequired()])
    # StringField for capturing student's email, with DataRequired and Email validators to ensure it's a valid email
    email = StringField('Email', validators=[DataRequired(), Email()])
    # TextAreaField for capturing grades obtained, with DataRequired validator to ensure it's not empty
    grades = TextAreaField('Grades Obtained', validators=[DataRequired()])
    # SelectField for capturing overall satisfaction level, with choices and DataRequired validator
    satisfaction = SelectField('Overall Satisfaction', choices=[
        ('','Select Satisfaction Level'),
        ('excellent','Excellent'),
        ('good','Good'),
        ('fair','Fair'),
        ('poor','Poor')
    ], validators=[DataRequired()])
    # TextAreaField for capturing suggestions for improvement, with DataRequired validator to ensure it's not empty
    improvement = TextAreaField('Suggestions for Improvement', validators=[DataRequired()])
    # SubmitField to submit the form
    button = SubmitField('Submit')
