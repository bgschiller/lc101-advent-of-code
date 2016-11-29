from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError

class SubmitChallenge(FlaskForm):
    answer = TextAreaField('answer', [DataRequired()])

    def validate_answer(form, field):
        if not field.data in form.acceptable_answers:
            raise ValidationError(
                "Sorry, that's not the answer I was expecting. Please contact Brian if you think this message is in error")

class SubmitSolution(FlaskForm):
    name = StringField('name', [DataRequired()])
    code = TextAreaField('code', [DataRequired()])

class BoxableChallenge(SubmitChallenge):
    answer = SelectField('answer', choices=[('boxable', 'Boxable'), ('unboxable', 'Unboxable')])
    acceptable_answers = ['unboxable']
