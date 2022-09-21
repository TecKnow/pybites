# nice snippet: https://gist.github.com/tonybruess/9405134
from collections import namedtuple
import re
from typing import Dict, Union, TypedDict

social_platforms = """Twitter
  Min: 1
  Max: 15
  Can contain: a-z A-Z 0-9 _

Facebook
  Min: 5
  Max: 50
  Can contain: a-z A-Z 0-9 .

Reddit
  Min: 3
  Max: 20
  Can contain: a-z A-Z 0-9 _ -
"""

# note range is of type range and regex is a re.compile object
Validator = namedtuple('Validator', 'range regex')


class NetworkDict(TypedDict):
    name: str
    min: int
    max: int
    can_contain: str


def parse_social_platform_string(parameters: str) -> NetworkDict:
    work_dict: Dict[str, Union[int, str]] = dict()
    for line in (stripped_line for raw_line in parameters.splitlines() if (stripped_line := raw_line.strip())):
        if ":" not in line:
            work_dict["name"] = line
        else:
            param_name, param_value = (element.strip()
                                       for element in line.split(":"))
            param_name = param_name.casefold()
            param_value_typed = int(param_value) if param_name in {
                "min", "max"} else str(param_value)
            assert isinstance(param_value_typed, (int, str))
            if param_name == "can contain":
                character_class = ''.join(param_value.split())
                work_dict["can_contain"] = f"[{character_class}]"
            else:
                work_dict[param_name] = param_value_typed
    res_dict: NetworkDict = {
        "name": str(work_dict["name"]),
        "min": int(work_dict["min"]),
        "max": int(work_dict["max"]),
        "can_contain": str(work_dict["can_contain"])
    }
    return res_dict


def parse_social_platforms_string() -> Dict[str, Validator]:
    """Convert the social_platforms string above into a dict where
       keys = social platformsname and values = validator namedtuples"""
    social_platforms_dict_list = [parse_social_platform_string(
        x) for x in social_platforms.split('\n\n')]
    res_dict = dict()
    for platform in social_platforms_dict_list:
        name_range = range(platform["min"], platform["max"]+1)
        platform_re = re.compile(rf"{platform['can_contain']}+")
        res_dict[platform["name"]] = Validator(name_range, platform_re)
    return res_dict


def validate_username(platform: str, username: str) -> bool:
    """Receives platforms(Twitter, Facebook or Reddit) and username string,
       raise a ValueError if the wrong platform is passed in,
       return True/False if username is valid for entered platform"""
    all_validators = parse_social_platforms_string()
    if platform not in all_validators:
        raise ValueError(f"Unknown social network {platform}")
    v = all_validators[platform]
    return len(username) in v.range and v.regex.fullmatch(username) is not None


if __name__ == "__main__":
    from pprint import pprint
    pprint(parse_social_platforms_string())
