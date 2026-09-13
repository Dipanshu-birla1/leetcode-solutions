class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        points1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j]]
        points2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j]]

        count = {}

        for x1, y1 in points1:
            for x2, y2 in points2:
                shift = (x2 - x1, y2 - y1)
                count[shift] = count.get(shift, 0) + 1

        return max(count.values(), default=0)