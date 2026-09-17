class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        INF = float('inf')
        best = [INF] * len(arr)

        prefix = 0
        seen = {0: -1}

        ans = INF
        min_len = INF

        for i in range(len(arr)):
            prefix += arr[i]

            if prefix - target in seen:
                start = seen[prefix - target] + 1
                length = i - start + 1

                if start > 0 and best[start - 1] != INF:
                    ans = min(ans, length + best[start - 1])

                min_len = min(min_len, length)

            best[i] = min_len
            seen[prefix] = i

        return -1 if ans == INF else ans