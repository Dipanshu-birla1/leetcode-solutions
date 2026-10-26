
class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0

            if grid[r][c] == 0:
                return 0

            value = grid[r][c]
            grid[r][c] = 0

            value += dfs(r - 1, c)
            value += dfs(r + 1, c)
            value += dfs(r, c - 1)
            value += dfs(r, c + 1)

            return value

        count = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    total = dfs(r, c)

                    if total % k == 0:
                        count += 1

        return count
