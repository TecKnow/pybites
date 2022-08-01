from typing import DefaultDict, List
from collections import defaultdict

def get_duplicate_indices(words: List[str]) -> List[int]:
    """Given a list of words, loop through the words and check for each
       word if it occurs more than once.
       If so return the index of its first occurrence.
       For example in the following list 'is' and 'it'
       occur more than once, and they are at indices 0 and 1 so you would
       return [0, 1]:
       ['is', 'it', 'true', 'or', 'is', 'it', 'not?'] => [0, 1]
       Make sure the returning list is unique and sorted in ascending order."""
    locations: DefaultDict[str, List[int]] = defaultdict(list)
    for position, word in enumerate(words):
      locations[word].append(position)
    return sorted([location_list[0] for location_list in locations.values() if len(location_list) > 1])