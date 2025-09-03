# Source: mypy.readthedocs.io
# for mypy to infer the type of "cs" from:
a, b, *cs = 1, 2  # error: Need type annotation for "cs"

rs: list[int]  # no assignment!
p, q, *rs = 1, 2  # OK - but interestingly for Pylance and pyright 
                  # it is an issue

# Source: mypy.readthedocs.io
l: list[int] = []       # Create empty list of int
d: dict[str, int] = {}  # Create empty dictionary (str -> int)