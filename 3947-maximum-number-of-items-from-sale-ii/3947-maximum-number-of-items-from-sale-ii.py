
class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)
        freq = [0] * (n + 1)
        min_price = float('inf')

        for f, p in items:
            freq[f] += 1
            min_price = min(min_price, p)

        cnt = [0] * (n + 1)

        for f in range(1, n + 1):
            for j in range(f, n + 1, f):
                cnt[f] += freq[j]
            cnt[f] -= 1

        items.sort(key=lambda x: x[1])

        ans = 0

        for f, p in items:
            if p >= 2 * min_price:
                break

            c = min(cnt[f], budget // p)
            ans += 2 * c
            budget -= c * p

        return ans + budget // min_price
