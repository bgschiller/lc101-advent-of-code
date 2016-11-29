from . import app
from flask import url_for, render_template, session, redirect
from .permissions import require_user_has_solved, require_advent_day_reached, NotYetPublishedError, NotYetSolvedError
from .forms import BoxableChallenge
@app.route('/')
def index():
    ''' list of challenges '''
    return render_template('index.html')

@app.errorhandler(NotYetPublishedError)
def not_yet_published_redir(error):
    return redirect(url_for('not_yet_published'))

@app.errorhandler(NotYetSolvedError)
def not_yet_solved_redir(error):
    return redirect(url_for('challenges_view', day=error.args[0]))

@app.route('/challenges/<int:day>', methods=['GET', 'OPTIONS', 'POST'])
@require_advent_day_reached
def challenges_view(day):
    form = BoxableChallenge()
    if form.validate_on_submit():
        print('you got it!')
        session['solved_challenges'] = session.get('solved_challenges',[]) + [day]
        return redirect(url_for('challenges_view', day=day))
    return render_template(
        'challenges/{}.html'.format(day),
        form=form,
        day=day,
        solved_challenges=session.get('solved_challenges', []))

@app.route('/not_yet_published')
def not_yet_published():
    return render_template('not_yet_published.html')

@app.route('/submissions/<int:day>')
@require_user_has_solved
def submissions_view(day):
    pass
