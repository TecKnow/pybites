def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    e = enumerate(seque, start=1)
    sum = 0
    for count, item in e:
        sum += item
        yield sum/count