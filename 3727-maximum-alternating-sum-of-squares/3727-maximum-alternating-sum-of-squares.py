class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted((x * x for x in nums), reverse=True)
        n = len(nums)

        positive_count = (n + 1) // 2
        return sum(squares[:positive_count]) - sum(squares[positive_count:])