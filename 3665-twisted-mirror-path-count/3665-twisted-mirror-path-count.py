
from functools import lru_cache

class Solution:
    def uniquePaths(self, grid):

        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # Direction: 0 = right, 1 = down
        memo = {}

        def resolve(r, c, direction):

            path = []

            while True:

                # Outside grid
                if r >= m or c >= n:
                    result = None
                    break

                state = (r, c, direction)

                # Already calculated
                if state in memo:
                    result = memo[state]
                    break

                # Empty cell: final destination
                if grid[r][c] == 0:
                    result = (r, c)
                    memo[state] = result
                    break

                # Mirror cell
                path.append(state)

                if direction == 0:
                    # Entered from left, turn down
                    r += 1
                    direction = 1

                else:
                    # Entered from above, turn right
                    c += 1
                    direction = 0

            # Cache all mirror states in this chain
            for state in reversed(path):
                memo[state] = result

            return result

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 1

        for i in range(m):
            for j in range(n):

                if dp[i][j] == 0:
                    continue

                ways = dp[i][j]

                # Move right
                nxt = resolve(i, j + 1, 0)

                if nxt is not None:
                    x, y = nxt
                    dp[x][y] = (dp[x][y] + ways) % MOD

                # Move down
                nxt = resolve(i + 1, j, 1)

                if nxt is not None:
                    x, y = nxt
                    dp[x][y] = (dp[x][y] + ways) % MOD

        return dp[m - 1][n - 1]
