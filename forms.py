from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField
from wtforms.fields import StringField, TextAreaField
from wtforms.fields.html5 import DateField, EmailField, TelField
from wtforms.validators import DataRequired, Length

class BeneficiaryForm(FlaskForm):
    applicant_name = StringField('Applicant Name:', validators=[DataRequired()])
    applicant_email = EmailField('Applicants Email:', validators=[DataRequired()])
    applicant_tel = TelField('Applicants Phone:', validators=[DataRequired(), Length(10)])
    applicant_desc = TextAreaField('Details About the applicant:', validators=[DataRequired()])
    applicant_dob = DateField('Applicant DOB:', validators=[DataRequired()])
    applicant_picture = FileField('Applicant Picture:', validators=[FileRequired()])

