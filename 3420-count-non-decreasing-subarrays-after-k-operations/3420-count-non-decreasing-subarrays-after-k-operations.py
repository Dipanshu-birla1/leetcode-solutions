
class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        cost = 0
        queue = Deque([(nums[-1], 1)])
        res = 1
        back = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            cur = nums[i]
            cnt = 1

            while queue and queue[-1][0] < cur:
                lesser, count = queue.pop()
                cnt += count
                cost += (cur-lesser) * count
            queue.append((cur, cnt))
            while cost > k:
                more, count = queue.popleft()
                count -= 1
                cost -= (more-nums[back])
                back -= 1
                if count > 0:
                    queue.appendleft((more, count))

            res += back - i + 1
        return res
                    