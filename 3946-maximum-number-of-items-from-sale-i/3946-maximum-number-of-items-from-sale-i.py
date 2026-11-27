class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        max_factor = max(p[0] for p in items)
        cnt_factor = [0] * (max_factor + 1)
        for factor, _ in items:
            cnt_factor[factor] += 1

        cnt_multi = [0] * (max_factor + 1)
        f = [0] * (budget + 1)
        min_price = inf
        sum_price = 0

        for factor, price in items:
            min_price = min(min_price, price)

            if cnt_multi[factor] == 0:
                for j in range(factor, max_factor + 1, factor):
                    cnt_multi[factor] += cnt_factor[j]
            cnt = cnt_multi[factor]

            sum_price = min(sum_price + price, budget)
            for j in range(sum_price, price - 1, -1):
                v = f[j - price] + cnt
                if v > f[j]: f[j] = v

        return max(fi + (budget - i) // min_price for i, fi in enumerate(f))
