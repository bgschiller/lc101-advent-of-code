import os

DEBUG = False
SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'moosecurry')
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://localhost/advent_of_code')
