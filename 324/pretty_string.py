import pprint
from functools import partial


pretty_string = partial(pprint.pformat, width=60, depth=2)
