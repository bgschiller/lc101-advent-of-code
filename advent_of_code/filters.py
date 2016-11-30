from . import app
from flask import Markup
from pygments import highlight
from pygments.util import ClassNotFound
from pygments.lexers import guess_lexer
from pygments.lexers.python import Python3Lexer
from pygments.formatters import HtmlFormatter

formatter = HtmlFormatter(cssclass='highlight')

@app.template_filter('highlight')
def highlight_filter(s):
    try:
        lexer = guess_lexer(s)
    except ClassNotFound:
        lexer = Python3Lexer()
    return Markup(highlight(s, lexer, formatter))
