import string

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


def validate_password(password):
    if (
        not (6 <= len(password) <= 12) or
        not len([c for c in password if c in string.digits]) >= 1 or
        not len([c for c in password if c in string.ascii_lowercase]) >= 2 or
        not len([c for c in password if c in string.ascii_uppercase]) >= 1 or
        not len([c for c in password if c in string.punctuation]) >= 1 or
        password in used_passwords
    ):
        return False
    else:
        used_passwords.add(password)
        return True
