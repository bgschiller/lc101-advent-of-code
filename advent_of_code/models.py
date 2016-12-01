import psycopg2
from flask import g
from . import app

def connect_db():
    conn = psycopg2.connect(app.config['DATABASE_URL'])
    conn.autocommit = True
    return conn

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def get_recent_submissions(day):
    return dictfetchall(
        '''
        SELECT * FROM submissions
        WHERE challenge_num = %(day)s
        ORDER BY created DESC
        LIMIT 20
        ''',
        dict(day=day))

def create_new_submission(day, name, code):
    res = dictfetchall(
        '''
        INSERT INTO submissions(challenge_num, name, code)
        VALUES (%(day)s, %(name)s, %(code)s)
        RETURNING *
        ''',
        dict(day=day, name=name, code=code))[0]
    return res

def dictfetchall(query, params=None):
    if params is None:
        params = ()
    with g.db.cursor() as c:
        c.execute(query, params)
        keys = [col[0] for col in c.description]
        return [
            dict(zip(keys, row))
            for row in c.fetchall()
        ]
