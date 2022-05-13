from functools import wraps

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):

    func.known_users = known_users
    func.logged_in_users = loggedin_users

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    if user in welcome.logged_in_users:
        return f"welcome back {user}"
    elif user in known_users:
        return "please login"
    else:
        return "please create an account"
