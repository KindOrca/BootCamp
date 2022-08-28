from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField, validators
from wtforms.validators import DataRequired

class PatientInfo(FlaskForm):
    Name = StringField('Name',validators=[DataRequired()])
    Age = IntegerField('Age',validators=[DataRequired(), validators.NumberRange(min=0, max=99)])
    Gender = BooleanField('Gender')
    Scholarship = BooleanField('Scholarship')
    Hipertension = BooleanField('Hipertension')
    Diabetes = BooleanField('Diabetes')
    Alcholism = BooleanField('Alcholism')
    Handcap = BooleanField('Handcap')
    SMS_received = BooleanField('SMS_received')
    Submit = SubmitField('Submit')