from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, ValidationError

class SubmitChallenge(FlaskForm):
    answer = StringField('answer', [DataRequired()])

    def validate_answer(form, field):
        if not field.data.replace('\r\n', '\n').strip().lower() in form.acceptable_answers:
            raise ValidationError(
                "Sorry, that's not the answer I was expecting. Please contact Brian if you think this message is in error")

class SubmitChallengeTextArea(SubmitChallenge):
    answer = TextAreaField('answer', [DataRequired()])

class SubmitSolution(FlaskForm):
    name = StringField('name', [DataRequired()])
    code = TextAreaField('code', [DataRequired()])
