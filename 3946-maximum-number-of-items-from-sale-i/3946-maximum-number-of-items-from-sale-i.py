class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        mx = max(f for f, p in items)

        freq = [0] * (mx + 1)
        for f, p in items:
            freq[f] += 1

        count = [0] * (mx + 1)

        for f in range(1, mx + 1):
            for m in range(f, mx + 1, f):
                count[f] += freq[m]

        min_price = min(p for f, p in items)

        dp = [0] * (budget + 1)

        for f, p in items:
            value = count[f]

            for b in range(budget, p - 1, -1):
                dp[b] = max(dp[b], dp[b - p] + value)

        return max(
            dp[b] + (budget - b) // min_price
            for b in range(budget + 1)
        )
