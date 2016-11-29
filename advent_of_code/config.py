import os

DEBUG = False
SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'moosecurry')
