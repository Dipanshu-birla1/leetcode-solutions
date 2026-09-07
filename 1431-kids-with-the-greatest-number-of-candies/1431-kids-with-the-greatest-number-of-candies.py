class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandies = max(candies)
        ans = []

        for i in candies:
            if (i+extraCandies)>= maxcandies:
                ans.append(True)
            else:
                ans.append(False)
        return ans            
                