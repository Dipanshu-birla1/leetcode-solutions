from bisect import bisect_right
from functools import lru_cache

class Solution:
    def maximumWeight(self, intervals):
        arr = [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        arr.sort()

        starts = [x[0] for x in arr]
        n = len(arr)

        nxt = [bisect_right(starts, arr[i][1]) for i in range(n)]

        @lru_cache(None)
        def dp(i, k):
            if i == n or k == 0:
                return 0, ()

            score1, res1 = dp(i + 1, k)

            l, r, w, idx = arr[i]
            score2, res2 = dp(nxt[i], k - 1)
            score2 += w
            res2 = tuple(sorted(res2 + (idx,)))

            if score2 > score1:
                return score2, res2
            if score1 > score2:
                return score1, res1

            return score1, min(res1, res2)

        return list(dp(0, 4)[1])