def combine_and_count(a: dict, b: dict) -> dict:
    """Combine two dictionaries.

    Return  new dictionary with the combined keys and values.
    For any key found in both dictionaries,
    return the sum of the values for that key.

    Args:
      a: The first dictionary.
      b: The second dictionary.

    Returns:
      A dictionary with the contents of both.
      Values of any shared keys are summed.
    """
    # Your code goes here.
    return {k: a.get(k, 0) + b.get(k, 0)
            for k in (a | b).keys()}
