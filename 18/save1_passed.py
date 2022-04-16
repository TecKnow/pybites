import os
import urllib.request
from collections import Counter

# data provided
stopwords_file = os.path.join('/tmp', 'stopwords')
harry_text = os.path.join('/tmp', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)

stopword_set = None
with open(stopwords_file) as fstop:
    stopword_set = {line.strip() for line in fstop}
    

def get_harry_most_common_word():
    with open(harry_text) as fsource:
        ssource = fsource.read()
        ssource = ssource.lower()
        ssource = (c for c in ssource if c.isalnum() or c.isspace())
        ssource = ''.join(ssource)
        ssource = ssource.split()
        ssource = [word for word in ssource if word not in stopword_set]
        harry_potter_words = Counter(ssource)
        return harry_potter_words.most_common(1)[0]