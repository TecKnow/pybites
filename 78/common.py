from typing import Dict, List


def common_languages(programmers: Dict[str, List[str]]) -> List[str]:
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    return list(set.intersection(*(set(languages) for languages in programmers.values())))
