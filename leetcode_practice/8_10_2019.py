# 136. Single number

# Independent solution with one SO lookup
# https://stackoverflow.com/questions/3282823/get-the-key-corresponding-to-the-minimum-value-within-a-dictionary
from collections import defaultdict


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_cts: Dict[int, int] = defaultdict(int)

        for number in nums:
            num_cts[number] += 1

        return min(num_cts, key=num_cts.get)

# 28. Implement strStr()


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        len_haystack = len(haystack)

        if not needle:
            return 0

        for i, char in enumerate(haystack):
            needle_candidate = haystack[i: min(i + len_needle, len_haystack)]
            if needle_candidate == needle:
                return i
        return -1
