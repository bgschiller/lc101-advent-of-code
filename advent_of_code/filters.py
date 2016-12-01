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

@app.template_filter('momentjs')
def momentjs_filter(s):
    return Markup("""<script>
document.write(moment("{0}Z").format('lll'))
</script>
<noscript>{0}</noscript>""".format(s.isoformat()))
