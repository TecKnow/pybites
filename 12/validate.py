from collections import namedtuple

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)


class UserDoesNotExist(Exception):
    pass


class UserAccessExpired(Exception):
    pass


class UserNoPermission(Exception):
    pass


def get_secret_token(username):
    found_user_list = [user for user in USERS if user.name == username]
    if (found_len := len(found_user_list)) == 0:
        raise UserDoesNotExist()
    elif found_len > 1:
        raise Exception(f"found more than 1 user for {username}")
    user = found_user_list[0]
    if user.expired:
        raise UserAccessExpired()
    elif user.role != ADMIN:
        raise UserNoPermission()
    else:
        return SECRET
