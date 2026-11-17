
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        cost = [[INF] * (n + 1) for _ in range(n)]

        for length in range(2, n + 1):
            for d in range(1, length):
                if length % d != 0:
                    continue

                groups = length // d
                if groups < 2:
                    continue

                for left in range(n - length + 1):
                    changes = 0

                    for r in range(d):
                        for q in range(groups // 2):
                            a = left + r + q * d
                            b = left + r + (groups - 1 - q) * d

                            if s[a] != s[b]:
                                changes += 1

                    right = left + length
                    cost[left][right] = min(
                        cost[left][right], changes
                    )

        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):
                for j in range(2 * (p - 1), i - 1):
                    dp[p][i] = min(
                        dp[p][i],
                        dp[p - 1][j] + cost[j][i]
                    )

        return dp[k][n]
