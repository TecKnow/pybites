import re
from typing import Dict


def get_users(passwd: str) -> Dict[str, str]:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    res: Dict[str, str] = dict()
    passwd_elements = [stripped_passwd_line.split(":") for password_line in passwd.splitlines(
    ) if (stripped_passwd_line := password_line.strip())]
    user_name_pairs = [(entry[0], entry[4]) for entry in passwd_elements]
    for user, name in user_name_pairs:
        if not name.strip():
            name = "unknown"
        else:
            name = " ".join([e.strip() for e in name.split(",") if e.strip()])
        res[user] = name
    return res
