from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, Email

class StudentProgressForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    student_number = StringField('Student Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    grades = TextAreaField('Grades Obtained', validators=[DataRequired()])
    satisfaction = SelectField('Overall Satisfaction', choices=[('','Select Satisfaction Level'),('excellent','Excellent'),('good','Good'),('fair','Fair'),('poor','Poor')], validators=[DataRequired()])
    improvement = TextAreaField('Suggestions for Improvement', validators=[DataRequired()])
    button = SubmitField('Submit')
