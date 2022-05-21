from functools import wraps

MAX_RETRIES = 3


class MaxRetriesException(Exception):
    pass


def retry(func):
    """Complete this decorator, make sure
       you print the exception thrown"""
    # ... retry MAX_RETRIES times
    # ...
    # make sure you include this for testing:
    # except Exception as exc:
    #     print(exc)
    # ...
    # and use wraps to preserve docstring
    #
    @wraps(func)
    def wrapper(*args, **kwargs):
        current_retries = 0
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if current_retries < MAX_RETRIES:
                    print(e)
                    current_retries += 1
                else:
                    raise MaxRetriesException() from e
    return wrapper
    