def num_ops(n):
    """
    Input: an integer number, the target number
    Output: the minimum number of operations required to reach to n from 1.

    Two operations rules:
    1.  multiply by 2
    2.  int. divide by 3

    The base number is 1. Meaning the operation will always start with 1
    These rules can be run in any order, and can be run independently.

    [Hint] the data structure is the key to solve it efficiently.
    """
    # you code
    if not hasattr(num_ops, "cache"):
        setattr(num_ops, "cache", {0: 1, 1: 0})
    current_candidates = list(num_ops.cache.keys())
    new_candidates = list()
    while n not in num_ops.cache.keys():
        for candidate in current_candidates:
            current_steps = num_ops.cache[candidate]
            double = candidate * 2
            third = candidate // 3
            if double not in num_ops.cache.keys():
                num_ops.cache[double] = current_steps + 1
                new_candidates.append(double)
            if third not in num_ops.cache.keys():
                num_ops.cache[third] = current_steps + 1
                new_candidates.append(third)
        current_candidates = new_candidates
        new_candidates = list()
    return num_ops.cache[n]
