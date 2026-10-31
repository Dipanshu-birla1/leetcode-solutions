class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        curRow = [0] * n
        curRow[0] = 1
        for row in grid:
            prvRow, curRow, prvCel = curRow, [0] * n, 0
            
            for idx, p in enumerate(prvRow):
                if row[idx] == 0:
                    curRow[idx], prvCel = prvCel + p, prvCel + p
                else:
                    curRow[idx], prvCel = prvCel, p

        return curRow[-1] %1_000_000_007