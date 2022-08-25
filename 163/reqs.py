from typing import List, NamedTuple, Dict
from itertools import chain, repeat


class VersionNumber(NamedTuple):
    major: int
    minor: int
    patch: int


zero_iter = repeat(0)


def ReqToDict(requirements: str) -> Dict[str, VersionNumber]:
    res = dict()
    for line in (line.strip() for line in requirements.splitlines() if line.strip()):
        package_name, version_string = line.split("==")
        major, minor, patch = (version_parts := version_string.split(
            ".")) + [0] * (3-len(version_parts))
        major, minor, patch = (int(x) for x in (major, minor, patch))
        res[package_name] = VersionNumber(major, minor, patch)
    return res


def changed_dependencies(old_reqs: str, new_reqs: str) -> List[str]:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    previous_packages = ReqToDict(old_reqs)
    new_packages = ReqToDict(new_reqs)
    res = list()
    for package, version in new_packages.items():
        if previous_packages.get(package, VersionNumber(-1, -1, -1)) < version:
            res.append(package)
    return res
