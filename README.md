# LaunchCode 101 Advent of Code

### Dev Environment setup

Make sure you have python3, virtualenvwrapper, and postgres installed (I recommend [postgres.app](http://postgresapp.com/) if you have a mac.

1. Fork this repo, and `git clone` it to your machine.
2. Make a virtual env for the repo `$ mkvirtualenv advent-of-code -p $(which python3)`
3. Install the dependencies `$ pip install -r requirements.txt`
4. Make a db `$ createdb advent_of_code`
5. Run migrations `$ cat migrations/*.sql | psql -d advent_of_code`
6. Run the server with `python run.py`
