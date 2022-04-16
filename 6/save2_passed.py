"""Checks community branch dir structure to see who submitted most
   and what challenge is more popular by number of PRs"""
from collections import Counter, namedtuple
import os
import urllib.request

# prep

tempfile = os.path.join('/tmp', 'dirnames')
urllib.request.urlretrieve('http://bit.ly/2ABUTjv', tempfile)

IGNORE = 'static templates data pybites bbelderbos hobojoe1848'.split()

users, popular_challenges = Counter(), Counter()

Stats = namedtuple('Stats', 'user challenge')


# code

def gen_files(filename=tempfile):
    """Return a generator of dir names reading in tempfile

       tempfile has this format:

       challenge<int>/file_or_dir<str>,is_dir<bool>
       03/rss.xml,False
       03/tags.html,False
       ...
       03/mridubhatnagar,True
       03/aleksandarknezevic,True

       -> use last column to filter out directories (= True)
    """
    with open(filename) as dirfile:
        content = dirfile.read()
        content = content.splitlines()
        return (line for line in content if not line.endswith("False"))

def diehard_pybites():
    """Return a Stats namedtuple (defined above) that contains the user that
       made the most PRs (ignoring the users in IGNORE) and a challenge tuple
       of most popular challenge and the amount of PRs for that challenge.
       Calling this function on the dataset (held tempfile) should return:
       Stats(user='clamytoe', challenge=('01', 7))
    """
    lines = gen_files()
    lines = [line for line in lines if not any(ignored in line for ignored in IGNORE)]
    number_list = [line[:line.find('/')] for line in lines]
    user_list = [line[line.find('/')+1:line.find(',')] for line in lines]
    users.update(user_list)
    popular_challenges.update(number_list)
    return Stats(user=users.most_common(1)[0][0], challenge=popular_challenges.most_common(1)[0] )