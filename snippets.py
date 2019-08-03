# A defaultdict works exactly like a normal dict, but it is initialized
# with a function (“default factory”) that takes no arguments and provides
# the default value for a nonexistent key.
# https://www.accelebrate.com/blog/using-defaultdict-python/

from collections import defaultdict

my_dict = defaultdict(int)  # int defaults to initializing a key with value 0
my_dict[key] += 1
