# A defaultdict works exactly like a normal dict, but it is initialized
# with a function (“default factory”) that takes no arguments and provides
# the default value for a nonexistent key.
# https://www.accelebrate.com/blog/using-defaultdict-python/

# Simplifying the case where you add a key to a dictionary if it doesn't exist
# in order to perform counting.
from collections import defaultdict

my_dict = defaultdict(int)  # int defaults to initializing a key with value 0
my_dict[key] += 1
