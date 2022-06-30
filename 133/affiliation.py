def generate_affiliation_link(url: str) -> str:
    *_, item_and_query = url.partition("/dp/")
    item, *_ = item_and_query.partition("/")
    return f"http://www.amazon.com/dp/{item}/?tag=pyb0f-20"
