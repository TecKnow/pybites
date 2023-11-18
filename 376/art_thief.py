def art_thief(paintings: list[int]) -> int:
    """Return the maximum value of paintings that can be stolen."""
    result = [-1] * len(paintings)
    result[-2:] = paintings[-2:]
    for i in range(len(paintings)-1, -1, -1):
        result[i] = paintings[i] + max(result[i+2:], default=0)
    print(result)
    return max(result, default=0)


if __name__ == "__main__":
    print(art_thief([6, 1, 9, 7, 4, 8, 3, 5, 2, 10]))
