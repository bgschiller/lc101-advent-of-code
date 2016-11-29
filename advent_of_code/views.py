from . import app
from flask import url_for, render_template, session, redirect, flash
from .permissions import require_user_has_solved, require_advent_day_reached, NotYetPublishedError, NotYetSolvedError
from .forms import BoxableChallenge, SubmitSolution
from .models import get_recent_submissions, create_new_submission

@app.errorhandler(NotYetPublishedError)
def not_yet_published_redir(error):
    return redirect(url_for('not_yet_published'))

@app.errorhandler(NotYetSolvedError)
def not_yet_solved_redir(error):
    flash('you must solve the problem before you can view or post solutions', 'warning')
    return redirect(url_for('challenges_view', day=error.args[0]))

@app.route('/not_yet_published')
def not_yet_published():
    flash('yolo', 'error')
    flash('good things', 'success')
    return render_template('not_yet_published.html')

@app.route('/')
def index():
    ''' list of challenges '''
    return render_template('index.html')

@app.route('/challenges/<int:day>', methods=['GET', 'OPTIONS', 'POST'])
#@require_advent_day_reached
def challenges_view(day):
    form = BoxableChallenge()
    if form.validate_on_submit():
        flash('you got it!', 'succhess')
        session['solved_challenges'] = session.get('solved_challenges',[]) + [day]
        return redirect(url_for('challenges_view', day=day))
    return render_template(
        'challenges/{}.html'.format(day),
        form=form,
        day=day,
        solved_challenges=session.get('solved_challenges', []))

@app.route('/submissions/<int:day>',  methods=['GET', 'OPTIONS', 'POST'])
@require_user_has_solved
def submissions_view(day):
    form = SubmitSolution(name=session.get('name'))
    if form.validate_on_submit():
        flash('solution submitted!', 'success')
        session['name'] = form.name.data
        create_new_submission(form.name.data, form.code.data)
        return redirect(url_for('submissions_view', day=day))

    return render_template(
        'submissions.html',
        form=form,
        submissions=get_recent_submissions(),
        day=day)
