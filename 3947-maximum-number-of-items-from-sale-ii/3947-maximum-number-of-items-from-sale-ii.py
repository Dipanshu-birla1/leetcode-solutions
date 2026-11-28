import collections

class Solution(object):
    def maximumSaleItems(self, items, budget):
        """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
        # Find the max factor to establish our sieve boundaries
        max_factor = max(f for f, _ in items)
        
        # Track the frequencies of each factor
        cnt = [0] * (max_factor + 1)
        min_p = float('inf')
        for f, price in items:
            cnt[f] += 1
            if price < min_p:
                min_p = price
                
        # Sieve: Precalculate how many items have a factor that is a multiple of i
        total_multiples = [0] * len(cnt)
        for i in range(1, len(total_multiples)):
            if not cnt[i]:
                continue
            for j in range(i, len(total_multiples), i):
                total_multiples[i] += cnt[j]
        
        # Group maximum available double-yield items by price
        # Only consider items where price < 2 * min_p
        group = collections.defaultdict(int)
        for f, price in items:
            if price >= 2 * min_p:
                continue
            # The item can give a free copy of any of its multiples (excluding itself)
            group[price] += (total_multiples[f] - 1)
            
        result = 0
        
        # Greedily buy the items that give a free duplicate (2 items per purchase)
        for p in sorted(group):
            if budget < p:
                break
            # We can buy at most what's available or what our budget permits
            copies_to_buy = min(group[p], budget // p)
            result += 2 * copies_to_buy
            budget -= copies_to_buy * p
            
        # Spend any remainder budget on the absolute cheapest items (1 item per purchase)
        result += budget // min_p
        return result