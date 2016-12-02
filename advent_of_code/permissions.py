from functools import wraps
from flask import session
import datetime
import inspect

class NotYetPublishedError(Exception):
    pass

class NotYetSolvedError(Exception):
    pass

def user_has_solved(day):
    return day in session.get('solved_challenges', [])

def advent_day_reached(day):
    return datetime.datetime.now() - datetime.timedelta(hours=6) > datetime.datetime(2016, 12, day)

def _require_day_based_permission(test, error):
    def decorator(view):
        argspec = inspect.getargspec(view)
        assert 'day' in argspec.args, "Can only decorate \
    functions that accept 'day' as a parameter"

        @wraps(view)
        def checks_test(*args, **kwargs):
            cargs = inspect.getcallargs(view, *args, **kwargs)
            if not test(cargs['day']):
                raise error(cargs['day'])
            return view(*args, **kwargs)
        return checks_test
    return decorator


require_advent_day_reached = _require_day_based_permission(advent_day_reached, NotYetPublishedError)
require_user_has_solved = _require_day_based_permission(user_has_solved, NotYetSolvedError)
