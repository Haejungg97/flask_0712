from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired()])
    content = testareafield('내용', validators=[DataRequired()])