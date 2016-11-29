from . import app
from flask import url_for, render_template, session
from .permissions import require_user_has_solved, require_advent_day_reached
from .forms import BoxableChallenge
@app.route('/')
def index():
    ''' list of challenges '''
    return render_template('index.html')

@app.route('/challenges/<int:day>', methods=['GET', 'OPTIONS', 'POST'])
#@require_advent_day_reached
def challenges_view(day):
    form = BoxableChallenge()
    if form.validate_on_submit():
        print('you got it!')
        session['solved_challenges'] = session.get('solved_challenges',[]) + [day]
    return render_template(
        'challenges/{}.html'.format(day),
        form=form,
        day=day,
        solved_challenges=session.get('solved_challenges', []))

@app.route('/submissions/<int:day>')
@require_user_has_solved
def submissions_view(day):
    pass
