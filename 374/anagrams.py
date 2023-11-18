def group_anagrams(strings: list[str]) -> list[list[str]]:
    """Group anagrams together."""
    results: dict[frozenset, set[str]] = dict()
    for word in strings:
        results.setdefault(frozenset(word), set()).add(word)
    return [list(word_set) for word_set in results.values()]


if __name__ == "__main__":
    group_anagrams()