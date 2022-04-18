from collections import OrderedDict
from math import inf

from pprint import pprint

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()


def get_belt(user_score, scores=scores, belts=belts):
    scores = [*scores] + [inf]
    belts = [None] + [*belts]
    scores_to_belts_dict = OrderedDict(zip(scores, belts))
    for k, v in scores_to_belts_dict.items():
        if user_score < k:
            return v
