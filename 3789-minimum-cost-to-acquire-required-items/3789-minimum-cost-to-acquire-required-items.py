
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

       
        option1 = need1 * cost1 + need2 * cost2
        common = min(need1, need2)

        option2 = common * costBoth
        option2 += (need1 - common) * cost1
        option2 += (need2 - common) * cost2

      
        option3 = max(need1, need2) * costBoth

        return min(option1, option2, option3)
