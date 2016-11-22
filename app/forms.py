from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, DateField, validators

class SetupForm(Form):
    pass_phrase = StringField('Pass Phrase', validators=[
        validators.InputRequired(), 
        validators.Length(min=14, max=50)
        ])
    expiry_date = DateField('Expiry Date', validators=[
        validators.InputRequired()
        ])