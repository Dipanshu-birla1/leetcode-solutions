from typing import List
from heapq import heappush, heappop
from collections import defaultdict
import numpy as np


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        small = []   # max-heap (negated) : lower half
        large = []   # min-heap : upper half
        delayed = defaultdict(int)
        sSize = 0
        lSize = 0
        sSum = 0
        lSum = 0
        cost = [0] * (n - x + 1)

        def prune_small():
            nonlocal small
            while small:
                v = -small[0]
                if delayed[v] > 0:
                    delayed[v] -= 1
                    heappop(small)
                else:
                    break

        def prune_large():
            while large:
                v = large[0]
                if delayed[v] > 0:
                    delayed[v] -= 1
                    heappop(large)
                else:
                    break

        def balance():
            nonlocal sSize, lSize, sSum, lSum
            while sSize > lSize + 1:
                v = -heappop(small)
                sSize -= 1
                sSum -= v
                heappush(large, v)
                lSize += 1
                lSum += v
                prune_small()
            while sSize < lSize:
                v = heappop(large)
                lSize -= 1
                lSum -= v
                heappush(small, -v)
                sSize += 1
                sSum += v
                prune_large()

        for i in range(n):
            v = nums[i]
            if not small or v <= -small[0]:
                heappush(small, -v)
                sSize += 1
                sSum += v
            else:
                heappush(large, v)
                lSize += 1
                lSum += v
            balance()
            if i >= x:
                out = nums[i - x]
                delayed[out] += 1
                if out <= -small[0]:
                    sSize -= 1
                    sSum -= out
                    if out == -small[0]:
                        prune_small()
                else:
                    lSize -= 1
                    lSum -= out
                    if large and out == large[0]:
                        prune_large()
                balance()
            if i >= x - 1:
                med = -small[0]
                cost[i - x + 1] = med * sSize - sSum + lSum - med * lSize

        INF = 1 << 60
        m = n - x + 1
        cost_np = np.array(cost, dtype=np.int64)
        dp_prev = np.zeros(n + 1, dtype=np.int64)
        for _ in range(k):
            b = np.full(n + 1, INF, dtype=np.int64)
            b[x:] = dp_prev[0:m] + cost_np
            dp_prev = np.minimum.accumulate(b)
        return int(dp_prev[n])