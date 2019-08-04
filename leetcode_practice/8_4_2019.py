from typing import List
# 189. Rotate an array


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def inplace_reversal(f_list, start, stop):
            assert 0 <= start <= n - 1
            assert 0 <= stop <= n - 1

            while start < stop:
                last_elt = f_list[stop]
                f_list[stop] = f_list[start]
                f_list[start] = last_elt

                start += 1
                stop -= 1

        if k > 0:
            inplace_reversal(nums, 0, n - 1)
            inplace_reversal(nums, 0, k - 1)
            inplace_reversal(nums, k, n - 1)
