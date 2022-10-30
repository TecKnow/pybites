from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if not lst_of_lst:
        return None
    res = list()
    sublist_iter = iter(lst_of_lst)
    res.extend(next(sublist_iter))
    for sublist in sublist_iter:
        res.append(sep)
        res.extend(sublist)
    return res
