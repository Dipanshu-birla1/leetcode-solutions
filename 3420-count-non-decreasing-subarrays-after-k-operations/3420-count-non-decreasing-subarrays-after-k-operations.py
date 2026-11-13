
from typing import List
from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dq = deque()

        cost = 0
        ans = 0
        j = n - 1

        for i in range(n - 1, -1, -1):
            num = nums[i]
            count = 1

            while dq and dq[-1][0] < num:
                next_num, next_count = dq.pop()

                count += next_count
                cost += (num - next_num) * next_count

            dq.append((num, count))

            while cost > k:
                rightmost_num, rightmost_count = dq.popleft()

                cost -= rightmost_num - nums[j]
                j -= 1

                if rightmost_count > 1:
                    dq.appendleft((rightmost_num, rightmost_count - 1))

            ans += j - i + 1

        return ans
