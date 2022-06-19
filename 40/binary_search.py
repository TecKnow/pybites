import bisect 
def binary_search(sequence, target):
    i = bisect.bisect_left(sequence, target)
    if i != len(sequence) and sequence[i] == target:
        return i
    return None