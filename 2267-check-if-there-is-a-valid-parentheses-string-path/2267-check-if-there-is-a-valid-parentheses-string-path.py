class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        if (m + n - 1) % 2 != 0:
            return False

        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                balance_change = 1 if grid[i][j] == '(' else -1
                prev = set()

                if i > 0:
                    prev |= dp[i - 1][j]

                if j > 0:
                    prev |= dp[i][j - 1]

                remaining = (m - 1 - i) + (n - 1 - j)

                for balance in prev:
                    new_balance = balance + balance_change

                    if 0 <= new_balance <= remaining:
                        dp[i][j].add(new_balance)

        return 0 in dp[m - 1][n - 1]