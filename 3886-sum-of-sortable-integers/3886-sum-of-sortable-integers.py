
from collections import Counter
from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        ans = 0

        def check(k):
            for start in range(0, n, k):
                block = nums[start:start + k]
                target = sorted_nums[start:start + k]

                if Counter(block) != Counter(target):
                    return False

                descents = sum(
                    block[i] > block[(i + 1) % k]
                    for i in range(k)
                )

                if descents > 1:
                    return False

            return True

        for k in range(1, n + 1):
            if n % k == 0 and check(k):
                ans += k

        return ans
