class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2
            ops = sum(max(0, d - mid) for d in diff)

            if ops <= k:
                right = mid
            else:
                left = mid + 1

        limit = left
        ans = 0
        used = 0

        for d in diff:
            reduced = min(d, limit)
            ans += reduced * reduced
            used += max(0, d - limit)

        remaining = k - used

        for d in diff:
            if remaining == 0:
                break
            if d >= limit and d > 0:
                ans -= limit * limit
                ans += (limit - 1) * (limit - 1)
                remaining -= 1

        return ans