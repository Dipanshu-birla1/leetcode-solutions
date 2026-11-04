
from typing import List
from collections import Counter
import heapq


class DualHeap:
    def __init__(self):
        self.small = []
        self.large = []
        self.delayed = Counter()

        self.small_size = 0
        self.large_size = 0

        self.small_sum = 0
        self.large_sum = 0

    def prune(self, heap, sign):
        while heap:
            num = sign * heap[0]

            if self.delayed[num] > 0:
                self.delayed[num] -= 1

                if self.delayed[num] == 0:
                    del self.delayed[num]

                heapq.heappop(heap)
            else:
                break

    def balance(self):
        if self.small_size > self.large_size + 1:
            self.prune(self.small, -1)

            num = -heapq.heappop(self.small)
            heapq.heappush(self.large, num)

            self.small_size -= 1
            self.large_size += 1

            self.small_sum -= num
            self.large_sum += num

            self.prune(self.small, -1)

        elif self.small_size < self.large_size:
            self.prune(self.large, 1)

            num = heapq.heappop(self.large)
            heapq.heappush(self.small, -num)

            self.large_size -= 1
            self.small_size += 1

            self.large_sum -= num
            self.small_sum += num

            self.prune(self.large, 1)

    def add(self, num):
        self.prune(self.small, -1)
        self.prune(self.large, 1)

        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.small_size += 1
            self.small_sum += num
        else:
            heapq.heappush(self.large, num)
            self.large_size += 1
            self.large_sum += num

        self.balance()

    def remove(self, num):
        self.prune(self.small, -1)
        self.prune(self.large, 1)

        self.delayed[num] += 1

        if num <= -self.small[0]:
            self.small_size -= 1
            self.small_sum -= num

            if num == -self.small[0]:
                self.prune(self.small, -1)
        else:
            self.large_size -= 1
            self.large_sum -= num

            if self.large and num == self.large[0]:
                self.prune(self.large, 1)

        self.balance()

    def get_cost(self):
        self.prune(self.small, -1)
        self.prune(self.large, 1)

        median = -self.small[0]

        left_cost = median * self.small_size - self.small_sum
        right_cost = self.large_sum - median * self.large_size

        return left_cost + right_cost


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:

        n = len(nums)

        # Calculate minimum cost of every window of size x
        dh = DualHeap()
        costs = []

        for i in range(n):
            dh.add(nums[i])

            if i >= x - 1:
                costs.append(dh.get_cost())
                dh.remove(nums[i - x + 1])

        # DP: minimum cost to select k non-overlapping windows
        INF = float('inf')

        dp = [[INF] * (k + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(n - 1, -1, -1):
            for j in range(1, k + 1):

                # Skip current position
                dp[i][j] = dp[i + 1][j]

                # Select window starting at i
                if i + x <= n:
                    take = costs[i] + dp[i + x][j - 1]
                    dp[i][j] = min(dp[i][j], take)

        return dp[0][k]
