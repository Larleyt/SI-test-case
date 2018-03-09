from itertools import takewhile, repeat


def lines(f):
    return takewhile(
        lambda s: s != "",
        (f.readline() for _ in repeat(None))
    )
