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
