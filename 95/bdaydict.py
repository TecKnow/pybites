from collections import UserDict
from collections.abc import MutableMapping
from datetime import date

MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(UserDict, MutableMapping):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __setitem__(self, name: str, birthday: date):
        for existing_birthday in self.data.values():
            if (birthday.month, birthday.day) == (existing_birthday.month, existing_birthday.day):
                print(MSG.format(name))
                break
        self.data.__setitem__(name, birthday)
