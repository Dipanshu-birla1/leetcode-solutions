
from typing import List
from math import gcd, lcm

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            product = 1
            g = 0
            l = 1

            for j in range(i, n):
                x = nums[j]

                product *= x
                g = gcd(g, x)
                l = lcm(l, x)

                if product == g * l:
                    ans = max(ans, j - i + 1)

        return ans
