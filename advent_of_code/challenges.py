from collections import namedtuple
from wtforms import StringField, TextAreaField, SelectField
from .forms import SubmitChallenge, SubmitChallengeTextArea

# We want a namedtuple, but with default parameters and non-standard
# behavior at initialization-time. So we're making a class that
# immediately inherits from the one produced by namedtuple, and tacking
# on some additional logic.
all_challenges = []

class Challenge(namedtuple(
    'ChallengeParent',
    ['day', 'title', 'form'])):
    def __new__(self, day, title, form=None, answers=None):
        if form is None:
            # You don't want a custom form? that's cool, we can make you a
            # standard one if you tell us what the acceptable_answers are.
            assert answers is not None, "must pass either 'form' or 'answers'"
            multiline_answer = any('\n' in a for a in answers)
            class form(SubmitChallengeTextArea if multiline_answer else SubmitChallenge):
                acceptable_answers = answers

        return super(Challenge, self).__new__(self, day, title, form)

class BoxableChallenge(SubmitChallenge):
    answer = SelectField('answer', choices=[('boxable', 'Boxable'), ('unboxable', 'Unboxable')])
    acceptable_answers = ['unboxable']

all_challenges.append(Challenge(
    day=1,
    title='well-wrapped presents',
    form=BoxableChallenge))
all_challenges.append(Challenge(
    day=2,
    title='conserving candles',
    answers=['66', '66%', '0.66']))
all_challenges.append(Challenge(
    day=3,
    title='wishlist snooping',
    answers=[
        'dear santa i would like a toy pup a toy kitten a toy bunny and a toy horse and also a small plane that i could ride in i would like a coloring book too',
        'dear santa i would like a toy pup a toy kitten a toy bunny and a toy horse and also a small plane that i could ride in i would like a coloring book too'.replace(' ', '')]))

all_challenges.append(Challenge(
    day=4,
    title='forecast fudging',
    answers=[
        '''1 high 65
2 low 41
7 low 41
10 high 65
13 low 45''']))

all_challenges.append(Challenge(
    day=5,
    title='cracking vigenere',
    answers=[
        "gettin' jiggy wit it",
        "getting jiggy wit it",
        "gettin jiggy with it",
        "getting jiggy with it",
    ]))

all_challenges.append(Challenge(
    day=6,
    title='better-wrapped presents',
    answers=[
    '''unboxable
boxable
unboxable
boxable''']))

all_challenges.append(Challenge(
    day=7,
    title='stock trading',
    answers=[
        "buying for $11 at 1:02 and selling for $93 at 4:18 makes $81"
    ]
))


def get_challenge(day):
    challenge = all_challenges[day - 1]
    assert challenge.day == day, "We got out-of-order challenges over here!"
    return challenge
