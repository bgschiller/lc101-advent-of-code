
def get_recent_submissions():

    submissions = [
        dict(name='Heidi the dog', code='''
So you see,
it was

all
    just
        a simple
            misunderstanding'''),
        dict(name="Cookin' with coolio", code='''
def launch_scrabble(words):
    """
    Words that begin with ‘q’ are 10 points, all other words count as one point.

    But since ‘q’ words are worth so many points, we want to make sure our players aren’t cheating and making up words that start with ‘q’. So for every word that begins with ‘q’, the program checks to make sure the following letter is ‘u’. If we find an exception, for instance “qrie”, negate all their points and give that cheater an overall score of 0!

    """
    points = 0
    for word in words: # words = ['dog'], word = 'dog'
        word = word.lower()
        if len(word) >= 1 and word[0] == "q":
            if len(word) >= 2 and word[1] == "u":
                points += 10
            else:
                return 0
        else:
            points += 1 # points = 1

    return points

''')
    ]
    return submissions

def create_new_submission(name, code):
    pass
