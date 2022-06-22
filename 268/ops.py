from collections import deque


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
    if n not in num_ops.cache.keys():
        work_deque = deque(num_ops.cache.items())
        while work_deque:
            current_value, current_steps = work_deque.popleft()
            if current_value == n:
                break
            if (double := current_value * 2) not in num_ops.cache.keys():
                num_ops.cache[double] = current_steps + 1
                work_deque.append((double, current_steps+1))
            if (third := current_value // 3) not in num_ops.cache.keys():
                num_ops.cache[third] = current_steps + 1
                work_deque.append((third, current_steps + 1))

    return num_ops.cache[n]


num_ops.cache = {0: 1, 1: 0}
