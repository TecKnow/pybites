def get_profile(name: str, age: int, *sports: str, **awards: str):
    if not isinstance(age, int) or len(sports) > 5:
        raise ValueError()
    res = {"name": name, "age": age}
    if sports:
        res["sports"] = sorted(sports)
    if awards:
        res["awards"] = awards
    return res
